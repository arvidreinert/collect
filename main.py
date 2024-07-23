from rectangle import *
from setup import *
class game():
    def __init__(self):
        self.running = True
        self.score = 0
        self.color_rects = []
        self.actual_color = self.make_random_base_color()
        self.gravity = 5
        self.color_rect = Rectangle((100,100),(width/2,height-120),self.actual_color,False)
        self.my_font = pygame.font.SysFont('Rage Italic', 100)
        self.text_surface = self.my_font.render(str(self.score), False, (0, 0, 0))


    def make_random_base_color(self):
        color = [0,0,0]
        color[random.choice([0,1,2])] = 250
        return tuple(color)

    def spawn_random_color_rect(self):
        color = self.make_random_base_color()
        color_rect = Rectangle((75,75),(random.randint(0, width),0),color,False)
        self.color_rects.append(color_rect)

    def run_game(self):
        counter = 0
        while self.running:
            clock.tick(30)
            #spawning rects
            if counter <= 50-self.score:
                counter += 1
            if counter == 50-self.score:
                for i in range(0,1+self.score):
                    self.spawn_random_color_rect()
                counter = 0
            for rect in self.color_rects:
                rect.change_position(0,self.gravity)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #here ia the button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            screen.fill((250,250,250))
            #rects.update(screen)
            for rect in self.color_rects:
                rect.update(screen)
            self.text_surface = self.my_font.render(f"{str(self.score)}", False, (0, 0, 0))
            screen.blit(self.text_surface, (width/2,120))
            self.color_rect.update(screen)
            pygame.display.update()

x = game()
x.run_game()