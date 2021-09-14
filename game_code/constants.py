import pygame

sprite_size = (32,32)

screen_size = (720,480)

black = (0,0,0)
red = (255,0,0)

worn_item_frame_locations = [(32, 32), (64, 32), (32, 64), (64, 64), (32, 96), (64, 96)]

bpack_frame_locations = [(192,32),(224,32),(256,32),(288,32),(320,32),(352,32),
                                 (192, 64), (224, 64), (256, 64), (288, 64), (320, 64), (352, 64),
                                 (192, 96), (224, 96), (256, 96), (288, 96), (320, 96), (352, 96),
                                 (192, 128), (224, 128), (256, 128), (288, 128), (320, 128), (352, 128)]

backpack_item_slots = [pygame.Rect(bpack_frame_locations[0], (sprite_size))]


