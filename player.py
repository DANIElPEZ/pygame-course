import pygame
import settings as conf
#creating a player
class Player:
     #initial configuration of player
     def __init__(self, x, y, player_idle_animations, player_run_animations):
          #is moving to backwards
          self.move_backwards=False
          #animations
          self.player_idle_animations=player_idle_animations
          self.player_run_animations=player_run_animations
          #current frame
          self.frame_index=0
          #get current time in miliseconds when game is initialized
          self.update_time=pygame.time.get_ticks()
          #get image
          self.player_current_animation=self.player_idle_animations[self.frame_index]
          #creating rectangle x,y,width,height
          self.shape=pygame.Rect(0,0,conf.width_player,conf.height_player)
          #overriding x,y position and origin point in center of shape
          self.shape.center=(x,y)

     def update(self, is_running):
          #update the frames, change images of animation
          duration_current_frame=100
          if is_running:
               self.player_current_animation=self.player_run_animations[self.frame_index]
          else:
               self.player_current_animation=self.player_idle_animations[self.frame_index]

          if pygame.time.get_ticks() - self.update_time>=duration_current_frame:
               self.frame_index+=1
               self.update_time=pygame.time.get_ticks()
          #reset the frame index
          if self.frame_index>=len(self.player_idle_animations):
               self.frame_index=0

     #drawing the player
     def draw(self, window_context):
          #drawing if is moving to backwards
          flip_image=pygame.transform.flip(self.player_current_animation,self.move_backwards,False)
          #center the player on box
          image_rect=flip_image.get_rect(center=self.shape.center)
          #drawing sprite
          window_context.blit(flip_image, image_rect.topleft)
          #drawing rectangle
          pygame.draw.rect(window_context,conf.color_box_player,self.shape,1)

     #moving the player
     def moving(self,delta_x,delta_y):
          if delta_x<0:
               self.move_backwards=True
          if delta_x>0:
               self.move_backwards=False
          self.shape.x+=delta_x
          self.shape.y+=delta_y