screen game_menu_day10:
    tag game_menu
    modal True

    add 'images/bg/ext_boathouse_day.jpg'
    
    if persistent.game_menu_day10 == '1_part':
        
        if persistent.game_menu_dv == 'on':
        
            imagebutton:
                auto 'mods/Slavia/images/Slavia_menu/game_menu_d10/dv_%s.png'
                focus_mask True
                action Jump('sl_d_10_dv'), Hide('game_menu') at DISSOLVE_MM_center

        else:
        
            imagebutton:
                idle 'mods/Slavia/images/Slavia_menu/game_menu_d10/dv_hover.png'
                hover 'mods/Slavia/images/Slavia_menu/game_menu_d10/dv_hover.png'
                focus_mask True
                action NullAction() at center
            
        if persistent.game_menu_mi == 'on':
        
            imagebutton:
                auto 'mods/Slavia/images/Slavia_menu/game_menu_d10/mi_%s.png'
                focus_mask True
                action Jump('sl_d_10_mi'), Hide('game_menu') at DISSOLVE_MM_right
                
        else:
        
            imagebutton:
                idle 'mods/Slavia/images/Slavia_menu/game_menu_d10/mi_hover.png'
                hover 'mods/Slavia/images/Slavia_menu/game_menu_d10/mi_hover.png'
                focus_mask True
                action NullAction() at right

                
        if persistent.game_menu_mz == 'on':
        
            imagebutton:
                auto 'mods/Slavia/images/Slavia_menu/game_menu_d10/mz_%s.png'
                focus_mask True
                action Jump('sl_d_10_mz'), Hide('game_menu') at DISSOLVE_MM_left
                
        else:
            
            imagebutton:
                idle 'mods/Slavia/images/Slavia_menu/game_menu_d10/mz_hover.png'
                hover 'mods/Slavia/images/Slavia_menu/game_menu_d10/mz_hover.png'
                focus_mask True
                action NullAction() at left
                

    elif persistent.game_menu_day10 == '2_part':
        
        if persistent.game_menu_un == 'on':
            
            imagebutton:
                auto 'mods/Slavia/images/Slavia_menu/game_menu_d10/un_%s.png'
                focus_mask True
                action Jump('sl_d_10_un'), Hide('game_menu') at DISSOLVE_MM_right
                
        else:
            
            imagebutton:
                idle 'mods/Slavia/images/Slavia_menu/game_menu_d10/un_hover.png'
                hover 'mods/Slavia/images/Slavia_menu/game_menu_d10/un_hover.png'
                focus_mask True
                action NullAction() at right
                

        if persistent.game_menu_sl == 'on':
            
            imagebutton:
                auto 'mods/Slavia/images/Slavia_menu/game_menu_d10/sl_%s.png'
                focus_mask True
                action Jump('sl_d_10_sl'), Hide('game_menu') at DISSOLVE_MM_left

        else:
             
            imagebutton:
                idle 'mods/Slavia/images/Slavia_menu/game_menu_d10/sl_hover.png'
                hover 'mods/Slavia/images/Slavia_menu/game_menu_d10/sl_hover.png'
                focus_mask True
                action NullAction() at left


        if persistent.game_menu_el == 'on':
            
            imagebutton:
                auto 'mods/Slavia/images/Slavia_menu/game_menu_d10/el_%s.png'
                focus_mask True
                action Jump('sl_d_10_el'), Hide('game_menu') at DISSOLVE_MM_center

        else:
            
            imagebutton:
                idle 'mods/Slavia/images/Slavia_menu/game_menu_d10/el_hover.png'
                hover 'mods/Slavia/images/Slavia_menu/game_menu_d10/el_hover.png'
                focus_mask True
                action NullAction() at center
                
    else:
    
        if persistent.game_menu_sh == 'on':
            
            imagebutton:
                auto 'mods/Slavia/images/Slavia_menu/game_menu_d10/sh_%s.png'
                focus_mask True
                action Jump('sl_d_10_sh'), Hide('game_menu') at DISSOLVE_MM_right

        else:
            
            imagebutton:
                idle 'mods/Slavia/images/Slavia_menu/game_menu_d10/sh_hover.png'
                hover 'mods/Slavia/images/Slavia_menu/game_menu_d10/sh_hover.png'
                focus_mask True
                action NullAction() at right
                
        if persistent.game_menu_iar == 'on':
            
            imagebutton:
                auto 'mods/Slavia/images/Slavia_menu/game_menu_d10/iar_%s.png'
                focus_mask True
                action Jump('sl_d_10_iar'), Hide('game_menu') at DISSOLVE_MM_left

        else:
             
            imagebutton:
                idle 'mods/Slavia/images/Slavia_menu/game_menu_d10/iar_hover.png'
                hover 'mods/Slavia/images/Slavia_menu/game_menu_d10/iar_hover.png'
                focus_mask True
                action NullAction() at left