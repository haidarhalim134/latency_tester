import pygame
import time

# Initialize pygame
pygame.init()

# Set the window size
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)  # white

latency = 0

# Run until the user closes the window
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Draw the circle
            pos = event.pos
            white = (255, 255, 255)
            black = (0, 0, 0)  # black
            radius = 100
            time.sleep(latency)
            pygame.draw.circle(screen, white, pos, radius)
            pygame.display.flip()
            # Wait for 1 second
            time.sleep(1)
            # Erase the circle
            pygame.draw.circle(screen, black, pos, radius)  # white
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                latency+= 0.005
            if event.key == pygame.K_DOWN and latency>0:
                latency-= 0.005 
    print(latency)
    pygame.draw.rect(screen, (0, 0, 0), (10, 10, 150, 36))        
    text = font.render(f"Latency: {latency}", True, text_color)
    screen.blit(text, (10, 10))
    pygame.display.flip()

# Clean up
pygame.quit()
