﻿screen Slavia_Gallery_cg:
# Меню            
    $ _game_menu_screen = None
    tag menu_Slavia
    modal True
    
    # Фон
    add prefix_Gallery+'Slavia_screen_mut.png'
    add Solid("#00000075") xpos -0.82
    add("#030b1d99")
    add Text('Арты', style = 'menu_sl_style_text')
    
    
    # Превью
    side "c b r":
        area (0.2, 0.1, 0.7, 0.85)
        viewport:
            draggable True
            mousewheel 'horizontal'
            scrollbars None
            frame:
                style 'default'
                xalign 0.8 yalign 0.65
                grid 9 4:
                    spacing 40
                    for i in range(0, len(name_cg)):
                        add s.make_button(name_cg[i][:-4], prefix_small_cg + name_cg[i], locked = sl_locked)
                        
                    
                    null
                    
                    
                    

    # Кнопки
    frame:
        style 'default'
        xalign 0.05 yalign 0.5
        grid 1 3:
            spacing 40
            for i in range(0, 3):    
                textbutton [text_button[2][0][i]] style "log_button" text_style "settings_link_sl_mm" xalign 0.05 yalign 0.5 action Show(text_button[2][1][i], transition = Fade(1.0, 0.0, 1.0, color='#000000'))