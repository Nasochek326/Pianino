import pygame
import setting
import note
import Menu
import pygame.freetype
pygame.init()


class Game:
    def __init__(self):
        self.stop = True
        self.okno = pygame.display.set_mode(setting.SIZE)
        self.ob = pygame.time.Clock()
        self.mus = note.Musik(setting.CHRISTMAS_TREE_NOTES, setting.CHRISTMAS_TREE_DURATION, self.okno)
        self.truenots = []
        self.winorlos = ''
        self.text = pygame.freetype.Font('Sounds/Softie Cyr.ttf', 45)
        self.kolnotstrue = 0
        self.ostatoknots = len(self.mus.numnot)
        self.ob_menu = Menu.Menu(self)
        self.proverka = 0
        self.lorw = ''

    def risovka(self):
        x = setting.SHIRINAPALOS
        self.okno.fill([250, 250, 250])
        for w in range(0, setting.KOLPALOS):
            pygame.draw.line(self.okno, [100, 100, 100], [x, 0], [x, setting.SIZE[1]])
            x = x + setting.SHIRINAPALOS
        self.mus.risovka(self.okno)
        self.text.render_to(self.okno, [setting.SIZE[0] - 380, setting.SIZE[1] - 50], 'Number' + ' : ' + str(self.kolnotstrue))
        self.text.render_to(self.okno, [setting.SIZE[0] - 380, setting.SIZE[1] - 90], 'Remains' + ' : ' + str(self.ostatoknots))
        if self.winorlos != '':
            self.text.render_to(self.okno, [setting.SIZE[0] - 200, setting.SIZE[0] - 300], self.winorlos)

    def proverka_events(self):
        events = pygame.event.get()
        for event in events:
            if pygame.QUIT == event.type:
                self.stop = False
            elif pygame.MOUSEBUTTONDOWN == event.type:
                for w in self.mus.nots:
                    if w.xitboks.collidepoint(event.pos) == True and w.nagata == 0:
                        w.click()
                        self.truenots.append(w)
                        self.kolnotstrue += 1
                        self.ostatoknots -= 1
            elif pygame.KEYDOWN == event.type and self.winorlos != '':
                if event.key == pygame.K_m:
                    self.proverka = 0

    def logik(self):
        if len(self.mus.numnot) != len(self.mus.nots):
            self.mus.spawnnota()
        elif len(self.mus.numnot) == len(self.mus.nots) and self.mus.nots[-1].xitboks.y > setting.SIZE[1]:
            if len(self.truenots) != len(self.mus.nots):
                self.winorlos = 'loser'
            elif len(self.truenots) == len(self.mus.nots):
                self.winorlos = 'winer'
        self.mus.dawn()

    def start_game(self):

        while self.stop == True:
            if self.proverka == 0:
                self.ob_menu.risovka()
                self.ob_menu.events()
            else:
                self.proverka_events()
                self.logik()
                self.risovka()
            self.ob.tick(50)
            pygame.display.update()


ob = Game()
ob.start_game()














