init python:
    ## new Class
    class Volleyball(renpy.Displayable):
        
        
        def __init__(self, **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            ## way on files
            self.coren = 'mods/Slavia/images/GUI/Volleyball/players/'
            self.sound_way = 'mods/Slavia/music/sounds/'
                
            ## name files
                ## img
            self.ball = self.coren + 'ball.png'
            self.user = self.coren + 'user.png'
            self.slavia = self.coren + 'slavia.png'
            self.alisa = self.coren + 'alisa.png'
            self.lena = self.coren + 'lena.png'
            
                ## sounds
            self.sounds_ball = ['ball.ogg', 'ball1.ogg', 'ball2.ogg', 'ball3.ogg']
            

            ## if you win
            self.win = None
            
            ## ball
            self.ball_x = 400
            self.ball_y = 500
            self.ball_z = 1.0
            self.speed_bx = 10
            self.speed_by = 10
            self.ball_r = 0
            
            ## cort
            self.MAX_Y_POS = 250
            self.MIN_Y_POS = 900
            self.MAX_X_POS = 5
            self.MIN_X_POS = 1700
            
            ## setca
            self.setca = self.MIN_X_POS/2
            
            ## user
            self.user_x = 1500
            self.user_y = 400
            self.rotate_user = 180
            self.user_speed = 75
            self.bounce_user = True
            
            ## dv
            self.dv_x = 400
            self.dv_y = 600
            self.speed_dvx = 10
            self.speed_dvy = 10
            self.rotate_dv = 0
            
            ## sl
            self.sl_x = 200
            
        ## render
        def render(self, width, height, st, at):
            
            ## obj_render
            rend = renpy.Render(width, height, st, at)
            
            ## transform and login image
            ball = Transform(child = self.ball, rotate = self.ball_r, zoom = self.ball_z)
            user = Transform(child = self.user, rotate = self.rotate_user)
            sl = Transform(child = self.slavia)
            dv = Transform(child = self.alisa, rotate = self.rotate_dv)
            un = Transform(child = self.lena, rotate = self.ball_r/2)
            
            ## render image
            rend.blit(renpy.render(ball, 75, 75, st, at), (self.ball_x, self.ball_y))
            rend.blit(renpy.render(user, 100, 100, st, at), (self.user_x, self.user_y))
            rend.blit(renpy.render(sl, 100, 100, st, at), (self.sl_x, self.ball_y))
            rend.blit(renpy.render(dv, 100, 100, st, at), (self.dv_x, self.dv_y))
            rend.blit(renpy.render(un, 100, 100, st, at), (self.sl_x/2 + 500, self.ball_y/2 + 100))
            
            ## every_moment
            renpy.redraw(self, 0)

            ## obj render
            return rend
            

        ## WORK EVENT
        def event(self, event, x, y, st):
            
            ## keymap
            if event.type == pygame.KEYDOWN:
                    #if you not wanne play
                if event.key == pygame.K_SPACE:
                    self.win = False
                    return self.win






            ## Wall for user
                ## STOP USER if he go to the not GAME ZONE
            if (renpy.get_mouse_pos()[0] < self.MIN_X_POS/2 + 100 and
                renpy.get_mouse_pos()[1] < self.MAX_Y_POS):
                
                        self.user_x = self.MIN_X_POS/2 + 100
                        self.user_y = self.MAX_Y_POS

                
            elif (renpy.get_mouse_pos()[0] < self.MIN_X_POS/2 + 100 and
                  renpy.get_mouse_pos()[1] > self.MIN_Y_POS):
                  
                        self.user_x = self.MIN_X_POS/2 + 100
                        self.user_y = self.MIN_Y_POS
        
        
            elif (renpy.get_mouse_pos()[0] > self.MIN_X_POS and
                  renpy.get_mouse_pos()[1] < self.MAX_Y_POS):
                    
                        self.user_x = self.MIN_X_POS
                        self.user_y = self.MAX_Y_POS
                    
                
            elif (renpy.get_mouse_pos()[0] > self.MIN_X_POS and
                  renpy.get_mouse_pos()[1] > self.MIN_Y_POS):
                  
                        self.user_x = self.MIN_X_POS
                        self.user_y = self.MIN_Y_POS
               
               
            elif renpy.get_mouse_pos()[0] < self.MIN_X_POS/2 + 100:
            
                        self.user_y = renpy.get_mouse_pos()[1]
                
                
            elif renpy.get_mouse_pos()[1] < self.MAX_Y_POS:
            
                        self.user_x = renpy.get_mouse_pos()[0]
                
                
            elif renpy.get_mouse_pos()[0] > self.MIN_X_POS:
            
                        self.user_y = renpy.get_mouse_pos()[1]
                
                
            elif renpy.get_mouse_pos()[1] > self.MIN_Y_POS:
            
                        self.user_x = renpy.get_mouse_pos()[0]
                
                
                
            elif (renpy.get_mouse_pos()[0] > self.MIN_X_POS/2 and
                  renpy.get_mouse_pos()[1] > self.MAX_Y_POS - 50 and
                  renpy.get_mouse_pos()[0] < self.MIN_X_POS - 50 and
                  renpy.get_mouse_pos()[1] < self.MIN_Y_POS - 50):
                  
                        self.user_x = renpy.get_mouse_pos()[0]
                        self.user_y = renpy.get_mouse_pos()[1]

            
            
            
            
            
            ## WALL for BALL
            if self.ball_x > self.MAX_X_POS:
                self.speed_bx *= -1

                
            if self.ball_y > self.MAX_Y_POS:                
                self.speed_by *= -1

            if self.ball_x < self.MIN_X_POS:                
                self.speed_bx *= -1
                
            if self.ball_y < self.MIN_Y_POS:              
                self.speed_by *= -1
                
                
                
            
            
            ## WALL for alisa chibi
            if (self.setca + 100 > self.dv_x and
                self.setca - 100 < self.dv_x and
                self.setca + 1080 > self.dv_y and
                self.setca - 1080 < self.dv_y):
                        
                        self.speed_dvx *= -1
                
                
            if self.dv_x > self.MAX_X_POS:
                        
                        self.speed_dvx *= -1
                
                
            if self.dv_y > self.MAX_Y_POS:
            
                        self.speed_dvy *= -1


            if self.dv_x < self.MIN_X_POS:
            
                        self.speed_dvx *= -1
                
                
            if self.dv_y < self.MIN_Y_POS:
            
                        self.speed_dvy *= -1

            
            
            ## ZOOM BALL 
            if (self.setca + 100 > self.ball_x and
                self.setca - 100 < self.ball_x and
                self.setca + 1080 > self.ball_y and
                self.setca - 1080 < self.ball_y):
                
                        self.ball_z += 0.05
                        self.bounce_user = False
            
            
            else:
            
                        if self.ball_z != 1.0:
                            self.ball_z -= 0.05
            
                
            
            
            
          ## IF BOUNCE BALL
            ## BOUNS BALL if it take Slavia
            if self.sl_x + 10 > self.ball_x and self.sl_x - 10 < self.ball_x:
                self.speed_bx *= -1
                renpy.sound.play(self.sound_way + self.sounds_ball[2], channel=0)
                self.speed_bx += 0.5
                self.speed_by += 0.6
                self.bounce_user = False
                
                
            
            
            ## BOUNS BALL if it take USER
            if self.bounce_user == False:
            
                if (self.user_x + 60 > self.ball_x and
                    self.user_x - 60 < self.ball_x and 
                    self.user_y + 60 > self.ball_y and
                    self.user_y - 60 < self.ball_y):
                    
                            self.speed_bx *= -1
                            self.bounce_user = True
                            renpy.sound.play(self.sound_way + self.sounds_ball[0], channel=0)
                            
                            
                            
                
            
            ## BOUNS BALL if it take LENA
            if ((self.sl_x/2 + 500) + 10 > self.ball_x and
                (self.sl_x/2 + 500) - 10 < self.ball_x and
                (self.ball_y/2 + 100) + 10 > self.ball_y and
                (self.ball_y/2 + 100) - 10 < self.ball_y):
                
                        self.speed_bx *= -1
                        renpy.sound.play(self.sound_way + self.sounds_ball[3], channel=0)
                        self.bounce_user = False
                
                
                
                
                
                
            ## BOUNS BALL if it take ALISA                
            if (self.dv_x + 10 > self.ball_x and
                self.dv_x - 10 < self.ball_x and
                self.dv_y + 10 > self.ball_y and
                self.dv_y - 10 < self.ball_y):
                
                        self.speed_bx *= -1
                        renpy.sound.play(self.sound_way + self.sounds_ball[1], channel=0)
                        self.bounce_user = False
            



            if self.sl_x-10 > self.ball_x:
                ## you hacker!!
                self.win = True
                return self.win


            ## go to the... every loop
            self.dv_x += self.speed_dvx
            self.dv_y += self.speed_dvy
            self.rotate_dv += 3
            self.ball_r += 4
            self.ball_x += self.speed_bx
            self.ball_y += self.speed_by
            

            ## restart screen in renpy
            renpy.restart_interaction()