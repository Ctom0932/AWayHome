from gamelib import*

game = Game(900,800,"A Way Home")

title = Image("A-Way-Home.png",game)
level4 = Image("Level-4.png",game)
level4.moveTo(150,50)
level5 = Image("Level-5.png",game)
level5.moveTo(150,50)
mc = Animation("scientist.png",3,game,196/4,176/2)
mc.resizeBy(50)
bk = Image("beach.jpg",game)
game.setBackground(bk)
bk.resizeTo(900,800)
fish = Image("fish.png",game)
cat = Image("cat.png",game)
door = Image("door.png",game)
kee = Image("key.png",game)
kee.resizeTo(200,100)
key = Image("keys.png",game)
key.resizeBy(5)
#Sound
ct = Sound("Rudy.wav",1)
music = Sound("Power Bots Loop.wav",2)


#Cat Setup
cat = []
for index in range(50):
        cat.append( Animation("cat.png",7,game,720/2,964/4) )
                    
for index in range(50):
         x = randint (100,700)
         y = randint(100,4000)
         s = randint(1,10)
         cat[index].moveTo(x, -y)
         cat[index].setSpeed(s,180)
         cat[index].resizeBy(-50)

#door Setup
door = []
for index in range(50):
        door.append( Image("door.png",game))
        door[index].resizeBy(-70)

#Level 4
catPassed = 0
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    
    level4.draw()
    mc.draw()
    mc.stop()
    cat[index].draw()
    music.play()
                
    for index in range(20):
        x = randint (300,600)
        y = randint(450,1300)
        cat[index].moveTowards(fish,5)
        fish.moveTo(x , y)        
        
        if keys.Pressed[K_SPACE]:
            fish.draw()
            fish.resizeTo(70,70)
            fish.visible = True
        if cat[index].collidedWith(fish):
            fish.visible = False
            ct.play()
            cat[index].visible = False

        if cat[index].collidedWith(mc):
            mc.health -= 20
            ct.play()
            cat[index].visible = False
        if mc.health <= 3:
            game.quit()
        if cat[index].isOffScreen("bottom") and cat[index].visible:
            catPassed += 1 
            cat[index].visible = False
        if catPassed >= 10:
            key.draw()
            key.moveTo(550,450)
        if key.collidedWith(mc):
            key.draw()
            key.moveTo(550,450)
            game.quit = True
         
                
    #mc Control
    if keys.Pressed[K_LEFT]:
        mc.prevFrame()
        mc.x -= 8
        
    if keys.Pressed[K_RIGHT]:
        mc.nextFrame()
        mc.x += 8

    if keys.Pressed[K_UP]:
        mc.nextFrame()
        mc.x += 8

    if keys.Pressed[K_DOWN]:
        mc.prevFrame()
        mc.x -= 8

    if mc.health < 1:
        game.over = True
        
    game.drawText("Health: " + str(mc.health),mc.x - 20,mc.y + 50)

    game.update(30)
game.over= False

#Level 5
while not game.over:
    game.processInput()
    game.clearBackground()
            
    mc.draw()
    mc.stop()
    door[index].moveTo(800,400)
    kee.moveTo(675,100)
    
    if mc.collidedWith(door[index]):
         game.quit()

    #mc Control
    if keys.Pressed[K_LEFT]:
        mc.prevFrame()
        mc.x -= 8
        
    if keys.Pressed[K_RIGHT]:
        mc.nextFrame()
        mc.x += 8

    if keys.Pressed[K_UP]:
        mc.nextFrame()
        mc.x += 8

    if keys.Pressed[K_DOWN]:
        mc.prevFrame()
        mc.x -= 8
     
    game.drawText("Health: " + str(mc.health),mc.x - 20,mc.y + 50)
    game.update(30)
game.over = False

#The End
while not game.over:
    game.processInput()
    game.clearBackground()

    game.drawText("The End "+str(mc),150, 200,"red")
    f = ("Comic Sans")
    game.update(30)
game.over = False
