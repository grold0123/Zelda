import pygame,pathlib
pygame.init()
pygame.display.set_mode((640,480),pygame.RESIZABLE)
class Level:
    #   ---------------
    #   CLASS CONSTANTS
    #   ---------------
    STONE = 'x'
    PLAYER = 'p'
    #   ---------------
    #   CLASS VARIABLES
    #   ---------------
    visibleSprites = []
    obstacleSprites = []
    worldMap = [
        ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
    ]
    #   ---------------
    #   CLASS METHODS
    #   ---------------
    @classmethod
    def draw(cls,display:pygame.Surface):
        args = [
            (obj.image,obj.rect)
            for obj in cls.visibleSprites
        ]
        display.blits(args)
    @classmethod
    def createMap(cls):
        for rowIndex,row in enumerate(cls.worldMap):
            for colIndex,element in enumerate(row):
                x = colIndex * GameObject.tileSize
                y = rowIndex * GameObject.tileSize
                pos = x,y
                if element == 'x':
                    Tile(pos,[Level.visibleSprites,Level.obstacleSprites])
                if element == 'p':
                    Player(pos,[Level.visibleSprites])
    #   ---------------
    #   CLASS INSTANCE
    #   ---------------
    def __init__(self):
        Level.createMap()
class Helpers:
    def loadSurfaces(fileDir:str):
        dirPath = pathlib.Path(fileDir)
        l = []
        for path in dirPath.glob('*.png'):
            surface = pygame.image.load(path).convert_alpha()
            l.append(surface)
        return l
class Assets:            
    class Surface:       
        class Objects:            
            grasses = Helpers.loadSurfaces('assets/graphics/grass')
        class Monsters:
            class Bamboo:
                attack = Helpers.loadSurfaces('assets/graphics/bamboo/attack')
                idle = Helpers.loadSurfaces('assets/graphics/bamboo/idle'),
                move = Helpers.loadSurfaces('assets/graphics/bamboo/move'),
            class Racoon:
                attack = Helpers.loadSurfaces('assets/graphics/racoon/attack')                                    
                idle = Helpers.loadSurfaces('assets/graphics/racoon/idle')
                move = Helpers.loadSurfaces('assets/graphics/racoon/move')
            class Spirit:
                attack = Helpers.loadSurfaces('assets/graphics/spirit/attack')                                    
                idle = Helpers.loadSurfaces('assets/graphics/spirit/idle')
                move = Helpers.loadSurfaces('assets/graphics/spirit/move')
            class Squid:
                attack = Helpers.loadSurfaces('assets/graphics/squid/attack')                                    
                idle = Helpers.loadSurfaces('assets/graphics/squid/idle')
                move = Helpers.loadSurfaces('assets/graphics/squid/move')

    def __init__(self):
        pass
class GameObject:        
    #   ---------------
    #   CLASS VARIABLES
    #   ---------------
    tileSize = 64
    #   ---------------
    #   ---------------
    #   CLASS METHODS
    #   ---------------    
    #   CLASS INSTANCE
    #   ---------------
    def __init__(self,pos,group:list):
        self.image = pygame.Surface((30,30))
        self.rect = self.image.get_frect(topleft = pos)
        if Level.visibleSprites in group:
            Level.visibleSprites.append(self)
        if Level.obstacleSprites in group:
            Level.obstacleSprites.append(self)    
    
class Player(GameObject):
    def __init__(self, pos, group=[Level.visibleSprites]):
        super().__init__(pos, group)
        self.image = pygame.image.load('assets/graphics/test/player.png')
        self.rect = self.image.get_rect(topleft = pos)
class Tile(GameObject):
    def __init__(self, pos, group=[Level.visibleSprites,Level.obstacleSprites]):
        super().__init__(pos, group)
        self.image = pygame.image.load('assets/graphics/test/rock.png')
        self.rect = self.image.get_rect(topleft = pos)
class Application:
    #   -----------------
    #   CLASS CONSTANTS
    #   -----------------
    RUNNING = 'running'
    QUIT = 'quit'
    START = 'start'
    #   -----------------
    #   CLASS VARIABLES
    #   -----------------
    display = pygame.display.get_surface()
    clock = pygame.time.Clock()    
    name = 'ZELDA'
    #   -----------------
    #   CLASS METHODS
    #   -----------------
    @classmethod
    def createStartScreen(cls):
        IMAGE = 'image'
        RECT = 'rect'
        temp = pygame.Surface(pygame.display.get_window_size(),pygame.SRCALPHA)
        bigFont = pygame.font.Font(None,120)
        smallFont = pygame.font.Font(None,30)        
        smalleseFont = pygame.font.Font(None,20)        
        gameTitle = {}
        gameTitle2 = {}
        promptText = {}
        gameTitle[IMAGE] = bigFont.render('ZELDA',True,'RED')
        gameTitle[RECT] = gameTitle[IMAGE].get_rect(center = temp.get_rect().center)
        gameTitle[RECT].y -= 20
        gameTitle2[IMAGE] = smallFont.render('made in pygame',True,'white')
        gameTitle2[RECT] = gameTitle2[IMAGE].get_rect(center = temp.get_rect().center)
        gameTitle2[RECT].y += 20
        promptText[IMAGE] = smalleseFont.render('Press Enter to start game',True,'dark gray')
        promptText[RECT] = promptText[IMAGE].get_rect(center = temp.get_rect().center)
        promptText[RECT].y += 100
        temp.blits([
            (gameTitle[IMAGE],gameTitle[RECT]),
            (gameTitle2[IMAGE],gameTitle2[RECT]),
            (promptText[IMAGE],promptText[RECT])
            ])
        return temp
    @classmethod
    def debugScreen(cls):
        pass 
    #   -----------------
    #   CLASS INSTANCE
    #   -----------------
    def __init__(self):
        pygame.display.set_caption(Application.name)
        self.level = Level()
        self.state = Application.START
    def update(self):
        while True:
            self.pollEvent()    
            match self.state:
                case Application.START : 
                    Application.display.fill('black')
                    Application.display.blit(Application.createStartScreen(),(0,0))
                case Application.RUNNING: 
                    Application.display.fill('white')
                    Level.draw(Application.display)
                case Application.QUIT: break            
            
            pygame.display.flip()
    def pollEvent(self):
        for event in pygame.event.get():
            match event.type :
                case pygame.QUIT: self.state = Application.QUIT
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_RETURN:
                            if self.state == Application.START: self.state = Application.RUNNING
                        
if __name__ == "__main__":
    game = Application()
    game.update()
    pygame.quit()