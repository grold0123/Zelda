import pygame
pygame.init()
pygame.display.set_mode((1280,720),pygame.RESIZABLE)


#----------------------
""""""
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
	tilesize = 64
	name = 'Zelda'
	clock = pygame.time.Clock()	
	display = pygame.display.get_surface()		
	#-----------------------------
	"""CLASS METHODS"""
	@classmethod
	def debug(cls,information:str,pos:tuple[int,int]=(10,10)):
		font = pygame.font.Font(None,35)
		debugSurface = font.render(information,True,'red')
		debugRect = debugSurface.get_rect(topleft = pos)
		Application.display.blit(debugSurface,debugRect)
	def createGridLines(cls):
		width,height = Application.display.get_size()				
		for y in range(height): # horizontal lines | y values increments 
			pygame.draw.line(Application.display,'white',(0,y),(width,y))
		for x in range(width): # vertical lines | x values increments 
			pygame.draw.line(Application.display,'white',(x,0),(x,height))					
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
						case pygame.K_F1: self.state = Application.DEBUG
							
	def update(self):
		while True:
			self.pollevent()
			match self.state:
				case Application.QUIT: break
				case Application.START:
					Application.display.fill('white')
				case Application.RUNNING:
					Application.display.fill('black')			
				case Application.DEBUG:
					Application.display.fill('blue')
					Application.createGridLines()
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