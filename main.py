import pygame
import input_handler
import event_handler
import game_world

class Game:
    pygame.init()

    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.console = input_handler.Console(self)
        self.events = event_handler.Events()
        pygame.display.toggle_fullscreen()

        self.world = game_world.World(self.console)
        self.player = self.world.player

    def run(self):
        while not self.console.quit:
            self.console.update()
            self.events.update()
            for event in self.events.finshed_events:
                self.resolve_event(event)
            self.events.finshed_events = []

            self.screen.fill((0, 0, 0))

            self.events.draw(self.screen)
            self.console.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

    def resolve_line(self, line):
        self.player.resolve_line(line)

    def resolve_event(self, event):
        self.world.resolve_event(event)

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()


