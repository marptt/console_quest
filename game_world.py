import pygame
import time
import event_handler
import Room
import random

yellow = (255, 255, 50)
red = (255, 10, 10)
white = (255, 255, 255)



class World:
    def __init__(self, console_in):
        self.room_factory = Room.RoomFactory()
        self.rooms = [self.room_factory.make_room(), self.room_factory.make_room(), self.room_factory.make_room(), self.room_factory.make_room()]
        self.events = event_handler.Events()
        self.player = Player(self, self.rooms[0])
        self.console = console_in

    def resolve_event(self, event):
        self.console.output_text(event.text, red)
        return

    def add_event(self, event):
        self.events.add_event(event)


class Player:
    def __init__(self, world, room):
        self.room = room
        self.world = world
        return

    def resolve_line(self, line):
        if line == "lol":
            event = event_handler.Event("lol indeed", 5)
            self.world.add_event(event)
        if line == "inspect room":
            self.world.console.output_text(self.room.inspect(), white)
        if line == "go west":
            n = random.randint(0,3)
            self.room = self.world.rooms[n]
            self.world.console.output_text(self.room.inspect(), white)
