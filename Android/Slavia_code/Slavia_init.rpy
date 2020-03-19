# $ user = os.environ.get('username') 

## Гарантириует хентай в андроид версии( ! )
init 9999999 python:

    prefix_game_hentai = 'Slavia/images/hentai/'
    
    for i in renpy.list_files():
        
        if i.startswith( (prefix_game_hentai) ) and i.endswith( ('.jpg') ):
            renpy.image('cg '+str(i)[21:-4], i)
            
            
init python:

    persistent.SL_version = '1.0.0_Android'
    
    ## Perfix for:
    prefix_name_bg = 'Slavia/images/bg/'
    prefix_name_cg = 'Slavia/images/cg/'
    prefix_small_cg = 'Slavia/images/images_small/cg/'
    prefix_small_bg = 'Slavia/images/images_small/bg/'
    sl_locked = 'Slavia/images/images_small/logo/logo1.png'
    prefix_name_https = 'Slavia/images/Slavia_menu/URL/'
    prefix_mm = 'Slavia/images/Slavia_menu/main_menu_Slavia/'
    prefix_Gallery = 'Slavia/images/Slavia_menu/Gallery_Slavia/'
    perfix_sound = 'Slavia/music/sounds/'
    prefix_music = 'Slavia/music/music/'
    prefix_ambience = 'Slavia/music/ambience/'
    prefix_fonts = 'Slavia/images/text/'
    prefix_sprites = 'Slavia/images/sprites/'
    prefix_GUI = 'Slavia/images/GUI/input/'
    direct_Volleyball = 'Slavia/images/GUI/Volleyball/'
    way_Leaves = 'Slavia/images/GUI/Leaves/'
    way_Vomiting = 'Slavia/images/GUI/Vomiting/'
    way_Blossom = 'Slavia/images/GUI/Blossom/'
    way_Fog = 'Slavia/images/GUI/Fog/'
    way_Semen = 'Slavia/images/GUI/Semen/'
    way_410 = 'Slavia/images/GUI/410/'
    size_under_input = 18
    input_text_six_day = 22
    AFTOR_SIZE = 30
    CREATE_SIZE = 30
    Spacing_MM = 0#(?)
    List_For_Sub = []
    


    ## Автоматическое объявление СГ и БГ.
    for i in renpy.list_files():
    
        if i.startswith((prefix_name_bg)) and i.endswith(('.png', '.jpg')):
            renpy.image('bg '+str(i)[17:-4], i)
            
        if i.startswith((prefix_name_cg)) and i.endswith(('.png', '.jpg')):
            renpy.image('cg '+str(i)[17:-4], i)
            

            


# Галерея

    s = Gallery()

    ## Name CG for Gallery CG
    name_cg = [ i[17:] for i in renpy.list_files() if i.startswith((prefix_name_cg)) and i.endswith(('.png', '.jpg')) ]
    


    ## Name Gallery BG image
    name_bg = [ i[17:] for i in renpy.list_files() if i.startswith((prefix_name_bg)) and i.endswith(('.png', '.jpg')) ]
    
    
    for cg in name_cg:
        s.button(cg[:-4])
        s.image( im.Crop(prefix_name_cg+cg, (0, 0, 1280, 720) ))
        s.unlock("cg "+cg[:-4])
        
    for bg in name_bg:
        s.button(bg[:-4])
        s.image( im.Crop(prefix_name_bg+bg, (0, 0, 1280, 720) ))
        s.unlock("bg "+bg[:-4])

        
    s.transition = fade
 

# Мyкзыкальная комната
    sl_music_name = [ i[19:] for i in renpy.list_files() if i.startswith((prefix_music)) and i.endswith(('.mp3', '.ogg')) ]
 
    mrs = MusicRoom(fadeout = 1.0)
    
    for i in range(0, len(sl_music_name)):
        mrs.add(prefix_music + sl_music_name[i])


    def volume_plus(channel = 'music', from_v = 1.0, end = 1.0):
        while from_v <= end:
            from_v += 0.1
            volume(from_v, channel)
            renpy.pause(0.15)

            
            
    def volume_minus(channel = 'music', from_v = 1.0, end = 1.0):
        while from_v >= end:
            from_v -= 0.1
            volume(from_v, channel)
            renpy.pause(0.15)
            
            




## AuTORS

    NAME_ADRES = {
                  'Дмитрий Zoтov{p}{size=20}Сценарист{/size}' : 'https://m.vk.com/grx9497502',
                  'Анна Достоевская{p}{size=20}Кодер{/size}' : 'https://m.vk.com/herrainsstudio',
                  '{size=27}Дмитрий Григорьев{/size}{p}{size=20}Композитор{/size}' : 'https://m.vk.com/hidekiraharu',
                  'Антон Шнайдер{p}{size=20}Художник{/size}' : 'https://m.vk.com/acid_flower',
                  #'Василий Санталов{p}{size=20}Художник{/size}' : 'https://m.vk.com/vasiliy05092005santalov'
                 }



## HTTPS//
    
    ## https:// for our society, vk steamcommunity and ficbook 
    HTTPS = {
             'fb_%s.png' : 'https://ficbook.net/readfic/7664488',
             'st_%s.png' : 'https://steamcommunity.com/sharedfiles/filedetails/?id=1649019361&searchtext=',
             'vk_%s.png' : 'https://vk.com/hris18485893'
            }
             

        
    ## TXT_btn in menu Gallery
    text_button = [
                    ## For music room
                      [
                            ['Фоны', 'Арты', 'Назад'],
                          
                            ['Slavia_Gallery_bg', 'Slavia_Gallery_cg', 'mm_Slavia']
                      ],
                      
                    ## For BG Gallery
                      [
                            ['Музыка', 'Арты', 'Назад'],
                            
                            ['slavia_music_room', 'Slavia_Gallery_cg','mm_Slavia']
                      ],
                      
                    ## For CG Gallery
                      [
                            ['Музыка', 'Фоны', 'Назад'],
                      
                            ['slavia_music_room', 'Slavia_Gallery_bg', 'mm_Slavia']
                      ]
                      
                  ]
    

    
    sl_music = {
                  
                "Arabesque - born to reggae" : prefix_music+"arabesque.mp3",
                "Neoton Familia - Falling Star" : prefix_music+"neoton_familia_falling_star.mp3",
                "Мираж - Звёзды нас ждут" : prefix_music+"mirazh_1.mp3",
                "Ricci e Poveri - Belle Italy" : prefix_music+"filichita.mp3",
                "Neoton Familia - Volt Egy Lany" : prefix_music+"volteglan.mp3",
                "B. Sarius - Kustennebel" : prefix_music+"kustennebel.mp3", 
                "Neoton Familia - Adam almodj csak tovabb" : prefix_music+"d3_adam_tovabb.mp3",
                "Neoton Familia - Karneval" : prefix_music+"d3_Karneval.mp3",
                "DJ Dimon - Alisa! Melafon!" : prefix_music+"d2_melafon.mp3",
                "R. Klayderman - Ballade pour Adeline" : prefix_music+"d2_ballade_Adeline.mp3",
                "Yuoko Oginome - Dancing hero" : prefix_music+"d2_dancing_hero.mp3",
                "Sandra - Heartbeat" : prefix_music+"d3_heartbeat.mp3",
                "Sandra - Change your mind" : prefix_music+"d3_changeyourmind.mp3",
                "Tsubame Mayumi - Hitomi wa cosumos" : prefix_music+"d3_hitomi_wa_cosmos.mp3",
                "Giorgio Moroder - Love theme" : prefix_music+"d3_moroder.mp3",
                "Веселые ребята - Последний раз" : prefix_music+"d3_posledniraz.mp3",
                "Viola Valentino - Comprame" : prefix_music+"d3_Comprame.mp3",
                "Teresa Teng - Wakare no yukan" : prefix_music+"d3_teresa_wakare.mp3",
                "Secret Service - Aux deux magots" : prefix_music+"d3_auxdeux.mp3",
                "Yuoko Oginome - Kanashimi present" : prefix_music+"d1_kanashimi.mp3",
                "Igor Korg - Nostalgia 3" : prefix_music+"d1_nostalgie.mp3",
                "Sandra - Secret Land" : prefix_music+"d1_Sandra_SL.mp3",
                "Scooter - Rhapsody in E" : prefix_music+"Scooter.mp3",
                "Пионерский гимн - Взвейтесь кострами" : prefix_music+"Pionerskiy.mp3",
                "Space - SOS" : prefix_music+"d5_SOS.mp3",
                "Lana Del Ray - High by the beach (Teoh v.)" : prefix_music+"hbtb.ogg",
                "Pochonbo Electronic Ensemble - Memories" : prefix_music+"D5_DPRK.mp3",
                "Dan Harrow - Dont break my heart" : prefix_music+"DAN.mp3",
                "Viola Valentino - Il posto della luna" : prefix_music+"Viola.mp3",
                "Francois Feldman - Le mal de toi" : prefix_music+"Fransis.mp3",
                "Murray Head - One night in Bangkok" : prefix_music+"Murray.mp3",
                "X-Perience - Game of love" : prefix_music+"X_PERIENCE.mp3",
                "С.С. Catch - Don`t wait too long" : prefix_music+"C.C. Catch - Dont wait too long.mp3",
                "Eva Csepregi - Watch the rain" : prefix_music+"watch_the_rain.mp3",
                "Bee Gees - How can you mend a broken heart" : prefix_music+"d3_bee_gees.mp3",
                "Warm sunset - Black_Be - HRiS" : prefix_music+"Warm sunset.mp3",
                "Анна Герман - Слуйчайность" : prefix_music+"Annagerman_1.mp3",
                "_Not_found_name_track_" : prefix_music+"hacker42.mp3",
                "Анна Герман - Реченька туманная" : prefix_music+"anna_german.mp3",
                "Kim Wilde - Cambodia" : prefix_music+"Kim Wilde - Cambodia.mp3",
                "ABBA - Thank you for the music" : prefix_music+"ABBA.mp3",
                "Mireille Mathieu - Siempre Amor" : prefix_music+"Siempre_Amor.mp3",
                "Goomday Dance Band - Seven tears" : prefix_music+"nagrada_robota.mp3",
                "Wind and rain - RMX" : prefix_music+"wind_and_rain_rmx.mp3",
                "Modern Martina - Инструметал №1" : prefix_music+"mm_instrumental.mp3",
                "Тили-тили тесто..." : prefix_music+"ula_song.mp3",
                "Kulmege" : prefix_music+"d8_kulmege.mp3",
                "Se Tu Vuoi - Highland" : prefix_music+"Se_tu_vuoi.mp3",
                "Midnight Lady - Chris Norman" : prefix_music+"Midnight_lady.mp3",
                "ABBA - One Of Us" : prefix_music+"ABBA - One Of Us.mp3",
                "Kim Wild - Camboja" : prefix_music+"Kim Wild - Camboja.mp3",
                "ABBA - Super Trouper" : prefix_music+"ABBA - Super Trouper.mp3",
                "Зодиак - Провинциальное диско" : prefix_music+"Zodiac.mp3",
                "Nicole - Ein bischen Frieden" : prefix_music+"Nicole - Ein bischen Frieden.mp3",
                "Miku - Bad Apple" : prefix_music+"Miku - Bad Apple.mp3",
                "Miku - Bad Applev RUS" : prefix_music+"Touhou Project RUS song.mp3",
                "V. flower - Close to you" : prefix_music+"closetoyou_dv_mil.ogg",
                "W - Koi no Vacance" : prefix_music+"W - Koi no Vacance.mp3",
                "Dchinghis Khan - Moskau" : prefix_music+"Moskau.mp3",
                "ABBA - Head Over Hills" : prefix_music+"ABBA - Head Over Hills.mp3",
                "Angel Beats - Ichiban no Takaramono" : prefix_music+"Angel Beats - Ichiban no Takaramono.mp3",
                "Secret Base - Anohana ED" : prefix_music+"Secret Base - Anohana ED.mp3",
                "Под шум и взрыв гранат..." : prefix_music+"d10_alice_song.mp3",
                "Igor Korg - Nostalgia depart" : prefix_music+"Nostalgia_depart.mp3",
                "Igor Korg - Nostalgia 13" : prefix_music+"nostalgia_shatunov.mp3",
                "Igor Korg - Nostalgia 18" : prefix_music+"nostalgia_final.mp3",
                "DuranDuran_Ordinary World_cover" : prefix_music+"DuranDuran_Ordinary World_cover.mp3",
                "R. Klayderman - Angelica Divina" : prefix_music+"Angelica_Divina.mp3",
                "Steins;Gate Movie Fuka Ryouiki no Deja Vu{p}(RUS cover Onsa Media)" : prefix_music+"Steins;Gate.mp3",
               }

    

    ## Функция для комнаты Мику "Да мигнёт свет!"
    def light_bug_1():
        volume (0.7, "sound")
        renpy.sound.play(sfx_discharge)
        persistent.sprite_time = "night"
        renpy.scene()
        renpy.show('bg int_musclub_rain', [center])
        renpy.show('sl normal pioneer', [right])
        renpy.show('mi smile pioneer', [left])
        renpy.transition(dspr)
        renpy.pause(0.25)
        persistent.sprite_time = "day"
        renpy.scene()
        renpy.show('bg int_musclub_rain_light', [center])
        renpy.show('sl normal pioneer', [right])
        renpy.show('mi smile pioneer', [left])
        renpy.transition(dspr)
        renpy.pause(0.25)
        persistent.sprite_time = "night"
        renpy.scene()
        renpy.show('bg int_musclub_rain', [center])
        renpy.show('sl normal pioneer', [right])
        renpy.show('mi smile pioneer', [left])
        renpy.transition(dspr)
        renpy.pause(0.25)
        persistent.sprite_time = "day"
        renpy.scene()
        renpy.show('bg int_musclub_rain_light', [center])
        renpy.show('sl normal pioneer', [right])
        renpy.show('mi smile pioneer', [left])
        renpy.transition(dspr)
        renpy.pause(0.25)
        renpy.sound.stop()  
        
        
    def light_bug_2():
        persistent.sprite_time = "night"
        renpy.sound.play(sfx_discharge)
        renpy.scene() 
        renpy.show('bg Hallway_2_night', [center])
        renpy.show('sl smile2 lobody far', [sl_trans_2])
        renpy.transition(dspr)
        renpy.pause(0.25)
        persistent.sprite_time = "day"
        renpy.scene() 
        renpy.show('bg Hallway_2', [center])
        renpy.show('sl smile2 lobody far', [sl_trans_2])
        renpy.transition(dspr)
        renpy.pause(0.25)
        persistent.sprite_time = "night"
        renpy.sound.play(sfx_discharge)
        renpy.scene()
        renpy.show('bg Hallway_2_night', [center])
        renpy.show('sl smile2 lobody far', [sl_trans_2])
        renpy.transition(dspr)
        renpy.pause(0.25)
        persistent.sprite_time = "day"
        renpy.scene() 
        renpy.show('bg Hallway_2', [center])
        renpy.show('sl smile2 lobody far', [sl_trans_2])
        renpy.transition(dspr)
        renpy.pause(0.25)
        persistent.sprite_time = "night"
        renpy.sound.play(sfx_discharge)
        renpy.scene() 
        renpy.show('bg Hallway_2_night', [center])
        renpy.show('sl smile2 lobody far', [sl_trans_2])
        renpy.transition(dspr)
        renpy.pause(0.25)
        renpy.sound.stop()
        # Не знаю...  ._.
        

    def Leaves():
        renpy.sound.play("sound/sfx/wind_gust.ogg")
        renpy.show('lay0_0', at_list = [lay0_0], zorder = 10)
        renpy.show('lay0_1', at_list = [lay0_1], zorder = 10)
        renpy.show('lay1_0', at_list = [lay1_0], zorder = -5)
        renpy.show('lay1_1', at_list = [lay1_1], zorder = 5)
        renpy.show('lay1_2', at_list = [lay1_2], zorder = 5)
        renpy.show('lay1_3', at_list = [lay1_3], zorder = -5)
        renpy.show('lay1_4', at_list = [lay1_4], zorder = 5)
        renpy.show('lay2_0', at_list = [lay2_0], zorder = -9)
        renpy.show('lay2_1', at_list = [lay2_1], zorder = -9)
        renpy.show('lay2_2', at_list = [lay2_2], zorder = -9)
        renpy.show('lay2_3', at_list = [lay2_3], zorder = -9)


    def Snow_Blossom():
        
        renpy.show('snow_0')
        renpy.show('snow_1')
        renpy.show('snow_2')
        renpy.show('snow_3')


    def Semen_1():
        renpy.show('s1', at_list = [sb_at(0.1, 0.1)])
        renpy.show('s2', at_list = [sb_at(0.7, 0.4)])
        renpy.show('s3', at_list = [sb_at(0.2, 0.5)])
        renpy.transition(dspr)
        renpy.pause(0.25)
        
    
    def Semen_2():
        renpy.show('s1', at_list = [sb_at(0.3, 0.1)])
        renpy.show('s5', at_list = [sb_at(0.7, 0.4)])
        renpy.show('s4', at_list = [sb_at(0.1, 0.7)])
        renpy.transition(dspr)
        renpy.pause(0.25)
        
    def Semen_3():
        renpy.show('s6', at_list = [sb_at(0.3, 0.1)])
        renpy.show('s5', at_list = [sb_at(0.7, 0.4)])
        renpy.show('s1', at_list = [sb_at(0.1, 0.7)])
        renpy.transition(dspr)
        renpy.pause(0.25)
        
        
    ## Настройки стилей
    # Стиль для текста над input - ом в 6 дне
    style.text_input = Style(style.default)
    style.text_input.color = '#61442f'
    style.text_input.size = size_under_input    
    style.text_input.font = prefix_fonts+'izhitsa.ttf'
    style.text_input.xpos = 0.25
    style.text_input.ypos = 0.25
    style.text_input.italic = True
    style.text_input.bold = True

    # Стиль для текста input - а в 6 дне
    style.input.layout = 'subtitle'
    style.input.color = '#ab8058'
    style.input.size = input_text_six_day
    style.input.xpos = 0.25
    style.input.ypos = 0.25
        
    style.AFTORS = Style(style.default)
    style.AFTORS.color = '#f1d076'
    style.AFTORS.size = AFTOR_SIZE
    style.AFTORS.font = prefix_fonts+'izhitsa.ttf'
        
    style.menu_sl_style_text = Style(style.default)
    style.menu_sl_style_text.font = prefix_fonts+'izhitsa.ttf'
    style.menu_sl_style_text.size = 50
    style.menu_sl_style_text.color = '#f1d076'
    style.menu_sl_style_text.xpos = 0.02
    style.menu_sl_style_text.ypos = 0.05

        
    style.settings_link_sl_mm = Style(style.default)
    style.settings_link_sl_mm.font  = "fonts/calibrib.ttf"
    style.settings_link_sl_mm.size = 40
    style.settings_link_sl_mm.kerning = 3
    style.settings_link_sl_mm.color = "#909ca3"
    style.settings_link_sl_mm.hover_color = "#ffffff"
    style.settings_link_sl_mm.selected_color = "#909ca3"
    style.settings_link_sl_mm.selected_idle_color = "#909ca3"
    style.settings_link_sl_mm.selected_hover_color = "#ffffff"
    style.settings_link_sl_mm.insensitive_color = "#909ca3"
    
    style.settings_link_sl_nb = Style(style.settings_link_sl_mm)
    style.settings_link_sl_nb.size = 60

    style.StyleSub_1 = Style(style.default)
    style.StyleSub_1.size = CREATE_SIZE
    style.StyleSub_1.color = '#ffd200'


    
init -1:

# Трансформации
    ## Transform NOT delete, i not wanna write what wthis to do!
    transform DISSOLVE:
        alpha 0.0
        linear 0.25 alpha 1.0


## this is transform for menu in game 10 day
    transform DISSOLVE_MM_right:
        right
        alpha 0.0
        linear 0.25 alpha 1.0
        on hover:
            right
            alpha 0.0
            linear 0.25 alpha 1.0
        on idle:
            right
            alpha 0.0
            linear 0.25 alpha 1.0

## this is transform for menu in game 10 day            
    transform DISSOLVE_MM_center:
        center
        alpha 0.0
        linear 0.25 alpha 1.0
        on hover:
            center
            alpha 0.0
            linear 0.25 alpha 1.0
        on idle:
            center
            alpha 0.0
            linear 0.25 alpha 1.0

## this is transform for menu in game 10 day
    transform DISSOLVE_MM_left:
        left
        alpha 0.0
        linear 0.25 alpha 1.0
        on hover:
            left
            alpha 0.0
            linear 0.25 alpha 1.0
        on idle:
            left
            alpha 0.0
            linear 0.25 alpha 1.0
            
    transform BG:
        center
        on hover:
            center
            DISSOLVE
    
    # Трансформации в main_menu(Субтитры(Грудь))
    transform HEN:
        xpos 0.552
        ypos 0.3874
        on idle:
            xpos 0.552
            ypos 0.3874
            DISSOLVE
        on hover:
            xpos 0.4905
            ypos 0.04
            DISSOLVE
        
    
    # Трансформации в main_menu(Выход(Косы))
    transform EXIT:
        xpos 0.729
        ypos 0.537
        on idle:
            xpos 0.729
            ypos 0.537
            DISSOLVE
        on hover:
            xpos 0.5675
            ypos 0.1359   
            DISSOLVE
    
    # Трансформации в main_menu(К галереи(Юбка))
    transform CG:   
        xpos 0.5065
        ypos 0.6265
        on idle:
            xpos 0.5065
            ypos 0.6265
            DISSOLVE
        on hover:
            xpos 0.4829
            ypos 0.0435
            DISSOLVE
    
    
    # Трансформации в main_menu(К музкомнате(Чулочек))
    transform MUSROOM:
        xpos 0.537
        ypos 0.875
        on idle:
            xpos 0.537
            ypos 0.875
            DISSOLVE
        on hover:            
            xpos 0.5
            ypos 0.0446
            DISSOLVE
         
            
    transform START:
        xpos 0.631
        ypos 0.529
        on idle:
            xpos 0.631
            ypos 0.529
            DISSOLVE
        on hover:
            xpos 0.632
            ypos 0.613
            DISSOLVE
            
            
    transform SUB:
        xpos 0.035
        ypos 0.05
        DISSOLVE
        on idle:
            linear 0.2 zoom 1.1
        on hover:
            linear 0.2 zoom 1.3
            
            
    transform GLAVA_1:
        on idle:
            DISSOLVE
            xpos 0.5
            ypos 0.5
            linear 0.5 rotate 15 zoom 1.0 
        on hover:
            DISSOLVE
            xpos 0.5
            ypos 0.5
            linear 1.0 rotate 0 zoom 1.5

            
    ## Transform NOT delete, i not wanna write what wthis to do!
    transform sl_trans_2:
        xpos 0.1
        zoom 1.0
    

        
    
    ## Transform NOT delete, i not wanna write what wthis to do!
    transform DISSOLVE_solid:
        xpos -0.7175
        DISSOLVE
        
    ## Transform NOT delete, i not wanna write what wthis to do!
    transform BTN_AUTORS:
        DISSOLVE
        on idle:
            linear 0.15 zoom 1.13
        on hover:
            linear 0.15 zoom 1.38
            

            

    # Текст вверх в титрах
    transform txt_up:              # Трансформация
        yalign 1.5                 # Для перемещения текста вверх
        linear 30.0 yalign -1.5    # В титрах!
        
    
    # Трансформация run
    transform run:                 
        zoom 1.05 anchor (48,27)   
        ease 0.20 pos (0, 0)      
        ease 0.20 pos (25,25)      
        ease 0.20 pos (0, 0)    
        ease 0.20 pos (-25,25)    
        repeat                   
    
    
    # Трансформация swim
    transform swim:                
        yalign 1.0        
        xalign 1.0                 
        linear 1.5 zoom 1.8         
        
    # Трансформация not_swim                                
    transform not_swim:            
        yalign 1.0                 
        xalign 1.0                 
        zoom 1.8                   
        yalign 1.0                 
        xalign 1.0                 
        linear 1.5 zoom 1.0        


    # В кабине втобуса               
    transform bus:                 # Эта трансформация
        xalign 0.5                 # Находится в кабине 
        yalign 0.4                 # Автобуса
        linear 1.0 zoom 2.0        # В первом дне
        
    
 
    # Показать ANN                 # Трансформация                       
    transform ann:                 # Кторую использует Аня что бы
        ypos 0.3                   # Показаться в левой части экрана
    
    
    # Показать OXY
    transform oxy:               # Трансформация
        ypos 0.2                  # Которую использует Окасана
        xpos .1                     # Что бы показаться и увеличиться в
        zoom 1.5                   # Левой части экрана
        
        
    # Славя спит    
    transform sleep_sl_2:          # Следующие две трансформации для
        xalign 0.5                 # Слави и Семена
        yalign 0.
        zoom 2.5        
    
    
    # Славя рядом
    transform sex_sl:              # Следующие две трансформации для
        xalign 0.5                 # Слави и Семена
        yalign 0.1
        linear 1.0 zoom 2.0
            
            
    # Толик заводит волгу    
    transform volga_tl:            # Эта трансформация
        xalign 1.0                 # Для того что бы Толик 
        yalign 0.9                 # Завел свою Волгу
        linear 1.0 zoom 2.5        # Рядом со столвой
        
        
    # Магнитофон соната
    transform son:                 # Магнитофон
        xpos 0.35                  # Соната
        ypos 0.75                  # Виолы
        
    
    transform scena:               # Трансформация
        ypos -0.2                  # На сцене
        xpos -0.24
        zoom 1.5
      
    transform btn_read_navig:
        alpha 0.0
        pause(7.0)
        linear 2.0 alpha 1.0
        on idle:
            linear 0.2 zoom 1.0
        on hover:
            linear 0.2 zoom 1.2
        
    # трансформация ven
    transform ven:     # для нормального 
        ypos 0.15      # показа венеры
        xpos 0.25

    # трансформация ven
    transform tr_ven:     # для нормального 
        ypos 0.2      # показа венеры
        xpos 0.25

    # Vomiting
    transform ani_Vomiting:
        linear 1.0 alpha 0.0
        linear 1.0 alpha 1.0
        repeat
        
# Трансформация с изображением    
    # На дискотеке
    transform disko:
        "images/bg/ext_square_night_party.jpg" with dissolve
        pause 1.0
        "images/bg/ext_square_night_party2.jpg" with dissolve
        pause 1.0
        repeat

    # Дискотека, мигание

    image ani_disko:
        contains disko
        
    
    ## Трансформация для хентай Слави
    transform hen_sl_home:
        zoom 2.5
        linear 1.5 ypos -0.5 xpos -0.7
        linear 2.0 xpos -0.8 ypos -1.0
        linear 2.0 ypos 0.0 xpos -1.0
        repeat
        
    ## Трансформация для хентай Слави
    transform consert:
        zoom 2.3
        linear 5.0 ypos -0.5 xpos -1.3
        linear 5.0 xpos -0.1 ypos -1.0
        linear 5.0 ypos 0.0 xpos -0.5
        repeat
   

    # Робот robor_normal
    transform robor_normal:
        prefix_sprites+"rob/robot_far.png"
        pos (0.5, 1.0)
    
    # Робот robor_close
    transform robor_close:
        prefix_sprites+"rob/robot_far.png"
        pos (0.5, 1.5)
        zoom 1.5
        
        
## Transform Leaves
    transform lay0_0:
        ypos 0.0
        xpos 0.3
        alpha 0.0
        
        parallel:
            linear 0.25 alpha 1.0
        
        parallel:
            linear 1.5 ypos 1.1 
        
        parallel:
            linear 2.0 xpos 1.1
            
        pause(60)
        repeat 3
            

    transform lay0_1:
        ypos 0.1
        xpos 0.0
        alpha 0.0
        
        parallel:
            linear 0.25 alpha 1.0
        
        parallel:
            linear 1.6 xpos 0.4
        
        parallel:
            linear 1.0 ypos 1.5
            
        pause(60)
        repeat 3
            
    transform lay1_0:
        xpos -0.1
        ypos -0.1
        
        parallel:
            linear 1.6 xpos 1.1
            
        parallel:
            linear 2.0 ypos 0.5
            
        pause(30)
        repeat 2

    transform lay1_1:
        xpos -0.1
        ypos -0.1
        
        parallel:
            linear 1.0 xpos 1.1
            
        parallel:
            linear 2.0 ypos 0.7
            
        pause(30)
        repeat 4
            
            
    transform lay1_2:
        xpos -0.1
        ypos -0.1
        
        parallel:
            linear 2.5 xpos 0.9
            
        parallel:
            linear 2.0 ypos 1.1
            
        pause(30)
        repeat 1
            
    transform lay1_3:
    
        xpos 0.5
        ypos -0.1
        
        parallel:
            linear 1.5 xpos 1.0
            
        parallel:
            linear 2.0 ypos 1.1
            
        pause(30)
        repeat 4
            
            
    transform lay1_4:
        
        xpos -0.1
        ypos 0.7

        parallel:
            linear 1.3 xpos 0.4
            
        parallel:
            linear 1.0 ypos 1.1
            
        pause(30)
        repeat 2
            
    transform lay2_0:
        xpos .42
        ypos -0.1
        pause(3.0)
        
        parallel:
            linear 1.0 xpos .43 xzoom 1.0
            linear 1.9 xpos .37 xzoom 0.5
            repeat
        
        parallel:
            ypos -0.1
            linear 10.0 ypos 1.1
            repeat
            
            
    transform lay2_1:
        xpos .22
        ypos -0.1
        pause(3.0)
        
        parallel:
            linear 0.8 xpos .23
            linear 0.9 xpos .2
            repeat
        
        parallel:
            ypos -0.1
            linear 8.0 ypos 1.1
            repeat
            
    transform lay2_2:
        xpos .82
        ypos -0.1
        pause(3.0)
        
        parallel:
            linear 1.2 xpos .83 xzoom -0.5
            linear 1.3 xpos .77 xzoom 1.1
            repeat
        
        parallel:
            ypos -0.1
            linear 6.0 ypos 1.1
            pause(3.0)
            repeat
            
    transform lay2_3:
        xpos .5
        ypos -0.1
        pause(3.0)
        
        parallel:
            linear 1.0 xpos .53
            linear 1.5 xpos .45
            
        parallel:
            ypos -0.1
            linear 15.0 ypos 1.1
            repeat


    transform Sub:
        
        xpos 0.1
        ypos 1.5
        
        linear 300.0 ypos -10.0
        
        
    transform sb_at(X, Y):
        
        xpos X
        ypos Y
        
        linear 2.0 ypos Y + 0.2
        
        time 2
        linear 1.0 alpha 0.0

init:

    # $ config.developer = True
    $ mods["Slavia_prolog"] = u"{font=Slavia/images/text/izhitsa.ttf}Возвращение Семена или орден Совёнка{/font}"

    # Канал на котором играет музыка в столовой
    $ renpy.music.register_channel("radio", mixer = "music", loop = True, stop_on_mute = True, tight = True)


# Переменные для игры(not persistent.data)
    # Для Dissolve                  # Мне кажется, это 
    $ dissolve2 = Dissolve(2)       # Не нуждается в обьяснении
    
    # Впервые в меню
    $ One = 0                       # Что бы музыка исправно играла в меню
    
    # Для input - а от Лены в 6 дне
    $ otvet_1 = False                 # Что бы сохранить его в переменную
    
    # Для input - а от Кибернетиков в 6 дне
    $ otvet_2 = False                 # Что бы сохранить его в переменную
    
    # Для input - а от Слави в 6 дне
    $ otvet_3 = False                 # Что бы сохранить его в переменную

    # Все правильные ответы в 6 дне для input - а от Лены
    $ OTVETS_1 = ['арине родионовне', 
                  'арина родионовна', 
                  'родионовна арина',
                  'родионовне арине',
                  'няня пушкина',
                  'няне пушкина', 
                  'арине', 'арина',
                  'родионовне', 
                  'родионовна']

    # Все правильные ответы в 6 дне для input - а от Кибернетиков              
    $ OTVETS_2 = ['дивергенция',
                  'оператор набла',
                  'операция в физике',
                  'операция в физике и не только',
                  'расхождение',
                  'разветвление',
                  'дифференциальный оператор',
                  'wind3(chr(115))*f',
                  'div*f', 'divf>0', 'divf<0', 'divf=0']
               
    # Все правильные ответы в 6 дне для input - а от Слави
    $ OTVETS_3 = ['командарм 62 армии', 
                  'чуйков', 
                  'шумилов', 
                  'чуйков и шумилов', 
                  'шумилов и чуйков', 
                  'командарм 62 армии и генерал 64 армии', 
                  'генерал 64 армии и командарм 62 армии',
                  'чуйков, командир 62 армии, и шумилов, генерал 64 армии',
                  'чуйков командир 62 армии и шумилов генерал 64 армии']



    ## Для титров
    image Text1 = ParameterizedText(style = "StyleSub_1")
    
# effect
    # fog
    image fog_ext_houses_day = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip("images/bg/ext_houses_day.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.7), im.matrix.brightness(-0.4)))
    image fog_ext_square_day = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip("images/bg/ext_square_day.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.7), im.matrix.brightness(-0.4)))
    image fog_ext_polyana_day = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip("images/bg/ext_polyana_day.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.7), im.matrix.brightness(-0.4)))
    image fog_ext_house_of_sl_sunset = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip(prefix_name_bg+"ext_house_of_sl_sunset.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.7), im.matrix.brightness(-0.4)))
    image fog_ext_path_day = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip("images/bg/ext_path_day.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.7), im.matrix.brightness(-0.4)))
    image fog_ext_musclub_day = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip("images/bg/ext_musclub_day.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.7), im.matrix.brightness(-0.4)))
    image fog_ext_washstand_day = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip("images/bg/ext_washstand_day.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.7), im.matrix.brightness(-0.4)))
    image fog_ext_no_bus = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip("images/bg/ext_no_bus.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.7), im.matrix.brightness(-0.4)))
    image fog_ext_house_of_mt_day = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip("images/bg/ext_house_of_mt_day.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.7), im.matrix.brightness(-0.4)))

    image fog_3m_ext_houses_day = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip("images/bg/ext_houses_day.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.5), im.matrix.brightness(-0.4)))
    image fog_3m_ext_house_of_sl_sunset = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip(prefix_name_bg+"ext_house_of_sl_sunset.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.5), im.matrix.brightness(-0.4)))
    image fog_3m_ext_musclub_day = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip("images/bg/ext_musclub_day.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.5), im.matrix.brightness(-0.4)))
    image fog_3m_ext_no_bus = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip("images/bg/ext_no_bus.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.5), im.matrix.brightness(-0.4)))
    image fog_3m_ext_square_day = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip("images/bg/ext_square_day.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.5), im.matrix.brightness(-0.4)))    
    image fog_3m_int_bus_night = im.Composite((1280, 720),(0,0), im.MatrixColor(im.Flip("images/bg/int_bus_night.jpg", horizontal = True), im.matrix.brightness(0.0)),(0,0),  im.MatrixColor(im.Alpha(way_Fog+'fog.jpg', 0.5), im.matrix.brightness(-0.4)))


    # Мутно
    image gallery = prefix_Gallery+"Slavia_screen_mut.png"

    
    # dark
    image bg ext_polyana_night_dark = im.MatrixColor("images/bg/ext_polyana_night.jpg", im.matrix.brightness(-0.4))


    # Темноватый оттенок
    transform black: ## Это для mm_Slavia
        "#00000075"
    image white = "#ffffff"
    image music = "#00000075"
    image music_room = "#030B1D99"
    

    # mp3
    $ qwer = prefix_music+'arabesque.mp3'                                            #1. Arabesque - born to reggae
    $ neoton = prefix_music+'neoton_familia_falling_star.mp3'                        #2. Neoton Familia - Falling Star
    $ mirazh = prefix_music+'mirazh_1.mp3'                                           #3. Мираж - Звёзды нас ждут
    $ DD_Ordinary_World_cover = prefix_music+'DuranDuran_Ordinary World_cover.mp3'   #4. DuranDuran_Ordinary World_cover    
    $ filichita = prefix_music+'filichita.mp3'                                       #5. Ricci e Poveri - Belle Italy
    $ volteglan = prefix_music+'volteglan.mp3'                                       #6. Neoton Familia - Volt Egy Lany
    $ sarius = prefix_music+'kustennebel.mp3'                                        #7. B. Sarius - Kustennebel
    $ adam_tovabb = prefix_music+'d3_adam_tovabb.mp3'                                #8. Neoton Familia - Adam almodj csak tovabb
    $ d3_Karneval = prefix_music+'d3_Karneval.mp3'                                   #9. Neoton Familia - Karneval
    $ d2_melafon = prefix_music+'d2_melafon.mp3'                                     #10. DJ Dimon - Alisa! Melafon! (DJ Dimon - Алиса! Мелафон!)
    $ d2_ballade_Adeline = prefix_music+'d2_ballade_Adeline.mp3'                     #11. R. Klayderman - Ballade pour Adeline
    $ d2_dancing_hero = prefix_music+'d2_dancing_hero.mp3'                           #12. Yuoko Oginome - Dancing hero
    $ d3_heartbeat = prefix_music+'d3_heartbeat.mp3'                                 #13. Sandra - Heartbeat
    $ d3_Comprame = prefix_music+'d3_Comprame.mp3'                                   #14. Viola Valentino - Comprame
    $ d3_changeyourmind = prefix_music+'d3_changeyourmind.mp3'                       #15. Sandra - Change your mind
    $ d3_hitomi_wa_cosmos = prefix_music+'d3_hitomi_wa_cosmos.mp3'                   #16. Tsubame Mayumi - Hitomi wa cosumos
    $ d3_moroder = prefix_music+'d3_moroder.mp3'                                     #17. Giorgio Moroder - Love theme
    $ d3_posledniraz = prefix_music+'d3_posledniraz.mp3'                             #18. Веселые ребята - Последний раз    
    $ d3_teresa_wakare = prefix_music+'d3_teresa_wakare.mp3'                         #19. Teresa Teng - Wakare no yukan
    $ d3_auxdeux = prefix_music+'d3_auxdeux.mp3'                                     #20. Secret Service - Aux deux magots
    $ d1_kanashimi = prefix_music+'d1_kanashimi.mp3'                                 #21. Yuoko Oginome - Kanashimi present
    $ d1_nostalgie = prefix_music+'d1_nostalgie.mp3'                                 #22. Игорь Корг - Ностальгия по 80м трек №3 (Igor Korg - Ностальгия по 80м трек 3)
    $ Sandra_SL = prefix_music+'d1_Sandra_SL.mp3'                                    #23. Sandra - Secret Land
    $ Scooter = prefix_music+'Scooter.mp3'                                           #24. Scooter - Rhapsody in E
    $ Pionerskiy = prefix_music+'Pionerskiy.mp3'                                     #25. Пионерский гимн - Взвейтесь кострами
    $ d5_SOS = prefix_music+'d5_SOS.mp3'                                             #26. Space - SOS
    $ hbtb = prefix_music+'hbtb.ogg'                                                 #27. Lana Del Ray - High by the beach (Teoh version)
    $ D5_DPRK = prefix_music+'D5_DPRK.mp3'                                           #28. Pochonbo Electronic Ensemble - Memories
    $ DAN = prefix_music+'DAN.mp3'                                                   #29. Dan Harrow - Dont break my heart
    $ viola = prefix_music+'Viola.mp3'                                               #30. Viola Valentino - Il posto della luna
    $ fransis = prefix_music+'Fransis.mp3'                                           #31. Francois Feldman - Le mal de toi
    $ murray = prefix_music+'Murray.mp3'                                             #32. Murray Head - One night in Bangkok
    $ X_PERIENCE = prefix_music+'X_PERIENCE.mp3'                                     #33. X-Perience - Game of love
    $ Catch_Dont_wait_too_long = prefix_music+'C.C. Catch - Dont wait too long.mp3'  #34. С.С. Catch - Don`t wait too long
    $ watch_the_rain = prefix_music+'watch_the_rain.mp3'                             #35. Eva Csepregi - Watch the rain
    $ d3_bee_gees = prefix_music+'d3_bee_gees.mp3'                                   #36. Bee Gees - How can you mend a broken heart
    $ Warm_sunset = prefix_music+'Warm sunset.mp3'                                   #37. Warm sunset - Black_Be - HRiS (Играет в главном меню(Сочинил наш человек!))
    $ annagerman_1 = prefix_music+'Annagerman_1.mp3'                                 #39. (Играет в столовой утром)
    $ hacker = prefix_music+'hacker42.mp3'                                           #40. (Название спросить)(Играет в моменте где Юля на пианино(синтезатор(и из колонок)))
    $ anna_german = prefix_music+'anna_german.mp3'                                   #41. Анна Герман
    $ kim_wilde_cambodia = prefix_music+'Kim Wilde - Cambodia.mp3'                   #42. Kim Wilde - Cambodia(Играет в момент песни Алисы и ярослава в Муз кружке)
    $ ABBA = prefix_music+'ABBA.mp3'                                                 #43. (Спросить название)(Играет в столовой в восьмой день)
    $ siempre_amor = prefix_music+'Siempre_Amor.mp3'                                 #44. Mireille Mathieu - Siempre Amor(Саунд Чек, прямо перед концертом(по всему совенку с разным звуком))                                                 
    $ nagrada_robota = prefix_music+'nagrada_robota.mp3'                             #45. (Спросить название)(В момент награждения робота)
    $ wind_and_rain_rmx = prefix_music+'wind_and_rain_rmx.mp3'                       #46. Wind and rain - RMX(во время конкурса красоты)
    $ mm_instrumental = prefix_music+'mm_instrumental.mp3'                           #47. (Спросить название)(Играет когда ульянка первый раз на сцене)
    $ ula_song = prefix_music+'ula_song.mp3'                                         #48. Тили-тили тесто (Песня ульянки)
    $ d8_kulmege = prefix_music+'d8_kulmege.mp3'                                     #49. Kulmege (Песня венеры)
    $ se_tu_vuoi = prefix_music+'Se_tu_vuoi.mp3'                                     #50. Se Tu Vuoi - Highland
    $ midnight_lady = prefix_music+'Midnight_lady.mp3'                               #51. Midnight Lady - Chris Norman
    $ ABBA_One_Of_Us = prefix_music+'ABBA - One Of Us.mp3'                           #52. ABBA - One Of Us
    $ Kim_Wild_Camboja = prefix_music+'Kim Wild - Camboja.mp3'                       #53. Kim Wild - Camboja
    $ ABBA_Super_Trouper = prefix_music+'ABBA - Super Trouper.mp3'                   #54. ABBA - Super Trouper
    $ Zodiac = prefix_music+'Zodiac.mp3'                                             #55. Уточнить название
    $ Nicole_Ein_bischen_Frieden = prefix_music+'Nicole - Ein bischen Frieden.mp3'   #56. Nicole - Ein bischen Frieden
    $ Miku_Bad_Apple = prefix_music+'Miku - Bad Apple.mp3'                           #57. Miku - Bad Apple
    $ Touhou_Project_RUS_song = prefix_music+'Touhou Project RUS song.mp3'           #58. Touhou Project RUS song
    $ closetoyou_dv_mil = prefix_music+'closetoyou_dv_mil.ogg'                       #59. V flower - Close to you
    $ W_Koi_no_Vacance = prefix_music+'W - Koi no Vacance.mp3'                       #60. W - Koi no Vacance
    $ moskau = prefix_music+'Moskau.mp3'                                             #61. Dchinghis Khan - Moskau
    $ ABBA_Head_Over_Hills = prefix_music+'ABBA - Head Over Hills.mp3'               #62. ABBA - Head Over Hills
    $ Ichiban_no_Takaramono = prefix_music+'Angel Beats - Ichiban no Takaramono.mp3' #63. Angel Beats - Ichiban no Takaramono
    $ Secret_Base = prefix_music+'Secret Base - Anohana ED.mp3'                      #64. Secret Base - Anohana ED
    $ d10_alice_song = prefix_music+'d10_alice_song.mp3'                             #65. Под шум и взрыв гранат
    $ Nostalgia_depart = prefix_music+'Nostalgia_depart.mp3'                         #66. Igor Korg - Nostalgia depart
    $ nostalgia_shatunov = prefix_music+'nostalgia_shatunov.mp3'                     #67. Igor Korg - Nostalgia 13
    $ nostalgia_final = prefix_music+'nostalgia_final.mp3'                           #68. Igor Korg - Nostalgia 18
    $ Angelica_Divina = prefix_music+'Angelica_Divina.mp3'                           #69. R. Klayderman - Angelica Divina
    $ SG_Fuka_Ryouiki_no_Deja_Vu = prefix_music+'Steins;Gate.mp3'                    #70. Steins;Gate Movie Fuka Ryouiki no Deja Vu Ending Song Full with lyrics
    
  
    # ambience
    $ ambience_safe_7dl = prefix_ambience+'ambience_safe_7dl.ogg'
    $ Lucy_c2 = prefix_ambience+'Lucy_c2.mp3'
    $ dct_ambience_vent = prefix_ambience+'dct_ambience_vent.ogg'
    $ forest_ambience_day = prefix_ambience+'forest_ambience_day.ogg'
    $ ambience_rain_inside = prefix_ambience+'ambience_rain_inside.mp3'
    $ ambience_rain_outside = prefix_ambience+'ambience_rain_outside.mp3'
    $ elek = prefix_ambience+'elek.mp3'
    $ koster = prefix_ambience+'koster.mp3'
    $ ambience_volley_7dl = prefix_ambience+'ambience_volley_7dl.ogg'



    # sfx_sounds
    $ tolpa = perfix_sound+'sf_crowd.mp3'
    $ telefon = perfix_sound+'battery.mp3'
    $ sfx_dron = perfix_sound+'sfx_dron.mp3'   
    $ sfx_meow6 = perfix_sound+'meow6.ogg'
    $ sfx_meow2 = perfix_sound+'meow2.ogg'
    $ sfx_meow1 = perfix_sound+'meow1.ogg'
    $ sfx_kitten = perfix_sound+'kitten.ogg'
    $ sfx_cat_hiss1 = perfix_sound+'sfx_cat_hiss1.ogg'
    $ sfx_cat_murr = perfix_sound+'sfx_cat_murr.ogg'
    $ sfx_myay = perfix_sound+'sfx_myay.ogg'
    $ sfx_cat_scream = perfix_sound+'sfx_cat_scream.ogg'
    $ sfx_ikarus_slom = perfix_sound+'sfx_ikarus_slom.mp3'
    $ sfx_uvb = perfix_sound+'UVB76.mp3'
    $ sfx_bike_ride = perfix_sound+'sfx_bike_ride.mp3'
    $ sfx_bike_stop = perfix_sound+'sfx_bike_stop.mp3'
    $ sfx_discharge = perfix_sound+'sfx_discharge.mp3'
    $ sfx_grom_1 = perfix_sound+'sfx_grom_1.mp3'
    $ sfx_grom_far = perfix_sound+'sfx_grom_far.mp3'
    $ sfx_grom_rain = perfix_sound+'sfx_grom_rain.mp3'
    $ ringtone_toreador = perfix_sound+'ringtone_toreador.mp3'
    $ sf_crowd = perfix_sound+'sf_crowd.mp3'



# sprites

    # alisa
    image dv laugh mrssport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), prefix_sprites+'normal/dv/dv4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), prefix_sprites+'normal/dv/dv4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), prefix_sprites+'normal/dv/dv4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_laugh.png'))
    
    image dv laugh mrssport far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/far/dv/dv_4_body.png', (0, 0), prefix_sprites+'far/dv/dv4_sport.png', (0, 0), 'images/sprites/far/dv/dv_4_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/far/dv/dv_4_body.png', (0, 0), prefix_sprites+'far/dv/dv4_sport.png', (0, 0), 'images/sprites/far/dv/dv_4_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/far/dv/dv_4_body.png', (0, 0), prefix_sprites+'far/dv/dv4_sport.png', (0, 0), 'images/sprites/far/dv/dv_4_laugh.png'))
    
    image dv normal mrssport far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/far/dv/dv_4_body.png', (0, 0), prefix_sprites+'far/dv/dv4_sport.png', (0, 0), 'images/sprites/far/dv/dv_4_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/far/dv/dv_4_body.png', (0, 0), prefix_sprites+'far/dv/dv4_sport.png', (0, 0), 'images/sprites/far/dv/dv_4_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/far/dv/dv_4_body.png', (0, 0), prefix_sprites+'far/dv/dv4_sport.png', (0, 0), 'images/sprites/far/dv/dv_4_normal.png'))
    
    image dv normal mrssport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), prefix_sprites+'normal/dv/dv4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), prefix_sprites+'normal/dv/dv4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), prefix_sprites+'normal/dv/dv4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_normal.png'))
    
    image dv smile mrssport far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/far/dv/dv_4_body.png', (0, 0), prefix_sprites+'far/dv/dv4_sport.png', (0, 0), 'images/sprites/far/dv/dv_4_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/far/dv/dv_4_body.png', (0, 0), prefix_sprites+'far/dv/dv4_sport.png', (0, 0), 'images/sprites/far/dv/dv_4_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/far/dv/dv_4_body.png', (0, 0), prefix_sprites+'far/dv/dv4_sport.png', (0, 0), 'images/sprites/far/dv/dv_4_smile.png'))
    
    image dv smile mrssport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), prefix_sprites+'normal/dv/dv4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), prefix_sprites+'normal/dv/dv4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), prefix_sprites+'normal/dv/dv4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_smile.png'))
    
    image dv grin mrssport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/dv/dv_2_body.png', (0, 0), prefix_sprites+'normal/dv/dv2_sport.png', (0, 0), 'images/sprites/normal/dv/dv_2_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_2_body.png', (0, 0), prefix_sprites+'normal/dv/dv2_sport.png', (0, 0), 'images/sprites/normal/dv/dv_2_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_2_body.png', (0, 0), prefix_sprites+'normal/dv/dv2_sport.png', (0, 0), 'images/sprites/normal/dv/dv_2_grin.png'))
    
    image dv surprise mrssport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), prefix_sprites+'normal/dv/dv1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_surprise.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), prefix_sprites+'normal/dv/dv1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_surprise.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), prefix_sprites+'normal/dv/dv1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_surprise.png'))
    
    image dv shocked mrssport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), prefix_sprites+'normal/dv/dv1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_shocked.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), prefix_sprites+'normal/dv/dv1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_shocked.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), prefix_sprites+'normal/dv/dv1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_shocked.png'))
    
    image dv scared mrssport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), prefix_sprites+'normal/dv/dv1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_scared.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), prefix_sprites+'normal/dv/dv1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_scared.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), prefix_sprites+'normal/dv/dv1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_scared.png'))
    
    image dv cry mrssport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), prefix_sprites+'normal/dv/dv1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), prefix_sprites+'normal/dv/dv1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), prefix_sprites+'normal/dv/dv1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_cry.png'))
    
    image dv guilty mrssport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), prefix_sprites+'normal/dv/dv3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_guilty.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), prefix_sprites+'normal/dv/dv3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_guilty.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), prefix_sprites+'normal/dv/dv3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_guilty.png'))
    
    image dv sad mrssport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), prefix_sprites+'normal/dv/dv3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), prefix_sprites+'normal/dv/dv3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), prefix_sprites+'normal/dv/dv3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_sad.png'))
    
    image dv shy mrssport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), prefix_sprites+'normal/dv/dv3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), prefix_sprites+'normal/dv/dv3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), prefix_sprites+'normal/dv/dv3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_shy.png'))
    
    image dv angry mrssport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/dv/dv_5_body.png', (0, 0), prefix_sprites+'normal/dv/dv5_sport.png', (0, 0), 'images/sprites/normal/dv/dv_5_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_5_body.png', (0, 0), prefix_sprites+'normal/dv/dv5_sport.png', (0, 0), 'images/sprites/normal/dv/dv_5_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_5_body.png', (0, 0), prefix_sprites+'normal/dv/dv5_sport.png', (0, 0), 'images/sprites/normal/dv/dv_5_angry.png'))
    
    image dv rage mrssport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/dv/dv_5_body.png', (0, 0), prefix_sprites+'normal/dv/dv5_sport.png', (0, 0), 'images/sprites/normal/dv/dv_5_rage.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_5_body.png', (0, 0), prefix_sprites+'normal/dv/dv5_sport.png', (0, 0), 'images/sprites/normal/dv/dv_5_rage.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), 'images/sprites/normal/dv/dv_5_body.png', (0, 0), prefix_sprites+'normal/dv/dv5_sport.png', (0, 0), 'images/sprites/normal/dv/dv_5_rage.png'))
    
    
     # Алиса Вечернее платье
    image dv laugh bpppody far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/dv/dv_4_bpppody.png", (0,0), "images/sprites/far/dv/dv_4_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/dv/dv_4_bpppody.png", (0,0), "images/sprites/far/dv/dv_4_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/dv/dv_4_bpppody.png", (0,0), "images/sprites/far/dv/dv_4_laugh.png"))

    image dv smile bpppody far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/dv/dv_4_bpppody.png", (0,0), "images/sprites/far/dv/dv_4_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/dv/dv_4_bpppody.png", (0,0), "images/sprites/far/dv/dv_4_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/dv/dv_4_bpppody.png", (0,0), "images/sprites/far/dv/dv_4_smile.png"))

    image dv normal bpppody far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/dv/dv_4_bpppody.png", (0,0), "images/sprites/far/dv/dv_4_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/dv/dv_4_bpppody.png", (0,0), "images/sprites/far/dv/dv_4_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/dv/dv_4_bpppody.png", (0,0), "images/sprites/far/dv/dv_4_normal.png"))

    image dv guitar far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/dv/dv_guitar.png", (0,0), prefix_sprites+"far/dv/dv_guitar.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/dv/dv_guitar.png", (0,0), prefix_sprites+"far/dv/dv_guitar.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/dv/dv_guitar.png", (0,0), prefix_sprites+"far/dv/dv_guitar.png"))

    
    # bars
    image bars em1_uniform = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/bars/ba_body.png', (0, 0), prefix_sprites+'normal/bars/ba_dress.png', (0, 0), prefix_sprites+'normal/bars/ba_em1.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/bars/ba_body.png', (0, 0), prefix_sprites+'normal/bars/ba_dress.png', (0, 0), prefix_sprites+'normal/bars/ba_em1.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/bars/ba_body.png', (0, 0), prefix_sprites+'normal/bars/ba_dress.png', (0, 0), prefix_sprites+'normal/bars/ba_em1.png'))
    
    image bars evil_uniform = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/bars/ba_body.png', (0, 0), prefix_sprites+'normal/bars/ba_dress.png', (0, 0), prefix_sprites+'normal/bars/ba_evil.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/bars/ba_body.png', (0, 0), prefix_sprites+'normal/bars/ba_dress.png', (0, 0), prefix_sprites+'normal/bars/ba_evil.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/bars/ba_body.png', (0, 0), prefix_sprites+'normal/bars/ba_dress.png', (0, 0), prefix_sprites+'normal/bars/ba_evil.png'))
    
    image bars smile_uniform = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/bars/ba_body.png', (0, 0), prefix_sprites+'normal/bars/ba_dress.png', (0, 0), prefix_sprites+'normal/bars/ba_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/bars/ba_body.png', (0, 0), prefix_sprites+'normal/bars/ba_dress.png', (0, 0), prefix_sprites+'normal/bars/ba_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/bars/ba_body.png', (0, 0), prefix_sprites+'normal/bars/ba_dress.png', (0, 0), prefix_sprites+'normal/bars/ba_smile.png'))



    # miku_yukata
    image mi smile yukata far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_2_yukata.png', (0, 0), 'images/sprites/far/mi/mi_2_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_2_yukata.png', (0, 0), 'images/sprites/far/mi/mi_2_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_2_yukata.png', (0, 0),  'images/sprites/far/mi/mi_2_smile.png'))
    
    image mi grin yukata far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_2_yukata.png', (0, 0), 'images/sprites/far/mi/mi_2_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_2_yukata.png', (0, 0), 'images/sprites/far/mi/mi_2_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_2_yukata.png', (0, 0),  'images/sprites/far/mi/mi_2_grin.png'))
    
    image mi happy yukata far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_2_yukata.png', (0, 0), 'images/sprites/far/mi/mi_2_happy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_2_yukata.png', (0, 0), 'images/sprites/far/mi/mi_2_happy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_2_yukata.png', (0, 0),  'images/sprites/far/mi/mi_2_happy.png'))
    
    image mi laugh yukata far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_1_yukata.png', (0, 0), 'images/sprites/far/mi/mi_1_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_1_yukata.png', (0, 0), 'images/sprites/far/mi/mi_1_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_1_yukata.png', (0, 0),  'images/sprites/far/mi/mi_1_laugh.png'))
    
    image mi shy yukata far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_1_yukata.png', (0, 0), 'images/sprites/far/mi/mi_1_shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_1_yukata.png', (0, 0), 'images/sprites/far/mi/mi_1_shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_1_yukata.png', (0, 0),  'images/sprites/far/mi/mi_1_shy.png'))
    
    image mi dontlike yukata far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_1_yukata.png', (0, 0), 'images/sprites/far/mi/mi_1_dontlike.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_1_yukata.png', (0, 0), 'images/sprites/far/mi/mi_1_dontlike.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_1_yukata.png', (0, 0),  'images/sprites/far/mi/mi_1_dontlike.png'))
    
    image mi normal yukata far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_3_yukata.png', (0, 0), 'images/sprites/far/mi/mi_3_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_3_yukata.png', (0, 0), 'images/sprites/far/mi/mi_3_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_3_yukata.png', (0, 0),  'images/sprites/far/mi/mi_3_normal.png'))
    
    image mi upset yukata far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_3_yukata.png', (0, 0), 'images/sprites/far/mi/mi_3_upset.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_3_yukata.png', (0, 0), 'images/sprites/far/mi/mi_3_upset.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), prefix_sprites+'far/mi/mi_3_yukata.png', (0, 0),  'images/sprites/far/mi/mi_3_upset.png'))
    
    image mi smile yukata close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_2_yukata.png', (0, 0), 'images/sprites/close/mi/mi_2_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_2_yukata.png', (0, 0), 'images/sprites/close/mi/mi_2_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_2_yukata.png', (0, 0),  'images/sprites/close/mi/mi_2_smile.png'))
    
    image mi grin yukata close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_2_yukata.png', (0, 0), 'images/sprites/close/mi/mi_2_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_2_yukata.png', (0, 0), 'images/sprites/close/mi/mi_2_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_2_yukata.png', (0, 0),  'images/sprites/close/mi/mi_2_grin.png'))
    
    image mi happy yukata close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_2_yukata.png', (0, 0), 'images/sprites/close/mi/mi_2_happy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_2_yukata.png', (0, 0), 'images/sprites/close/mi/mi_2_happy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_2_yukata.png', (0, 0),  'images/sprites/close/mi/mi_2_happy.png'))
    
    image mi laugh yukata close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_1_yukata.png', (0, 0), 'images/sprites/close/mi/mi_1_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_1_yukata.png', (0, 0), 'images/sprites/close/mi/mi_1_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_1_yukata.png', (0, 0),  'images/sprites/close/mi/mi_1_laugh.png'))
    
    image mi shy yukata close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_1_yukata.png', (0, 0), 'images/sprites/close/mi/mi_1_shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_1_yukata.png', (0, 0), 'images/sprites/close/mi/mi_1_shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_1_yukata.png', (0, 0),  'images/sprites/close/mi/mi_1_shy.png'))
    
    image mi dontlike yukata close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_1_yukata.png', (0, 0), 'images/sprites/close/mi/mi_1_dontlike.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_1_yukata.png', (0, 0), 'images/sprites/close/mi/mi_1_dontlike.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_1_yukata.png', (0, 0),  'images/sprites/close/mi/mi_1_dontlike.png'))
    
    image mi normal yukata close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'close/mi/mi_3_yukata.png', (0, 0), 'images/sprites/close/mi/mi_3_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'close/mi/mi_3_yukata.png', (0, 0), 'images/sprites/close/mi/mi_3_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720), (0, 0), prefix_sprites+'close/mi/mi_3_yukata.png', (0, 0),  'images/sprites/close/mi/mi_3_normal.png'))
    
    image mi smile yukata normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_2_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_2_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_2_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_2_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_2_yukata.png', (0, 0),  'images/sprites/normal/mi/mi_2_smile.png'))
    
    image mi grin yukata normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_2_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_2_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_2_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_2_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_2_yukata.png', (0, 0),  'images/sprites/normal/mi/mi_2_grin.png'))
    
    image mi happy yukata normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_2_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_2_happy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_2_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_2_happy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_2_yukata.png', (0, 0),  'images/sprites/normal/mi/mi_2_happy.png'))
    
    image mi laugh yukata normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_1_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_1_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_1_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_1_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_1_yukata.png', (0, 0),  'images/sprites/normal/mi/mi_1_laugh.png'))
    
    image mi shy yukata normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_1_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_1_shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_1_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_1_shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_1_yukata.png', (0, 0),  'images/sprites/normal/mi/mi_1_shy.png'))
    
    image mi dontlike yukata normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_1_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_1_dontlike.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_1_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_1_dontlike.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_1_yukata.png', (0, 0),  'images/sprites/normal/mi/mi_1_dontlike.png'))
    
    image mi normal yukata normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_3_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_3_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_3_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_3_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_3_yukata.png', (0, 0),  'images/sprites/normal/mi/mi_3_normal.png'))
    
    image mi upset yukata normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_3_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_3_upset.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_3_yukata.png', (0, 0), 'images/sprites/normal/mi/mi_3_upset.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mi/mi_3_yukata.png', (0, 0),  'images/sprites/normal/mi/mi_3_upset.png'))
    
    image mi smile voca far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_2_body.png', (0, 0), prefix_sprites+'far/mi/mi_2_voca.png', (0, 0), 'images/sprites/far/mi/mi_2_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_2_body.png', (0, 0), prefix_sprites+'far/mi/mi_2_voca.png', (0, 0), 'images/sprites/far/mi/mi_2_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_2_body.png', (0, 0), prefix_sprites+'far/mi/mi_2_voca.png', (0, 0),  'images/sprites/far/mi/mi_2_smile.png'))
    
    image mi grin voca far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_2_body.png', (0, 0), prefix_sprites+'far/mi/mi_2_voca.png', (0, 0), 'images/sprites/far/mi/mi_2_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_2_body.png', (0, 0), prefix_sprites+'far/mi/mi_2_voca.png', (0, 0), 'images/sprites/far/mi/mi_2_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_2_body.png', (0, 0), prefix_sprites+'far/mi/mi_2_voca.png', (0, 0),  'images/sprites/far/mi/mi_2_grin.png'))
    
    image mi happy voca far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_2_body.png', (0, 0), prefix_sprites+'far/mi/mi_2_voca.png', (0, 0), 'images/sprites/far/mi/mi_2_happy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_2_body.png', (0, 0), prefix_sprites+'far/mi/mi_2_voca.png', (0, 0), 'images/sprites/far/mi/mi_2_happy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_2_body.png', (0, 0), prefix_sprites+'far/mi/mi_2_voca.png', (0, 0),  'images/sprites/far/mi/mi_2_happy.png'))
    
    image mi laugh voca far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_1_body.png', (0, 0), prefix_sprites+'far/mi/mi_1_voca.png', (0, 0), 'images/sprites/far/mi/mi_1_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_1_body.png', (0, 0), prefix_sprites+'far/mi/mi_1_voca.png', (0, 0), 'images/sprites/far/mi/mi_1_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_1_body.png', (0, 0), prefix_sprites+'far/mi/mi_1_voca.png', (0, 0),  'images/sprites/far/mi/mi_1_laugh.png'))
    
    image mi shy voca far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_1_body.png', (0, 0), prefix_sprites+'far/mi/mi_1_voca.png', (0, 0), 'images/sprites/far/mi/mi_1_shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_1_body.png', (0, 0), prefix_sprites+'far/mi/mi_1_voca.png', (0, 0), 'images/sprites/far/mi/mi_1_shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_1_body.png', (0, 0), prefix_sprites+'far/mi/mi_1_voca.png', (0, 0),  'images/sprites/far/mi/mi_1_shy.png'))
    
    image mi dontlike voca far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_1_body.png', (0, 0), prefix_sprites+'far/mi/mi_1_voca.png', (0, 0), 'images/sprites/far/mi/mi_1_dontlike.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_1_body.png', (0, 0), prefix_sprites+'far/mi/mi_1_voca.png', (0, 0), 'images/sprites/far/mi/mi_1_dontlike.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_1_body.png', (0, 0), prefix_sprites+'far/mi/mi_1_voca.png', (0, 0),  'images/sprites/far/mi/mi_1_dontlike.png'))
    
    image mi normal voca far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_3_body.png', (0, 0), prefix_sprites+'far/mi/mi_3_voca.png', (0, 0), 'images/sprites/far/mi/mi_3_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_3_body.png', (0, 0), prefix_sprites+'far/mi/mi_3_voca.png', (0, 0), 'images/sprites/far/mi/mi_3_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_3_body.png', (0, 0), prefix_sprites+'far/mi/mi_3_voca.png', (0, 0),  'images/sprites/far/mi/mi_3_normal.png'))
    
    image mi upset voca far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_3_body.png', (0, 0), prefix_sprites+'far/mi/mi_3_voca.png', (0, 0), 'images/sprites/far/mi/mi_3_upset.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_3_body.png', (0, 0), prefix_sprites+'far/mi/mi_3_voca.png', (0, 0), 'images/sprites/far/mi/mi_3_upset.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), 'images/sprites/far/mi/mi_3_body.png', (0, 0), prefix_sprites+'far/mi/mi_3_voca.png', (0, 0),  'images/sprites/far/mi/mi_3_upset.png'))
    
    image mi smile voca normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_voca.png', (0, 0), 'images/sprites/normal/mi/mi_2_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_voca.png', (0, 0), 'images/sprites/normal/mi/mi_2_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_voca.png', (0, 0),  'images/sprites/normal/mi/mi_2_smile.png'))
    
    image mi grin voca normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_voca.png', (0, 0), 'images/sprites/normal/mi/mi_2_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_voca.png', (0, 0), 'images/sprites/normal/mi/mi_2_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_voca.png', (0, 0),  'images/sprites/normal/mi/mi_2_grin.png'))
    
    image mi happy voca normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_voca.png', (0, 0), 'images/sprites/normal/mi/mi_2_happy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_voca.png', (0, 0), 'images/sprites/normal/mi/mi_2_happy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_voca.png', (0, 0),  'images/sprites/normal/mi/mi_2_happy.png'))
    
    image mi laugh voca normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_voca.png', (0, 0), 'images/sprites/normal/mi/mi_1_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_voca.png', (0, 0), 'images/sprites/normal/mi/mi_1_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_voca.png', (0, 0),  'images/sprites/normal/mi/mi_1_laugh.png'))
    
    image mi shy voca normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_voca.png', (0, 0), 'images/sprites/normal/mi/mi_1_shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_voca.png', (0, 0), 'images/sprites/normal/mi/mi_1_shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_voca.png', (0, 0),  'images/sprites/normal/mi/mi_1_shy.png'))
    
    image mi dontlike voca normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_voca.png', (0, 0), 'images/sprites/normal/mi/mi_1_dontlike.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_voca.png', (0, 0), 'images/sprites/normal/mi/mi_1_dontlike.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_voca.png', (0, 0),  'images/sprites/normal/mi/mi_1_dontlike.png'))
    
    image mi normal voca normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_voca.png', (0, 0), 'images/sprites/normal/mi/mi_3_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_voca.png', (0, 0), 'images/sprites/normal/mi/mi_3_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_voca.png', (0, 0),  'images/sprites/normal/mi/mi_3_normal.png'))
    
    image mi upset voca normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_voca.png', (0, 0), 'images/sprites/normal/mi/mi_3_upset.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_voca.png', (0, 0), 'images/sprites/normal/mi/mi_3_upset.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_voca.png', (0, 0),  'images/sprites/normal/mi/mi_3_upset.png'))
    
    image mi smile2 voca normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_voca.png', (0, 0), prefix_sprites+'normal/mi/mi_3_smile2.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_voca.png', (0, 0), prefix_sprites+'normal/mi/mi_3_smile2.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_voca.png', (0, 0),  prefix_sprites+'normal/mi/mi_3_smile2.png'))
    


    # Мику casual
    # _1_
    # dontlike
    image mi casual dontlike = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi_1_dontlike.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi_1_dontlike.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0),  'images/sprites/normal/mi/mi_1_dontlike.png'))
    
    
    # cry
    image mi casual cry = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi_1_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi_1_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0),  'images/sprites/normal/mi/mi_1_cry.png'))
    
    # laugh
    image mi casual laugh = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi_1_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi/mi_1_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0),  'images/sprites/normal/mi/mi_1_laugh.png'))
    
    # scared
    image mi casual scared = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi_1_scared.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi_1_scared.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0),  'images/sprites/normal/mi/mi_1_scared.png'))
    
    # surprise
    image mi casual surprise = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi_1_surprise.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi_1_surprise.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0),  'images/sprites/normal/mi/mi_1_surprise.png'))

    # shy
    image mi casual shy = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi_1_shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi_1_shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0),  'images/sprites/normal/mi/mi_1_shy.png'))
   

    image mi casual shocked = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi_1_shocked.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0), 'images/sprites/normal/mi/mi_1_shocked.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_1_body.png', (0, 0), prefix_sprites+'normal/mi/mi_1_casual.png', (0, 0),  'images/sprites/normal/mi/mi_1_shocked.png'))


    
    # _2_
    # cry_smile
    image mi casual cry_smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_casual.png', (0, 0), 'images/sprites/normal/mi/mi_2_cry_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_casual.png', (0, 0), 'images/sprites/normal/mi/mi_2_cry_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_casual.png', (0, 0),  'images/sprites/normal/mi/mi_2_cry_smile.png'))
    
    
    # grin
    image mi casual grin = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_casual.png', (0, 0), 'images/sprites/normal/mi/mi_2_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_casual.png', (0, 0), 'images/sprites/normal/mi/mi_2_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_casual.png', (0, 0),  'images/sprites/normal/mi/mi_2_grin.png'))


    # sad
    image mi casual sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_casual.png', (0, 0), 'images/sprites/normal/mi/mi_2_sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_casual.png', (0, 0), 'images/sprites/normal/mi/mi_2_sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_2_body.png', (0, 0), prefix_sprites+'normal/mi/mi_2_casual.png', (0, 0),  'images/sprites/normal/mi/mi_2_sad.png'))



    # _3_
    # rage
    image mi casual rage = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_casual.png', (0, 0), 'images/sprites/normal/mi/mi_3_rage.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_casual.png', (0, 0), 'images/sprites/normal/mi/mi_3_rage.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_casual.png', (0, 0),  'images/sprites/normal/mi/mi_3_rage.png'))


    # angry
    image mi casual angry = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_casual.png', (0, 0), 'images/sprites/normal/mi/mi_3_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_casual.png', (0, 0), 'images/sprites/normal/mi/mi_3_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_casual.png', (0, 0),  'images/sprites/normal/mi/mi_3_angry.png'))


    # upset
    image mi casual upset = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_casual.png', (0, 0), 'images/sprites/normal/mi/mi_3_upset.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_casual.png', (0, 0), 'images/sprites/normal/mi/mi_3_upset.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_casual.png', (0, 0),  'images/sprites/normal/mi/mi_3_upset.png'))    


    # normal
    image mi casual normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_casual.png', (0, 0), 'images/sprites/normal/mi/mi_3_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_casual.png', (0, 0), 'images/sprites/normal/mi/mi_3_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/normal/mi/mi_3_body.png', (0, 0), prefix_sprites+'normal/mi/mi_3_casual.png', (0, 0),  'images/sprites/normal/mi/mi_3_normal.png'))    


    # mz, Женя
    # Ухмыляется
    image mz casual glasses grin = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mz/mz_1_casual.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_1_casual.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_1_casual.png'))

    # Огорчена рассторена
    image mz casual hope = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mz/mz_1_casual_hope.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_1_casual_hope.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_1_casual_hope.png'))

    # Спокойная
    image mz casual bukal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mz/mz_1_casual_bucal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_1_casual_bucal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_1_casual_bucal.png'))


    # Смеётся
    image mz casual laugh = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mz/mz_1_casual_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_1_casual_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_1_casual_laugh.png'))

    # Нормальная
    image mz casual normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mz/mz_1_casual_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_1_casual_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_1_casual_normal.png'))

    # Злится и смущена
    image mz casual ang_shy = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mz/mz_2_casual_shyangr.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_2_casual_shyangr.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_2_casual_shyangr.png'))

    # В очках Злится и смущена
    image mz casual glasses ang_shy = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/mz/mz_2_casual_shyangrgl.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_2_casual_shyangrgl.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/mz/mz_2_casual_shyangrgl.png'))



    # gen, гена
    image gen normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((533, 720), (0, 0), prefix_sprites+'gen/genda_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((533, 720),  (0, 0), prefix_sprites+'gen/genda_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((533, 720),  (0, 0), prefix_sprites+'gen/genda_normal.png'))



    # el, Сыроега
    image el casual normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'el/el_1_shirt_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'el/el_1_shirt_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'el/el_1_shirt_norm.png'))


    image el casual serious = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'el/el_3_shirt_ser.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'el/el_3_shirt_ser.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'el/el_3_shirt_ser.png'))


    # mz_swim
    image mz swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/mz/mz_1_body.png', (0, 0), prefix_sprites+'far/mz/mz1_swimsuit.png', (0, 0), 'images/sprites/far/mz/mz_1_bukal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720),  (0, 0), prefix_sprites+'far/mz/mz_1_body.png', (0, 0), prefix_sprites+'far/mz/mz1_swimsuit.png', (0, 0), 'images/sprites/far/mz/mz_1_bukal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'far/mz/mz_1_body.png', (0, 0), prefix_sprites+'far/mz/mz1_swimsuit.png', (0, 0), 'images/sprites/far/mz/mz_1_bukal.png'))
  

  # sl
    # sl_hair
    image sl hair tender dress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_4_body2.png', (0, 0), prefix_sprites+'normal/sl/sl2_4_dress.png', (0, 0), 'images/sprites/normal/sl/sl_4_tender.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_4_body2.png', (0, 0), prefix_sprites+'normal/sl/sl2_4_dress.png', (0, 0), 'images/sprites/normal/sl/sl_4_tender.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_4_body2.png', (0, 0), prefix_sprites+'normal/sl/sl2_4_dress.png', (0, 0), 'images/sprites/normal/sl/sl_4_tender.png'))
    
    image sl hair normal dress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_1_body2.png', (0, 0), 'images/sprites/normal/sl/sl_1_dress.png', (0, 0), 'images/sprites/normal/sl/sl_1_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_1_body2.png', (0, 0), 'images/sprites/normal/sl/sl_1_dress.png', (0, 0), 'images/sprites/normal/sl/sl_1_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_1_body2.png', (0, 0), 'images/sprites/normal/sl/sl_1_dress.png', (0, 0), 'images/sprites/normal/sl/sl_1_normal.png'))
    
    image sl hair smile2 dress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_2_body2.png', (0, 0), prefix_sprites+'normal/sl/sl2_2_dress.png', (0, 0), 'images/sprites/normal/sl/sl_2_smile2.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_2_body2.png', (0, 0), prefix_sprites+'normal/sl/sl2_2_dress.png', (0, 0), 'images/sprites/normal/sl/sl_2_smile2.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_2_body2.png', (0, 0), prefix_sprites+'normal/sl/sl2_2_dress.png', (0, 0), 'images/sprites/normal/sl/sl_2_smile2.png'))
    
    image sl hair smile dress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_1_body2.png', (0, 0), 'images/sprites/normal/sl/sl_1_dress.png', (0, 0), 'images/sprites/normal/sl/sl_1_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_1_body2.png', (0, 0), 'images/sprites/normal/sl/sl_1_dress.png', (0, 0), 'images/sprites/normal/sl/sl_1_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_1_body2.png', (0, 0), 'images/sprites/normal/sl/sl_1_dress.png', (0, 0), 'images/sprites/normal/sl/sl_1_smile.png'))
    
    
    
    # sl_underwear
    image sl underwear = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_underwear.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_underwear.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/sl_underwear.png'))
    
    # sl_body

    image sl_body_forest = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_1_body2.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_1_body2.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_1_body2.png'))
    
    image sl_imoji_forest = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_25_neutral.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'mods/Slavia/images/sprites/normal/sl/sl_25_neutral.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/sl_25_neutral.png'))



  ###########Что за говно я сотворила? Ладно лень переделывать, работает и похуй!#############################15 июля 2019
    # sl_opacity
        # Это спрайт двойной сложности. Любые изменения в структуре одной части повлияют на другую.
            # Первая часть отвечает за то чтобы формa была прозрачной.
    image slpo_pioneer opacity1 = im.MatrixColor("images/sprites/close/sl/sl_1_pioneer.png", im.matrix.opacity(0.6))
    image slpo_pioneer opacity2 = im.MatrixColor("images/sprites/close/sl/sl_2_pioneer.png", im.matrix.opacity(0.6))
            # Вторая часть отвечает за то что бы появилось ТЕЛО с ЭМОЦИЕЙ.
    image slbo_body opacyty normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/close/sl/sl_1_body.png', (0, 0), 'images/sprites/close/sl/sl_1_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/close/sl/sl_1_body.png', (0, 0), 'images/sprites/close/sl/sl_1_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/close/sl/sl_1_body.png', (0, 0), 'images/sprites/close/sl/sl_1_normal.png'))        
    
    image slbo_body opacyty shy = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/close/sl/sl_2_body.png', (0, 0), 'images/sprites/close/sl/sl_2_shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/close/sl/sl_2_body.png', (0, 0), 'images/sprites/close/sl/sl_2_shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/close/sl/sl_2_body.png', (0, 0), 'images/sprites/close/sl/sl_2_shy.png'))
    
    image slbo_body opacyty smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/close/sl/sl_1_body.png', (0, 0), 'images/sprites/close/sl/sl_1_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), 'images/sprites/close/sl/sl_1_body.png', (0, 0), 'images/sprites/close/sl/sl_1_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), 'images/sprites/close/sl/sl_1_body.png', (0, 0), 'images/sprites/close/sl/sl_1_smile.png'))
    
    
    # sl roz, Славя с розами
    image sl roz = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/Slavya_kruzh_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/Slavya_kruzh_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/Slavya_kruzh_norm.png'))

    
     # Славя в костюмчике Мэйдо-тян
    image sl happy lobody far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/sl/sl_2_LObody.png",(0,0), "images/sprites/far/sl/sl_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/sl/sl_2_LObody.png",(0,0), "images/sprites/far/sl/sl_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/sl/sl_2_LObody.png",(0,0), "images/sprites/far/sl/sl_2_happy.png") )

    
    image sl shy lobody far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/sl/sl_2_LObody.png",(0,0), "images/sprites/far/sl/sl_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/sl/sl_2_LObody.png",(0,0), "images/sprites/far/sl/sl_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/sl/sl_2_LObody.png",(0,0), "images/sprites/far/sl/sl_2_shy.png") )


    image sl smile2 lobody far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/sl/sl_2_LObody.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/sl/sl_2_LObody.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/sl/sl_2_LObody.png", (0,0), "images/sprites/far/sl/sl_2_smile2.png") )

 # happy_cry
    # dress
    image sl dress happy_cry = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/sl/sl_4_dress_happy_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720),  (0, 0), prefix_sprites+'close/sl/sl_4_dress_happy_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720), (0, 0), prefix_sprites+'close/sl/sl_4_dress_happy_cry.png'))


    # swim
    image sl swim happy_cry = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'close/sl/sl_4_swim_happy_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720),  (0, 0), prefix_sprites+'close/sl/sl_4_swim_happy_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720), (0, 0), prefix_sprites+'close/sl/sl_4_swim_happy_cry.png'))


    image sl pioneer grin = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/sl/sl_2_pioneer_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/sl/sl_2_pioneer_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/sl/sl_2_pioneer_grin.png'))

    image sl sport grin = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/sl/sl_2_sport_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/sl/sl_2_sport_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/sl/sl_2_sport_grin.png'))

    image sl swim grin = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/sl/sl_2_swim_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/sl/sl_2_swim_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/sl/sl_2_swim_grin.png'))

    image sl pioneer happy_cry = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/sl/sl_4_pioneer_happycry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/sl/sl_4_pioneer_happycry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/sl/sl_4_pioneer_happycry.png'))
    

    # casual
    # dontlike
    image sl casual dontlike = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_1_casual_dontlike.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_1_casual_dontlike.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_1_casual_dontlike.png'))
    
    
    #serious
    image sl casual serious = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_1_casual_serious.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_1_casual_serious.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_1_casual_serious.png'))
    
    # smile
    image sl casual smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_1_casual_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_1_casual_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_1_casual_smile.png'))
    
    # grin
    image sl casual grin = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_grin.png'))
    
    # happy
    image sl casual happy = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_happy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_happy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_happy.png'))
    
    # laugh
    image sl casual laugh = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_laugh.png'))
    
    # shy
    image sl casual shy = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_shy.png'))
    
    # smile2
    image sl casual smile2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_smile2.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_smile2.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_2_casual_smile2.png'))
    
    # happy2
    image sl casual happy2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_3_casual_happy2.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_3_casual_happy2.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_3_casual_happy2.png'))
    
    # sad
    image sl casual sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_3_casual_sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_3_casual_sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_3_casual_sad.png'))
    
    # surprise
    image sl casual surprise = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_3_casual_surprise.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_3_casual_surprise.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_3_casual_surprise.png'))
    
    # upset
    image sl casual upset = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_3_casual_upset.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_3_casual_upset.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_3_casual_upset.png'))
    
    # cry
    image sl casual cry = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_4_casual_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_4_casual_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_4_casual_cry.png'))
        
    # happy_cry
    image sl casual happy_cry = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_4_casual_happycry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_4_casual_happycry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_4_casual_happycry.png'))
    
    # scared
    image sl casual scared = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_4_casual_scared.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_4_casual_scared.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_4_casual_scared.png'))
    
    # tender
    image sl casual tender = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_4_casual_tender.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720),  (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_4_casual_tender.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720), (0, 0), prefix_sprites+'normal/sl/casual/casual/sl_4_casual_tender.png'))
    


    
# ann
    # HOW ON ANN?
#   show ann pioneer normal:            # Так же вы просто 
#       ypos 0.3                        # можете использовать трансформацию ann

    image ann pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((377, 511), (0, 0), prefix_sprites+'ann/ann_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((377, 511), (0, 0), prefix_sprites+'ann/ann_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((377, 511),  (0, 0), prefix_sprites+'ann/ann_norm.png'))
    
    image ann pioneer sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((377, 511), (0, 0), prefix_sprites+'ann/ann_sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((377, 511), (0, 0), prefix_sprites+'ann/ann_sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((377, 511),  (0, 0), prefix_sprites+'ann/ann_sad.png'))
    
    image ann pioneer shocked = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((377, 511), (0, 0), prefix_sprites+'ann/ann_shocked.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((377, 511), (0, 0), prefix_sprites+'ann/ann_shocked.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((377, 511),  (0, 0), prefix_sprites+'ann/ann_shocked.png'))
    
    image ann pioneer smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((377, 511), (0, 0), prefix_sprites+'ann/ann_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((377, 511), (0, 0), prefix_sprites+'ann/ann_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((377, 511),  (0, 0), prefix_sprites+'ann/ann_smile.png'))
    
    
    # oxy
    # HOW ON OXY?
#   show oxy normal at center:          # Так же вы просто 
#       yalign -0.4 subpixel True       # можете использовать
#       xalign .1 subpixel True         # трансформацию
#       zoom 1.5                        # oxy

    image oxy sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((267, 533), (0, 0), prefix_sprites+'oxy/oxy_sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((267, 533), (0, 0), prefix_sprites+'oxy/oxy_sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((267, 533),  (0, 0), prefix_sprites+'oxy/oxy_sad.png'))
    
    image oxy scared = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((267, 533), (0, 0), prefix_sprites+'oxy/oxy_scared.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((267, 533), (0, 0), prefix_sprites+'oxy/oxy_scared.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((267, 533),  (0, 0), prefix_sprites+'oxy/oxy_scared.png'))
    
    image oxy normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((267, 533), (0, 0), prefix_sprites+'oxy/oxy_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((267, 533), (0, 0), prefix_sprites+'oxy/oxy_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((267, 533),  (0, 0), prefix_sprites+'oxy/oxy_normal.png'))
    
    image oxy smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((267, 533), (0, 0), prefix_sprites+'oxy/oxy_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((267, 533), (0, 0), prefix_sprites+'oxy/oxy_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((267, 533),  (0, 0), prefix_sprites+'oxy/oxy_smile.png'))
    
    image oxy smile_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((267, 533), (0, 0), prefix_sprites+'oxy/oxy_smile_2.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((267, 533), (0, 0), prefix_sprites+'oxy/oxy_smile_2.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((267, 533),  (0, 0), prefix_sprites+'oxy/oxy_smile_2.png'))
    
    
    # cat
    image w_cat = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'cats/close/cat_hris.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'cats/close/cat_hris.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'cats/close/cat_hris.png'))
    
    image b_cat = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'cats/close/cat_rb.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'cats/close/cat_rb.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'cats/close/cat_rb.png'))
    
    image cat_washstand = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1280, 720), (0, 0), prefix_sprites+'cats/normal/cat_washstand.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1280, 720), (0, 0), prefix_sprites+'cats/normal/cat_washstand.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((1280, 720),  (0, 0), prefix_sprites+'cats/normal/cat_washstand.png'))
    
    image cat_stand = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1280, 720), (0, 0), prefix_sprites+'cats/normal/cat_musclub_1.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1280, 720), (0, 0), prefix_sprites+'cats/normal/cat_musclub_1.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((1280, 720),  (0, 0), prefix_sprites+'cats/normal/cat_musclub_1.png'))
    
    image kot1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 787), (0, 0), prefix_sprites+'cats/normal/1_kot.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 787), (0, 0), prefix_sprites+'cats/normal/1_kot.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 787),  (0, 0), prefix_sprites+'cats/normal/1_kot.png'))
    
    image kot2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 787), (0, 0), prefix_sprites+'cats/normal/2_kot.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 787), (0, 0), prefix_sprites+'cats/normal/2_kot.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 787),  (0, 0), prefix_sprites+'cats/normal/2_kot.png'))
    
    image kot3 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 787), (0, 0), prefix_sprites+'cats/normal/3_kot.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 787), (0, 0), prefix_sprites+'cats/normal/3_kot.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 787),  (0, 0), prefix_sprites+'cats/normal/3_kot.png'))
    
    image kot4 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 787), (0, 0), prefix_sprites+'cats/normal/4_kot.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 787), (0, 0), prefix_sprites+'cats/normal/4_kot.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 787),  (0, 0), prefix_sprites+'cats/normal/4_kot.png'))

  # Робот и его контейнеры
    image rob = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((267, 720), (0, 0), prefix_sprites+'rob/robot_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((267, 720), (0, 0), prefix_sprites+'rob/robot_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((267, 720),  (0, 0), prefix_sprites+'rob/robot_far.png'))
    
 # tl
    image tl = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((408, 720), (0, 0), prefix_sprites+'tl/tl_1_pioneer.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((408, 720), (0, 0), prefix_sprites+'tl/tl_1_pioneer.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((408, 720),  (0, 0), prefix_sprites+'tl/tl_1_pioneer.png'))
    
    image tl smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((408, 720), (0, 0), prefix_sprites+'tl/tl_1_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((408, 720), (0, 0), prefix_sprites+'tl/tl_1_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((408, 720),  (0, 0), prefix_sprites+'tl/tl_1_smile.png'))
    
    image tl angry = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((408, 720), (0, 0), prefix_sprites+'tl/tl_1_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((408, 720), (0, 0), prefix_sprites+'tl/tl_1_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((408, 720),  (0, 0), prefix_sprites+'tl/tl_1_angry.png'))
    
    image tl thful = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((408, 720), (0, 0), prefix_sprites+'tl/tl_1_thful.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((408, 720), (0, 0), prefix_sprites+'tl/tl_1_thful.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((408, 720),  (0, 0), prefix_sprites+'tl/tl_1_thful.png'))
    

 # UVAO
  # В пионер форме
    # далеко
    image uvp grin far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_grin_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_grin_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'far/uv/uvp_grin_far.png'))
    
    image uvp angry far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_angry_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_angry_far.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'far/uv/uvp_angry_far.png'))
    
    image uvp dontlike far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_dontlike_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_dontlike_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'far/uv/uvp_dontlike_far.png'))
    
    image uvp guilty far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_guilty_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_guilty_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'far/uv/uvp_guilty_far.png'))
    
    image uvp laugh far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_laugh_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_laugh_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'far/uv/uvp_laugh_far.png'))
    
    image uvp normal far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_normal_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_normal_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'far/uv/uvp_normal_far.png'))
    
    image uvp rage far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_rage_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_rage_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'far/uv/uvp_rage_far.png'))
    
    image uvp shocked far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_shocked_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_shocked_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'far/uv/uvp_shocked_far.png'))
    
    image uvp smile far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_smile_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_smile_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'far/uv/uvp_smile_far.png'))
    
    image uvp surp2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_surp2_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_surp2_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'far/uv/uvp_surp2_far.png'))
    
    image uvp surp far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_surp_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_surp_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'far/uv/uvp_surp_far.png'))
    
    image uvp upset far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_upset_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/uvp_upset_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'far/uv/uvp_upset_far.png'))

    # нормально
    image uvp angry = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'auv/uvp_angry.png'))
    
    image uvp dontlike = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_dontlike.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_dontlike.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'auv/uvp_dontlike.png'))
    
    image uvp guilty = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_guilty.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_guilty.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'auv/uvp_guilty.png'))
    
    image uvp laugh = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'auv/uvp_laugh.png'))
    
    image uvp normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'auv/uvp_normal.png'))
    
    image uvp rage = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_rage.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_rage.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'auv/uvp_rage.png'))
    
    image uvp shocked = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_shocked.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_shocked.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'auv/uvp_shocked.png'))
    
    image uvp smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'auv/uvp_smile.png'))
    
    image uvp surp2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_surp2.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_surp2.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'auv/uvp_surp2.png'))
    
    image uvp surp = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_surp.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_surp.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'auv/uvp_surp.png'))
    
    image uvp upset = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_upset.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/uvp_upset.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'auv/uvp_upset.png'))
    
    
  # Dark_uvp
    image uvp grin dark far = im.MatrixColor(prefix_sprites+"far/uv/uvp_grin_far.png", im.matrix.brightness(-0.8))
    image uvp angry dark far = im.MatrixColor(prefix_sprites+"far/uv/uvp_angry_far.png", im.matrix.brightness(-0.8))
    image uvp dontlike dark far = im.MatrixColor(prefix_sprites+"far/uv/uvp_dontlike_far.png", im.matrix.brightness(-0.8))
    image uvp guilty dark far = im.MatrixColor(prefix_sprites+"far/uv/uvp_guilty_far.png", im.matrix.brightness(-0.8))
    image uvp laugh dark far = im.MatrixColor(prefix_sprites+"far/uv/uvp_laugh_far.png", im.matrix.brightness(-0.8))
    image uvp normal dark far = im.MatrixColor(prefix_sprites+"far/uv/uvp_normal_far.png", im.matrix.brightness(-0.8))
    image uvp rage dark far = im.MatrixColor(prefix_sprites+"far/uv/uvp_rage_far.png", im.matrix.brightness(-0.8))
    image uvp shocked dark far = im.MatrixColor(prefix_sprites+"far/uv/uvp_shocked_far.png", im.matrix.brightness(-0.8))
    image uvp smile dark far = im.MatrixColor(prefix_sprites+"far/uv/uvp_smile_far.png", im.matrix.brightness(-0.8))
    image uvp surp2 dark far = im.MatrixColor(prefix_sprites+"far/uv/uvp_surp2_far.png", im.matrix.brightness(-0.8))
    image uvp surp dark far = im.MatrixColor(prefix_sprites+"far/uv/uvp_surp_far.png", im.matrix.brightness(-0.8))
    image uvp upset dark far = im.MatrixColor(prefix_sprites+"far/uv/uvp_upset_far.png", im.matrix.brightness(-0.8))
    
    
  # С планшетом
    image uvplanshet far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/Ulia_Fanfick_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'far/uv/Ulia_Fanfick_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'far/uv/Ulia_Fanfick_far.png'))

  #_В шубе
    image uvp coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/Yulya_coat.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'auv/Yulya_coat.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'auv/Yulya_coat.png'))
    
  #_В ЭкспоЦентре
    image uvp ad = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/uv/ulia_ad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'far/uv/ulia_ad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'far/uv/ulia_ad.png')) 
    
  # nt, Повар
    image nt normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'normal/nt/nt_1_cook.png', (0, 0), prefix_sprites+'normal/nt/nt_1_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'normal/nt/nt_1_cook.png', (0, 0), prefix_sprites+'normal/nt/nt_1_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), prefix_sprites+'normal/nt/nt_1_cook.png', (0, 0),  prefix_sprites+'normal/nt/nt_1_normal.png'))
    
    image nt laugh = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'normal/nt/nt_1_cook.png', (0, 0), prefix_sprites+'normal/nt/nt_1_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'normal/nt/nt_1_cook.png', (0, 0), prefix_sprites+'normal/nt/nt_1_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), prefix_sprites+'normal/nt/nt_1_cook.png', (0, 0),  prefix_sprites+'normal/nt/nt_1_laugh.png'))
    
    image nt sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'normal/nt/nt_1_cook.png', (0, 0), prefix_sprites+'normal/nt/nt_1_sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'normal/nt/nt_1_cook.png', (0, 0), prefix_sprites+'normal/nt/nt_1_sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), prefix_sprites+'normal/nt/nt_1_cook.png', (0, 0),  prefix_sprites+'normal/nt/nt_1_sad.png'))
    
    image nt smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'normal/nt/nt_1_cook.png', (0, 0), prefix_sprites+'normal/nt/nt_1_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'normal/nt/nt_1_cook.png', (0, 0), prefix_sprites+'normal/nt/nt_1_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720), (0, 0), prefix_sprites+'normal/nt/nt_1_cook.png', (0, 0),  prefix_sprites+'normal/nt/nt_1_smile.png'))


  # iar, Ярик
   # Близко
    # Поза первая
     # Пионерская форма
    image iar pioneer angry_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_pioneer_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_pioneer_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar1_pioneer_angry.png'))

    image iar pioneer normal_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_pioneer_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_pioneer_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar1_pioneer_norm.png'))

    image iar pioneer smile_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_pioneer_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_pioneer_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar1_pioneer_smile.png'))
################################################################################
     # Повседневный костюмчик
    image iar daily angry_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_rest_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_rest_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar1_rest_angry.png'))

    image iar daily normal_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_rest_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_rest_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar1_rest_norm.png'))

    image iar daily smile_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_rest_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_rest_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar1_rest_smile.png'))
################################################################################
     # Спортивный костюм
    image iar sport angry_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_sport_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_sport_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar1_sport_angry.png'))

    image iar sport normal_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_sport_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_sport_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar1_sport_norm.png'))

    image iar sport smile_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_sport_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_sport_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar1_sport_smile.png'))
################################################################################
     # Плавки. (Купальник что ли)
    image iar swim angry_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_swim_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_swim_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar1_swim_angry.png'))

    image iar swim normal_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_swim_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_swim_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar1_swim_norm.png'))

    image iar swim smile_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_swim_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar1_swim_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar1_swim_smile.png'))
################################################################################    
################################################################################    
    # Поза вторая
     # Пионерская форма
    image iar pioneer angry_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_pioneer_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_pioneer_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar2_pioneer_angry.png'))

    image iar pioneer normal_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_pioneer_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_pioneer_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar2_pioneer_norm.png'))

    image iar pioneer smile_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_pioneer_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_pioneer_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar2_pioneer_smile.png'))
################################################################################
     # Повседневный костюмчик
    image iar daily angry_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_rest_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_rest_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar2_rest_angry.png'))

    image iar daily normal_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_rest_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_rest_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar2_rest_norm.png'))

    image iar daily smile_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_rest_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_rest_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar2_rest_smile.png'))
################################################################################    
     # Спортивный костюм
    image iar sport angry_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_sport_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_sport_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar2_sport_angry.png'))

    image iar sport normal_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_sport_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_sport_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar2_sport_norm.png'))

    image iar sport smile_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_sport_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_sport_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar2_sport_smile.png'))
################################################################################
     # Плавки. (Купальник что ли)
    image iar swim angry_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_swim_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_swim_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar2_swim_angry.png'))

    image iar swim normal_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_swim_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_swim_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'iar/close/iar2_swim_norm.png'))

    image iar swim smile_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_swim_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'iar/close/iar2_swim_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'close/iar2_swim_smile.png'))
################################################################################
################################################################################
################################################################################
   # Далеко
    # Поза первая
     # Пионерская форма
    image iar pioneer angry_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_pioneer_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_pioneer_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar1_pioneer_angry.png'))

    image iar pioneer normal_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_pioneer_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_pioneer_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar1_pioneer_norm.png'))

    image iar pioneer smile_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_pioneer_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_pioneer_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar1_pioneer_smile.png'))
################################################################################
     # Повседневный костюмчик
    image iar daily angry_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_rest_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_rest_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar1_rest_angry.png'))

    image iar daily normal_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_rest_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_rest_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar1_rest_norm.png'))

    image iar daily smile_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_rest_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_rest_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar1_rest_smile.png'))
################################################################################
     # Спортивный костюм
    image iar sport angry_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_sport_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_sport_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar1_sport_angry.png'))

    image iar sport normal_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_sport_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_sport_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar1_sport_norm.png'))

    image iar sport smile_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_sport_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_sport_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar1_sport_smile.png'))
################################################################################
     # Плавки. (Купальник что ли)
    image iar swim angry_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_swim_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_swim_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar1_swim_angry.png'))

    image iar swim normal_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_swim_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_swim_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar1_swim_norm.png'))

    image iar swim smile_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_swim_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar1_swim_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar1_swim_smile.png'))
################################################################################    
################################################################################    
    # Поза вторая
     # Пионерская форма
    image iar pioneer angry_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_pioneer_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_pioneer_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar2_pioneer_angry.png'))

    image iar pioneer normal_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_pioneer_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_pioneer_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar2_pioneer_norm.png'))

    image iar pioneer smile_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_pioneer_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_pioneer_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar2_pioneer_smile.png'))
################################################################################
     # Повседневный костюмчик
    image iar daily angry_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_rest_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_rest_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar2_rest_angry.png'))

    image iar daily normal_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_rest_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_rest_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar2_rest_norm.png'))

    image iar daily smile_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_rest_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_rest_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar2_rest_smile.png'))
################################################################################    
     # Спортивный костюм
    image iar sport angry_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_sport_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_sport_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar2_sport_angry.png'))

    image iar sport normal_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_sport_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_sport_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar2_sport_norm.png'))

    image iar sport smile_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_sport_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_sport_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar2_sport_smile.png'))
################################################################################
     # Плавки. (Купальник что ли)
    image iar swim angry_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_swim_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_swim_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar2_swim_angry.png'))

    image iar swim normal_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_swim_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_swim_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar2_swim_norm.png'))

    image iar swim smile_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_swim_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'iar/far/iar2_swim_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/far/iar2_swim_smile.png'))
################################################################################
################################################################################
################################################################################
   # Нормально
    # Поза первая
     # Пионерская форма
    image iar pioneer angry_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_pioneer_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_pioneer_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar1_pioneer_angry.png'))

    image iar pioneer normal_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_pioneer_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_pioneer_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar1_pioneer_norm.png'))

    image iar pioneer smile_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_pioneer_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_pioneer_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar1_pioneer_smile.png'))
################################################################################
     # Повседневный костюмчик
    image iar daily angry_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_rest_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_rest_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar1_rest_angry.png'))

    image iar daily normal_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_rest_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_rest_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar1_rest_norm.png'))

    image iar daily smile_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_rest_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_rest_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar1_rest_smile.png'))
################################################################################
     # Спортивный костюм
    image iar sport angry_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_sport_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_sport_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar1_sport_angry.png'))

    image iar sport normal_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_sport_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_sport_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar1_sport_norm.png'))

    image iar sport smile_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_sport_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_sport_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar1_sport_smile.png'))
################################################################################
     # Плавки. (Купальник что ли)
    image iar swim angry_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_swim_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_swim_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar1_swim_angry.png'))

    image iar swim normal_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_swim_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_swim_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar1_swim_norm.png'))

    image iar swim smile_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_swim_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar1_swim_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar1_swim_smile.png'))
################################################################################    
################################################################################    
    # Поза вторая
     # Пионерская форма
    image iar pioneer angry_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_pioneer_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_pioneer_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar2_pioneer_angry.png'))

    image iar pioneer normal_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_pioneer_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_pioneer_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar2_pioneer_norm.png'))

    image iar pioneer smile_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_pioneer_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_pioneer_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar2_pioneer_smile.png'))
################################################################################
     # Повседневный костюмчик
    image iar daily angry_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_rest_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_rest_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar2_rest_angry.png'))

    image iar daily normal_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_rest_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_rest_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar2_rest_norm.png'))

    image iar daily smile_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_rest_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_rest_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar2_rest_smile.png'))
################################################################################    
     # Спортивный костюм
    image iar sport angry_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_sport_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_sport_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar2_sport_angry.png'))

    image iar sport normal_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_sport_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_sport_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'iar/normal/iar2_sport_norm.png'))

    image iar sport smile_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_sport_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_sport_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar2_sport_smile.png'))
################################################################################
     # Плавки. (Купальник что ли)
    image iar swim angry_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_swim_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_swim_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar2_swim_angry.png'))

    image iar swim normal_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_swim_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_swim_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar2_swim_norm.png'))

    image iar swim smile_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_swim_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'iar/normal/iar2_swim_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'iar/normal/iar2_swim_smile.png'))
################################################################################
################################################################################
################################################################################    
    # cs, Виола
     # Виола, Вечернее платье
    image cs normal bodych far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630, 720), (0,0), prefix_sprites+"far/cs/cs_1_bodych.png",(0,0), "images/sprites/far/cs/cs_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630, 720), (0,0), prefix_sprites+"far/cs/cs_1_bodych.png",(0,0), "images/sprites/far/cs/cs_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630, 720), (0,0), prefix_sprites+"far/cs/cs_1_bodych.png",(0,0), "images/sprites/far/cs/cs_1_normal.png") )


    image cs shy bodych far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630, 720), (0,0), prefix_sprites+"far/cs/cs_1_bodych.png",(0,0), "images/sprites/far/cs/cs_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630, 720), (0,0), prefix_sprites+"far/cs/cs_1_bodych.png",(0,0), "images/sprites/far/cs/cs_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630, 720), (0,0), prefix_sprites+"far/cs/cs_1_bodych.png",(0,0), "images/sprites/far/cs/cs_1_shy.png") )


    image cs smile bodych far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630, 720), (0,0), prefix_sprites+"far/cs/cs_1_bodych.png",(0,0), "images/sprites/far/cs/cs_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630, 720), (0,0), prefix_sprites+"far/cs/cs_1_bodych.png",(0,0), "images/sprites/far/cs/cs_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630, 720), (0,0), prefix_sprites+"far/cs/cs_1_bodych.png",(0,0), "images/sprites/far/cs/cs_1_smile.png") )

    
    # un, Лена
     # Лена, Костюм Рерто-Лоли
    image un angry2 lobody far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png",(0,0), "images/sprites/far/un/un_3_angry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png",(0,0), "images/sprites/far/un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png", (0,0), "images/sprites/far/un/un_3_angry2.png") )
    

    image un grin lobody far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png",(0,0), "images/sprites/far/un/un_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png",(0,0), "images/sprites/far/un/un_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png", (0,0), "images/sprites/far/un/un_3_grin.png") )


    image un laugh lobody far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png",(0,0), "images/sprites/far/un/un_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png",(0,0), "images/sprites/far/un/un_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png", (0,0), "images/sprites/far/un/un_3_laugh.png") )


    image un rage lobody far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png",(0,0), "images/sprites/far/un/un_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png",(0,0), "images/sprites/far/un/un_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png", (0,0), "images/sprites/far/un/un_3_rage.png") )
    

    image un serious lobody far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png",(0,0), "images/sprites/far/un/un_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png",(0,0), "images/sprites/far/un/un_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png", (0,0), "images/sprites/far/un/un_3_serious.png") )


    image un smile3 lobody far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png",(0,0), "images/sprites/far/un/un_3_smile3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png",(0,0), "images/sprites/far/un/un_3_smile3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,720), (0,0), prefix_sprites+"far/un/un_3_LObody2.png", (0,0), "images/sprites/far/un/un_3_smile3.png") )
    
    
    image mz bukal dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_bukal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_bukal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_bukal.png") )

    
     # Женя в платье
    image mz rage dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_2_body.png", (0,0), prefix_sprites+"far/mz/mz_2_dress.png",(0,0), "images/sprites/far/mz/mz_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_2_body.png", (0,0), prefix_sprites+"far/mz/mz_2_dress.png",(0,0), "images/sprites/far/mz/mz_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_2_body.png", (0,0), prefix_sprites+"far/mz/mz_2_dress.png", (0,0), "images/sprites/far/mz/mz_2_rage.png") )
    

    image mz normal dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_normal.png") )


    image mz smile dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_3_body.png",(0,0), prefix_sprites+"far/mz/mz_3_dress.png",(0,0), "images/sprites/far/mz/mz_3_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_3_body.png",(0,0), prefix_sprites+"far/mz/mz_3_dress.png",(0,0), "images/sprites/far/mz/mz_3_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_3_body.png",(0,0), prefix_sprites+"far/mz/mz_3_dress.png",(0,0), "images/sprites/far/mz/mz_3_smile.png") )


    image mz shy dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_shy.png",(0,0), prefix_sprites+"far/mz/mz_3_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_shy.png",(0,0), prefix_sprites+"far/mz/mz_3_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_shy.png",(0,0), prefix_sprites+"far/mz/mz_3_dress.png") )


    image mz laugh dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_laugh.png") )


    image mz angry dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_angry.png",(0,0), prefix_sprites+"far/mz/mz_2_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_angry.png",(0,0), prefix_sprites+"far/mz/mz_2_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_angry.png",(0,0), prefix_sprites+"far/mz/mz_2_dress.png") )

    
    # Женя в Платье с очками^^
    image mz rage glasses dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_2_body.png", (0,0), prefix_sprites+"far/mz/mz_2_dress.png",(0,0), "images/sprites/far/mz/mz_2_rage.png", (0,0), "images/sprites/far/mz/mz_2_glasses.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_2_body.png", (0,0), prefix_sprites+"far/mz/mz_2_dress.png",(0,0), "images/sprites/far/mz/mz_2_rage.png", (0,0), "images/sprites/far/mz/mz_2_glasses.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_2_body.png", (0,0), prefix_sprites+"far/mz/mz_2_dress.png", (0,0), "images/sprites/far/mz/mz_2_rage.png", (0,0), "images/sprites/far/mz/mz_2_glasses.png") )
    

    image mz normal glasses dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_normal.png", (0,0), "images/sprites/far/mz/mz_1_glasses.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_normal.png", (0,0), "images/sprites/far/mz/mz_1_glasses.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_normal.png", (0,0), "images/sprites/far/mz/mz_1_glasses.png") )


    image mz smile glasses dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_3_body.png",(0,0), prefix_sprites+"far/mz/mz_3_dress.png",(0,0), "images/sprites/far/mz/mz_3_smile.png", (0,0), "images/sprites/far/mz/mz_3_glasses.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_3_body.png",(0,0), prefix_sprites+"far/mz/mz_3_dress.png",(0,0), "images/sprites/far/mz/mz_3_smile.png", (0,0), "images/sprites/far/mz/mz_3_glasses.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_3_body.png",(0,0), prefix_sprites+"far/mz/mz_3_dress.png",(0,0), "images/sprites/far/mz/mz_3_smile.png", (0,0), "images/sprites/far/mz/mz_3_glasses.png") )


    image mz shy glasses dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_shy.png",(0,0), prefix_sprites+"far/mz/mz_3_dress.png", (0,0), "images/sprites/far/mz/mz_3_glasses.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_shy.png",(0,0), prefix_sprites+"far/mz/mz_3_dress.png", (0,0), "images/sprites/far/mz/mz_3_glasses.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_shy.png",(0,0), prefix_sprites+"far/mz/mz_3_dress.png", (0,0), "images/sprites/far/mz/mz_3_glasses.png") )


    image mz laugh glasses dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_laugh.png", (0,0), "images/sprites/far/mz/mz_1_glasses.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_laugh.png", (0,0), "images/sprites/far/mz/mz_1_glasses.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_laugh.png", (0,0), "images/sprites/far/mz/mz_1_glasses.png") )


    image mz angry glasses dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_angry.png",(0,0), prefix_sprites+"far/mz/mz_2_dress.png", (0,0), "images/sprites/far/mz/mz_2_glasses.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_angry.png",(0,0), prefix_sprites+"far/mz/mz_2_dress.png", (0,0), "images/sprites/far/mz/mz_2_glasses.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_angry.png",(0,0), prefix_sprites+"far/mz/mz_2_dress.png", (0,0), "images/sprites/far/mz/mz_2_glasses.png") )


    image mz bukal glasses dress far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_bukal.png", (0,0), "images/sprites/far/mz/mz_1_glasses.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_bukal.png", (0,0), "images/sprites/far/mz/mz_1_glasses.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"far/mz/mz_1_body.png",(0,0), prefix_sprites+"far/mz/mz_1_dress.png",(0,0), "images/sprites/far/mz/mz_1_bukal.png", (0,0), "images/sprites/far/mz/mz_1_glasses.png") )




   # Игорёк
    # Поза 1
     # Пионерская форма
      # angry
    image ig pioneer_1 angry = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_pioneer.png",(0,0), prefix_sprites+"ig/vt_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_pioneer.png",(0,0), prefix_sprites+"ig/vt_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_pioneer.png",(0,0), prefix_sprites+"ig/vt_1_angry.png") )


      # rage
    image ig pioneer_1 rage = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_pioneer.png",(0,0), prefix_sprites+"ig/vt_1_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_pioneer.png",(0,0), prefix_sprites+"ig/vt_1_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_pioneer.png",(0,0), prefix_sprites+"ig/vt_1_rage.png") )


      # shy
    image ig pioneer_1 shy = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_pioneer.png",(0,0), prefix_sprites+"ig/vt_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_pioneer.png",(0,0), prefix_sprites+"ig/vt_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_pioneer.png",(0,0), prefix_sprites+"ig/vt_1_shy.png") )



     # Спортивная форма
      # angry
    image ig shirt_1 angry = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_shirt.png",(0,0), prefix_sprites+"ig/vt_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_shirt.png",(0,0), prefix_sprites+"ig/vt_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_shirt.png",(0,0), prefix_sprites+"ig/vt_1_angry.png") )


      # rage
    image ig shirt_1 rage = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_shirt.png",(0,0), prefix_sprites+"ig/vt_1_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_shirt.png",(0,0), prefix_sprites+"ig/vt_1_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_shirt.png",(0,0), prefix_sprites+"ig/vt_1_rage.png") )


      # shy
    image ig shirt_1 shy = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_shirt.png",(0,0), prefix_sprites+"ig/vt_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_shirt.png",(0,0), prefix_sprites+"ig/vt_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_shirt.png",(0,0), prefix_sprites+"ig/vt_1_shy.png") )

     # swim форма
      # angry
    image ig swim_1 angry = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_angry.png") )


      # rage
    image ig swim_1 rage = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_rage.png") )


      # shy
    image ig swim_1 shy = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0),  prefix_sprites+"ig/vt_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0),  prefix_sprites+"ig/vt_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_1_body.png",(0,0), prefix_sprites+"ig/vt_1_shy.png") )


    # Поза 2
     # Пионерская форма
      # normal
    image ig pioneer_2 normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_pioneer.png",(0,0), prefix_sprites+"ig/vt_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_pioneer.png",(0,0), prefix_sprites+"ig/vt_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_pioneer.png",(0,0), prefix_sprites+"ig/vt_2_normal.png") )
    
      
      # sad
    image ig pioneer_2 sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_pioneer.png",(0,0), prefix_sprites+"ig/vt_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_pioneer.png",(0,0), prefix_sprites+"ig/vt_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_pioneer.png",(0,0), prefix_sprites+"ig/vt_2_sad.png") )
      
      
      # smile
    image ig pioneer_2 smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_pioneer.png",(0,0), prefix_sprites+"ig/vt_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_pioneer.png",(0,0), prefix_sprites+"ig/vt_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_pioneer.png",(0,0), prefix_sprites+"ig/vt_2_smile.png") )


     # Спортивная форма
      # normal
    image ig shirt_2 normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_shirt.png",(0,0), prefix_sprites+"ig/vt_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_shirt.png",(0,0), prefix_sprites+"ig/vt_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_shirt.png",(0,0), prefix_sprites+"ig/vt_2_normal.png") )
    
      
      # sad
    image ig shirt_2 sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_shirt.png",(0,0), prefix_sprites+"ig/vt_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_shirt.png",(0,0), prefix_sprites+"ig/vt_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_shirt.png",(0,0), prefix_sprites+"ig/vt_2_sad.png") )
      
      
      # smile
    image ig shirt_2 smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_shirt.png",(0,0), prefix_sprites+"ig/vt_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_shirt.png",(0,0), prefix_sprites+"ig/vt_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_shirt.png",(0,0), prefix_sprites+"ig/vt_2_smile.png") )


     #  swim форма
      # normal
    image ig swim_2 normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_normal.png") )
    
      
      # sad
    image ig swim_2 sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_sad.png") )

   
      # smile
    image ig swim_2 smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0),  prefix_sprites+"ig/vt_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_2_body.png",(0,0), prefix_sprites+"ig/vt_2_smile.png") )
    
    
    # Поза 3
     # Пионерская форма
      # laugh
    image ig pioneer_3 laugh = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_pioneer.png",(0,0), prefix_sprites+"ig/vt_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_pioneer.png",(0,0), prefix_sprites+"ig/vt_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_pioneer.png",(0,0), prefix_sprites+"ig/vt_3_laugh.png") )
    
      
      # scared
    image ig pioneer_3 scared = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_pioneer.png",(0,0), prefix_sprites+"ig/vt_3_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_pioneer.png",(0,0), prefix_sprites+"ig/vt_3_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_pioneer.png",(0,0), prefix_sprites+"ig/vt_3_scared.png") )
      


     # Спортивная форма
      # laugh
    image ig shirt_3 laugh = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_shirt.png",(0,0), prefix_sprites+"ig/vt_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_shirt.png",(0,0), prefix_sprites+"ig/vt_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_shirt.png",(0,0), prefix_sprites+"ig/vt_3_laugh.png") )
    
      
      # scared
    image ig shirt_3 scared = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_shirt.png",(0,0), prefix_sprites+"ig/vt_3_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_shirt.png",(0,0), prefix_sprites+"ig/vt_3_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_shirt.png",(0,0), prefix_sprites+"ig/vt_3_scared.png") )
      
      

     #  swim форма
      # laugh
    image ig swim_3 laugh = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_laugh.png") )
    
      
      # scared
    image ig swim_3 scared = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((450,720), (0,0), prefix_sprites+"ig/vt_3_body.png",(0,0), prefix_sprites+"ig/vt_3_scared.png") )



    # Спрайты венеры, VEN
    # В пионерской форме
    # Нормальная
    image ven pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ven/ven_pioneer_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ven/ven_pioneer_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'ven/ven_pioneer_normal.png'))

    # Улыбка
    image ven pioneer smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ven/ven_pioneer_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ven/ven_pioneer_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'ven/ven_pioneer_smile.png'))

    # Недовольство
    image ven pioneer angry = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ven/ven_pioneer_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ven/ven_pioneer_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'ven/ven_pioneer_angry.png'))
    
    # В платье   
    # Нормальная
    image ven dress normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ven/ven_dress_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ven/ven_dress_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'ven/ven_dress_normal.png'))
    
    # Улыбка
    image ven dress smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ven/ven_dress_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ven/ven_dress_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'ven/ven_dress_smile.png')) 
   
    # Недовольство
    image ven dress angry = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ven/ven_dress_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ven/ven_dress_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'ven/ven_dress_angry.png'))




    # Женщина из партии
    # Ухмыляется
    image rim grin = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'rim/rim_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'rim/rim_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'rim/rim_grin.png'))    
   
    # Смеётся
    image rim laugh = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'rim/rim_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'rim/rim_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'rim/rim_laugh.png'))

    # Нормальная эмоция
    image rim normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'rim/rim_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'rim/rim_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'rim/rim_normal.png'))    
   
    # Улыбается
    image rim smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'rim/rim_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'rim/rim_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'rim/rim_smile.png'))
    
    
    # Бабушка
    # Нормально
    image gr normal  = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'gr/gr_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'gr/gr_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'gr/gr_norm.png'))

    # Улыбка
    image gr smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'gr/gr_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'gr/gr_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'gr/gr_smile.png'))
    
    
    
   
    # Дмитрий
    # close
    # поза 1
    # angry
    image ds angry_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ds/close/ds1_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ds/close/ds1_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'ds/close/ds1_angry.png'))
    
    

    # norm
    image ds normal_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ds/close/ds1_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ds/close/ds1_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'ds/close/ds1_norm.png'))
    
    

    # smile
    image ds smile_1 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ds/close/ds1_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ds/close/ds1_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'ds/close/ds1_smile.png'))
    
    

    # поза 2
    # angry
    image ds angry_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ds/close/ds2_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ds/close/ds2_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'ds/close/ds2_angry.png'))
    
    


    # normal
    image ds normal_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ds/close/ds2_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ds/close/ds2_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'ds/close/ds2_norm.png'))
    
    

    # smile 
    image ds smile_2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ds/close/ds2_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ds/close/ds2_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'ds/close/ds2_smile.png'))   
 
 
    # far
    # Поза 1
    # angry
    image ds angry_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ds/far/ds1_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ds/far/ds1_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'ds/far/ds1_angry.png'))
    
    # normal
    image ds normal_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ds/far/ds1_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ds/far/ds1_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'ds/far/ds1_norm.png'))
 
    # smile
    image ds smile_1 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ds/far/ds1_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ds/far/ds1_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'ds/far/ds1_smile.png'))
    
    
    # Поза 2
    # angry
    image ds angry_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ds/far/ds2_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ds/far/ds2_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'ds/far/ds2_angry.png'))
    
    # normal
    image ds normal_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ds/far/ds2_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ds/far/ds2_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'ds/far/ds2_norm.png'))
 
    # smile
    image ds smile_2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ds/far/ds2_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ds/far/ds2_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'ds/far/ds2_smile.png'))
    
    
    # normal
    # Поза 1
    # angry
    image ds angry_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ds/normal/ds1_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ds/normal/ds1_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'ds/normal/ds1_angry.png'))
    
    # normal
    image ds normal_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ds/normal/ds1_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ds/normal/ds1_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'ds/normal/ds1_norm.png'))
 
    # smile
    image ds smile_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ds/normal/ds1_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ds/normal/ds1_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'ds/normal/ds1_smile.png'))
    
    
    # Поза 2
    # angry
    image ds angry_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ds/normal/ds2_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ds/normal/ds2_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'ds/normal/ds2_angry.png'))
    
    # normal
    image ds normal_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ds/normal/ds2_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ds/normal/ds2_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'ds/normal/ds2_norm.png'))
 
    # smile
    image ds smile_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ds/normal/ds2_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ds/normal/ds2_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'ds/normal/ds2_smile.png'))
    
    
    # Катя
    # злится
    image kt angry = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'kt/kt_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'kt/kt_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'kt/kt_angry.png'))    

    # ухмяляется
    image kt grin = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'kt/kt_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'kt/kt_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'kt/kt_grin.png'))  
    
    # нормальная
    image kt normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'kt/kt_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'kt/kt_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'kt/kt_normal.png'))  
    
    # серьзная
    image kt serious = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'kt/kt_serious.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'kt/kt_serious.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'kt/kt_serious.png'))  
    
    
    # Шокированая
    image kt shocked = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'kt/kt_shocked.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'kt/kt_shocked.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'kt/kt_shocked.png'))  
    
    
    
    
    # mk, Мисато
    # far
    # dontlike
    image mk dontlike far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'mk/far/mk_dontlike.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'mk/far/mk_dontlike.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'mk/far/mk_dontlike.png'))  

    
    # sad
    image mk sad far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'mk/far/mk_sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'mk/far/mk_sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'mk/far/mk_sad.png')) 
    
    
    # smile
    image mk smile far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'mk/far/mk_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'mk/far/mk_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'mk/far/mk_smile.png'))
    
    
    # normal
    # dontlike
    image mk dontlike = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'mk/normal/mk_dontlike.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'mk/normal/mk_dontlike.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'mk/normal/mk_dontlike.png'))


    # sad
    image mk sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'mk/normal/mk_sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'mk/normal/mk_sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'mk/normal/mk_sad.png')) 
    
    
    # smile
    image mk smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'mk/normal/mk_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'mk/normal/mk_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'mk/normal/mk_smile.png'))


##prologue
    #_model 
    image model_1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'md/model1.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'md/model1.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'md/model1.png'))

    image model_2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'md/model2.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'md/model2.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'md/model2.png'))

    #_fotograph
    image ft = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ft/ft.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'ft/ft.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'ft/ft.png'))
    
    ## ant
    image ant grin = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ant/ant_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ant/ant_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'ant/ant_grin.png'))
    
    image ant normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ant/ant_norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ant/ant_norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'ant/ant_norm.png'))    

    image ant smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ant/ant_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((600, 720), (0, 0), prefix_sprites+'ant/ant_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((600, 720),  (0, 0), prefix_sprites+'ant/ant_smile.png'))
    


    # UVAO brother
    image ur default = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ur/ur_default.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 720), (0, 0), prefix_sprites+'ur/ur_default.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 720),  (0, 0), prefix_sprites+'ur/ur_default.png'))

    
# elements
    # sonata
    image sonata = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((227, 133), (0, 0), prefix_sprites+'elements/sonata323s.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((227, 133), (0, 0), prefix_sprites+'elements/sonata323s.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((227, 133),  (0, 0), prefix_sprites+'elements/sonata323s.png'))
    
    # P63A1
    image P63A1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((367, 720), (0, 0), prefix_sprites+'elements/P63A1.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((367, 720), (0, 0), prefix_sprites+'elements/P63A1.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((367, 720),  (0, 0), prefix_sprites+'elements/P63A1.png'))    
    
    # ez_a_divat_87
    image ez_a_divat_87 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((287, 527), (0, 0), prefix_sprites+'elements/ez_a_divat_87.jpg'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((287, 527), (0, 0), prefix_sprites+'elements/ez_a_divat_87.jpg'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((287, 527),  (0, 0), prefix_sprites+'elements/ez_a_divat_87.jpg'))
    
    # argo0041
    image argo0041 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((450, 347), (0, 0), prefix_sprites+'elements/argo0041.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((450, 347), (0, 0), prefix_sprites+'elements/argo0041.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((450, 347),  (0, 0), prefix_sprites+'elements/argo0041.png'))
    
    # DX712
    image DX712 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'elements/DX712.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((750, 720), (0, 0), prefix_sprites+'elements/DX712.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((750, 720),  (0, 0), prefix_sprites+'elements/DX712.png'))
    
    # Casio_DW6600
    image Casio_DW6600 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((427, 427), (0, 0), prefix_sprites+'elements/Casio_DW6600.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((427, 427), (0, 0), prefix_sprites+'elements/Casio_DW6600.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((427, 427),  (0, 0), prefix_sprites+'elements/Casio_DW6600.png'))

    # foto
    image foto = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((389, 218), (0, 0), prefix_sprites+'elements/foto.jpg'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((389, 218), (0, 0), prefix_sprites+'elements/foto.jpg'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((389, 218),  (0, 0), prefix_sprites+'elements/foto.jpg'))
    
    # NATIONAL
    image NATIONAL = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((209, 107), (0, 0), prefix_sprites+'elements/NATIONAL.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((209, 107), (0, 0), prefix_sprites+'elements/NATIONAL.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((209, 107),  (0, 0), prefix_sprites+'elements/NATIONAL.png'))

# cars

    image XJS = prefix_sprites+'cars/XJS.png'
    image STARION = prefix_sprites+'cars/STARION.png'
    image LEOF31 = prefix_sprites+'cars/LEOF31.png'
    image XJ12 = prefix_sprites+'cars/XJ12.png'
    image AZLK410 = prefix_sprites+'cars/AZLK410.png'
  
  
# Leaves

    image lay0_0 = way_Leaves+'lay_0/lvs_lay0_0.png'
    image lay0_1 = way_Leaves+'lay_0/lvs_lay0_1.png'
    image lay1_0 = way_Leaves+'lay_1/lvs_lay1_0.png'
    image lay1_1 = way_Leaves+'lay_1/lvs_lay1_1.png'
    image lay1_2 = way_Leaves+'lay_1/lvs_lay1_2.png'
    image lay1_3 = way_Leaves+'lay_1/lvs_lay1_3.png'
    image lay1_4 = way_Leaves+'lay_1/lvs_lay1_4.png'
    image lay2_0 = way_Leaves+'lay_2/lvs_lay2_0.png'
    image lay2_1 = way_Leaves+'lay_2/lvs_lay2_1.png'
    image lay2_2 = way_Leaves+'lay_2/lvs_lay2_2.png'
    image lay2_3 = way_Leaves+'lay_2/lvs_lay2_3.png'


# vomiting
    
    image vomiting = way_Vomiting+'vomiting.png'
  
  
# snow img

    image snow_0 = SnowBlossom(way_Blossom+'Snow/0.png', count = 128, xspeed = 0, yspeed = (110, 210), fast = True, border = 80)
    image snow_1 = SnowBlossom(way_Blossom+'Snow/1.png', count = 16, xspeed = 0, yspeed = (100, 200), fast = True, border = 80)
    image snow_2 = SnowBlossom(way_Blossom+'Snow/2.png', count = 4, xspeed = 0, yspeed = (90, 190), fast = True, border = 80)
    image snow_3 = SnowBlossom(way_Blossom+'Snow/3.png', count = 4, xspeed = 0, yspeed = (80, 180), fast = True, border = 80)


# rain

    image rain_square = SnowBlossom(Transform(way_Blossom+'Rain/0.png', rotate = 18), count = 100, xspeed = 200, yspeed = 600, fast = True, border = 80)
    image rain = SnowBlossom(way_Blossom+'Rain/0.png', count = 100, xspeed = 700, yspeed = 600, fast = True, border = 80)
    image rain_beach = SnowBlossom(Transform(way_Blossom+'Rain/0.png', rotate = 10), count = 100, xspeed = 400, yspeed = 600, fast = True, border = 80)
    image mus_rain = SnowBlossom(way_Blossom+'Rain/1.png', count = 100, xspeed = -700, yspeed = 600, fast = True, border = 80)
    image forest_rain = SnowBlossom(way_Blossom+'Rain/2.png', count = 100, xspeed = 0, yspeed = 600, fast = True, border = 80)
    image easy_rain = SnowBlossom(way_Blossom+'Rain/0.png', count = 50, xspeed = 300, yspeed = 400, fast = True, border = 80)
    
    
# 410

    image _410 = way_410+'444.png'


# Semen

    image s1 = Animation(way_Semen+'1/0.png', 0.5,
                         way_Semen+'1/1.png', 0.5,
                         way_Semen+'1/2.png', 0.5,
                         way_Semen+'1/3.png', 0.5,
                         way_Semen+'1/4.png', 0.5,
                         way_Semen+'1/5.png', 0.5,)
                         
    image s2 = Animation(way_Semen+'2/0.png', 0.5,
                         way_Semen+'2/1.png', 0.5,
                         way_Semen+'2/2.png', 0.5,
                         way_Semen+'2/3.png', 0.5,
                         way_Semen+'2/4.png', 0.5,
                         way_Semen+'2/5.png', 0.5,)
                         
    image s3 = Animation(way_Semen+'3/0.png', 0.5,
                         way_Semen+'3/1.png', 0.5,
                         way_Semen+'3/2.png', 0.5,
                         way_Semen+'3/3.png', 0.5,
                         way_Semen+'3/4.png', 0.5,
                         way_Semen+'3/5.png', 0.5,)
                         
    image s4 = Animation(way_Semen+'4/0.png', 0.5,
                         way_Semen+'4/1.png', 0.5,
                         way_Semen+'4/2.png', 0.5,
                         way_Semen+'4/3.png', 0.5,
                         way_Semen+'4/4.png', 0.5,
                         way_Semen+'4/5.png', 0.5,)
                         
    image s5 = Animation(way_Semen+'5/0.png', 0.5,
                         way_Semen+'5/1.png', 0.5,
                         way_Semen+'5/2.png', 0.5,
                         way_Semen+'5/3.png', 0.5,
                         way_Semen+'5/4.png', 0.5,
                         way_Semen+'5/5.png', 0.5,)
                         
    image s6 = Animation(way_Semen+'6/0.png', 0.5,
                         way_Semen+'6/1.png', 0.5,
                         way_Semen+'6/2.png', 0.5,
                         way_Semen+'6/3.png', 0.5,
                         way_Semen+'6/4.png', 0.5,
                         way_Semen+'6/5.png', 0.5,)


    # adv_Slavia
    define f = Character('Отец', color = "#ccffcc", what_color="#f1d076")
    define ox = Character('Охранник', color = "#ffccff", what_color="#f1d076")
    define w = Character('Женщина', color = "#ffcc99", what_color="#f1d076")
    define a = Character('Администратор', color = "#ff99cc", what_color="#f1d076")
    define m_1 = Character('Первый гитарист', color='#99ff66', what_color='f1d076')
    define mm = Character('Второй гитарист', color = "#99ff66", what_color="#f1d076")
    define mmm = Character('Третий гитарист', color = "#99ff66", what_color="#f1d076")
    define h = Character('Хозяин автомобилей', color = "#cc66ff", what_color="#f1d076")
    define gggg = Character('Голос', color = "#009933", what_color="#f1d076")
    define ggg = Character('Девочка', color = "#ffff00", what_color="#f1d076")
    define ant = Character('Антон', color = "#66ccff", what_color="#f1d076")
    define ddd = Character('Дмитрий', color = "#ff6699", what_color="#f1d076")
    define off = Character('Официант', color = "#666633", what_color="#f1d076")
    define sss = Character('Света', color = "#3399ff", what_color="#f1d076")
    define pc = Character('Продавец коктейлей', color = "#9966ff", what_color="#f1d076")
    define tttt = Character('???', color = "#ffffff", what_color="#f1d076")
    define pio = Character('Пионер', color = "#900000", what_color="#f1d076")
    define miii = Character('Черныш', color = "#993366", what_color="#f1d076")
    define viii = Character('Котик', color = "#993366", what_color="#f1d076")
    define iar = Character('Ярик', color = "#cc0099", what_color="#f1d076")
    define shi = Character('Белая кошка', color = "#ffcc00", what_color="#f1d076")
    define ba = Character('Борис Алексеевич', color = "#66ff33", what_color="#f1d076")
    define ani = Character('Аня', color = "#00ffff", what_color="#f1d076")
    define tl = Character('Толик', color = "#99ff99", what_color="#f1d076")
    define deti = Character('Дети', color = "#cc00ff", what_color="#f1d076")
    define muh = Character('Алексей Максимович', color = "#00ff99", what_color="#f1d076")
    define wuhu = Character('Администратор', color = "#ffffff", what_color="#f1d076")
    define ffffff = Character('Мужчина', color = "#ffffff", what_color="#f1d076")
    define fffff2 = Character('Мужчина2', color = "#ffffff", what_color="#f1d076")
    define fffff3 = Character('Мужчина3', color = "#ffffff", what_color="#f1d076")
    define pet = Character('Петя', color = "#ffffff", what_color="#f1d076")
    define geo = Character('Старший Геолог', color = "#ffffff", what_color="#f1d076")
    define mis = Character('«Мисато»', color = "#00ff00", what_color="#f1d076")
    define dan = Character('Даня', color = "#3399ff", what_color="#f1d076")
    define ali = Character('Алька', color = "#00ff99", what_color="#f1d076")
    define bur = Character('Девушка', color = "#ffffff", what_color="#f1d076")
    define oxu = Character('Оксана', color = "#cc99ff", what_color="#f1d076")
    define art = Character('Артём', color = "#ff0066", what_color="#f1d076")
    define dir = Character('Директор', color = "#00ff99", what_color="#f1d076")
    define pov = Character('Тетя Нюра', color = "#3399ff", what_color="#f1d076")
    define ser = Character('Сергей', color = "#99ff99", what_color="#f1d076")
    define zam = Character('Зам. 3-го Отряда', color = "#00ff00", what_color="#f1d076")
    define pos = Character('Игорь', color = "#3399ff", what_color="#f1d076")
    define gol = Character('Странный голос 1', color = "#99ff66", what_color="#f1d076")
    define gol1 = Character('Странный голос 2', color = "#99ff66", what_color="#f1d076")
    define nach = Character('Начальник', color = "#c8ffc8", what_color="#f1d076")
    define ktot = Character('Кто-то', color = "#c8ffc8", what_color="#f1d076")
    define diz = Character('Дизайнер', color = "#c8ffc8", what_color="#f1d076")
    define bux = Character('Бугалтер', color = "#c8ffc8", what_color="#f1d076")
    define ven = Character('Венера', color = "#00ff99", what_color="#f1d076")
    define plan = Character('Девушка с планшетом', color = "#ffffff", what_color="#f1d076")
    define ded = Character('Дед Иван', color = "#00ffff", what_color="#f1d076")
    define rod = Character('Родион', color = "#00ffff", what_color="#f1d076")
    define kul = Character('Кулаков', color = "#99ff99", what_color = "#f1d076")
    define mic = Character('Микрофон', color = "#ffffff", what_color="#f1d076")
    define rob = Character('Робот', color = "#ffffff", what_color="#f1d076")
    define tol = Character('Толпа', color = "#ffffff", what_color="#f1d076")
    define ot7 = Character('Первый отряд', color = "#ffffff", what_color="#f1d076")
    define dm = Character('Римма', color = "#00ff99", what_color="#f1d076")
    define il = Character('Илья', color = "#cc0000", what_color="#f1d076")
    define ram = Character('Рамиль', color = "#ff9966", what_color="#f1d076")
    define pr = Character('Повар', color = "#ff9966", what_color="#f1d076")
    define kat = Character('Катя', color = "#ccffcc", what_color="#f1d076")
    define andr = Character('Андрис', color = "#ccffcc", what_color="#f1d076")
    define poz = Character('Старушка', color = "#ffffff", what_color="#f1d076")           
    define om = Character('Дедушка Мику', color = "#ffffff", what_color="#f1d076")
    define vod = Character('Водитель', color = "#ffffff", what_color="#f1d076")
    define nik = Character('Голос', color = "#666699", what_color="#f1d076")
    define piko = Character('Пионерка', color = "#900000", what_color="#f1d076")
    define dev = Character('Девочка', color = "#cc0000", what_color="#f1d076")
    define tel = Character("Телефон", color="#ccffcc", what_color="#f1d076")
    define ha_ha = Character('Объявление', color = "#ffffff", what_color="#f1d076")
    define rrr = Character("Радио", color="#c8ffc8", what_color="#f1d076")
    define slth = Character('Славя', color = "#ffd200", what_color="#f1d076", what_prefix = "~", what_suffix = "~")
    
    # nvl_Slavia
    define solo = Character(_("Солисты"), color = "#ffffff", what_color="#f1d076", kind=nvl)
    define mus = Character(_("Музыка"), color = "#ffffff", what_color="#f1d076", kind=nvl)
    define pes = Character(_("Песня"), color="#c8ffc8", what_color="#f1d076", kind=nvl)