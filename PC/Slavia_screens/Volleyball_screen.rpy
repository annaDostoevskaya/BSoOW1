screen Volleyball_screen():
    
    ## Define Volleyball()
    default Volleyball = Volleyball()
    
    
    
    ## add BG
    add direct_Volleyball + 'bg/cort.png' at DISSOLVE
    
    ## add GAME
    add Volleyball
    
    ## add persons
    add direct_Volleyball + 'viewers/boris.png' xpos(1700/2)+200  ypos 50 rotate 90
    
    add direct_Volleyball + 'viewers/tolick.png' xpos(1700/2)+150  ypos 150 rotate -77
    
    add direct_Volleyball + 'viewers/OD.png' xpos(1700/2)-300 ypos 39 rotate 75
    
    add direct_Volleyball + 'viewers/viola.png' xpos(1700/2)-170 ypos 30 rotate 110