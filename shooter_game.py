from pygame import *
from random import *
#mixer.init()
#mixer.music.load('МАРКОВИЧ - Гимн анонимусов.wav')
#mixer.music.play()
window = display.set_mode((1000,1000))
display.set_caption("a")

background = transform.scale(image.load('1625510695_8-kartinkin-com-p-pikselnii-fon-kosmos-krasivie-foni-8.jpg'),(1000,1000))
clock = time.Clock()
FPS = 120



class Hero(sprite.Sprite):
    def __init__(self,speed,imagename,x,y):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(imagename),(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(Hero):
    def __init__(self,speed,imagename,x,y):
        super().__init__(speed,imagename,x,y)
    def fire():
        keys = key.get_pressed()
        if keys[K_SPACE]:
            bul = Bul()
            b.add(bul)


    def update(self):
        keys = key.get_pressed()
        if keys[K_RIGHT]:
            self.rect.x += 10

        if keys[K_LEFT]:
            self.rect.x -= 10
    
font.init()
font1 = font.Font(None, 36)

lost = 0
class Enemy(Hero):
    def __init__(self,speed,imagename,x,y):
        super().__init__(speed,imagename,x,y)
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y >= 1000:
            self.rect.y = 0
            self.rect.x = randint(0,900)
            lost = lost + 1

class Bul(Hero):
    def __init__(self,speed,imagename,x,y):
        super().__init__(speed,imagename,x,y)
    

    def update(self):
        keys = key.get_pressed()
        if keys[K_SPACE]:
            self.rect.y -= 10
            

        

b = sprite.Group()
mon = sprite.Group()


for i in range(5):
    en = Enemy(1,'04821ddc31574525e733c0a8786c711e.jpg',0,0)
    en.add(mon)




    
herom = Player(10,'1625665346_3-kartinkin-com-p-kosmicheskii-korabl-piksel-art-art-krasivo-3.png',800,800)    




game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    t = font1.render("пропущено(Zа Россию,зеленский ******,всу ******,Путин лучший):" + str(lost), 1, (255, 255, 255))

               
    
    window.blit(background,(0,0))
    clock.tick(FPS)
    en.reset()
    en.update()
    herom.reset()
    herom.update()
    mon.update()
    mon.draw(window)
    b.update()
    b.draw(window)
    window.blit(t, (10, 10))
    display.update()


    





















game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

window.blit(background,(0,0))
clock.tick(FPS)
display.update()