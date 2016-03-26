import pygame
import time

yellow = (255, 255, 50)
red = (255, 10, 10)
white = (255, 255, 255)


class Events:
    pending_events = []
    finished_events = []

    def __init__(self):
        return

    def update(self):
        for event in self.pending_events:
            event.update()
            if event.is_finished:
                self.finished_events.insert(0, event)
                self.pending_events.remove(event)

    def draw(self, screen):
        n = 0
        for event in self.pending_events:
            event.draw(n, screen)
            n += 1

    def add_event(self, event):
        self.pending_events.insert(0, event)


class Event:
    def __init__(self, text, duration):
        self.text = text
        self.start_time = time.time()
        self.end_time = self.start_time + duration
        self.is_finished = False
        self.time_left = duration

    def update(self):
        self.time_left = self.end_time - time.time()
        self.is_finished = self.time_left <= 0

    def draw(self, position, screen):
        font = pygame.font.SysFont("mono", 26)
        text = font.render(self.text, False, white)
        screen.blit(text, (500, 500-position*27))

        text = font.render("{:10.2f}".format(self.time_left), False, white)
        screen.blit(text, (800, 500-position*27))


