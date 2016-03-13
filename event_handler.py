import pygame
import time

yellow = (255, 255, 50)
red = (255, 10, 10)
white = (255, 255, 255)


class Events:
    pending_events = []
    finshed_events = []

    def __init__(self):
        return

    def update(self):
        for event in self.pending_events:
            event.update()
            if event.is_finished:
                self.finshed_events.insert(0, event)
                self.pending_events.remove(event)

    def draw(self, screen):
        n = 0
        for event in self.pending_events:
            event.draw(n, screen)
            n += 1

    def add_event(self, event):
        self.pending_events.insert(0, event)

class Event:
    text = ""
    start_time = 0
    end_time = 0
    is_finished = False

    def __init__(self, text_in, duration):
        self.text = text_in
        self.start_time = time.time()
        self.end_time = self.start_time + duration

    def update(self):
        self.is_finished = time.time() > self.end_time

    def draw(self, position, screen):
        font = pygame.font.SysFont("mono", 26)
        text = font.render(self.text, False, white)
        screen.blit(text, (500, 500-position*27))

        text = font.render(str(self.end_time-time.time()), False, white)
        screen.blit(text, (800, 500-position*27))


