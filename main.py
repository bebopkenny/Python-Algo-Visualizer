import pygame 
import random
pygame.init()

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    BLUE = 70,130,180
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE
    
    SIDE_PAD = 100
    TOP_PAD = 150
    
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)
        
    def set_list(self, lst):
        self.lst = lst
        self.min_val = max(lst)        
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst)) # width of the block
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val)) # height of the block
        self.start_x = self.SIDE_PAD // 2
        
def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val) # number in this range
        lst.append(val)
    
    return lst
    
def main():
    clock = pygame.time.Clock()
    run = True
    
    n = 50
    min_val = 0
    max_val = 100
    
    lst = generate_starting_list(n, min_val, max)
    draw_info = DrawInformation(800, 600, lst)
    
    while run:
         clock.tick(60) # FPS
         
         pygame.display.update()
         
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run = False
    pygame.quit()
    
if __name__ == "__main__":
    main()