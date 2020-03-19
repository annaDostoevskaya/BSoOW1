# Ввод в курс дела
screen txt_op_sl_mm():
    $ _game_menu_screen = None
    tag menu_Slavia
    modal True
   
    add prefix_name_cg + "standart_slavia.png"
    
    textbutton '{size=70}Далее{/size}':
        style "log_button"
        text_style 'AFTORS'
        xalign .98
        yalign .05
        hovered Play("sound", perfix_sound + 'menu_click.ogg')
        action [Hide("txt_op_sl_mm", transition = Fade(1.0, 0.0, 1.0, color='#000000')), Jump('mm_Slavia')]
        at btn_read_navig
     
    frame background Frame("images/gui/choice/"+persistent.timeofday+"/choice_box.png", 10, 10) xalign 0.01 yalign -0.02 left_padding 200 right_padding 200 bottom_padding 150 top_padding 150 at DISSOLVE:
        text 'Вы можете нажать на:{p}{p}{color=#ff5050}Косы,{/color} для того чтобы {color=#33cc33}Выйти{/color} из мода,{p}{p}{color=#ff5050}Чулочки,{/color} для того чтобы перейти в {color=#33cc33}Музыкальную Комнату,{/color}{p}{p}{color=#ff5050}Юбку,{/color} для того чтобы перейти в {color=#33cc33}Галерею Артов,{/color}{p}{p}На {color=#ff5050}Фон{/color} позади Слави, для того чтобы перейти в {color=#33cc33}Галерею Фонов,{/color}{p}{p}Или вы можете взять {color=#ff5050}Славю за руку,{/color} чтобы {color=#33cc33}Начать{/color} это путешествие!{p}{p}{p}Так же не забывайте, что мы нуждаемся в поддержке!{p}Поэтому подписывайтесь на нашу грппу во ВКонтакте,{p}Стим Мастерскую{p}И лайкайте Фанфик на ФикБуке{p}({color=#ff5050}Грудь{/color} - активирует {color=#33cc33}18+{/color}){p}{p}Это Андроид версия,{p}что-то может работать не так как задумывалось.' size 25 color "#ffdd7d" xmaximum 1.0 at DISSOLVE
    

    
# screen_menu
screen mm_Slavia:
    tag menu_Slavia
    modal True
    
    $ _game_menu_screen = None
    $ persistent.menu = None
    
    # bg mm_Slavia
    add prefix_name_cg + 'standart_slavia.png'
    add Solid("#00000075")  at DISSOLVE_solid


    imagebutton:
        auto prefix_mm + 'start_%s.png'
        focus_mask True
        action [Hide("mm_Slavia", transition = Fade(1.0, 0.0, 1.0, color='#000000')), Jump('Slavia_day1')]
        at START
        


    imagebutton:
        auto prefix_mm + 'cg_gallery_%s.png'
        focus_mask True
        hovered Play("sound", "sound/sfx/wind_gust.ogg")
        action Show('Slavia_Gallery_cg', transition = Fade(1.0, 0.0, 1.0, color='#000000'))
        at CG
        
        
    imagebutton:
        auto prefix_mm + 'bg_%s.png'
        focus_mask True
        action Show('Slavia_Gallery_bg', transition = Fade(1.0, 0.0, 1.0, color='#000000'))
        at BG
        

    imagebutton:
        auto prefix_mm + 'musroom_%s.png'
        focus_mask True
        action Show('slavia_music_room', transition = Fade(1.0, 0.0, 1.0, color='#000000'))
        at MUSROOM
        

    imagebutton:
        auto prefix_mm + 'hen_%s.png'
        focus_mask True
        action [Hide('mm_Slavia', transition = Fade(1.0, 0.0, 1.0, color='#000000')), Jump('hentai')]
        at HEN
        

    imagebutton:
        auto prefix_mm + 'logo_%s.png'
        focus_mask True 
        action [Hide('mm_Slavia', transition = Fade(1.0, 0.0, 1.0, color='#000000')), Jump('Slavia_create')]
        at SUB         


    imagebutton:
        auto prefix_mm + 'exit_%s.png'
        focus_mask True 
        action [Hide('mm_Slavia', transition = Fade(1.0, 0.0, 1.0, color='#000000')), MainMenu(confirm = False)] 
        at EXIT


 
        
# Ссылка
    # Ссылка на фик-бук
    frame:
        style 'default'
        yalign 0.95
        xalign 0.05
        grid len(HTTPS) 1:
            spacing 30
            for page, https in HTTPS.iteritems():
                imagebutton:
                    auto prefix_name_https + page # Путь к кнопкам
                    focus_mask True
                    hovered Play("sound", perfix_sound + 'menu_click.ogg')
                    action OpenURL(https) # Ссылка
                    at DISSOLVE

# Наши инициалы
    frame:
        style 'default'
        yalign 0.5
        xalign 0.05
        grid 1 len(NAME_ADRES):
            spacing Spacing_MM
            for name, adress in NAME_ADRES.iteritems():
                textbutton name:
                    style "log_button"
                    text_style 'AFTORS'
                    hovered Play("sound", perfix_sound + 'menu_click.ogg')
                    action OpenURL(adress)
                    at BTN_AUTORS


label mm_Slavia:

    $ _game_menu_screen = None
    
    
    if persistent.end_game != True:
        scene cg standart_slavia with fade
        
    if not persistent.your_name:
    
        $ day_time()
        'Заполни регистрационный лист, пионер!'
        $ your_name = renpy.call_screen("enter_your_name")

        menu:

            'Пионер!':
                $ persistent.pol = 'b'
                python:
                    your_name = your_name.strip() or 'Пионерка'
                $ persistent.your_name = your_name
                
            'Пионерка!':
                $ persistent.pol = 'g'
                python:
                    your_name = your_name.strip() or 'Пионерка'    
                $ persistent.your_name = your_name
                        
        if persistent.pol == 'b':
            'Приятной игры, дорогой [persistent.your_name]'
            
        else:
            'Приятной игры, дорогая [persistent.your_name]'
            
    
    if One == 0:
        if persistent.end_game == True:
            $ persistent.end_game = False

        else:
            play music Warm_sunset fadein 3
            
        $ One = 1
        
        
    if persistent.read_navig != True:
        $ persistent.read_navig = True
        call screen txt_op_sl_mm()
        
        
    call screen mm_Slavia
    
label hentai:
    $ _game_menu_screen = None
    
    if not persistent.hentai:
        play sound sfx_konami_on
        $ persistent.hentai = True
        
    else:
        play sound sfx_konami_off
        $ persistent.hentai = False
    jump mm_Slavia