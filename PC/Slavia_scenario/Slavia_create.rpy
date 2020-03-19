label Slavia_previu:

    window hide
    
    $ _game_menu_screen = None
    
    scene cg hris_splash with fade
    
    $ renpy.pause(5.0, hard = True)
    
    scene black with fade
    show text '{size=50}{color=#FF0800}{size=70}(!)ПРЕДУПРЕЖДЕНИЕ{/size}{/color}{p}{p}Это художестенное произведение.{p}Все персонажи, организации, меcта и события выдуманы{p} и не связаны с реальными лицами.{/size}': 
        center
        ypos 0.25
    with dissolve2
    
    $ renpy.pause(10.0, hard = True)
    
    jump mm_Slavia
    


label Slavia_create:

    window hide

    $ _game_menu_screen = None

    play music SG_Fuka_Ryouiki_no_Deja_Vu fadein 3
    scene cg hris_splash with fade

    show Text1 'Команда Her Rain is Studio благодарит за чтение нашей модификации!{p}{p}{p}Сценарист и Продюсер - Дмитрий Zotov{p}{p}Кодер - Анна Достоевская. Благодаря ей, мод увидел свет{p}{p}{p}Художники - {p}{p}Евгений Слушев {p}{p}Илья Кунц{p}{p}Elkimi-chan{p}{p}PolinaOwl{p}{p}Марк Тэйлор{p}{p}Mnrlchk{p}{p}Мария Валерьевна{p}{p}Everlasting Summer. Лаборатория фотошопа{p}{p}Sarasvati{p}{p}Илья Балин{p}{p}{p}Композитор - Дмитрий Григорьев{p}{p}{p}При создании мода использовались фоны и спрайты{p}{p}- Булки, кефир, рок-н-ролл{p}{p}- 7 Дней лета (Alpha version){p}{p}- Мое Рыжее Счастье{p}{p}- Эти Безумные Деньки{p}{p}- Двое Стражей{p}{p}- Дни Со Славей{p}{p}- 7 дней с Мику{p}{p}- Крысиный яд{p}{p}{p}- Группа в контакте "Бесконечное лето/Everlasting summer Fan group"{p}{p}- Группа в контакте "Как создать свой мод для игры Бесконечное Лето"{p}{p}- Группа в контакте "Visual novels, аниме фоны, спрайты, RPG maker"{p}{p}{p}- Интернет-сайты https://www.hifiengine.com/ и http://www.rw6ase.narod.ru/ {p}{p}- Поиск по картинкам Яндекса{p}{p}{p}Отдельные благодарности{p}{p}Сердечно благодарю за предоставленные ЦГ и фоны Lord Kunzite{p}{p}Благодарю за предоставленный спрайт кошки Илью Токачирова{p}(Домарощинера){p}{p}Благодарим Евгения Геса, за то что поверил в нас!{p}{p}Спасибо Ротамелу, Гвидо Ван Россуму и Денису Ритчи{p}{p}{p}Спасибо создателям модов и фанфиков {p}{p}"7 Дней Лета",{p}{p}"Мое Рыжее Счастье",{p}{p}"Чудо по имени Славя",{p}{p}"Бесконечные каникулы",{p}{p}"DVA",{p}{p}"Мы танцевали среди звезд",{p}{p}«ПОСЛЕДНИЙ ШАНС ДЛЯ ДВОИХ или PER ASPERA AD ASTRA»,{p}{p}за ламповость и вдохновение{p}{p}{p}И, конечно, Soviet Games за замечательную новеллу!{p}{p}{p}Продолжение следует...' at Sub


    $ renpy.pause(160.0, hard = True)

    scene cg standart_slavia with dissolve2
    
    jump mm_Slavia