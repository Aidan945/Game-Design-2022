import threading
import pygame
import random
import os
os.system('cls')

# 48 by 64
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))


sprite_x = 48
sprite_y = 64
scale = 3

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

test_surface_image = pygame.image.load("pygamefiles/images/cyberpunk background.jpg")
test_surface_image_scale = pygame.transform.scale(test_surface_image, (1200, 700))
grass_surface_image = pygame.image.load("pygamefiles/images/grass background.jpg")
grass_surface_image_scale = pygame.transform.scale(grass_surface_image, (screen_width, screen_height))
space_surface_image = pygame.image.load("pygamefiles/images/grass background.jpg")
space_surface_image_scale = pygame.transform.scale(space_surface_image, (screen_width, screen_height))

pygame.init()
pygame.font.init()
#  Background
intro_font = pygame.font.SysFont("comicsans", 100)
intro_font_words = intro_font.render("select a background", False, BLACK)

player_health = 10
health_font = pygame.font.SysFont("comicsans", 40)
health_font_show = health_font.render("your health is "+str(player_health), False, WHITE)

priest_sheet = pygame.image.load("pygamefiles/images/priestsheet.png")

bone_sheet = pygame.image.load("pygamefiles/images/Bone Spin.gif")
bone_index = 0


def get_image(sheet, frame_x, frame_y, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame_x*width), (frame_y*height), width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)

    return image





def collision():
    if pygame.sprite.spritecollideany(character.sprite, object_group):
        return True


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.gravity = 0
        self.jump_scale = 1.2
        self.jump_vel = 10
        self.vel = 8
        self.jump = False
        self.left = False
        self.right = False
        self.character_x = screen_width/2 - 70
        self.character_y = 200
        self.floor = 600
        self.left = False
        self.right = False

        front = get_image(priest_sheet, 1, 2, 48, 64, scale, BLACK)
        left_1 = get_image(priest_sheet, 0, 3, 48, 64, scale, BLACK)
        left_2 = get_image(priest_sheet, 1, 3, 48, 64, scale, BLACK)
        left_3 = get_image(priest_sheet, 2, 3, 48, 64, scale, BLACK)
        right_1 = get_image(priest_sheet, 0, 1, 48, 64, scale, BLACK)
        right_2 = get_image(priest_sheet, 1, 1, 48, 64, scale, BLACK)
        right_3 = get_image(priest_sheet, 2, 1, 48, 64, scale, BLACK)
        self.player_walk_left = [front, left_1, left_2, left_3, right_1, right_2, right_3, right_3]
        self.player_index = 0
        self.image = self.player_walk_left[self.player_index]
        self.rect = self.image.get_rect(topleft=(self.character_x, self.character_y))
        self.hitbox = (self.rect.x+19, self.rect.y, 10, 48)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == self.floor:
            self.gravity = (-20 * self.jump_scale)
        if keys[pygame.K_d] and self.rect.x < 1080:
            self.rect.x += self.vel
            self.right = True
            self.left = False

        if keys[pygame.K_a] and self.rect.x > -25:
            self.rect.x -= self.vel
            self.right = False
            self.left = True

        if not keys[pygame.K_d] and not [pygame.K_a]:
            self.right = False
            self.left = False

        return self.rect.x

    def character_animation(self):
        keys = pygame.key.get_pressed()
        if self.left and self.rect.bottom == self.floor:
            self.player_index += .15
            self.image = self.player_walk_left[int(self.player_index)]
        if self.player_index >= 3.85 and self.left:
            self.player_index = 1
        if self.right and self.rect.bottom == self.floor:
            if self.player_index < 4:
                self.player_index = 4
            self.player_index += .15
            self.image = self.player_walk_left[int(self.player_index)]
        if self.player_index >= 6 and self.right:
            self.player_index = 4
        if keys[pygame.K_a] and keys[pygame.K_d]:
            self.player_index = 0
            self.image = self.player_walk_left[self.player_index]
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.player_index = 0
            self.image = self.player_walk_left[self.player_index]
        if self.right and self.rect.bottom != self.floor:
            self.player_index = 5
            self.image = self.player_walk_left[self.player_index]
        if self.left and self.rect.bottom != self.floor:
            self.player_index = 2
            self.image = self.player_walk_left[self.player_index]
        if not keys[pygame.K_a] and not keys[pygame.K_d] and self.rect.bottom != self.floor:
            self.player_index = 0
            self.image = self.player_walk_left[self.player_index]

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        rect_x = self.rect.x
        if self.rect.bottom >= self.floor:
            self.gravity = 0
            self.rect.bottom = self.floor
        return rect_x

    def player_top(self):
        player_top = self.rect.y

        return int(player_top)

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.character_animation()
        self.player_top()



character = pygame.sprite.GroupSingle()
character.add(Player())

player_top = Player.player_top(Player())

objects = 2
character_health = 1100


class Objects(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if objects == 1:
            self.scale = 200
            missel = pygame.image.load("pygamefiles/images/missel.png")
            missel_scale = pygame.transform.scale(missel, (self.scale, self.scale))
            explo = pygame.image.load("pygamefiles/images/explosion.png")
            explosion = pygame.transform.scale(explo, (self.scale, self.scale))

            self.decimal = 0
            self.rocket_speed = 10
            self.rocket_floor = 600
            self.animation_index = 0
            self.frames = [missel_scale, explosion]
            self.image = self.frames[self.animation_index]
            self.rect = self.image.get_rect(center=(random.randint(0, screen_width-self.image.get_width())+50, random.randint(200, 400)*-1))
        if objects == 2:
            bone1 = get_image(bone_sheet, 0, 0, 32, 32, 4, BLACK)
            bone2 = get_image(bone_sheet, 1, 0, 32, 32, 4, BLACK)
            bone3 = get_image(bone_sheet, 2, 0, 32, 32, 4, BLACK)
            bone4 = get_image(bone_sheet, 3, 0, 32, 32, 4, BLACK)
            self.bone_spin_bones = [bone1, bone2, bone3, bone4, bone4]
            self.bone_index = 0
            self.image = self.bone_spin_bones[self.bone_index]
            self.rect = self.image.get_rect(topleft=(random.randint(0, screen_width-self.image.get_width())+50, random.randint(200, 400)*-1))

    def object_move(self):
        if objects == 1:
            if self.rect.bottom < self.rocket_floor:
                self.rect.y += self.rocket_speed
        if objects == 2:
            self.rect.y += 6

    def animation_state(self):
        if objects == 1:
            if self.rect.bottom >= self.rocket_floor:
                self.animation_index = 1
                self.image = self.frames[self.animation_index]
        if objects == 2:
            self.bone_index += .23
            if self.bone_index > 4:
                self.bone_index = 0
            self.image = self.bone_spin_bones[int(self.bone_index)]

    def remove_rocket(self):
        if objects == 1:
            if pygame.sprite.spritecollideany(character.sprite, object_group, None) and self.rect.y + 250 < Player.apply_gravity(Player()) and self.rect.x in range(Player.player_input(Player())-300):
                self.rocket_floor = Player.apply_gravity(Player()) - 50
            else:
                self.rocket_floor = 600
            if self.animation_index == 1 and self.rect.bottom >= self.rocket_floor:
                self.rect.y += self.decimal
                self.decimal += .05
                self.scale -= 1
                self.image = self.frames[self.animation_index]
            if self.rect.bottom > self.rocket_floor + 9:
                self.kill()
        if objects == 2:
            if self.rect.y > 800:
                self.kill()

    def collide(self):
        if pygame.sprite.spritecollideany(character.sprite, object_group, None):
            self.kill()

    def update(self):
        self.object_move()
        self.animation_state()
        self.remove_rocket()
        # self.collide()


object_group = pygame.sprite.Group()


clock = pygame.time.Clock()

#  Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 300)

game_active = False
background = 0
un_active_screen = 1

FPS = 30
missel_rect_color_display = BLUE
bone_color_display = BLUE

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == obstacle_timer and game_active:
            object_group.add(Objects())

    if game_active:

        if background == 1:
            screen.blit(test_surface_image_scale, (0, 0))
        if background == 2:
            screen.blit(grass_surface_image_scale, (0, 0))
        if background == 3:
            screen.blit(space_surface_image_scale, (0, 0))

        if collision():
            character_health -= 2

        character.draw(screen)
        character.update()



        pygame.draw.rect(screen, RED, (50, 40, 1100, 50))
        pygame.draw.rect(screen, GREEN, (50, 40, character_health, 50))
        object_group.draw(screen)
        object_group.update()

    elif un_active_screen == 1:
        text_surface_cyberpunk_opening = pygame.transform.scale(test_surface_image, (1200 / 3, 700 / 3))
        cyberpunk_opening_rect = text_surface_cyberpunk_opening.get_rect(topleft=((
        (screen_width - 2 * text_surface_cyberpunk_opening.get_width()) / 3,
        (screen_height - text_surface_cyberpunk_opening.get_height()) / 3)))


        grass_surface_image_scale_opening = pygame.transform.scale(grass_surface_image,
                                                                   (screen_width / 3, screen_height / 3))
        grass_surface_image_scale_opening_rect = grass_surface_image_scale_opening.get_rect(topleft=((
                                                                                                                 screen_width - 2 * text_surface_cyberpunk_opening.get_width()) * 2 / 3 + text_surface_cyberpunk_opening.get_width(),
                                                                                                     (
                                                                                                                 screen_height - text_surface_cyberpunk_opening.get_height()) / 3))


        space_surface_image_scale_opening = pygame.transform.scale(space_surface_image,
                                                                   (screen_width // 3, screen_height / 3))
        space_surface_image_scale_opening_rect = space_surface_image_scale_opening.get_rect(
            topleft=(int(screen_width / 2 - int(space_surface_image_scale_opening.get_width() / 2)), 430))
        mouse_pos = pygame.mouse.get_pos()
        screen.fill((111, 196, 169))
        screen.blit(text_surface_cyberpunk_opening, cyberpunk_opening_rect)
        screen.blit(grass_surface_image_scale_opening, grass_surface_image_scale_opening_rect)
        screen.blit(space_surface_image_scale_opening, space_surface_image_scale_opening_rect)
        screen.blit(intro_font_words, (135, 10))
        if pygame.mouse.get_pressed()[0] and cyberpunk_opening_rect.collidepoint(mouse_pos):
            background = 1
            un_active_screen = 2
            pygame.time.delay(200)
        if pygame.mouse.get_pressed()[0] and grass_surface_image_scale_opening_rect.collidepoint(mouse_pos):
            background = 2
            un_active_screen = 2
            pygame.time.delay(200)
        if pygame.mouse.get_pressed()[0] and space_surface_image_scale_opening_rect.collidepoint(mouse_pos):
            background = 3
            un_active_screen = 2
            pygame.time.delay(200)

    elif un_active_screen == 2:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill((111, 196, 169))
        bone1 = get_image(bone_sheet, 0, 0, 32, 60, 8, BLACK)
        bone2 = get_image(bone_sheet, 1, 0, 32, 60, 8, BLACK)
        bone3 = get_image(bone_sheet, 2, 0, 32, 60, 8, BLACK)
        bone4 = get_image(bone_sheet, 3, 0, 32, 60, 8, BLACK)

        bone_spin_bones = [bone1, bone2, bone3, bone4, bone4]

        bone_image = bone_spin_bones[bone_index]
        bone_rect = bone_image.get_rect(topleft=(225, screen_height/2 - bone_image.get_height()/2+110))

        FPS = 20

        bone_index += 1
        bone_image = bone_spin_bones[bone_index]
        if bone_index == 4:
            bone_index = 0

        bone_rect_color = pygame.Rect(200, 200, 300, 300)
        pygame.draw.rect(screen, bone_color_display, bone_rect_color)
        screen.blit(bone_image, bone_rect)



        missel = pygame.image.load("pygamefiles/images/missel.png")
        missel_scale = pygame.transform.scale(missel, (270, 270))
        missel_rect = missel_scale.get_rect(topleft=(713, screen_height/2-missel_scale.get_height()/2-10))

        missel_rect_color = pygame.Rect(700, 200, 300, 300)
        pygame.draw.rect(screen, missel_rect_color_display, missel_rect_color)
        screen.blit(missel_scale, missel_rect)

        intro_font = pygame.font.SysFont("comicsans", 100)
        intro_font_words = intro_font.render("select a projectile", False, BLACK)
        screen.blit(intro_font_words, (screen_width/2-intro_font_words.get_width()/2, 20))

        if missel_rect_color.collidepoint(mouse_pos):
            missel_rect_color_display = RED
        else:
            missel_rect_color_display = BLUE
        if bone_rect_color.collidepoint(mouse_pos):
            bone_color_display = RED
        else:
            bone_color_display = BLUE
        if missel_rect_color.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            un_active_screen = 3
            game_active = True
            objects = 1
            FPS = 60

        if bone_rect_color.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            un_active_screen = 3
            game_active = True
            objects = 2
            FPS = 60

    pygame.display.update()

pygame.quit()
