## Для input - а your_name
screen enter_your_name():
    
    add Solid('#00000090')
    add prefix_GUI+'base.png' zoom 2.0 xzoom 0.31 xalign 0.5 yalign 0.45


    vbox:
    
        style 'vbox_input'
    
        xysize (0.4, 0.4)
        
        align(.45,  .4)
        
        text '«Введите ваше имя,\n                      пожалуйста»\n\n\n\n' style 'text_input'
        
        input id 'enter_your_name' length 20 style 'input'


## Для input - а от Лены в 6 дне
screen enter_otvet_1():
    
    add Solid('#00000090')
    add prefix_GUI+'base.png' zoom 2.0 xzoom 0.31 xalign 0.5 yalign 0.45
        
    
    vbox:
    
        style 'vbox_input'
    
        xysize (0.4, 0.4)
        
        align(.45,  .4)
        
        text '«Подруга дней моих суровых,\n              голубка дряхлая моя»\n\n\n\n' style 'text_input'
        
        input id 'enter_otvet_1' length 16 style 'input'


## Для input - а от Кибернетиков в 6 дне
screen enter_otvet_2():
    
    add Solid('#00000090')
    add prefix_GUI+'base.png' zoom 2.0 xzoom 0.31 xalign 0.5 yalign 0.45


    
    vbox:
    
        xysize (0.4, 0.4)
        
        align(.45,  .4)
        
        text '«Один из базовых элементов\n              физического языка»\n\n\n\n' style 'text_input'
        
        input id 'enter_otvet_2' length 30 style 'input'


## Для input - а от Слави в 6 дне
screen enter_otvet_3():
    
    add Solid('#00000090')
    add prefix_GUI+'base.png' zoom 2.0 xzoom 0.5 xalign 0.5 yalign 0.45

    
    vbox:
    
        xysize (0.4, 0.4)
        
        align(.45,  .4)
        
        text '«Как звали командующих армиями,\n              что держали, оборону Сталинграда»\n\n\n\n' style 'text_input'

        input id 'enter_otvet_3' length 55 maximum(0.45, 0.45) style 'input'