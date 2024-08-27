import pygame
import setting
import random
import pygame.freetype
pygame.init()


class Note:
    image_nate_long = pygame.image.load('long_tile.png')
    rasmer = image_nate_long.get_size()
    image_nate_long = pygame.transform.scale(image_nate_long, [setting.SHIRINAPALOS, rasmer[1]])
    image_nate_long_pressed = pygame.image.load('long_tile_pressed.png')
    rasmer = image_nate_long_pressed.get_size()
    image_nate_long_pressed = pygame.transform.scale(image_nate_long_pressed, [setting.SHIRINAPALOS, rasmer[1]])
    image_nate_short = pygame.image.load('short_tile.png')
    rasmer = image_nate_short.get_size()
    image_nate_short = pygame.transform.scale(image_nate_short, [setting.SHIRINAPALOS, rasmer[1]])
    image_nate_short_pressed = pygame.image.load('short_tile_pressed.png')
    rasmer = image_nate_short_pressed.get_size()
    image_nate_short_pressed = pygame.transform.scale(image_nate_short_pressed, [setting.SHIRINAPALOS, rasmer[1]])

    def __init__(self, x, y, long_short, name_note):
        if long_short == 1:
            self.image = Note.image_nate_short
        elif long_short == 2:
            self.image = Note.image_nate_long
        self.xitboks = pygame.rect.Rect([x, y], self.image.get_size())
        self.long_short = long_short
        self.name = name_note
        self.random = random.randint(0, setting.KOLPALOS)
        self.ram = random.randint(0, setting.KOLPALOS - 1)
        self.xitboks.x = self.xitboks.x * self.ram
        self.musik = pygame.mixer.Sound('Sounds/' + self.name + '.ogg')
        self.musik.set_volume(0.09)
        self.text = pygame.freetype.Font('Sounds/Softie Cyr.ttf', 45)
        self.nagata = 0

    def risovka(self, okno):
        okno.blit(self.image, self.xitboks)
        self.text.render_to(okno, [self.xitboks.centerx - 25, self.xitboks.centery - 20], self.name)

    def dawn(self):
        self.xitboks.y = self.xitboks.y + 10

    def click(self):
        self.nagata = 1
        if self.long_short == 1:
            self.image = Note.image_nate_short_pressed
        elif self.long_short == 2:
            self.image = Note.image_nate_long_pressed
        self.musik.play()


class Musik:
    def __init__(self, numnot, dlinnot, okno):
        self.numnot = numnot
        self.dlnnot = dlinnot
        self.nots = []
        self.timeril = 0
        self.timesas = 0
        self.kol = 0
        self.okno = okno

    def spawnnota(self):
        if self.nots != [] and self.nots[-1].long_short == 1:
            timespawnnot = 800
        else:
            timespawnnot = 1500
        if self.timeril - self.timesas > timespawnnot:
            note = Note(setting.SHIRINAPALOS, 0, self.dlnnot[self.kol], self.numnot[self.kol])
            self.nots.append(note)
            self.kol += 1
            self.timesas = pygame.time.get_ticks()
        self.timeril = pygame.time.get_ticks()

    def risovka(self, okno):
        for w in self.nots:
            w.risovka(okno)

    def dawn(self):
        for w in self.nots:
            w.dawn()



