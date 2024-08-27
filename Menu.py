import pygame
import pygame.freetype
import note
import setting


class Menu:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('menu.png')
        self.ob_texts = pygame.freetype.Font('Sounds/Softie Cyr.ttf', 45)
        self.kolor1 = [0, 250, 0]
        self.kolor2 = [250, 0, 0]
        self.kolor3 = [250, 0, 0]
        self.proverka = 1
        self.mus = note.Musik(setting.CHRISTMAS_TREE_NOTES, setting.CHRISTMAS_TREE_DURATION, self.game.okno)

    def risovka(self):
        self.game.okno.blit(self.image, [0, 0])
        self.ob_texts.render_to(self.game.okno, [100, 200], 'Tree', self.kolor1)
        self.ob_texts.render_to(self.game.okno, [100, 250], 'Bereza', self.kolor2)
        self.ob_texts.render_to(self.game.okno, [100, 300], 'Dobroe ytro', self.kolor3)

    def events(self):
        events = pygame.event.get()
        for event in events:
            if pygame.QUIT == event.type:
                self.game.stop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and self.proverka == 1:
                    self.kolor1 = [250, 0, 0]
                    self.kolor2 = [0, 250, 0]
                    self.proverka = 2
                elif event.key == pygame.K_DOWN and self.proverka == 2:
                    self.kolor2 = [250, 0, 0]
                    self.kolor3 = [0, 250, 0]
                    self.proverka = 3
                elif event.key == pygame.K_UP and self.proverka == 2:
                    self.kolor1 = [0, 250, 0]
                    self.kolor2 = [250, 0, 0]
                    self.proverka = 1
                elif event.key == pygame.K_UP and self.proverka == 3:
                    self.kolor2 = [0, 250, 0]
                    self.kolor3 = [250, 0, 0]
                    self.proverka = 2
                elif event.key == pygame.K_RETURN:
                    self.game.proverka = 1
                    self.game.winorlos = ''
                    self.game.kolnotstrue = 0
                    if self.proverka == 1:
                        self.game.mus = note.Musik(setting.CHRISTMAS_TREE_NOTES, setting.CHRISTMAS_TREE_DURATION, self.game.okno)
                    elif self.proverka == 2:
                        self.game.mus = note.Musik(setting.BIRCH_NOTES, setting.BIRCH_DURATION, self.game.okno)
                    elif self.proverka == 3:
                        self.game.mus = note.Musik(setting.MORNING_NOTES, setting.MORNING_DURATION, self.game.okno)
                    self.game.ostatoknots = len(self.mus.numnot)


























































































