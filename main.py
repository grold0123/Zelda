import pygame
pygame.init()
pygame.display.set_mode((640,480),pygame.RESIZABLE)
#----------------------
"""CLASS"""
class Type:
    #----------------------
    """CLASS CONSTANSTS"""
    #----------------------
    """CLASS VARIABLES"""        
    #----------------------
    """CLASS METHODS"""    
    #----------------------
    """CLASS INSTANCE"""
    def __init__(self):
        pass
#----------------------
"""APPLICATION CLASS"""
class Application:	
    #-----------------------------
    """CLASS CONSTANTS"""
    RUNNING = 'RUNNING'
    QUIT = 'QUIT'
    START = 'START'
    DEBUG = 'DEBUG'
    #-----------------------------	
    """CLASS VARIABLES"""
    fps = 60    
    name = 'Zelda'
    clock = pygame.time.Clock()	
    display = pygame.display.get_surface()		
    #-----------------------------
    """CLASS METHODS"""
    @classmethod
    def debug(cls,information:str,pos:tuple[int,int]=(10,10)):        
        font = pygame.font.Font(None,20)
        debugSurface = font.render(information,True,'red','white')
        debugRect = debugSurface.get_rect(topleft = pos)
        Application.display.blit(debugSurface,debugRect)
    def gridLines():
        width,height = Application.display.get_size()				
        for y in range(height): # horizontal lines | y values increments 
            pygame.draw.line(Application.display,'white',(0,y*25),(width,y*25))
        for x in range(width): # vertical lines | x values increments 
            pygame.draw.line(Application.display,'white',(x*25,0),(x*25,height))					
    def startScreen():
        GAMETITLE = 'game title'
        GAMETITLE2 = 'game title 2'
        PROMPT = 'prompt'
        SURFACE = 'surface'
        RECT = 'rect'
        windowCenter = pygame.display.get_surface().get_rect().center
        bigFont = pygame.font.Font(None,110)
        mediumFont = pygame.font.Font(None,20)
        smallFont = pygame.font.Font(None,25)                
        texts = {
            GAMETITLE:{
                SURFACE:None,
                RECT:None
            },
            GAMETITLE2:{
                SURFACE:None,
                RECT:None,
            },
            PROMPT:{
                SURFACE:None,
                RECT:None,
            }
        }

        texts[GAMETITLE][SURFACE] = bigFont.render(Application.name,True,'red')
        texts[GAMETITLE][RECT] = texts[GAMETITLE][SURFACE].get_rect(center = windowCenter)

        texts[GAMETITLE2][SURFACE] = mediumFont.render('made in pygame',True,'white')
        texts[GAMETITLE2][RECT] = texts[GAMETITLE2][SURFACE].get_rect(center = windowCenter)

        texts[PROMPT][SURFACE] = smallFont.render('Press Enter to start game',True,'dark gray')
        texts[PROMPT][RECT] = texts[PROMPT][SURFACE].get_rect(center = windowCenter)
      
        texts[GAMETITLE][RECT].y -= 20
        texts[GAMETITLE2][RECT].y += 20
        texts[PROMPT][RECT].y += 90

        Application.display.blits([
            (texts[GAMETITLE][SURFACE],texts[GAMETITLE][RECT]),
            (texts[GAMETITLE2][SURFACE],texts[GAMETITLE2][RECT]),
            (texts[PROMPT][SURFACE],texts[PROMPT][RECT])
        ])
    #-----------------------------
    """CLASS INSTANCE"""
    def __init__(self):		  		
        pygame.display.set_caption('Zelda')		
        self.state = Application.START
        self.systemMsg = ''
    def pollevent(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT : self.state = Application.QUIT
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_RETURN: 
                            if self.state == Application.START: self.state = Application.RUNNING
                        case pygame.K_F1: 
                            if self.state == Application.DEBUG: self.state = Application.RUNNING
                            elif self.state != Application.DEBUG and self.state == Application.RUNNING:
                                self.state = Application.DEBUG
                                self.systemMsg = 'Entered DEBUG mode'
                case pygame.VIDEORESIZE: Application.display = pygame.display.set_mode(event.size,pygame.RESIZABLE)
    def update(self):
        while True:
            self.pollevent()
            match self.state:
                case Application.QUIT: break
                case Application.START:
                    Application.display.fill('black')
                    Application.startScreen()
                case Application.RUNNING:                    			
                    Application.display.fill('white')
                case Application.DEBUG:
                    Application.display.fill('blue')
                    Application.gridLines()
                    Application.debug(self.systemMsg)
            pygame.display.flip()			
#----------------------
"""MAIN FUNCTION"""
def main():
    game = Application()
    game.update()
    pygame.quit()
#----------------------
if __name__ == '__main__':
    main()