import pygame
import sys
import os
import subprocess

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Choose a file to run: ")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def run_file(filename):
    # Checking if the file exists
    if os.path.exists(filename):
        # Running the file
        subprocess.run(["python", filename], check=True)
    else:
        print(f"The file '{filename}' does not exist.")

def main():
    while True:
        # Clear the screen
        screen.fill(WHITE)

        # Displaying the options to the user
        draw_text("Choose a file to run:", font, BLACK, 50, 50)
        draw_text("1. PLAY WITH A FRIEND", font, BLACK, 50, 100)
        draw_text("2. PLAY WITH AI", font, BLACK, 50, 150)
        draw_text("3. Exit", font, BLACK, 50, 200)
        draw_text("Enter 1/2/3 TO CHOOSE", font, BLACK, 50, 250)

        # Update the display
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    run_file("game1.py")
                elif event.key == pygame.K_2:
                    run_file("game2.py")
                elif event.key == pygame.K_3:
                    print("Exiting...")
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
