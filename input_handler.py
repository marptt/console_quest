import pygame
import main

yellow = (255, 255, 50)
red = (255, 10, 10)
white = (255, 255, 255)
text_size = 26
line_distance = 1
console_height = height = 1070-(text_size+line_distance)


def is_character(char):
    return char < 256


class Console:
    def __init__(self, game_in):
        self.current_line = ""
        self.line_queue = []
        self.line_history = []
        self.quit = False
        self.game = game_in

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.line_queue.insert(0, self.current_line)
                    self.current_line = ""
                elif event.key == pygame.K_ESCAPE:
                    self.quit = True
                elif event.key == pygame.K_BACKSPACE:
                    self.current_line = self.current_line[:-1]
                elif is_character(event.key):
                    self.current_line += chr(event.key)
        while self.line_queue:
            newline = self.line_queue.pop()
            self.line_history.insert(0, Line(newline, yellow))
            self.game.resolve_line(newline)

    def draw(self, screen):
        font = pygame.font.SysFont("mono", text_size)
        text = font.render(">" + self.current_line, False, white)
        screen.blit(text, (10, height))

        n = 0
        for line in self.line_history:
            n += 1
            line.draw(n, screen)

    def output_text(self, text, color):
        self.line_history.insert(0, Line(text, color))


class Line:
    color = ()
    text = ""

    def __init__(self, text_in, color_in):
        self.color = color_in
        self.text = text_in

    def draw(self, n, screen):
        font = pygame.font.SysFont("mono", text_size)
        s = font.render(self.text , False, self.color)
        screen.blit(s, (10, console_height-(text_size+line_distance)*n))
