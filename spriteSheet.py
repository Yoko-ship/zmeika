import pygame

class SpriteSheet():
    def __init__(self,image):
        self.sheet = image
    
    def get_image(self,frame,row,width,height,scale,color):
        image = pygame.Surface((width,height)).convert_alpha()
        x = frame * width
        y = row * height
        image.blit(self.sheet,(0,0),(x,y,width,height)) # Frame (тоесть какую картинку достать можно настроить,если width то надо frame умножать на width
        # если height то умножаем на height и так нужно точные размеры передавать)
        image = pygame.transform.scale(image,(width * scale, height * scale)) # Увеличиваем размер картинки
        image.set_colorkey(color) # Убираем черный фон
        return image