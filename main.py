import pygame
from settings import Settings

pygame.init()

class Build:
    def __init__(self):
        #settings
        self.settings = Settings()
        #Screen Initialization
        pygame.display.set_caption(self.settings.name)
        self.screen = pygame.display.set_mode((self.settings.width,self.settings.width),pygame.FULLSCREEN)
        
        #Variables
        self.running = True
        self.clock = pygame.time.Clock()
        
    def run(self):
        while self.running:
            self.clock.tick(self.settings.refresh_rate) #60 Hz
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("[DEBUG]Exited: Quit")
                    self.running = False
                elif keys[pygame.K_ESCAPE]:
                    print("[DEBUG] Exited : Escape")
                    self.running = False
            
build = Build()
build.run()