screen slavia_music_room:   
    $ _game_menu_screen = None
    tag menu_Slavia
    modal True

    add(prefix_Gallery + 'Slavia_screen_mut.png')
    add("#030b1d99")
    add Text('Музыка', style = 'menu_sl_style_text')
    add Solid("#00000075") xpos -0.82
    
    ## music_room_btn
    side "c b r":
        area (0.3, 0.1, 0.61, 0.85)
        viewport id "music_box":
            draggable True
            mousewheel True
            scrollbars None
            frame:
                style 'default'
                xalign 0.8 yalign 0.65
                grid 1 len(sl_music):
                    spacing 20
                    for name, track in sorted(sl_music.iteritems()):
                        textbutton name style "log_button" text_style "settings_link_sl_mm" action mrs.Play(track)


    ## button
    frame:
        style 'default'
        xalign 0.05 yalign 0.5
        grid 1 3:
            spacing 40
            for i in range(0, 3):
                textbutton [text_button[0][0][i]] style "log_button" text_style "settings_link_sl_mm" action Show(text_button[0][1][i], transition = Fade(1.0, 0.0, 1.0, color='#000000'))
    textbutton 'Старт' style "log_button" text_style "settings_link_sl_mm" xalign 0.05 yalign 0.8 action [Hide("menu_Slavia"), Jump ("Slavia_day1")]
    textbutton 'Уйти' style "log_button" text_style "settings_link_sl_mm" xalign 0.05 yalign 0.9 action [Hide('mm_Slavia', transition = Fade(1.0, 0.0, 1.0, color='#000000')), MainMenu(confirm = False)] 
        