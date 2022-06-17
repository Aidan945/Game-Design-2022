# Aidan Zarski
import pygame, random, os
os.system('cls')

level_map_1 = [
'                             ',
'                                                   ', 
'                                                   ',
'                                                   ',
'                                                   ',
' XX     L                                          ',
' XX P                                              ',
' XXXX                                           X  ',
' XXXX                                     XXX      ',
' XX    X  XXXX        XX             XX            ',
'       X  XXXX    XX  XXX      XX                  ',
'     XXX  XXXXXX  XX  XXXX                         ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

TILE_SIZE = 64
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = TILE_SIZE * len(level_map_1)
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

CHARACTER_SPEED = 8 # how fast the character moves

def get_image(sheet, frame_x, frame_y, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame_x*width), (frame_y*height), width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)

    return image

# the size of the player
scale = 1.5

class Player(pygame.sprite.Sprite):
    def __init__(self, choose_character, player_x, player_y):
        super().__init__()
        self.gravity = 1.5
        self.jump_scale = 1.2
        self.jump_vel = 25
        self.vel = CHARACTER_SPEED
        self.jump = False
        self.left = False
        self.right = False
        self.character_x = player_x
        self.character_y = player_y
        self.floor = 600
        self.on_ground = False
        self.on_ceiling = False





        priest_sheet = pygame.image.load("pygamefiles/images/priestsheet.png")
        front = get_image(priest_sheet, 1, 2, 48, 64, scale, "black")
        left_1 = get_image(priest_sheet, 0, 3, 48, 64, scale, "black")
        left_2 = get_image(priest_sheet, 1, 3, 48, 64, scale, "black")
        left_3 = get_image(priest_sheet, 2, 3, 48, 64, scale, "black")
        right_1 = get_image(priest_sheet, 0, 1, 48, 64, scale, "black")
        right_2 = get_image(priest_sheet, 1, 1, 48, 64, scale, "black")
        right_3 = get_image(priest_sheet, 2, 1, 48, 64, scale, "black")
        self.player_walk_left = [front, left_1, left_2, left_3, right_1, right_2, right_3, right_3]
        self.player_index = 0
        self.image = self.player_walk_left[self.player_index]
        self.rect = self.image.get_rect(topleft=(self.character_x, self.character_y))
        
        self.direction = pygame.math.Vector2(0, 0)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.direction.y == 0 and not self.on_ceiling:
            self.direction.y = -self.jump_vel
        elif keys[pygame.K_d]:
            self.direction.x = 1
            # self.rect.x += self.direction.x * self.vel
            self.right = True
            self.left = False

        elif keys[pygame.K_a]:
            self.direction.x = -1
            # self.rect.x += self.direction.x * self.vel
            self.right = False
            self.left = True

        elif not keys[pygame.K_d] and [pygame.K_a]:
            self.direction.x = 0
            self.right = False
            self.left = False

    def character_animation(self):
        keys = pygame.key.get_pressed()
        if self.left and self.direction.y == 0:
            self.player_index += .15
            self.image = self.player_walk_left[int(self.player_index)]
        if self.player_index >= 3.85 and self.left:
            self.player_index = 1
        if self.right and self.direction.y == 0:
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
        if self.right and self.direction.y != 0:
            self.player_index = 5
            self.image = self.player_walk_left[self.player_index]
        if self.left and self.direction.y != 0:
            self.player_index = 2
            self.image = self.player_walk_left[self.player_index]
        if not keys[pygame.K_a] and not keys[pygame.K_d] and self.direction.y != 0:
            self.player_index = 0
            self.image = self.player_walk_left[self.player_index]

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
        # if self.rect.bottom >= self.floor:
        #     self.gravity = 0
        #     self.rect.bottom = self.floor
        
    def update(self):
        self.player_input()
        self.character_animation()


class Default_Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class Floating_tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size*2, size*.5))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift    



class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_shift = 0
        self.current_x = 0

        #dust
        self.dust_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False

    def setup_level(self, layout): # this function sets uf the level using the layout.
        self.player = pygame.sprite.GroupSingle() # creates a single sprite group for the player
        self.tiles = pygame.sprite.Group() # creates a sprite group for the tiles.
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if val == 'X':
                    tile = Default_Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile)
                if val == "P":
                    tile = Floating_tile((x, y), TILE_SIZE)
                    self.tiles.add(tile)

                if val == 'P':
                    player = Player(1, x, y)
                    self.player.add(player)

    def scroll_horizontal(self): # this function moves the level horizontaly 
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < SCREEN_WIDTH//3 and direction_x < 0:
            self.world_shift = CHARACTER_SPEED
            player.vel = 0

        elif player_x > (3 * SCREEN_WIDTH//5 + TILE_SIZE) and direction_x > 0:
            self.world_shift = -CHARACTER_SPEED
            player.vel = 0

        else:
            player.vel = CHARACTER_SPEED
            self.world_shift = 0

    def horizontal_movement_collisions(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.vel

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    self.current_x = player.rect.right

    def vertical_movement_collisions(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.on_ground = True
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.on_ceiling = True
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling = False

    def run(self):

        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_horizontal()

        # player
        self.player.update()
        self.horizontal_movement_collisions()
        self.vertical_movement_collisions()
        self.player.draw(self.display_surface)

Level_1 = Level(level_map_1, screen)

clock = pygame.time.Clock()
FPS = 60
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill("blue")        


    Level_1.run()

      


    pygame.display.update()


        
