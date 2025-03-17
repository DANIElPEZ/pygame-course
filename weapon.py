import pygame
import math
import settings as conf

class Weapon:
     #crating weapon
     def __init__(self, image, bullet_image):
          self.bullet=None
          self.move_backwards=False
          self.bullet_image=bullet_image
          self.image=image
          self.trigger=False
          #current angle
          self.angle=0
          #rotation method
          self.rotate_image=self.image
          #shape of weapon
          self.shape=self.rotate_image.get_rect()

     def update(self, player):
          #center the weapon to center of player
          self.shape.center=player.shape.center
          #move weapon
          self.shape.y+=player.shape.height/5
          #flip weapon when move to backwards
          if self.move_backwards:
               self.shape.x-=player.shape.width/2.4
               self.angle=-self.angle_atan2()
          if not self.move_backwards:
               self.shape.x+=player.shape.width/2.7
               self.angle=self.angle_atan2()

          #calculate the angle to rotate the weapon
          self.rotate_image=pygame.transform.rotate(self.image, self.angle)

          #if mouse is pressed trigger the weapon, position 0=left click
          if pygame.mouse.get_pressed()[0] and not self.trigger:
               self.angle=self.angle_atan2()
               self.bullet=Bullet(self.bullet_image,self.shape.centerx,self.shape.centery,self.angle)
               self.trigger=True

          if not pygame.mouse.get_pressed()[0]:
               self.trigger=False

          return self.bullet

     def draw(self, window_context):
          flip_image=pygame.transform.flip(self.rotate_image, self.move_backwards, False)
          window_context.blit(flip_image, self.shape)

     def moving(self, delta_x):
          if delta_x<0:
               self.move_backwards=True
          if delta_x>0:
               self.move_backwards=False

     #calculating the angle
     def angle_atan2(self):
          #get the mouse position
          mouse_x, mouse_y=pygame.mouse.get_pos()
          #calculating the delta distance between mouse and weapon
          delta_x=mouse_x-self.shape.centerx
          delta_y=mouse_y-self.shape.centery
          angle_rad=math.atan2(-delta_y, delta_x)
          return math.degrees(angle_rad)
     
#inheritance of sprite class
class  Bullet(pygame.sprite.Sprite):
     def __init__(self, image, x, y, angle):
          pygame.sprite.Sprite.__init__(self)
          #obligatory properties to super class
          self.bullet_image=image
          self.angle=angle
          self.image=pygame.transform.rotate(self.bullet_image,self.angle)
          self.rect=self.image.get_rect()
          self.rect.center=(x,y)
          #calculating direction by angle
          self.speedx=math.cos(math.radians(self.angle))*conf.bullet_speed
          self.speedy=-math.sin(math.radians(self.angle))*conf.bullet_speed

     def draw(self, windows_context):
          windows_context.blit(self.image, (self.rect.centerx, self.rect.centery))

     def update(self):
          self.rect.x+=self.speedx
          self.rect.y+=self.speedy

          if self.rect.right<0 or self.rect.left>conf.width_window or self.rect.top<0 or self.rect.bottom>conf.height_window:
               self.kill()