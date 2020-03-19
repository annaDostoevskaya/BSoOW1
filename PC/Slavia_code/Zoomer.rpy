init -1 python:

    class Zoomer(renpy.Displayable):
        
        
        def __init__(self, img, **kwargs):
            
            
            renpy.Displayable.__init__(self, img, **kwargs)
            
            self.img = img
            self.zoom = 1.0
            self.xpos = 0
            self.ypos = 0
            
            self.img_ms_alpha = 1.0
            self.t_a = 0.05
        
        def render(self, width, height, st, at):

            rend = renpy.Render(width, height, st, at)
            
            trans_img = Transform(child = self.img, zoom = self.zoom)
            
            trans_mouse = Transform(Animation('mods/Slavia/images/GUI/mouse/wheel/myshka0.png', 1.0,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka0.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka1.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka2.png', self.t_a, 
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka3.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka4.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka5.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka6.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka7.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka8.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka9.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka9.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka8.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka7.png', self.t_a, 
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka6.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka5.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka4.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka3.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka2.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka1.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/wheel/myshka0.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka0.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka1.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka2.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka3.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka4.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka5.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka6.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka7.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka7.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka6.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka5.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka4.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka3.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka2.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka1.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/up/myshka0.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/right/myshka0.png', self.t_a, 
                                              'mods/Slavia/images/GUI/mouse/right/myshka1.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/right/myshka2.png', self.t_a, 
                                              'mods/Slavia/images/GUI/mouse/right/myshka3.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/right/myshka4.png', self.t_a, 
                                              'mods/Slavia/images/GUI/mouse/right/myshka5.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/right/myshka6.png', self.t_a, 
                                              'mods/Slavia/images/GUI/mouse/right/myshka7.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/right/myshka8.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/right/myshka9.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/right/myshka9.png', self.t_a, 
                                              'mods/Slavia/images/GUI/mouse/right/myshka8.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/right/myshka7.png', self.t_a, 
                                              'mods/Slavia/images/GUI/mouse/right/myshka6.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/right/myshka5.png', self.t_a, 
                                              'mods/Slavia/images/GUI/mouse/right/myshka4.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/right/myshka3.png', self.t_a, 
                                              'mods/Slavia/images/GUI/mouse/right/myshka2.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/right/myshka1.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/right/myshka0.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka0.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka1.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka2.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka3.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka4.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka5.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka6.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka7.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka8.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka9.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka9.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka8.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka7.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka6.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka5.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka4.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka3.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka2.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka1.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/left/myshka0.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka0.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka1.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka2.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka3.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka4.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka5.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka6.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka7.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka7.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka6.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka5.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka4.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka3.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka2.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka1.png', self.t_a,
                                              'mods/Slavia/images/GUI/mouse/down/myshka0.png', self.t_a),
                                              alpha = self.img_ms_alpha)
        
            rend.blit(renpy.render(Solid('#404040'), 1920, 1080, st, at), (0, 0))
            rend.blit(renpy.render(trans_img, 1920, 1080, st, at), (self.xpos, self.ypos))
            rend.blit(renpy.render(trans_mouse, 300, 300, st, at), (0, 0))
            
            ## every_moment
            renpy.redraw(self, 0)

            ## obj render
            return rend
        
        
        def event(self, event, x, y, st):
       

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.img_ms_alpha -= 0.1
                    if self.zoom < 3.0:
                        self.zoom += .1
                            
                if event.button == 5:
                    self.img_ms_alpha -= 0.1
                    if self.zoom > 1.0:
                        self.zoom -= .1
                        

            if self.xpos < 1920/2:
                if renpy.get_mouse_pos()[0] > 1670:
                    self.xpos += 10*self.zoom
                    
            if self.xpos > -1920/2:
                if renpy.get_mouse_pos()[0] < 250:
                    self.xpos -= 10*self.zoom

            if self.ypos < 1080/2:
                if renpy.get_mouse_pos()[1] > 930:
                    self.ypos += 10*self.zoom          

            if self.ypos > -1080/2:
                if renpy.get_mouse_pos()[1] < 250:
                    self.ypos -= 10*self.zoom
                    
                    
            if self.zoom == 1.0:
                self.xpos = 0
                self.ypos = 0
                
            if self.xpos > 0:
                self.xpos = 0
                
            if self.ypos > 0:
                self.ypos = 0
            
            
            ## restart screen in renpy
            renpy.restart_interaction()