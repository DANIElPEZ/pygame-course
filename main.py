import pygame
import settings as conf
from player import Player
from weapon import Weapon
import random

class Main:
     def __init__(self):
          running=True
          pygame.init()
          #change the icon
          icon=pygame.image.load('assets/icon.png')
          pygame.display.set_icon(icon)
          #change title game
          pygame.display.set_caption("The hacker chicken")
          #create window instance
          window=pygame.display.set_mode((conf.width_window,conf.height_window))

          #creating an animation
          animations_idle_player=[]
          for img in range(1,3):
               img_player=pygame.image.load(f'assets/Idle_player{img}.png')
               animations_idle_player.append(self.scale_image(img_player,conf.scale_player))

          animations_run_player=[]
          for img in range(1,3):
               img_player=pygame.image.load(f'assets/run_player{img}.png')
               animations_run_player.append(self.scale_image(img_player,conf.scale_player))
          
          #instance of player
          player=Player(30,30,animations_idle_player, animations_run_player)

          #create an image
          weapon_image=pygame.image.load('assets/gun.png')
          weapon_image=self.scale_image(weapon_image,conf.scale_weapon)
          malware_bullet=pygame.image.load('assets/bullet.png')
          #instance of weapon
          weapon=Weapon(weapon_image, malware_bullet)

          'list of sprites'
          #bullets list
          bullets_list=pygame.sprite.Group()
          #list of enemies
          enemies_list=[]

          #enemies
          animation_walking_enemie=[]
          for img in range(1,3):
               img_enemie=pygame.image.load(f'assets/Walking_enemie{img}.png')
               animation_walking_enemie.append(self.scale_image(img_enemie,conf.scale_player))

          #initial position
          for enemie in range(10):
               x_enemie=random.randint(0,conf.width_window)
               y_enemie=random.randint(0,conf.height_window)
               enemie=Player(x_enemie,y_enemie,animation_walking_enemie,[])
               enemies_list.append(enemie)
          #moving variables
          is_running_player=False
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
               player.update(is_running_player)
               player.draw(window)

               weapon.moving(delta_x)
               bullet=weapon.update(player)
               weapon.draw(window)

               x_enemie=random.randint(0,conf.width_window)
               y_enemie=random.randint(0,conf.height_window)

               for enemie_update in enemies_list:
               #enemie.moving(x_enemie,y_enemie)
                    enemie_update.update(False)
                    enemie_update.draw(window)

               #add bullet to list of bullets
               if bullet:
                    bullets_list.add(bullet)

               #draw bullets
               for bullet_item in bullets_list:
                    bullet_item.draw(window)
               #update bullets
               for bullet_update in bullets_list:
                    bullet_update.update()

               #get all events
               for event in pygame.event.get():
                    #execute event
                    if event.type == pygame.QUIT:
                         running=False

                    if event.type == pygame.KEYDOWN:
                         is_running_player=True
                         if event.key == pygame.K_w:
                              move_up=True
                         if event.key == pygame.K_s:
                              move_down=True
                         if event.key == pygame.K_a:
                              move_left=True
                         if event.key == pygame.K_d:
                              move_right=True

                    if event.type == pygame.KEYUP:
                         is_running_player=False
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