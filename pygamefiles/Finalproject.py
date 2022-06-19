# Aidan Zarski
from ast import Return
from glob import glob
from itertools import count
from turtle import title
import pygame, time,os,random, math, sys, datetime
pygame.init()
os.system('cls')

level_map_1 = [
'                                                                                                                                      ',
'                                                                                                                                      ', 
'                                                                                                                                      ',
'                                                                                                                                      ',
'                                                                                                                           E          ',
'                                                             CC   CC   CC   CC   CCC  CCC  CCC  CCC  CCC  CCC  CCC  CCC                ',
'         P CC                                           CC   L    L    L    L    XXX  XXX  XXX  XXX  XXX  XXX  XXX  XXX  XXX          ',
'         XXXX                                     CCCC  XX                                                                            ',
'         XXXX    CCCCCCC   X  CCCCC         CC    XXXX                                                                                ',
'         XX      XXXXXXX      XXXXX   CCC   XX                                                                                        ',
'                 XXXXXXX      XXXX    XXX                                                                                             ',
'                 XXXXXXX      XXXX                                                                                                    ',
'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD']
level_map_2 = [
'                                                                                                                                     D',
'                                                                                                                                     D', 
'                                                                                                                                     D',
'                                                                                                                                     D',
'                                                              CCCC                                                          E        D',
'                                                            C XXXX    CC   CC   CC  CC  CC  CC       CCC  CCC    CC   CC        CCC  D',
'         P                                              C   X         L    L    XX  XX  XX  XX   C   XXX  XXX    L    L   XXXXXXXXX  D',
'             CC                                   CCCC  X                                        X                                   D',
'        L    L    CCCCCC   X  CCCCC          CC   XXXX                                                                               D',
'                 XXXXXXX      XXXXX   CCC    XX                                                                                      D',
'                 XXXXXXX      XXXX    XXX                                                                                            D',
'                 XXXXXXX      XXXX                                                                                                   D',
'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD']
level_map_3 = [
'D                                                                                                                                     ',
'D                                                                                                                                     ', 
'D                                                                                                                                     ',
'D     P                                         CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC                                             ',
'D    XXX                                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                             ',
'D                                               X                                                                                     ',
'D          L                                 L  X  E                                                                                  ',
'D                   C                    CC     X       CC                                                                           ',
'D                CCC CCC      CCCC       L      XXXXXXXXXXX  L         CC  CC   CCCCC                                                 ',
'D                XXX XXX  CC  XXXX   CC                           L    L   L    XXXXX   L                                             ',
'D                XXX XXX  L   XXXX   L                                                                                                ',
'D                XXX XXX      XXXX                                                                                                    ',
'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD']
level_map_4 = [
'D                                                                                                                                     ',
'D                                                                                                                                     ', 
'D                                                                                     CC                    CC  CCCCCCCCCC            ',
'D                        CC   CC  CC  CC  CCC  CC  CCC   CCC  CC  CC  CC  XXX    CC   XX   CC  CCC  CCCCCC  L   XXXXXXXXXX            ',
'D                        L    L   L   L   XXX  L   XXX   XXX  L   L   L   XXX    XX        XX  XXX  XXXXXX               D            ',
'D                     CC                                                                                                 D            ',
'D                     XX                                                                                                 D            ',
'D         P         X                                                                                                    D            ',
'D        XXXXXXXXXXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD            ',
'D        XX    E                                                                                                                      ',
'D                  CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC              ',
'D            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX        ',
'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD']
level_map_5 = [
'D                                                                                                                                    D',
'D                                                                                                                                    D', 
'D                                                                                                                                    D',
'D                                                                                                                                    D',
'D                                                                                                                         XXX        D',
'D                                    CC   CC   CC           L   L   L   L                                             XX    D        D',
'D                   C  L             XX   XX   XX        C                  L                                    XX         D        D',
'D   P               X             X                 L    X                      L    X  L  X    L    X    L    X            D        D',
'DXXXXXXXXDDXXDDXDDXXXXXDDDDDXXXXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD        D',
'DE                                                                                                                                   D',
'D  CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC   D',
'DXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXD',
'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD']

TILE_SIZE = 64
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = TILE_SIZE * len(level_map_1)
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)



colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),
"RED" : (255, 0, 0),
"GREEN" : (0, 255, 0),
"BLUE" : (0, 0,255),
# SHADES,
"BLACK" : (0, 0, 0),
"DARK_GREY" : (60, 60, 60),
"DARK_SLATE_GREY" : (47, 79, 79),
"DIM_GREY" : (105, 105, 105),
"FREE_SPEECH_GREY" : (99, 86, 136),
"GREY" : (190, 190, 190),
"GREY0" : (0, 0, 0),
"GREY1" : (3, 3, 3),
"GREY2" : (5, 5, 5),
"GREY3" : (8, 8, 8),
"GREY4" : (10, 10, 10),
"GREY5" : (13, 13, 13),
"GREY6" : (15, 15, 15),
"GREY7" : (18, 18, 18),
"GREY8" : (20, 20, 20),
"GREY9" : (23, 23, 23),
"GREY10" : (26, 26, 26),
"GREY11" : (28, 28, 28),
"GREY12" : (31, 31, 31),
"GREY13" : (33, 33, 33),
"GREY14" : (36, 36, 36),
"GREY15" : (38, 38, 38),
"GREY16" : (41, 41, 41),
"GREY17" : (43, 43, 43),
"GREY18" : (46, 46, 46),
"GREY19" : (48, 48, 48),
"GREY20" : (51, 51, 51),
"GREY21" : (54, 54, 54),
"GREY22" : (56, 56, 56),
"GREY23" : (59, 59, 59),
"GREY24" : (61, 61, 61),
"GREY25" : (64, 64, 64),
"GREY26" : (66, 66, 66),
"GREY27" : (69, 69, 69),
"GREY28" : (71, 71, 71),
"GREY29" : (74, 74, 74),
"GREY30" : (77, 77, 77),
"GREY31" : (79, 79, 79),
"GREY32" : (82, 82, 82),
"GREY33" : (84, 84, 84),
"GREY34" : (87, 87, 87),
"GREY35" : (89, 89, 89),
"GREY36" : (92, 92, 92),
"GREY37" : (94, 94, 94),
"GREY38" : (97, 97, 97),
"GREY39" : (99, 99, 99),
"GREY40" : (102, 102, 102),
"GREY41" : (105, 105, 105),
"GREY42" : (107, 107, 107),
"GREY43" : (110, 110, 110),
"GREY44" : (112, 112, 112),
"GREY45" : (115, 115, 115),
"GREY46" : (117, 117, 117),
"GREY47" : (120, 120, 120),
"GREY48" : (122, 122, 122),
"GREY49" : (125, 125, 125),
"GREY50" : (127, 127, 127),
"GREY51" : (130, 130, 130),
"GREY52" : (133, 133, 133),
"GREY53" : (135, 135, 135),
"GREY54" : (138, 138, 138),
"GREY55" : (140, 140, 140),
"GREY56" : (143, 143, 143),
"GREY57" : (145, 145, 145),
"GREY58" : (148, 148, 148),
"GREY59" : (150, 150, 150),
"GREY60" : (153, 153, 153),
"GREY61" : (156, 156, 156),
"GREY62" : (158, 158, 158),
"GREY63" : (161, 161, 161),
"GREY64" : (163, 163, 163),
"GREY65" : (166, 166, 166),
"GREY66" : (168, 168, 168),
"GREY67" : (171, 171, 171),
"GREY68" : (173, 173, 173),
"GREY69" : (176, 176, 176),
"GREY70" : (179, 179, 179),
"GREY71" : (181, 181, 181),
"GREY72" : (184, 184, 184),
"GREY73" : (186, 186, 186),
"GREY74" : (189, 189, 189),
"GREY75" : (191, 191, 191),
"GREY76" : (194, 194, 194),
"GREY77" : (196, 196, 196),
"GREY78" : (199, 199, 199),
"GREY79" : (201, 201, 201),
"GREY80" : (204, 204, 204),
"GREY81" : (207, 207, 207),
"GREY82" : (209, 209, 209),
"GREY83" : (212, 212, 212),
"GREY84" : (214, 214, 214),
"GREY85" : (217, 217, 217),
"GREY86" : (219, 219, 219),
"GREY87" : (222, 222, 222),
"GREY88" : (224, 224, 224),
"GREY89" : (227, 227, 227),
"GREY90" : (229, 229, 229),
"GREY91" : (232, 232, 232),
"GREY92" : (235, 235, 235),
"GREY93" : (237, 237, 237),
"GREY94" : (240, 240, 240),
"GREY95" : (242, 242, 242),
"GREY96" : (245, 245, 245),
"GREY97" : (247, 247, 247),
"GREY98" : (250, 250, 250),
"GREY99" : (252, 252, 252),
"LIGHT_GREY" : (211, 211, 211),
"SLATE_GREY" : (112, 128, 144),
"SLATE_GREY_1" : (198, 226, 255),
"SLATE_GREY_2" : (185, 211, 238),
"SLATE_GREY_3" : (159, 182, 205),
"SLATE_GREY_4" : (108, 123, 139),
"VERY_LIGHT_GREY" : (205, 205, 205),
"WHITE" : (255, 255,255),
 
 
"ALICE_BLUE" : (240, 248, 255),
"AQUA" : (0, 255, 255),
"AQUAMARINE" : (127, 255, 212),
"AQUAMARINE_1" : (127, 255, 212),
"AQUAMARINE_2" : (118, 238, 198),
"AQUAMARINE_3" : (102, 205, 170),
"AQUAMARINE_4" : (69, 139, 116),
"AZURE" : (240, 255, 255),
"AZURE_1" : (240, 255, 255),
"AZURE_2" : (224, 238, 238),
"AZURE_3" : (193, 205, 205),
"AZURE_4" : (131, 139, 139),
"BLUE_1" : (0, 0, 255),
"BLUE_2" : (0, 0, 238),
"BLUE_3" : (0, 0, 205),
"BLUE_4" : (0, 0, 139),
"BLUE_VIOLET" : (138, 43, 226),
"CADET_BLUE" : (95, 159, 159),
"CADET_BLUE_1" : (1152, 245, 255),
"CADET_BLUE_2" : (142, 229, 238),
"CADET_BLUE_3" : (122, 197, 205),
"CADET_BLUE_4" : (83, 134, 139),
"CORN_FLOWER_BLUE" : (66, 66, 111),
"CYAN" : (0, 255, 255),
"CYAN_1" : (0, 255, 255),
"CYAN_2" : (0, 238, 238),
"CYAN_3" : (0, 205, 205),
"CYAN_4" : (0, 139, 139),
"DARK_SLATE_BLUE" : (36, 24, 130),
"DARK_TURQUOISE" : (112, 147, 219),
"DEEP_SKY_BLUE" : (0, 191, 255),
"DEEP_SKY_BLUE_1" : (0, 191, 255),
"DEEP_SKY_BLUE_2" : (0, 178, 238),
"DEEP_SKY_BLUE_3" : (0, 154, 205),
"DEEP_SKY_BLUE_4" : (0, 104, 139),
"DODGER_BLUE" : (30, 144, 255),
"DODGER_BLUE_1" : (30, 144, 255),
"DODGER_BLUE_2" : (28, 134, 238),
"DODGER_BLUE_3" : (24, 116, 205),
"DODGER_BLUE_4" : (16, 78, 139),
"FREE_SPEECH_BLUE" : (65, 86, 197),
"LIGHT_BLUE" : (173, 216, 230),
"LIGHT_BLUE_1" : (191, 239, 255),
"LIGHT_BLUE_2" : (178, 223, 238),
"LIGHT_BLUE_3" : (154, 192, 205),
"LIGHT_BLUE_4" : (104, 131, 139),
"LIGHT_CYAN" : (224, 255, 255),
"LIGHT_CYAN_1" : (224, 255, 255),
"LIGHT_CYAN_2" : (209, 238, 238),
"LIGHT_CYAN_3" : (180, 205, 205),
"LIGHT_CYAN_4" : (122, 139, 139),
"LIGHT_SKY_BLUE" : (135, 206, 250),
"LIGHT_SKY_BLUE_1" : (176, 226, 255),
"LIGHT_SKY_BLUE_2" : (164, 211, 238),
"LIGHT_SKY_BLUE_3" : (141, 182, 205),
"LIGHT_SKY_BLUE_4" : (96, 123, 139),
"LIGHT_SLATE_BLUE" : (132, 112, 255),
"LIGHT_STEEL_BLUE" : (176, 196, 222),
"LIGHT_STEEL_BLUE_1" : (202, 225, 255),
"LIGHT_STEEL_BLUE_2" : (188, 210, 238),
"LIGHT_STEEL_BLUE_3" : (162, 181, 205),
"LIGHT_STEEL_BLUE_4" : (110, 123, 139),
"MEDIUM_BLUE" : (0, 0, 205),
"MEDIUM_SLATE_BLUE" : (123, 104, 238),
"MEDIUM_TURQUOISE" : (72, 209, 204),
"MIDNIGHT_BLUE" : (25, 25, 112),
"NAVY" : (0, 0, 128),
"NAVY_BLUE" : (0, 0, 128),
"NEON_BLUE" : (77, 77, 255),
"NEW_MIDNIGHT_BLUE" : (0, 0, 156),
"PALE_TURQUOISE" : (187, 255, 255),
"PALE_TURQUOISE_1" : (187, 255, 255),
"PALE_TURQUOISE_2" : (174, 238, 238),
"PALE_TURQUOISE_3" : (150, 205, 205),
"PALE_TURQUOISE_4" : (102, 139, 139),
"POWDER_BLUE" : (176, 224, 230),
"RICH_BLUE" : (89, 89, 171),
"ROYAL_BLUE" : (65, 105, 225),
"ROYAL_BLUE_1" : (72, 118, 255),
"ROYAL_BLUE_2" : (67, 110, 238),
"ROYAL_BLUE_3" : (58, 95, 205),
"ROYAL_BLUE_4" : (39, 64, 139),
"ROYAL_BLUE_5" : (0, 34, 102),
"SKY_BLUE" : (135, 206, 235),
"SKY_BLUE_1" : (135, 206, 255),
"SKY_BLUE_2" : (126, 192, 238),
"SKY_BLUE_3" : (108, 166, 205),
"SKY_BLUE_4" : (74, 112, 139),
"SLATE_BLUE" : (131, 111, 255),
"SLATE_BLUE_1" : (122, 103, 238),
"SLATE_BLUE_2" : (122, 103, 238),
"SLATE_BLUE_3" : (105, 89, 205),
"SLATE_BLUE_4" : (71, 60, 139),
"STEEL_BLUE" : (70, 130, 180),
"STEEL_BLUE_1" : (99, 184, 255),
"STEEL_BLUE_2" : (92, 172, 238),
"STEEL_BLUE_3" : (79, 148, 205),
"STEEL_BLUE_4" : (54, 100, 139),
"SUMMER_SKY" : (56, 176, 222),
"TEAL" : (0, 128, 128),
"TRUE_IRIS_BLUE" : (3, 180, 204),
"TURQUOISE" : (64, 224, 208),
"TURQUOISE_1" : (0, 245, 255),
"TURQUOISE_2" : (0, 229, 238),
"TURQUOISE_3" : (0, 197, 205),
"TURQUOISE_4" : (0, 134,139),
 
 
"BAKERS_CHOCOLATE" : (92, 51, 23),
"BEIGE" : (245, 245, 220),
"BROWN" : (166, 42, 42),
"BROWN_1" : (255, 64, 64),
"BROWN_2" : (238, 59, 59),
"BROWN_3" : (205, 51, 51),
"BROWN_4" : (139, 35, 35),
"BURLYWOOD" : (222, 184, 135),
"BURLYWOOD_1" : (255, 211, 155),
"BURLYWOOD_2" : (238, 197, 145),
"BURLYWOOD_3" : (205, 170, 125),
"BURLYWOOD_4" : (139, 115, 85),
"CHOCOLATE" : (210, 105, 30),
"CHOCOLATE_1" : (255, 127, 36),
"CHOCOLATE_2" : (238, 118, 33),
"CHOCOLATE_3" : (205, 102, 29),
"CHOCOLATE_4" : (139, 69, 19),
"DARK_BROWN" : (92, 64, 51),
"DARK_TAN" : (151, 105, 79),
"DARK_WOOD" : (133, 94, 66),
"LIGHT_WOOD" : (133, 99, 99),
"MEDIUM_WOOD" : (166, 128, 100),
"NEW_TAN" : (235, 199, 158),
"PERU" : (205, 133, 63),
"ROSY_BROWN" : (188, 143, 143),
"ROSY_BROWN_1" : (255, 193, 193),
"ROSY_BROWN_2" : (238, 180, 180),
"ROSY_BROWN_3" : (205, 155, 155),
"ROSY_BROWN_4" : (139, 105, 105),
"SADDLE_BROWN" : (139, 69, 19),
"SANDY_BROWN" : (244, 164, 96),
"SEMI_SWEET_CHOCOLATE" : (107, 66, 38),
"SIENNA" : (142, 107, 35),
"TAN" : (219, 147, 112),
"TAN_1" : (255, 165, 79),
"TAN_2" : (238, 154, 73),
"TAN_3" : (205, 133, 63),
"TAN_4" : (139, 90, 43),
"VERY_DARK_BROWN" : (92, 64,51),
 
"CHARTREUSE" : (127, 255, 0),
"CHARTREUSE_1" : (127, 255, 0),
"CHARTREUSE_2" : (118, 238, 0),
"CHARTREUSE_3" : (102, 205, 0),
"CHARTREUSE_4" : (69, 139, 0),
"DARK_GREEN" : (47, 79, 47),
"DARK_GREEN_COPPER" : (74, 118, 110),
"DARK_KHAKI" : (189, 183, 107),
"DARK_OLIVE_GREEN" : (85, 107, 47),
"DARK_OLIVE_GREEN_1" : (202, 255, 112),
"DARK_OLIVE_GREEN_2" : (188, 238, 104),
"DARK_OLIVE_GREEN_3" : (162, 205, 90),
"DARK_OLIVE_GREEN_4" : (110, 139, 61),
"DARK_SEA_GREEN" : (143, 188, 143),
"DARK_SEA_GREEN_1" : (193, 255, 193),
"DARK_SEA_GREEN_2" : (180, 238, 180),
"DARK_SEA_GREEN_3" : (155, 205, 155),
"DARK_SEA_GREEN_4" : (105, 139, 105),
"FOREST_GREEN" : (34, 139, 34),
"FREE_SPEECH_GREEN" : (9, 249, 17),
"GREEN_1" : (0, 255, 0),
"GREEN_2" : (0, 238, 0),
"GREEN_3" : (0, 205, 0),
"GREEN_4" : (0, 139, 0),
"GREEN_YELLOW" : (173, 255, 47),
"KHAKI" : (240, 230, 140),
"KHAKI_1" : (255, 246, 143),
"KHAKI_2" : (238, 230, 133),
"KHAKI_3" : (205, 198, 115),
"KHAKI_4" : (139, 134, 78),
"LAWN_GREEN" : (124, 252, 0),
"LIGHT_SEA_GREEN" : (32, 178, 170),
"LIME" : (0, 255, 0),
"MEDIUM_SEA_GREEN" : (60, 179, 113),
"MEDIUM_SPRING_GREEN" : (0, 250, 154),
"MINT_CREAM" : (245, 255, 250),
"OLIVE" : (128, 128, 0),
"OLIVE_DRAB" : (107, 142, 35),
"OLIVE_DRAB_1" : (192, 255, 62),
"OLIVE_DRAB_2" : (179, 238, 58),
"OLIVE_DRAB_3" : (154, 205, 50),
"OLIVE_DRAB_4" : (105, 139, 34),
"PALE_GREEN" : (152, 251, 152),
"PALE_GREEN_1" : (154, 255, 154),
"PALE_GREEN_2" : (144, 238, 144),
"PALE_GREEN_3" : (124, 205, 124),
"PALE_GREEN_4" : (84, 139, 84),
"SEA_GREEN" : (46, 139, 87),
"SEA_GREEN_1" : (84, 255, 159),
"SEA_GREEN_2" : (78, 238, 148),
"SEA_GREEN_3" : (67, 205, 128),
"SEA_GREEN_4" : (46, 139, 87),
"SPRING_GREEN" : (0, 255, 127),
"SPRING_GREEN_1" : (0, 255, 127),
"SPRING_GREEN_2" : (0, 238, 118),
"SPRING_GREEN_3" : (0, 205, 102),
"SPRING_GREEN_4" : (0, 139, 69),
"YELLOW_GREEN" : (154, 205,50),
"BISQUE" : (255, 228, 196),
"BISQUE_1" : (255, 228, 196),
"BISQUE_2" : (238, 213, 183),
"BISQUE_3" : (205, 183, 158),
"BISQUE_4" : (139, 125, 107),
"CORAL" : (255, 127, 0),
"CORAL_1" : (255, 114, 86),
"CORAL_2" : (238, 106, 80),
"CORAL_3" : (205, 91, 69),
"CORAL_4" : (139, 62, 47),
"DARK_ORANGE" : (255, 140, 0),
"DARK_ORANGE_1" : (255, 127, 0),
"DARK_ORANGE_2" : (238, 118, 0),
"DARK_ORANGE_3" : (205, 102, 0),
"DARK_ORANGE_4" : (139, 69, 0),
"DARK_SALMON" : (233, 150, 122),
"HONEYDEW" : (240, 255, 240),
"HONEYDEW_1" : (240, 255, 240),
"HONEYDEW_2" : (224, 238, 224),
"HONEYDEW_3" : (193, 205, 193),
"HONEYDEW_4" : (131, 139, 131),
"LIGHT_CORAL" : (240, 128, 128),
"LIGHT_SALMON" : (255, 160, 122),
"LIGHT_SALMON_1" : (255, 160, 122),
"LIGHT_SALMON_2" : (238, 149, 114),
"LIGHT_SALMON_3" : (205, 129, 98),
"LIGHT_SALMON_4" : (139, 87, 66),
"MANDARIN_ORANGE" : (142, 35, 35),
"ORANGE" : (255, 165, 0),
"ORANGE_1" : (255, 165, 0),
"ORANGE_2" : (238, 154, 0),
"ORANGE_3" : (205, 133, 0),
"ORANGE_4" : (139, 90, 0),
"ORANGE_RED" : (255, 36, 0),
"PEACH_PUFF" : (255, 218, 185),
"PEACH_PUFF_1" : (255, 218, 185),
"PEACH_PUFF_2" : (238, 203, 173),
"PEACH_PUFF_3" : (205, 175, 149),
"PEACH_PUFF_4" : (139, 119, 101),
"SALMON" : (250, 128, 114),
"SALMON_1" : (255, 140, 105),
"SALMON_2" : (238, 130, 98),
"SALMON_3" : (205, 112, 84),
"SALMON_4" : (139, 76, 57),
"SIENNA_1" : (255, 130, 71),
"SIENNA_2" : (238, 121, 66),
"SIENNA_3" : (205, 104, 57),
"SIENNA_4" : (139, 71, 38),
"DEEP_PINK," : (255, 20, 147),
"DEEP_PINK_1" : (255, 20, 147),
"DEEP_PINK_2" : (238, 18, 137),
"DEEP_PINK_3" : (205, 16, 118),
"DEEP_PINK_4" : (139, 10, 80),
"DUSTY_ROSE" : (133, 99, 99),
"FIREBRICK" : (178, 34, 34),
"FIREBRICK_1" : (255, 48, 48),
"FIREBRICK_2" : (238, 44, 44),
"FIREBRICK_3" : (205, 38, 38),
"FIREBRICK_4" : (139, 26, 26),
"FELDSPAR" : (209, 146, 117),
"FLESH" : (245, 204, 176),
"FREE_SPEECH_MAGENTA" : (227, 91, 216),
"FREE_SPEECH_RED" : (192, 0, 0),
"HOT_PINK" : (255, 105, 180),
"HOT_PINK_1" : (255, 110, 180),
"HOT_PINK_2" : (238, 106, 167),
"HOT_PINK_3" : (205, 96, 144),
"HOT_PINK_4" : (139, 58, 98),
"INDIAN_RED" : (205, 92, 92),
"INDIAN_RED_1" : (255, 106, 106),
"INDIAN_RED_2" : (238, 99, 99),
"INDIAN_RED_3" : (205, 85, 85),
"INDIAN_RED_4" : (139, 58, 58),
"LIGHT_PINK" : (255, 182, 193),
"LIGHT_PINK_1" : (255, 174, 185),
"LIGHT_PINK_2" : (238, 162, 173),
"LIGHT_PINK_3" : (205, 140, 149),
"LIGHT_PINK_4" : (139, 95, 101),
"MEDIUM_VIOLET_RED" : (199, 21, 133),
"MISTY_ROSE" : (255, 228, 225),
"MISTY_ROSE_1" : (255, 228, 225),
"MISTY_ROSE_2" : (238, 213, 210),
"MISTY_ROSE_3" : (205, 183, 181),
"MISTY_ROSE_4" : (139, 125, 123),
"ORANGE_RED_1" : (255, 69, 0),
"ORANGE_RED_2" : (238, 64, 0),
"ORANGE_RED_3" : (205, 55, 0),
"ORANGE_RED_4" : (139, 37, 0),
"PALE_VIOLET_RED" : (219, 112, 147),
"PALE_VIOLET_RED_1" : (255, 130, 171),
"PALE_VIOLET_RED_2" : (238, 121, 159),
"PALE_VIOLET_RED_3" : (205, 104, 137),
"PALE_VIOLET_RED_4" : (139, 71, 93),
"PINK" : (255, 192, 203),
"PINK_1" : (255, 181, 197),
"PINK_2" : (238, 169, 184),
"PINK_3" : (205, 145, 158),
"PINK_4" : (139, 99, 108),
"RED_1" : (255, 0, 0),
"RED_2" : (238, 0, 0),
"RED_3" : (205, 0, 0),
"RED_4" : (139, 0, 0),
"SCARLET" : (140, 23, 23),
"SPICY_PINK" : (255, 28, 174),
"TOMATO" : (255, 99, 71),
"TOMATO_1" : (255, 99, 71),
"TOMATO_2" : (238, 92, 66),
"TOMATO_3" : (205, 79, 57),
"TOMATO_4" : (139, 54, 38),
"VIOLET_RED" : (208, 32, 144),
"VIOLET_RED_1" : (255, 62, 150),
"VIOLET_RED_2" : (238, 58, 140),
"VIOLET_RED_3" : (205, 50, 120),
"VIOLET_RED_4" : (139, 34, 82),
 
"DARK_ORCHID," : (153, 50, 204),
"DARK_ORCHID_1" : (191, 62, 255),
"DARK_ORCHID_2" : (178, 58, 238),
"DARK_ORCHID_3" : (154, 50, 205),
"DARK_ORCHID_4" : (104, 34, 139),
"DARK_PURPLE" : (135, 31, 120),
"DARK_VIOLET" : (148, 0, 211),
"FUCHSIA" : (255, 0, 255),
"LAVENDER" : (230, 230, 250),
"LAVENDER_BLUSH" : (255, 240, 245),
"LAVENDER_BLUSH_1" : (255, 240, 245),
"LAVENDER_BLUSH_2" : (238, 224, 229),
"LAVENDER_BLUSH_3" : (205, 193, 197),
"LAVENDER_BLUSH_4" : (139, 131, 134),
"MAGENTA" : (255, 0, 255),
"MAGENTA_1" : (255, 0, 255),
"MAGENTA_2" : (238, 0, 238),
"MAGENTA_3" : (205, 0, 205),
"MAGENTA_4" : (139, 0, 139),
"MAROON" : (176, 48, 96),
"MAROON_1" : (255, 52, 179),
"MAROON_2" : (238, 48, 167),
"MAROON_3" : (205, 41, 144),
"MAROON_4" : (139, 28, 98),
"MEDIUM_ORCHID" : (186, 85, 211),
"MEDIUM_ORCHID_1" : (224, 102, 255),
"MEDIUM_ORCHID_2" : (209, 95, 238),
"MEDIUM_ORCHID_3" : (180, 82, 205),
"MEDIUM_ORCHID_4" : (122, 55, 139),
"MEDIUM_PURPLE" : (147, 112, 219),
"MEDIUM_PURPLE_1" : (171, 130, 255),
"MEDIUM_PURPLE_2" : (159, 121, 238),
"MEDIUM_PURPLE_3" : (137, 104, 205),
"MEDIUM_PURPLE_4" : (93, 71, 139),
"NEON_PINK" : (255, 110, 199),
"ORCHID" : (218, 112, 214),
"ORCHID_1" : (219, 112, 219),
"ORCHID_2" : (238, 122, 233),
"ORCHID_3" : (205, 105, 201),
"ORCHID_4" : (139, 71, 137),
"PLUM" : (221, 160, 221),
"PLUM_1" : (255, 187, 255),
"PLUM_2" : (238, 174, 238),
"PLUM_3" : (205, 150, 205),
"PLUM_4" : (139, 102, 139),
"PURPLE" : (160, 32, 240),
"PURPLE_1" : (155, 48, 255),
"PURPLE_2" : (145, 44, 238),
"PURPLE_3" : (125, 38, 205),
"PURPLE_4" : (85, 26, 139),
"THISTLE" : (216, 191, 216),
"THISTLE_1" : (255, 225, 255),
"THISTLE_2" : (238, 210, 238),
"THISTLE_3" : (205, 181, 205),
"THISTLE_4" : (139, 123, 139),
"VIOLET" : (238, 130, 238),
"VIOLET_BLUE" : (159, 95, 159),
 
"BLANCHED_ALMOND," : (255, 235, 205),
"DARK_GOLDENROD" : (184, 134, 11),
"DARK_GOLDENROD_1" : (255, 185, 15),
"DARK_GOLDENROD_2" : (238, 173, 14),
"DARK_GOLDENROD_3" : (205, 149, 12),
"DARK_GOLDENROD_4" : (139, 101, 8),
"LEMON_CHIFFON" : (255, 250, 205),
"LEMON_CHIFFON_1" : (255, 250, 205),
"LEMON_CHIFFON_2" : (238, 233, 191),
"LEMON_CHIFFON_3" : (205, 201, 165),
"LEMON_CHIFFON_4" : (139, 137, 112),
"LIGHT_GOLDENROD" : (238, 221, 130),
"LIGHT_GOLDENROD_1" : (255, 236, 139),
"LIGHT_GOLDENROD_2" : (238, 220, 130),
"LIGHT_GOLDENROD_3" : (205, 190, 112),
"LIGHT_GOLDENROD_4" : (139, 129, 76),
"LIGHT_GOLDENROD_YELLOW" : (250, 250, 210),
"LIGHT_YELLOW" : (255, 255, 224),
"LIGHT_YELLOW_1" : (255, 255, 224),
"LIGHT_YELLOW_2" : (238, 238, 209),
"LIGHT_YELLOW_3" : (205, 205, 180),
"LIGHT_YELLOW_4" : (139, 139, 122),
"PALE_GOLDENROD" : (238, 232, 170),
"PAPAYA_WHIP" : (255, 239, 213),
"CORNSILK" : (255, 248, 220),
"CORNSILK_1" : (255, 248, 220),
"CORNSILK_2" : (238, 232, 205),
"CORNSILK_3" : (205, 200, 177),
"CORNSILK_4" : (139, 236, 120),
"GOLDENROD" : (218, 165, 32),
"GOLDENROD_1" : (255, 193, 37),
"GOLDENROD_2" : (238, 180, 34),
"GOLDENROD_3" : (205, 155, 29),
"GOLDENROD_4" : (139, 105, 20),
"MOCCASIN" : (255, 228, 181),
"YELLOW" : (255, 255, 0),
"YELLOW_1" : (255, 255, 0),
"YELLOW_2" : (238, 238, 0),
"YELLOW_3" : (205, 205, 0),
"YELLOW_4" : (139, 139, 0),
"GOLD" : (255, 215, 0),
"GOLD_1" : (255, 215, 0),
"GOLD_2" : (238, 201, 0),
"GOLD_3" : (205, 173, 0),
"GOLD_4" : (139, 117, 0),
"MEDIUM_GOLDENROD" : (234, 234, 174),
"ANTIQUE_WHITE" : (250, 235, 215),
"ANTIQUE_WHITE_1" : (255, 239, 219),
"ANTIQUE_WHITE_2" : (238, 223, 204),
"ANTIQUE_WHITE_3" : (205, 192, 176),
"ANTIQUE_WHITE_4" : (139, 131, 120),
"FLORAL_WHITE" : (255, 250, 240),
"GHOST_WHITE" : (248, 248, 255),
"NAVAJO_WHITE" : (255, 222, 173),
"NAVAJO_WHITE_1" : (255, 222, 173),
"NAVAJO_WHITE_2" : (238, 207, 161),
"NAVAJO_WHITE_3" : (205, 179, 139),
"NAVAJO_WHITE_4" : (139, 121, 94),
"OLD_LACE" : (253, 245, 230),
"WHITE_SMOKE" : (245, 245, 245),
"GAINSBORO" : (220, 220, 220),
"IVORY" : (255, 255, 240),
"IVORY_1" : (255, 255, 240),
"IVORY_2" : (238, 238, 224),
"IVORY_3" : (205, 205, 193),
"IVORY_4" : (139, 139, 131),
"LINEN" : (250, 240, 230),
"SEASHELL" : (255, 245, 238),
"SEASHELL_1" : (255, 245, 238),
"SEASHELL_2" : (238, 229, 222),
"SEASHELL_3" : (205, 197, 191),
"SEASHELL_4" : (139, 134, 130),
"SNOW" : (255, 250, 250),
"SNOW_1" : (255, 250, 250),
"SNOW_2" : (238, 233, 233),
"SNOW_3" : (205, 201, 201),
"SNOW_4" : (139, 137, 137),
"WHEAT" : (245, 222, 179),
"WHEAT_1" : (255, 231, 186),
"WHEAT_2" : (238, 216, 174),
"WHEAT_3" : (205, 186, 150),
"WHEAT_4" : (139, 126, 102),
"QUARTZ" : (217, 217, 243),
}
clr=colors.get("limeGreen")
#create dispay wind with any name y like

pygame.display.set_caption("My First Game")  #change the title of my window

#images
bg=pygame.image.load('PygameFiles\images\\bgSmaller.jpg')
char = pygame.image.load('PygameFiles\images\PixelArtTutorial.png')
char = pygame.transform.scale(char, (50, 50))


#square Var
hb=50
wb=50
xb=100
yb=300

#character vars
charx = xb
chary = yb

#circle
cx=350
cy=350
rad=25

#inscribed box
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse varuables
mx = 0
my = 0

#objects to draw
square=pygame.Rect(xb,yb,wb,hb)
insSquare=pygame.Rect(xig,yig,ibox,ibox)
mountainSqaure = pygame.Rect(250, 320, 180, 250)

#collors

buttoncolor= colors.get ("limeGreen")
squareClr=colors.get("pink")
circleClr=colors.get("blue")
backgrnd=colors.get("white")

#Game control
run = True
Game = False
speed=2

#Menu items
message = ["Instructions", "Setting", "Game","Scoreboard", "Exit"]

def menu():
    screen.fill(colors.get("white"))
    ymenu = 155
    Title = TITLE_FONT.render("Game Menu", 1, colors.get("blue"))
    xd = SCREEN_WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))

    #                      x, y, width, height
    Button_1 = pygame.Rect(30, 145, 150, 50)
    Button_2 = pygame.Rect(30, 195, 150, 50)
    Button_3 = pygame.Rect(30, 245, 150, 50)
    Button_4 = pygame.Rect(30, 295, 150, 50)
    Button_5 = pygame.Rect(30, 345, 150, 50)

    pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_2)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_4)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_5)


    for item in message:
        text = MENU_FONT.render(item, 1, colors.get('blue'))
        screen.blit(text, (40, ymenu))
        pygame.display.update()
        pygame.time.delay(50)
        ymenu += 50
    run = True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    Instructions()        
                if Button_2.collidepoint((mx, my)):
                    settings()
                if Button_3.collidepoint((mx, my)):
                    run = False 
                    Title = TITLE_FONT.render("Loading...", 1, colors.get("blue"))
                    screen.blit(Title,(50,50))
                    pygame.draw.rect(screen, "blue", Button_3)        

                if Button_4.collidepoint((mx, my)):
                    scoreboard()
                if Button_5.collidepoint((mx, my)):
                    pygame.quit()
                    sys.exit()
        

            screen.fill(colors.get("white"))
            screen.blit(Title, (xd, 50))
            ymenu = 155
            pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
            pygame.draw.rect(screen, colors.get("limeGreen"), Button_2)
            pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
            pygame.draw.rect(screen, colors.get("limeGreen"), Button_4)
            pygame.draw.rect(screen, colors.get("limeGreen"), Button_5)
  
            for item in message:
                text = MENU_FONT.render(item, 1, colors.get('blue'))
                screen.blit(text, (40, ymenu))
                ymenu += 50    
            
            pygame.display.update()          

def Instructions():
    #rendering text objects
    Title = TITLE_FONT.render("Instructions", 1, colors.get("blue"))
    text1 = MENU_FONT.render("Go back", 1, colors.get("blue"))


    #fills screen with white
    screen.fill(colors.get("white"))

    #creating button options
    Button_back = pygame.Rect(200, 400, 130, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_back)


    #Instructions
    myFile = open("PygameFiles\instructions.txt", "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = SCREEN_WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    screen.blit(text1, (225, 410))


    pygame.display.update()
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
                

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_back.collidepoint((mx, my)):
                    run = False
                                     
def settings ():
    global SCREEN_WIDTH, SCREEN_HEIGHT, backgrnd, screen, buttoncolor
    Title = TITLE_FONT.render("Circle eats Square", 1, colors.get("blue"))
    screen.fill(backgrnd)
    ymenu = 155
    xd = SCREEN_WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    
    Bx= SCREEN_WIDTH//3

    Button_Color = pygame.Rect(Bx, 150, SCREEN_WIDTH//3, 40)
    Button_Background = pygame.Rect(Bx, 200, SCREEN_WIDTH//3, 40)
    Button_Sizeincrease= pygame.Rect(Bx, 250, SCREEN_WIDTH//3, 40)
    Button_Sizedecrease= pygame.Rect(Bx, 300, SCREEN_WIDTH//3, 40)
    
    
    pygame.draw.rect(screen, buttoncolor, Button_Color)
    pygame.draw.rect(screen, buttoncolor, Button_Background)
    pygame.draw.rect(screen, buttoncolor, Button_Sizeincrease)
    pygame.draw.rect(screen, buttoncolor, Button_Sizedecrease)
    
    color = MENU_FONT.render("Randomize button color", 1, colors.get("blue"))
    bgcolor = MENU_FONT.render("Randomize background color", 1, colors.get("blue"))
    sizeincrease = MENU_FONT.render("Increase screen size",1, colors.get ("blue"))
    sizedecrease = MENU_FONT.render("Decrease screen size",1, colors.get ("blue"))

  
    screen.blit(color, (SCREEN_WIDTH//2 - (color.get_width()//2), 160))
    screen.blit(bgcolor, (SCREEN_WIDTH//2 - (bgcolor.get_width()//2), 210))
    screen.blit(sizeincrease, (SCREEN_WIDTH//2 - (sizeincrease.get_width()//2), 260))
    screen.blit(sizedecrease, (SCREEN_WIDTH//2 - (sizedecrease.get_width()//2), 310))
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
       
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                mx=mousepos[0]
                my=mousepos[1]
                if Button_Color.collidepoint(mx,my):
                    buttoncolor=(random.randint(0,255),random.randint(0,255), random.randint(0,255))
                    
                if Button_Background.collidepoint(mx,my):
                    backgrnd=(random.randint(0,255),random.randint(0,255), random.randint(0,255))
                if Button_Sizeincrease.collidepoint(mx, my) and SCREEN_WIDTH < 1400:
                    SCREEN_WIDTH+=100
                    

                    # screen= pygame.display.set_mode((WIDTH,HEIGHT))
                    
                if Button_Sizedecrease.collidepoint(mx, my) and SCREEN_WIDTH >900:
                    SCREEN_WIDTH -=100
  
                screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
                screen.fill(backgrnd)
                xd = SCREEN_WIDTH//2 - (Title.get_width()//2)
                Bx = SCREEN_WIDTH//3  
                screen.blit(Title, (xd, 50))
                Button_Color = pygame.Rect(Bx, 150, SCREEN_WIDTH//3, 40)
                Button_Background = pygame.Rect(Bx, 200, SCREEN_WIDTH//3, 40)
                Button_Sizeincrease= pygame.Rect(Bx, 250, SCREEN_WIDTH//3, 40)
                Button_Sizedecrease= pygame.Rect(Bx, 300, SCREEN_WIDTH//3, 40)
                pygame.draw.rect(screen, buttoncolor, Button_Color)
                pygame.draw.rect(screen, buttoncolor, Button_Background)
                pygame.draw.rect(screen, buttoncolor, Button_Sizeincrease)
                pygame.draw.rect(screen, buttoncolor, Button_Sizedecrease)
                screen.blit(color, (SCREEN_WIDTH//2 - (color.get_width()//2), 160))
                screen.blit(bgcolor, (SCREEN_WIDTH//2 - (bgcolor.get_width()//2), 210))
                screen.blit(sizeincrease, (SCREEN_WIDTH//2 - (sizeincrease.get_width()//2), 260))
                screen.blit(sizedecrease, (SCREEN_WIDTH//2 - (sizedecrease.get_width()//2), 310))  
                pygame.display.update() 
           
def scoreboard():
    #rendering text objects
    Title = TITLE_FONT.render("Scoreboard", 1, colors.get("blue"))
    text1 = MENU_FONT.render("Go back", 1, colors.get("blue"))


    #fills screen with white
    screen.fill(colors.get("white"))

    #creating button options
    Button_back = pygame.Rect(200, 400, 130, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_back)


    #Instructions
    myFile = open("scoreboard.txt", "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = SCREEN_WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    screen.blit(text1, (225, 410))


    pygame.display.update()
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
                

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_back.collidepoint((mx, my)):
                    run = False



CHARACTER_SPEED = 8 # how fast the character moves


def get_image(sheet, frame_x, frame_y, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame_x*width), (frame_y*height), width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)

    return image

def get_background_image(image_path): # scales immages to the size of the screen
    image = pygame.image.load(image_path)
    background = pygame.transform.scale(image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    return background

CLOUD_BG = get_background_image("pygamefiles/images/clouds.jpg")
GRASS_BG = get_background_image("pygamefiles/images/grass background.jpg")
FOREST_BG = get_background_image("pygamefiles/images/forest.jpg")
PURPLESTAR_BG = get_background_image("pygamefiles/images/purple.jpg")
SEA_BG = get_background_image("pygamefiles/images/sea.jpg")
CYBERPUNK_BG = get_background_image("pygamefiles/images/cyberpunk background.jpg")
BRICKS_BG = get_background_image("pygamefiles/images/manybricks.png")


# the scale of the player
scale = 1.5

# player class
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


        if choose_character == 1:
            santa_sheet = pygame.image.load("pygamefiles/images/Santa_character.png")
            front = get_image(santa_sheet, 1, 2, 48, 64, scale, "black")
            left_1 = get_image(santa_sheet, 0, 3, 48, 64, scale, "black")
            left_2 = get_image(santa_sheet, 1, 3, 48, 64, scale, "black")
            left_3 = get_image(santa_sheet, 2, 3, 48, 64, scale, "black")
            right_1 = get_image(santa_sheet, 0, 1, 48, 64, scale, "black")
            right_2 = get_image(santa_sheet, 1, 1, 48, 64, scale, "black")
            right_3 = get_image(santa_sheet, 2, 1, 48, 64, scale, "black")
            self.player_walk_left = [front, left_1, left_2, left_3, right_1, right_2, right_3, right_3]
            self.player_index = 0
            self.image = self.player_walk_left[self.player_index]

        if choose_character == 2:
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

    def player_input(self): # moves the player based on the input
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

    def character_animation(self): # animates the character
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

    def apply_gravity(self): # applies gravity
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
        
    def update(self): # updates the player
        self.player_input()
        self.character_animation()


# Tile classes
class Default_Tile(pygame.sprite.Sprite):
    def __init__(self, tile_select, pos, size):
        super().__init__()
        scale = size/16
        if tile_select == 1:
            framex = 1
            framey = random.randint(5, 6)
        if tile_select == 2:    
            framex = random.randint(0, 1)
            framey = framex = random.randint(0, 1)
        brick_sheet = pygame.image.load("pygamefiles/images/manybricks.png")
        brick = get_image(brick_sheet,framex ,framey , 16, 16, scale, "black")
        self.image = brick
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class Floating_tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size*2, size*.5))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=pos)
        self.location = pos
        self.upspeed = 2
        self.upmove = self.upspeed

    def move_up(self):
        if self.rect.y == self.location[1]+TILE_SIZE:
            self.upmove = -self.upspeed
        if self.rect.y == self.location[1]:
            self.upmove = self.upspeed   
        self.rect.y += self.upmove    
           

    def update(self, x_shift):
        self.rect.x += x_shift 
        self.move_up()   

class Lava_tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.lava_pic_sheet = pygame.image.load("pygamefiles/images/lava.png")
        self.scale = 4
        self.frame = 7
        self.lava_pic = get_image(self.lava_pic_sheet, self.frame,0,16,16,scale,"black")
        self.image = self.lava_pic
        self.rect = self.image.get_rect(topleft=pos)

  

        self.lava_pic = get_image(self.lava_pic_sheet, int(self.frame),0,16,16,self.scale,"black")
        self.image = self.lava_pic



    def update(self, x_shift):
        self.rect.x += x_shift


class Coin_Tiles(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        coin_sheet = pygame.image.load("pygamefiles/images/coin.png")
        # gets the frames of the sprite sheet
        scale = 1 # scale of th coin size
        coin1 = get_image(coin_sheet,0 ,0 , 40, 44, scale, "black")
        coin2 = get_image(coin_sheet,0 ,1 , 40, 44, scale, "black")
        coin3 = get_image(coin_sheet,0 ,2 , 40, 44, scale, "black")
        coin4 = get_image(coin_sheet,0 ,3 , 40, 44, scale, "black")
        self.coin_frames = [coin1, coin2, coin3, coin4]
        self.frame_index = 0
        self.frame_speed = .1
        self.image = self.coin_frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

    def update_frames(self):
        self.frame_index += self.frame_speed
        if self.frame_index > len(self.coin_frames):
            self.frame_index = 0
        self.image = self.coin_frames[int(self.frame_index)]


    def update(self, x_shift):
        self.rect.x += x_shift
        self.update_frames()

class Door_tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        scale = 4
        door_sheet = pygame.image.load("pygamefiles/images/door.png")
        door_closed = get_image(door_sheet,0 ,0 , 16, 32, scale, "black")
        door_open = get_image(door_sheet,4 ,0 , 16, 32, scale, "black")
        self.door_frames = [door_closed,door_open]
        self.door_frame = 0
        self.image = self.door_frames[self.door_frame]
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
        self.image = self.door_frames[self.door_frame]


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_shift = 0
        self.current_x = 0

        #dust
        self.dust_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False

    def setup_level(self, layout): # this function sets up the level using the layout.
        global block_count, player_count
        self.player = pygame.sprite.GroupSingle() # creates a single sprite group for the player
        self.tiles = pygame.sprite.Group() # creates a sprite group for the tiles.
        self.death_tiles = pygame.sprite.Group() # creats a sprite group with tiles that kill the player when they collide
        self.coin_tiles = pygame.sprite.Group() # creates a spritegroup for coins
        self.door_tile = pygame.sprite.Group() # creates a sprite group for the door
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if val == 'X': 
                    tile = Default_Tile(block_count, (x, y), TILE_SIZE) # this creates a square tile
                    self.tiles.add(tile)
                if val == "L":
                    tile = Floating_tile((x, y), TILE_SIZE) # this creates a floating tile that moves up and down
                    self.tiles.add(tile)

                if val == "D":
                    tile = Lava_tile((x,y), TILE_SIZE) # this creates a lave tile that kills the player 
                    self.death_tiles.add(tile) 

                if val == "C":
                    tile = Coin_Tiles((x,y), TILE_SIZE) # creates the coin sprite
                    self.coin_tiles.add(tile) 

                if val == "E":
                    tile = Door_tile((x,y), TILE_SIZE) # creates the door sprite
                    self.door_tile.add(tile)


                if val == 'P':
                    player = Player(player_count, x, y)
                    self.player.add(player) # this creates the player sprite
                    
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

    def horizontal_movement_collisions(self): # this function checks if the player collided into the tiles horrizontally
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

    def vertical_movement_collisions(self): # this function checks if the player collided into the tiles verdically
        player = self.player.sprite
        self.tiles.update(self.world_shift)
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

    def check_lava_collisions(self): # this function kills the player if they collide with the lava
        global run, death_count
        player = self.player.sprite
        

        for sprite in self.death_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                TITLE_FONT = pygame.font.SysFont('comicsans', 150)
                Title = TITLE_FONT.render("You Died!", 1, "black") # creates the text "you dies when he player lands in the lava"
                xd = SCREEN_WIDTH//2 - (Title.get_width()//2)
                screen.blit(Title, (xd, 200))
                pygame.display.update()      
                pygame.time.delay(500)
                run = False

    def collect_coins(self): # this function collects the coins
        global coin_count, coin_amount, all_coins_collected, level_count
        player = self.player.sprite
        
        for sprite in self.coin_tiles.sprites():
            if sprite.rect.colliderect(player.rect): # checks if the player collieded with a coin
                sprite.kill()
                coin_count += 1 # adds one to the coin count
                if coin_count == coin_amount: # sets all counts collected to true if all the coins are collected
                    all_coins_collected = True
                    
    def enter_door(self): # this function takes the player to the next level if they enter the door with the coins
        global coin_count, level_count, coin_amount
        player = self.player.sprite
        for sprite in self.door_tile.sprites():
            if sprite.rect.colliderect(player.rect) and coin_count == coin_amount: # checks if the player collieded with the door and collected all the coins
                sprite.door_frame = 1
                player.rect.x = sprite.rect.x
                player.rect.y = sprite.rect.y+35

                if level_count == 1: # runs when level_count is equal to 1  
                    screen.blit(CLOUD_BG,(0,0))        
                if level_count == 2: # runs when level_count is equal to 2
                    screen.blit(FOREST_BG, (0,0))   
                if level_count == 3: # runs when level_count is equal to 3       
                    screen.blit(SEA_BG, (0,0))        
                if level_count == 4: # runs when level_count is equal to 4            
                    screen.blit(CYBERPUNK_BG, (0,0))          
                if level_count == 5: # runs when level_count is equal to 5      
                    screen.blit(GRASS_BG, (0,0))
                    
                self.tiles.draw(self.display_surface)
                self.coin_tiles.draw(self.display_surface)
                self.coin_tiles.update(self.world_shift)
                self.player.update()
                self.player.draw(self.display_surface)
                self.door_tile.update(self.world_shift)
                self.door_tile.draw(self.display_surface)
                
                self.death_tiles.draw(self.display_surface) # draws the lava tiles
                self.death_tiles.update(self.world_shift)
                level_count +=1
                coin_count = 0
                TITLE_FONT = pygame.font.SysFont('comicsans', 150)
                Title = TITLE_FONT.render("You beat level "+str(level_count-1)+"!", 1, "black") # creates the text "you dies when he player lands in the lava"
                xd = SCREEN_WIDTH//2 - (Title.get_width()//2)
                screen.blit(Title, (xd, 200))   
                pygame.display.update()
                pygame.time.delay(2000)
                
  
                
    def run(self):

        # level tiles
        self.tiles.draw(self.display_surface)
        self.scroll_horizontal()

        # coins
        self.coin_tiles.draw(self.display_surface)
        self.coin_tiles.update(self.world_shift)
        self.collect_coins()

        
        # player
        self.horizontal_movement_collisions()
        self.vertical_movement_collisions()
        self.player.update()
        self.player.draw(self.display_surface)
        
        # door tile
        self.door_tile.draw(self.display_surface)
        self.door_tile.update(self.world_shift)
        self.enter_door()

        # death tiles
        self.death_tiles.draw(self.display_surface) # draws the lava tiles
        self.check_lava_collisions() #checks if the player collided with the lava
        self.death_tiles.update(self.world_shift)

        
def count_layout_coins(layout): # this function counts the number of coins in the layout
    global coin_amount
    for _, row in enumerate(layout):
        for _, val in enumerate(row):
            if val == "C":
                coin_amount += 1
    return coin_amount            

TOP_FONT = 'comicsans' # the font of the text at the top of the screen
TOP_TEXT_SIZE = 35 # the font size of the text at the top of the screen

def show_deathcount():
    global death_count
    TITLE_FONT = pygame.font.SysFont(TOP_FONT, TOP_TEXT_SIZE)
    Title = TITLE_FONT.render("Death Count: "+str(death_count-1), 1, "black") # Displays the deathcount
    screen.blit(Title, (20, 20)) # puts the deathcount at the top left of the screen
    
death_count = -1 # counts the deaths


def show_coin_count():
    global coin_amount, coin_count
    TITLE_FONT = pygame.font.SysFont(TOP_FONT, TOP_TEXT_SIZE)
    Title = TITLE_FONT.render("Coins Collected: "+str(coin_count)+"/"+str(coin_amount),1,"black") # Displays the coin count
    xd = SCREEN_WIDTH//2 - (Title.get_width()//2) # centers the text on the screen
    screen.blit(Title, (xd, 20)) 

def show_level_count():
    global level_count
    TITLE_FONT = pygame.font.SysFont(TOP_FONT, TOP_TEXT_SIZE)
    Title = TITLE_FONT.render("Level: "+str(level_count),1,"black") # Displays the coin count
    xd = SCREEN_WIDTH - (Title.get_width()+30) # centers the text on the screen
    screen.blit(Title, (xd, 20)) 

File_update = True
def exit_screen(): # runs after the last level is beat
    global death_count, name, File_update
    TITLE_FONT = pygame.font.SysFont('comicsans', 90)
    Title = TITLE_FONT.render("You Beat all five levels!",1,"white") 
    xd = SCREEN_WIDTH//2 - (Title.get_width()//2) # centers the text on the screen
    deaths_show = TITLE_FONT.render("You died "+str(death_count-1)+" times!",1,"white") 
    xs = SCREEN_WIDTH//2 - (deaths_show.get_width()//2) # centers the text on the screen
    screen.blit(BRICKS_BG, (0,0))
    screen.blit(Title, (xd, 20))
    screen.blit(deaths_show,(xs, 200)) 

    if File_update:
        date=datetime.datetime.now()
        scoreLine="Deaths: "+str(death_count-1)+ "    "+name+"    " +date.strftime("%m/%d/%Y")+'\n' #turning the string into a score
        myfile=open('scoreboard.txt','a')
        myfile.write(scoreLine)
        myfile.close()
        File_update = False


player_count = 2
block_count = 2

display_number = 1
def opening_screen():
    global display_number, level_count, player_count, block_count, run



    if display_number == 1:
        TITLE_FONT = pygame.font.SysFont('comicsans', 90)
        Title = TITLE_FONT.render("Select a character",1,"white") 
        xd = SCREEN_WIDTH//2 - (Title.get_width()//2) # centers the text on the screen

        santa_sheet = pygame.image.load("pygamefiles/images/Santa_character.png")
        santa_image = get_image(santa_sheet, 1, 2, 48, 64, 8, "black")
        santax = SCREEN_WIDTH//2 - (santa_image.get_width()//2)
        santa_rect = santa_image.get_rect(topleft=(santax-250,200))

        priest_sheet = pygame.image.load("pygamefiles/images/priestsheet.png")
        priest_image = get_image(priest_sheet, 1, 2, 48, 64, 8, "black")
        priestx = SCREEN_WIDTH//2 - (priest_image.get_width()//2)
        priest_rect = priest_image.get_rect(topleft=(priestx+250,200))

        screen.blit(BRICKS_BG, (0,0))
        screen.blit(Title, (xd, 20))
        screen.blit(santa_image,(santa_rect.x,santa_rect.y))
        screen.blit(priest_image,(priest_rect.x,priest_rect.y))
        for event in pygame.event.get():         
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                mx=mousepos[0]
                my=mousepos[1]
                if santa_rect.collidepoint(mx,my):
                    display_number +=1
                    player_count = 1
                if priest_rect.collidepoint(mx,my): 
                    display_number +=1
                    player_count = 2  

    if display_number == 2:
        TITLE_FONT = pygame.font.SysFont('comicsans', 90)
        Title = TITLE_FONT.render("Select a block!",1,"white") 
        xd = SCREEN_WIDTH//2 - (Title.get_width()//2) # centers the text on the screen

        block_sheet = pygame.image.load("pygamefiles/images/manybricks.png")
        green_blocks = get_image(block_sheet, 1, 1, 16, 16, 16, "black")
        greenx = SCREEN_WIDTH//2 - (green_blocks.get_width()//2)
        green_rect = green_blocks.get_rect(topleft=(greenx-250,200))


        pink_blocks = get_image(block_sheet, 1, 5, 16, 16, 16, "black")
        pinkx = SCREEN_WIDTH//2 - (pink_blocks.get_width()//2)
        pink_rect = pink_blocks.get_rect(topleft=(pinkx+250,200))

        screen.blit(BRICKS_BG, (0,0))
        screen.blit(Title, (xd, 20))
        screen.blit(green_blocks,(green_rect.x,green_rect.y))
        screen.blit(pink_blocks,(pink_rect.x,pink_rect.y))
        for event in pygame.event.get():         
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                mx=mousepos[0]
                my=mousepos[1]
                if green_rect.collidepoint(mx,my):
                    block_count = 2
                    run = False
                    level_count +=1
                    
                if pink_rect.collidepoint(mx,my): 
                    block_count = 1
                    run = False
                    level_count +=1   

def input_name():
    # name variable
    user_name = ""

    #rendering text objects

    Title = TITLE_FONT.render("Input your name", 1, colors.get("blue"))
    text1 = MENU_FONT.render("enter your name in the green box", 1, colors.get("blue"))
    user_text = MENU_FONT.render(user_name,1, colors.get("BLACK"))

    #fills screen with white
    screen.fill(colors.get("white"))


    # renderig fonts to the screen
    xd = SCREEN_WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    # text1_x = WIDTH//2 - (text1.get_width()//2)
    # screen.blit(text1, (text1_x, 350))

    # creats the box for typing
    botton_box_x = SCREEN_WIDTH//2 - SCREEN_WIDTH//4
    Button_box = pygame.Rect(botton_box_x, 400, SCREEN_WIDTH//2, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_box)

    pygame.display.update()
        
    run = True    
    while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    print(user_name)
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                    

                if event.type == pygame.KEYDOWN:
                    if event.key ==  pygame.K_RETURN: # enter the name
                        run = False
                        print(user_name) 
                    if event.key == pygame.K_BACKSPACE: # remove the last letter of the name
                        user_name = user_name[0:len(user_name)-1]
                    elif event.key != pygame.K_RETURN: # add the character to the end of the string
                        user_name += event.unicode 

                    pygame.draw.rect(screen, colors.get("limeGreen"), Button_box)
                    user_text = MENU_FONT.render(user_name,1, colors.get("BLACK"))
                    screen.blit(user_text, (botton_box_x + 20, 410))
                    pygame.display.update()       # updates the screen
    return user_name                

name = input_name()
menu()

CLOUD_BG = get_background_image("pygamefiles/images/clouds.jpg")
GRASS_BG = get_background_image("pygamefiles/images/grass background.jpg")
FOREST_BG = get_background_image("pygamefiles/images/forest.jpg")
PURPLESTAR_BG = get_background_image("pygamefiles/images/purple.jpg")
SEA_BG = get_background_image("pygamefiles/images/sea.jpg")
CYBERPUNK_BG = get_background_image("pygamefiles/images/cyberpunk background.jpg")
BRICKS_BG = get_background_image("pygamefiles/images/manybricks.png")

level_count = 0

while True:
    
    coin_count = 0 # counts the coins collected
    all_coins_collected = False #    

    
    Level_1 = Level(level_map_1, screen) # creates the level 1 
    Level_2 = Level(level_map_2, screen) # creates the level 2
    level_3 = Level(level_map_3, screen) # creates the level 3
    level_4 = Level(level_map_4, screen) # creates the level 4
    level_5 = Level(level_map_5, screen) # creates the level 5


    death_count += 1 # adds one to the death count

    clock = pygame.time.Clock()
    FPS = 60
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if level_count == 0:
            opening_screen()        
        coin_amount = 0 # variable for the amount of coins on the layout
        if level_count == 1: # runs when level_count is equal to 1  
            coin_amount = count_layout_coins(level_map_1) # sets the coin amount equal to the number of coins in the level
            screen.blit(CLOUD_BG,(0,0))        
            Level_1.run()
        if level_count == 2: # runs when level_count is equal to 2
            coin_amount = count_layout_coins(level_map_2) # sets the coin amount equal to the number of coins in the level
            screen.blit(FOREST_BG, (0,0))
            Level_2.run() 
        if level_count == 3: # runs when level_count is equal to 3
            coin_amount = count_layout_coins(level_map_3)
            screen.blit(SEA_BG, (0,0))
            level_3.run()
        if level_count == 4: # runs when level_count is equal to 4
            coin_amount = count_layout_coins(level_map_4)
            screen.blit(CYBERPUNK_BG, (0,0))
            level_4.run()
        if level_count == 5: # runs when level_count is equal to 5
            coin_amount = count_layout_coins(level_map_5)
            screen.blit(GRASS_BG, (0,0))
            level_5.run()  
        if level_count == 6:# runs the exit screen if level_count is equal to 6
            exit_screen()      

        # displays the text at the top on the screen  
        if level_count < 6 and level_count > 0:     
            show_deathcount()
            show_coin_count()
            show_level_count()

        pygame.display.update()


        
