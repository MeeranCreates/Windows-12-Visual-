import pygame

pygame.init()

class Build:
    def __init__(self):
        #Screen Initialization
        pygame.display.set_caption("Windows:12 (Visual Edition)")
        self.screen = pygame.display.set_mode((2560, 1440),pygame.FULLSCREEN)
        
        #Variables
        self.running = True
        self.clock = pygame.time.Clock()
        
    def run(self):
        while self.running:
            self.clock.tick(60) #60 Hz
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