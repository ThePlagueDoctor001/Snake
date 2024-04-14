import pygame
import random

class GameObject:
    def __init__(self):
        self.position = (400, 300)  
        self.body_color = None

    def draw(self, screen):
        pass

class Apple(GameObject):
    def __init__(self):
        super().__init__()
        self.body_color = (255, 0, 0)  
        self.randomize_position()

    def randomize_position(self):
        x = random.randint(0, 800)  
        y = random.randint(0, 600)  
        self.position = (x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, self.body_color, self.position, 10)  

class Snake(GameObject):
    def __init__(self):
        super().__init__()
        self.length = 1
        self.positions = [self.position]  
        self.direction = "right"  
        self.next_direction = None
        self.body_color = (0, 255, 0)  

    def update_direction(self, key):
        if key == pygame.K_UP and self.direction != "down":
            self.next_direction = "up"
        elif key == pygame.K_DOWN and self.direction != "up":
            self.next_direction = "down"
        elif key == pygame.K_LEFT and self.direction != "right":
            self.next_direction = "left"
        elif key == pygame.K_RIGHT and self.direction != "left":
            self.next_direction = "right"

    def move(self):
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

        x, y = self.positions[0]  

        if self.direction == "up":
            y -= 20
        elif self.direction == "down":
            y += 20
        elif self.direction == "left":
            x -= 20
        elif self.direction == "right":
            x += 20

        self.positions.insert(0, (x, y))  

        if len(self.positions) > self.length:
            self.positions.pop()  

    def draw(self, screen):
        for pos in self.positions:
            pygame.draw.rect(screen, self.body_color, (pos[0], pos[1], 20, 20))  

    def get_head_position(self):
        return self.positions[0]

    def reset(self):
        self.length = 1
        self.positions = [self.position]
        self.direction = "right"

def handle_keys(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            snake.update_direction(event.key)

def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple()

    while True:
        screen.fill((0, 0, 0))

        handle_keys(snake)
        snake.move()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()

        if len(snake.positions) != len(set(snake.positions)):
            snake.reset()

        snake.draw(screen)
        apple.draw(screen)

        pygame.display.update()
        clock.tick(20)

if __name__ == '__main__':
    main()
