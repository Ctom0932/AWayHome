from gamelib import *

game =  Game(900,800, "A Way Home")

#Graphic Set Up
logo = Image("A-Way-Home.png",game)
howtoplay = Image("How-To-Play.png",game)

play = Image("play.png",game)
bk = Image("1.jpg",game)
bk.resizeTo(1000,1000)
mc = Animation("girl.png",8,game,196/4,176/2)
mc.resizeBy(100)
mc.moveTo(50,700)
ms = Image("mine_shaft.png",game)
ms.resizeBy(20)
keyboard = Image("keyboard.png",game)
arrow = Image("arrow.png",game)
arrow.resizeBy(-80)
back = Image("Back.png",game)
js = Animation("gem.png",6,game,90/3,104/2)
js.resizeBy(550)
js.moveTo(830,650)


#Story Graphics
story = Image("Story bg.png",game)
sb = Image("Story Bg.png",game)
ssb1 = Image("speechbubble1.gif",game)
ssb1.moveTo(223,420)
ssb2 = Image("speechbubble2.gif",game)
ssb2.moveTo(200,600)
ssb3 = Image("speechbubble3.gif",game)
ssb3.moveTo(200,405)
ssb4 = Image("speechbubble4.gif",game)
ssb4.moveTo(200,405)

#Graphics - Level 2
bklv2 = Image("sea2.jpg",game)
bklv2.resizeTo(900, 800)
game.setBackground(bklv2)
boat = Image("boat.png",game)
key = Image("key.png",game)
key.moveTo(800,450)
key.resizeBy(-80)
key.visible = False

#Cutscreen
ms = Image("mine_shaft.png",game)
ms.resizeTo(900,700)
portal = Image("portal.jpg",game)
portal.resizeTo(900,700)
db1 = Image("db1.png",game)
db1.moveTo(500,700)
db2 = Image("db2.png",game)
db2.moveTo(500,700)
db3 = Image("db3.png",game)
db3.moveTo(500,700)
db4 = Image("db4.png",game)
db4.moveTo(500,700)
db5 = Image("db5.png",game)
db5.moveTo(500,700)
db6 = Image("db6.png",game)
db6.moveTo(500,700)
db7 = Image("db7.png",game)
db7.moveTo(500,700)
db8 = Image("db8.png",game)
db8.moveTo(500,700)
db9 = Image("db9.png",game)
db9.moveTo(500,700)
db10 = Image("db10.png",game)
db10.moveTo(500,700)
db11 = Image("db11.png",game)
db11.moveTo(500,700)

#Character
mclv2 = Image("mc2.png",game)
mclv2.resizeBy(40)
mclv2.moveTo(50,450)
mc2 = Animation("girl.png",8,game,196/4,176/2)
mc2.resizeBy(240)
mc2.moveTo(50,600)
mc3 = Image("mc2.png",game)
mc3.resizeBy(240)
mc3.moveTo(100,600)
happy = Image("happy.png",game)
happy.moveTo(850,600)

#Fish Setup
fish = []
for index in range(20):
    fish.append( Image("fish.png",game))

for index in range(20):
    x = randint(50,850)
    y = randint(400,900)
    s = randint(1,5)
    fish[index].setSpeed(s,360)
    fish[index].moveTo(x,y)
    fish[index].resizeBy(-65)

#Cat Setup 1
cat = []
for index in range(7):
    cat.append( Animation("cat.png",7,game,720/2,964/4))

for index in range(7):
        x = randint(50,800)
        y = randint(100,850)
        s = randint(2,6)
        cat[index].moveTo(x, -y)
        cat[index].setSpeed(s,180)
        cat[index].resizeBy(-40)

#Cat Setup 2
cat2 = []
for index in range(3):
    cat2.append( Animation("cat.png",7,game,720/2,964/4))

for index in range(3):
        x = randint(50,850)
        y = randint(100,850)
        s = randint(2,6)
        cat2[index].moveTo(x, -y)
        cat2[index].setSpeed(s,180)
        cat2[index].resizeBy(-40)

#Sound
ct = Sound("Rudy.wav",3)
music = Sound("Power Bots Loop.wav",2)
bm = Sound("Fantasy Game Loop.wav",1)

#Falling Rocks
rock = []
for index in range (30):
    rock.append( Image("Rocks.png",game))

for index in range (30):
        x = randint(100,900)
        y = randint(100,900)
        s = randint(1,10)
        rock[index].setSpeed(s,180)
        rock[index].resizeBy(-90)
        rock[index].moveTo(x,-y)
            
#Start Up Screen
while not game.over:
    game.processInput()
    bk.draw()
    logo.draw()
    logo.moveTo(450,300)
    howtoplay.draw()
    howtoplay.moveTo(450,600)
    play.draw()
    play.moveTo(450,500)
    js.draw()
    mc.draw()
    mc.stop()
    bm.play()



    if howtoplay.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
        keyboard.draw()
        arrow.draw()
        back.draw()
        back.moveTo(110,60)
        arrow.moveTo(685,650)
    
        game.drawText("To move the character, you have to use the up, down, right, left arrows. To throw, press the spacebar", 100,700)

    game.update(30)
game.over = False


#How to play Set up Screen
while not game.over:
    game.processInput()
    game.clearBackground()
    keyboard.draw()
    arrow.draw()
    back.draw()
    back.moveTo(110,60)
    arrow.moveTo(685,650)
    
    game.drawText("To move the character, you have to use the up, down, right, left arrows. To throw, press the spacebar", 100,700)

    if back.collidedWith(mouse) and mouse.LeftClick:
         game.over = True

    game.update(30)
game.over = False

#Back to Start Screen
while not game.over:
    game.processInput()
    game.clearBackground()
    bk.draw()
    logo.draw()
    logo.moveTo(450,300)
    howtoplay.draw()
    howtoplay.moveTo(450,700)
    play.draw()
    play.moveTo(450,600)
    js.draw()
    mc.draw()

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    game.update(30)
game.over = False

timeframe = 0
while not game.over:
    game.processInput()
    game.clearBackground()
    sb.draw()
    mc.draw()
    mc.stop()

    timeframe += 0.5
    print(timeframe)

    if timeframe >= 0 and timeframe <= 100:
        ssb1.draw()
    elif timeframe >= 100 and timeframe <= 200:
        ssb2.draw()
    elif timeframe >= 200 and timeframe <= 300:
        ssb3.draw()
    elif timeframe >= 300 and timeframe <= 400:
        ssb4.draw()
    elif timeframe >= 500 and timeframe <= 550:
        game.over = True

    game.update(30)
game.over = False

#Level 1
while not game.over:
    game.processInput()
    game.clearBackground()
    ms.draw()
    mc.draw()
    mc.stop()
    js.draw()

    for index in range(30):
        rock[index].move()
        if rock[index].collidedWith(mc):
                mc.health -=10
                rock[index].visible = False

    
    
#Hero Control
    if keys.Pressed[K_LEFT]:
        mc.prevFrame()
        mc.x -=5

    if keys.Pressed[K_RIGHT]:
        mc.nextFrame()
        mc.x +=5

    if keys.Pressed[K_UP]:
        mc.prevFrame()
        mc.y -=5

    if keys.Pressed[K_DOWN]:
        mc.nextFrame()
        mc.y +=5

    if mc.health < 5:
        game.over = True

    game.drawText("Health" + str(mc.health),mc.x, mc.y +80)

    if mc.collidedWith(js):
        game.over = True

    game.update(30)
game.over = False

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
    bm.play()

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
while not game.over and mc.health >0:
    game.processInput()
    game.scrollBackground("left",2)

    mclv2.draw()

    #Cat 1 
    for index in range(7):
        cat[index].move()
        if cat[index].collidedWith(mclv2) or cat[index].collidedWith(boat):
            ct.play()
            mclv2.health -= 10
            cat[index].visible = False
            catpassed += 1

        if cat[index].isOffScreen("bottom") and cat[index].visible:
            cat[index].visible = False
            catpassed += 1

    #Cat 2
    for index in range(3):
        cat2[index].moveTowards(mclv2,5)
        if cat2[index].collidedWith(mclv2):
            ct.play()
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
         
    game.drawText("Fish Collected:"+str(fishcount),mclv2.x, mclv2.y +100)
    game.drawText("Health:" + str(mc.health),mclv2.x,mclv2.y + 75)
    game.update(30)
game.over = False

#Level 4 - Graphics
mclvl4 = Animation("girl.png",3,game,196/4,176/2)
mclvl4.resizeBy(50)
mclvl4.moveTo(50,550)
fish2 = Image("fish.png",game)
fish2.resizeBy(-40)
fish2.visible = False
bk3 = Image("beach.jpg",game)
bk3.resizeTo(900,800)
door = Image("door.png",game)
kee = Image("key.png",game)
kee.resizeTo(200,100)
key2 = Image("keys.jpg",game)
key2.resizeBy(5)


#cat setup
cat3 = []
for index in range(20):
    cat3.append(Animation("cat.png",7,game,720/2,964/4))

for index in range(20):
    x = randint(50,850)
    y = randint(100,850)
    s = randint(2,6)
    cat3[index].moveTo(x, -y)
    cat3[index].setSpeed(s,180)
    cat3[index].resizeBy(-40)

#door Setup
door = []
for index in range(50):
        door.append( Image("door.png",game))
        door[index].resizeBy(-70)

#Level 4
catpassed2 = 0
while not game.over:
    game.processInput()
    game.clearBackground()

    bk3.draw()
    fish2.move()
    mclvl4.draw()
    mclvl4.stop()

    music.play()

    for index in range(20):
        cat3[index].move()
        if cat3[index].collidedWith(fish2):
           cat3[index].visible = False
           fish2.visible = False
           catpassed2 += 1
           ct.play()
        if cat3[index].collidedWith(mclvl4):
            mc.health -= 5
        if cat3[index].isOffScreen("bottom"):
            catpassed2 += 1

    if keys.Pressed[K_SPACE]:
        fish2.moveTo(mclvl4.x,mclvl4.y)
        fish2.setSpeed(24,0)
        fish2.visible = True

    if catpassed2 == 20:
        game.over = True

    #Hero Control
    if keys.Pressed[K_LEFT]:
        mclvl4.prevFrame()
        mclvl4.x -=5

    if keys.Pressed[K_RIGHT]:
        mclvl4.nextFrame()
        mclvl4.x +=5
        
    if mclvl4.health < 1:
        game.over = True
   
    game.drawText("Health:" + str(mclvl4.health),mclvl4.x,mclvl4.y + 75)
    game.update(30)
game.over= False

#Level 5
while not game.over :
    game.processInput()
    game.clearBackground()
            
    mclvl4.draw()
    mclvl4.stop()
    door[index].moveTo(800,400)
    kee.moveTo(675,100)
    
    if mclvl4.collidedWith(door[index]):
         game.over = True

    #mc Control
    if keys.Pressed[K_UP]:
        mclvl4.y -= 8
    if keys.Pressed[K_DOWN]:
        mclvl4.y += 8
    if keys.Pressed[K_RIGHT]:
        mclvl4.x += 8
    if keys.Pressed[K_LEFT]:
        mclvl4.x -= 8
        
    game.drawText("Health: " + str(mc.health),mclvl4.x - 20,mclvl4.y + 50)
    game.update(30)
game.over = False

#The End
while not game.over:
    game.processInput()
    game.clearBackground()
   
    game.drawText("Game Over " + str(),400,300)
    game.update(30)
game.quit()
