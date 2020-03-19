screen Slavia_Gallery_bg:
# Меню
    $ _game_menu_screen = None
    tag menu_Slavia
    modal True
    
    # Фон
    add prefix_Gallery + 'Slavia_screen_mut.png'
    add("#030b1d99")
    add Solid("#00000075") xpos -0.82
    add Text('Фоны', style = 'menu_sl_style_text')
    
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
                grid 23 4:
                    spacing 40
                    for i in range(0, len(name_bg)):
                        add s.make_button(name_bg[i][:-4], prefix_small_bg + name_bg[i], locked = sl_locked)
                        
                    null
                    null
                    null
                    


    # Кнопки
    frame:
        style 'default'
        xalign 0.05 yalign 0.5
        grid 1 3:
            spacing 40
            for i in range(0, 3):
                textbutton [text_button[1][0][i]] style "log_button" text_style "settings_link_sl_mm" action Show(text_button[1][1][i], transition = Fade(1.0, 0.0, 1.0, color='#000000'))
    textbutton 'Старт' style "log_button" text_style "settings_link_sl_mm" xalign 0.05 yalign 0.8 action [Hide("menu_Slavia"), Jump ("Slavia_day1")]
    textbutton 'Уйти' style "log_button" text_style "settings_link_sl_mm" xalign 0.05 yalign 0.9 action [Hide('mm_Slavia', transition = Fade(1.0, 0.0, 1.0, color='#000000')), MainMenu(confirm = False)] 
  
    