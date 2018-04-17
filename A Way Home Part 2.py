#CutScreen
timeframe = 0
while not game.over:
    game.processInput()
    game.clearBackground()
    timeframe += 0.5
    print(timeframe)

    portal.draw()
    mc3.draw()
    happy.draw()

    if timeframe >=0 and timeframe <=100:
        db1.draw()
        happy.visible = False
    elif timeframe >=100 and timeframe <=200:
        db2.draw()
        happy.visible = True
        mc3.visible = False
    elif timeframe >=200 and timeframe <=300:
        db3.draw()
        mc3.visible = True
        happy.visible = False
    elif timeframe >=300 and timeframe <=400:
        db4.draw()
        happy.visible = True
        mc3.visible = False
    elif timeframe >=400 and timeframe <=500:
        db5.draw()
        happy.visible = True
        mc3.visible = False
    elif timeframe >=500 and timeframe <=600:
        db6.draw()
        mc3.visible = True
        happy.visible = False
    elif timeframe >=600 and timeframe <=700:
        db7.draw()
        mc3.visible = True
        happy.visible = False
    elif timeframe >=700 and timeframe <=800:
        db8.draw()
        happy.visible = True
        mc3.visible = False
    elif timeframe >=800 and timeframe <=900:
        db9.draw()
        happy.visible = True
        mc3.visible = False
    elif timeframe >=900 and timeframe <=1000:
        db10.draw()
        happy.visible = True
        mc3.visible = False
    elif timeframe >=1000 and timeframe <=1100:
        db11.draw()
        mc3.visible = True
        happy.visible = False
    elif timeframe >=1100 and timeframe <=1150:
        game.over = True
        
    game.update(30)
game.over = False

#level 2 - catching fish
fishcount = 0
catpassed = 0 
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)

    mclv2.draw()

    #Cat 1 
    for index in range(7):
        cat[index].move()
        if cat[index].collidedWith(mclv2) or cat[index].collidedWith(boat):
            rudy.play()
            mclv2.health -= 10
            cat[index].visible = False
            catpassed += 1

        if cat[index].isOffScreen("bottom") and cat[index].visible:
            cat[index].visible = False
            catpassed += 1

    #Cat 2
    for index in range(3):
        cat2[index].moveTowards(mc,5)
        if cat2[index].collidedWith(mc):
            rudy.play()
            mclv2.health -= 5
            cat2[index].visible = False
            catpassed += 1
                   
    #Fish
    for index in range(20):
        fish[index].move()
        
        if fish[index].y < 350:
            s = randint(1,5)
            fish[index].setSpeed(s,180)
            fish[index].move()

        if fish[index].collidedWith(mclv2) or fish[index].collidedWith(boat):
            fishcount += 1
            fish[index].visible = False

        if fish[index].isOffScreen("bottom") and fish[index].visible:
            fish[index].visible = False
            
    #Mc control
    if keys.Pressed[K_LEFT]:
        mclv2.x -= 8

    if keys.Pressed[K_RIGHT]:
        mclv2.x += 8

    if keys.Pressed[K_UP]:
        mclv2.y -= 8

    if keys.Pressed[K_DOWN]:
        mclv2.y += 8

    boat.moveTo(mclv2.x,mclv2.y+45)

    if mclv2.health < 1:
        game.over = True
        
    if catpassed  == 10:
        key.draw()
        key.visible = True

    if key.collidedWith(mclv2):
        game.over = True
         
    game.drawText("Fish Collected:"+str(fishcount),mc.x, mc.y +100)
    game.drawText("Health:" + str(mc.health),mc.x,mc.y + 75)
    game.update(30)
game.over = False
