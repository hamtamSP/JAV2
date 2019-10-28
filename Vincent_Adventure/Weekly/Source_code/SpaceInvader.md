Source Code: by Vincent


    #================================Import Liabraries=================================
    from microbit import *
    import random
    #====================================Functions=====================================
    def outscreen_x(spacecraft_x): # Prevent Spacecrat fromgoing out of screen
        if (spacecraft_x > 4):
            spacecraft_x = 4
        if (spacecraft_x < 0):
            spacecraft_x = 0
        return spacecraft_x

    def alien_move_y(alien_y): # Alien move Downwards
        alien_y = alien_y + 1
        if (alien_y > 4):
            alien_y = 0
        return alien_y
    def nextalien(alien_y, alien_x): # Next Alien Spawn
        if (alien_y == 0):
            alien_x = random.randint(0,4)
        return alien_x
    #======================================Setup=======================================
    spacecraft_x = 2
    alien_x = random.randint(0,4)
    alien_y = 0
    score = 0
    random.seed()
    display.show(Image.HAPPY) # Prepare for game to start
    sleep(1000)
    #==================================Game Start Loop=================================
    while True:
        #draw the display
        display.clear()
        display.set_pixel(spacecraft_x,4,6)
        display.set_pixel(alien_x,alien_y,7)
    #==================================Buttons Movements===============================
        if button_a.is_pressed():
            #move left
            spacecraft_x = spacecraft_x - 1

        if button_b.is_pressed():
            #move right
            spacecraft_x = spacecraft_x + 1
    #==================================Spacecraft Collison=============================
        if (alien_x == spacecraft_x and alien_y ==4):
            display.show(Image.SAD)
            sleep(1000)
            break
    #====================================Activities====================================      
        # Alien Move Down
        alien_y = alien_move_y(alien_y)
        # Check and adjust Spacecraft remains in screen
        spacecraft_x = outscreen_x(spacecraft_x)
        # prepare next Alien
        alien_x = nextalien(alien_y,alien_x)
        #Record Score
        score = score + 1
        #some delay to view the screen
        sleep(100)
    #====================================Game Over=====================================
    display.scroll("Game Over!")
    print("Your Score is :" + str(int(score)))
