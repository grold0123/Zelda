import pygame 
pygame.init()
pygame.display.set_mode((640,480),pygame.RESIZABLE)

#--------------------------------------------------
"""SURFACE CLASS"""
class Surface:
    #----------------------------------------------
    """VARIABLES"""
    display = pygame.display.get_surface()
    testRock = pygame.image.load('assets/graphics/test/rock.png')
    testPlayer = pygame.image.load('assets/graphics/test/player.png')
#--------------------------------------------------
"""TILE CLASS"""
class Tile(pygame.sprite.Sprite):    
    def __init__(self,pos,*groups):
        super().__init__(*groups)
        self.image = Surface.testRock
        self.rect = self.image.get_rect(topleft = pos)
#--------------------------------------------------
"""PLAYER CLASS"""
class Player(pygame.sprite.Sprite):
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'
    def __init__(self,pos,*groups):
        super().__init__(*groups)
        self.image = Surface.testPlayer
        self.rect = self.image.get_rect(topleft = pos)        
        self.speed = 10      
    def input(self):
        keyState = pygame.key.get_pressed()
        self.direction = pygame.math.Vector2()
        if keyState[pygame.K_UP]: self.direction.y = -1
        elif keyState[pygame.K_DOWN]: self.direction.y = 1
        if keyState[pygame.K_RIGHT]: self.direction.x = 1
        elif keyState[pygame.K_LEFT]: self.direction.x = -1
    def move(self):
        if self.direction.magnitude() != 0: self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * self.speed 
        self.collision(Player.HORIZONTAL)
        self.rect.y += self.direction.y * self.speed 
        self.collision(Player.VERTICAL)
    def collision(self,direction):
        if direction == Player.HORIZONTAL:
            for sprite in Level.obstacleSprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: self.rect.right = sprite.rect.left
                    elif self.direction.x < 0: self.rect.left = sprite.rect.right
        elif direction == Player.VERTICAL:
            for sprite in Level.obstacleSprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: self.rect.top = sprite.rect.bottom
    def update(self):
        self.input()
        self.move()
#--------------------------------------------------
"""LEVEL CLASS"""
class Level:
    tileSize = 64
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
    visibleSprites = pygame.sprite.Group()
    obstacleSprites = pygame.sprite.Group()
    player = None
    def __init__(self):
        self.createMap()
    def createMap(self):
        for rowIndex,row in enumerate(Level.worldMap):
            for colIndex,col in enumerate(row):
                x = colIndex * Level.tileSize
                y = rowIndex * Level.tileSize
                match col:
                    case 'x': Tile((x,y),[Level.visibleSprites,Level.obstacleSprites])
                    case 'p': 
                       Level.player = Player((x,y),[Level.visibleSprites])

    def update(self): 
        Level.visibleSprites.draw(Surface.display)
        Level.visibleSprites.update()
        Application.debug(str(Level.player.direction))
#--------------------------------------------------
"""APPLICATION CLASS"""
class Application:
    #----------------------------------------------
    """CONSTANTS"""
    RUNNING = 'running'
    QUIT = 'quit'
    START = 'start'
    DEBUG = 'debug'
    #----------------------------------------------
    """VARIABLES"""
    clock = pygame.time.Clock()
    name = 'Zelda'
    deltaTime = 0
    #----------------------------------------------
    """METHODS"""
    @classmethod
    def debug(cls,information,pos:tuple[int,int]=(20,20)):
        font = pygame.font.Font(None,25)
        debugSurface = font.render(information,True,'red','white')
        debugRect = debugSurface.get_rect(topleft = pos)
        Surface.display.blit(debugSurface,debugRect)
    @classmethod
    def startScreen(cls):
        center = Surface.display.get_rect().center
        afont = pygame.font.Font(None,110)
        bfont = pygame.font.Font(None,20)
        cfont = pygame.font.Font(None,25)

        aSurface = afont.render(Application.name,True,'Red')
        aRect = aSurface.get_rect(center = center )

        bSurface = bfont.render('made in pygame',True,'white')
        bRect = bSurface.get_rect(center = center )

        cSurface = cfont.render('Press Enter to start game',True,'light gray')
        cRect = cSurface.get_rect(center = center )

        aRect.y += -10
        bRect.y += 25
        cRect.y += 60

        Surface.display.blits([
            (aSurface,aRect),
            (bSurface,bRect),
            (cSurface,cRect)
        ])
    @classmethod 
    def drawGrid(cls):
        offset = 25
        width,height = Surface.display.get_size()
        for x in range(width):
            pygame.draw.line(Surface.display,'white',(x*offset,0),(x*offset,height))
        for y in range(height):
            pygame.draw.line(Surface.display,'white',(0,y*offset),(width,y*offset))
    #----------------------------------------------
    """INSTANCE"""
    def __init__(self):
        self.state = Application.START
        self.sysMsg = ''        
        pygame.display.set_caption(f"{Application.name} | {self.state}")
    def handleEvents(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT: self.state = Application.QUIT
                case pygame.KEYDOWN : 
                    match event.key:
                        case pygame.K_RETURN:
                            if self.state == Application.START: 
                                self.state = Application.RUNNING
                                pygame.display.set_caption(f"{Application.name} | {self.state}")
                        case pygame.K_F1:
                            if self.state != Application.DEBUG and self.state == Application.RUNNING:
                                self.state = Application.DEBUG
                                pygame.display.set_caption(f"{Application.name} | {self.state}")
                                self.sysMsg = 'Entered DEBUG mode'
                            elif self.state == Application.DEBUG:
                                self.state = Application.RUNNING
                                pygame.display.set_caption(f"{Application.name} | {self.state}")
                                self.sysMsg = ''
    def update(self):
        level = Level()
        while True:
            
            self.handleEvents()
            match self.state:
                case Application.QUIT:break 
                case Application.START: 
                    Surface.display.fill('black')
                    Application.startScreen()
                case Application.RUNNING : 
                    Surface.display.fill('white')                    
                    level.update()                    
                case Application.DEBUG:
                    Surface.display.fill('blue')
                    Application.drawGrid()
                    Application.debug(self.sysMsg)
            pygame.display.flip()
            Application.clock.tick(60)
#--------------------------------------------------
"""MAIN FUNCTION"""
def main():
    game = Application()
    game.update()
    pygame.quit()
#--------------------------------------------------
if __name__ == "__main__":
    main()