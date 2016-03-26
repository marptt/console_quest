import pygame
import main

yellow = (255, 255, 50)
red = (255, 10, 10)
white = (255, 255, 255)
text_size = 26
line_distance = 1
console_height = height = 1070-(text_size+line_distance)
console_width_characters = 28

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
            n += line.draw(n, screen)

    def output_text(self, text, color):
        self.line_history.insert(0, Line(text, color))


class Line:
    color = ()
    text = ""

    def __init__(self, text_in, color_in):
        self.color = color_in
        self.text = text_in

    def draw(self, n, screen):
        lines = line_break(self.text)

        line_count = len(lines)
        for line in lines:
            font = pygame.font.SysFont("mono", text_size)
            s = font.render(line, False, self.color)
            screen.blit(s, (10, console_height-(text_size+line_distance)*(n+line_count)))
            line_count -= 1
        return len(lines)


def line_break(text):
    return_lines = []
    lines = text.split()
    current_line = ""
    current_length = 0
    while lines:
        line = lines.pop(0)
        if len(line) > console_width_characters:
            line_first_half = line[0:console_width_characters - current_length - 1] + "-"
            line_second_half = line[console_width_characters - current_length - 1: -1]
            lines.insert(0, line_second_half)
            current_line += line_first_half
            return_lines.append(current_line)
            current_line = ""
            current_length = 0
        elif len(line) + current_length > console_width_characters:
            lines.insert(0, line)
            return_lines.append(current_line)
            current_line = ""
            current_length = 0
        else:
            current_line += line + " "
            current_length += len(line)

    if current_line != "":
        return_lines.append(current_line)
    return return_lines
