import pygame
import math

# Initialize pygame and create window
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Earth and Moon Simulation")

# Define colors
white = (255, 255, 255)
blue = (50, 153, 213)
grey = (192, 192, 192)

# Initialize positions and sizes
earth_x, earth_y = 350, 250
moon_x, moon_y = 400, 250
earth_radius = 50
moon_radius = 20

# Main game loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the Earth
    pygame.draw.circle(screen, blue, (earth_x, earth_y), earth_radius)

    # Draw the Moon
    pygame.draw.circle(screen, grey, (moon_x, moon_y), moon_radius)

    # Update the Moon's position
    moon_x += 1
    moon_y = 250 + math.sin(moon_x / 10) * 50

    # Update the screen
    pygame.display.flip()

pygame.quit()