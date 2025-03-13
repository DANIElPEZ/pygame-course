import pygame
import math

class Weapon:
     #crating weapon
     def __init__(self, image):
          self.move_backwards=False
          self.image=image
          #current angle
          self.angle=0
          #rotation method
          self.rotate_image=self.image
          #shape of weapon
          self.shape=self.rotate_image.get_rect()

     def update(self, player):
          #get the mouse position
          mouse_x, mouse_y=pygame.mouse.get_pos()
          #center the weapon to center of player
          self.shape.center=player.shape.center
          #calculating the delta distance between mouse and weapon
          delta_x=mouse_x-self.shape.x
          delta_y=mouse_y-self.shape.y
          self.angle=self.angle_atan2(delta_x, delta_y)
          self.rotate_image=pygame.transform.rotate(self.image, self.angle)

     def draw(self, window_context):
          flip_image=pygame.transform.flip(self.rotate_image, self.move_backwards, False)
          window_context.blit(flip_image, self.shape)

     def moving(self, delta_x):
          if delta_x<0:
               self.move_backwards=True
          if delta_x>0:
               self.move_backwards=False

     #calculating the angle
     def angle_atan2(self, delta_x, delta_y):
          return math.degrees(math.atan2(delta_x, delta_y))