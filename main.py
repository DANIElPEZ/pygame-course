import pygame
import settings as conf
from player import Player
from weapon import Weapon

class Main:
     def __init__(self):
          running=True
          pygame.init()
          #change title game
          pygame.display.set_caption("game")
          #create window instance
          window=pygame.display.set_mode((conf.width_window,conf.height_window))

          #creating an animation
          animations_idle_player=[]
          for img in range(1,3):
               img_player=pygame.image.load(f'assets/Idle{img}.png')
               animations_idle_player.append(self.scale_image(img_player,conf.scale_player))

          animations_run_player=[]
          for img in range(1,3):
               img_player=pygame.image.load(f'assets/run{img}.png')
               animations_run_player.append(self.scale_image(img_player,conf.scale_player))
          
          #instance of player
          player=Player(10,10,animations_idle_player, animations_run_player)

          #create an image
          weapon_image=pygame.image.load('assets/phone.png')
          weapon_image=self.scale_image(weapon_image,conf.scale_weapon)
          #instance of weapon
          weapon=Weapon(weapon_image)

          #moving variables
          is_running=False
          #is moving
          move_up=move_down=move_left=move_right=False
          #controling frames per second
          clock=pygame.time.Clock()

          #infinite game loop
          while running:
               #set fps
               clock.tick(conf.frames)
               #clear the canvas
               window.fill(conf.clear_canvas_color)

               #delta moving
               delta_x, delta_y=0, 0
               #moving events
               if move_up:
                    delta_y=-conf.speed_player
               if move_down:
                    delta_y=conf.speed_player
               if move_left:
                    delta_x=-conf.speed_player
               if move_right:
                    delta_x=conf.speed_player

               #drawing the objects on window
               player.moving(delta_x,delta_y)
               player.update(is_running)
               player.draw(window)

               weapon.moving(delta_x)
               weapon.update(player)
               weapon.draw(window)

               #get all events
               for event in pygame.event.get():
                    #execute event
                    if event.type == pygame.QUIT:
                         running=False

                    if event.type == pygame.KEYDOWN:
                         is_running=True
                         if event.key == pygame.K_w:
                              move_up=True
                         if event.key == pygame.K_s:
                              move_down=True
                         if event.key == pygame.K_a:
                              move_left=True
                         if event.key == pygame.K_d:
                              move_right=True

                    if event.type == pygame.KEYUP:
                         is_running=False
                         if event.key == pygame.K_w:
                              move_up=False
                         if event.key == pygame.K_s:
                              move_down=False
                         if event.key == pygame.K_a:
                              move_left=False
                         if event.key == pygame.K_d:
                              move_right=False

               #updating the window
               pygame.display.update()
          pygame.quit()

     #scale function
     def scale_image(self,img, scale):
          width=img.get_width()
          height=img.get_height()
          new_scale_image=pygame.transform.scale(img, (width*scale, height*scale))
          return new_scale_image

if __name__ == '__main__':
     Main()