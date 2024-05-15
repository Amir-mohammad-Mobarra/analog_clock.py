import pygame
from math import radians, sin, cos
from datetime import datetime


class Clock:
    def __init__(self):
        self.height = 650
        self.width = 650
        self.white = (255, 255, 255)
        self.blue = (34, 79, 228)
        self.FPS = 60
        self.center = (self.width // 2, self.height // 2)
        self.clock_radius = self.width // 2

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Analog clock')
        self.clock = pygame.time.Clock()

    def numbers(self, num, size, position):
        font = pygame.font.SysFont('Calibri', size, True, False)
        text = font.render(str(num), True, self.white)
        text_rect = text.get_rect(center=position)
        self.screen.blit(text, text_rect)

    def polar_to_cartesian(self, r, theta):
        x = r * sin(radians(theta))
        y = r * cos(radians(theta))
        return self.width // 2 + x, self.height // 2 - y

    def draw_circle(self, screen):
        pygame.draw.circle(screen, self.white, self.center, self.clock_radius - 10, 5)

        pygame.draw.circle(screen, self.white, self.center, 10)

        for num in range(1, 13):
            self.numbers(num, 60, self.polar_to_cartesian(self.clock_radius - 80, num * 30))

        for num in range(0, 360, 6):
            if num % 5:
                pygame.draw.line(screen, self.white, self.polar_to_cartesian(self.clock_radius - 15, num),
                                 self.polar_to_cartesian(self.clock_radius - 30, num), 2)
            else:
                pygame.draw.line(screen, self.white, self.polar_to_cartesian(self.clock_radius - 15, num),
                                 self.polar_to_cartesian(self.clock_radius - 35, num), 6)

    def draw_clock_hand(self):
        current_time = datetime.now()
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour
        # hour
        r = self.clock_radius - 180
        theta = (hour + minute/60 + second/3600) * (360/12)
        pygame.draw.line(self.screen, self.white, self.center,
                         self.polar_to_cartesian(r, theta), 14)
        # minute
        r = self.clock_radius - 150
        theta = (minute + second/60) * (360/12)
        pygame.draw.line(self.screen, self.white, self.center,
                         self.polar_to_cartesian(r, theta), 14)
        # second
        r = self.clock_radius - 110
        theta = second * (360/12)
        pygame.draw.line(self.screen, self.white, self.center,
                         self.polar_to_cartesian(r, theta), 14)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.screen.fill(self.blue)
            self.draw_circle(self.screen)
            self.draw_clock_hand()

            pygame.display.update()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    my_clock = Clock()
    my_clock.run()
