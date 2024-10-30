import pygame
import random
import spriteSheet


pygame.init()
screen_width = 1000
screen_heigth = 800
screen = pygame.display.set_mode((screen_width,screen_heigth)) #** создает окно заданного размера
clock = pygame.time.Clock() #* для фпс'a
pygame.display.set_caption("My game")  #* Названия окна


#Sprites
player_sprites = pygame.sprite.Group() #* Создаем спрайты
ball_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()


#animation
player_images = []
player_image_numbers = 0


black = (0,0,0)
img = pygame.image.load("img\\whtdragon's animals and running horses- now with more dragons! (1).png")
sprite = spriteSheet.SpriteSheet(img)
for i in range(3):
    image = sprite.get_image(i,0,48,62,2,black)
    player_images.append(image)

for j in range(3):
    image = sprite.get_image(j,1,48,55,2,black)
    player_images.append(image)

for k in range(3):
    image = sprite.get_image(k,2,48,53,2,black)
    player_images.append(image)

for l in range(3):
    image = sprite.get_image(l,3,48,50,2,black)
    player_images.append(image)




last_update = pygame.time.get_ticks()
animation_coldown = 150
apple_image = pygame.image.load("img\\Pasted-20241028-184245.png").convert_alpha()

enemy_image = pygame.image.load("img\\enemas (1).png")
enemy_image_list = [

]

enemy_sprite_sheet = spriteSheet.SpriteSheet(enemy_image)
for e in range(5):
    enemy_images = enemy_sprite_sheet.get_image(e,0,75,92,1,black)
    enemy_image_list.append(enemy_images)


enemy_number = 0
enemy_animation = 200
enemy_last_update = pygame.time.get_ticks()


#Text
score = 0
set_font = pygame.font.SysFont("monospace",20)

#Speed
speedX = 3
speedY = 3

enemyX = 3
enemyY = 3

#Others
done = True
pygame.mixer.init()
test = False


class Player(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(1,screen_width),random.randint(1,screen_heigth))

    def update(self):
        global done,imageNumber,last_update,player_image_numbers

        current_update = pygame.time.get_ticks()
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            if player_image_numbers < 6 or player_image_numbers > 8:
                player_image_numbers = 6
            self.rect.x += speedX
            if current_update - last_update >= animation_coldown:
                player_image_numbers += 1
                last_update = current_update
                if player_image_numbers > 8:
                    player_image_numbers = 6

        elif key[pygame.K_LEFT]:
            self.rect.x -= speedX
            if player_image_numbers < 3 or player_image_numbers > 5:
                player_image_numbers = 3
            if current_update - last_update >= animation_coldown:
                player_image_numbers += 1
                last_update = current_update
                if player_image_numbers > 5:
                    player_image_numbers = 3

        elif key[pygame.K_UP]:
            self.rect.y -= speedY
            if player_image_numbers < 9 or player_image_numbers > 11:
                player_image_numbers = 9
            if current_update - last_update >= animation_coldown:
                player_image_numbers += 1
                last_update = current_update
                if player_image_numbers > 11:
                    player_image_numbers = 9
        
        elif key[pygame.K_DOWN]:
            self.rect.y += speedY
            if current_update - last_update >= animation_coldown:
                player_image_numbers += 1
                last_update = current_update
                if player_image_numbers >= 3:
                    player_image_numbers = 0

        if self.rect.x >= screen_width -50:
            pygame.mixer.music.load("img\\snake-dies-game-over.mp3")
            pygame.mixer.music.play()
            pygame.time.wait(500)
            done = False
            

        elif self.rect.x <= -50:
            pygame.mixer.music.load("img\\snake-dies-game-over.mp3")
            pygame.mixer.music.play()
            pygame.time.wait(500)
            done = False     

        elif self.rect.y >= screen_heigth - 50:
            pygame.mixer.music.load("img\\snake-dies-game-over.mp3")
            pygame.mixer.music.play()
            pygame.time.wait(500)
            done = False
        elif self.rect.y <= -50:
            pygame.mixer.music.load("img\\snake-dies-game-over.mp3")
            pygame.mixer.music.play()
            pygame.time.wait(500)
            done = False

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = apple_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(1,screen_width -10),random.randint(1,screen_heigth -10))

    def update(self):
        global score,speedY,speedX,enemyY,enemyX

        if pygame.sprite.collide_mask(player,apple):
            self.rect.center = (random.randint(1,screen_width - 20),random.randint(1,screen_heigth - 20))
            score += 1
            pygame.mixer.music.load("img\\food_G1U6tlb.mp3")
            pygame.mixer.music.play()
            if score == 10 or score == 12 or score == 15 or score == 40 or score == 50 or score == 60 or score == 70 or score == 80:
                speedX += 1
                speedY += 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottomright = (200,200)

    def update(self):
        global done,enemy_number,enemy_last_update
        current_time = pygame.time.get_ticks()
        if current_time - enemy_last_update >= enemy_animation:
            enemy_number += 1
            enemy_last_update = current_time
            if enemy_number >= 5:
                enemy_number = 0
        
        self.rect.x += enemyX
        self.rect.y += enemyY
        

        if self.rect.y >= screen_heigth:
            self.rect.y = 0
            self.rect.y += enemyY

        elif self.rect.y <= 0:
            self.rect.y = screen_heigth
            self.rect.y -= enemyY
        
        elif self.rect.x >= screen_width:
            self.rect.x = 0
            self.rect.x += enemyX

        elif self.rect.x <= 0:
            self.rect.x = screen_width
            self.rect.x -= enemyX

        if pygame.sprite.collide_mask(enemy,player):
            pygame.mixer.music.load("img\\snake-dies-game-over.mp3")
            pygame.mixer.music.play()
            pygame.time.wait(500)
            done = False
            

player = Player(player_images[player_image_numbers])
player_sprites.add(player)

apple = Apple()
ball_sprites.add(apple)

enemy = Enemy(enemy_image_list[0])
enemy_sprites.add(enemy)


while done:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False



    player_sprites.update()
    ball_sprites.update()
    enemy_sprites.update()
    screen.blit(player_images[player_image_numbers],player)
    screen.blit(apple.image,apple)
    screen.blit(enemy_image_list[enemy_number],enemy)
    score_text = set_font.render(f"Score:{score}",True,(255,255,255))
    screen.blit(score_text,(10,10))
    clock.tick(60)
    pygame.display.update()
    pygame.display.flip()


pygame.quit()
