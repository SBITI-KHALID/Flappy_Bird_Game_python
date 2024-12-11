import pygame as p
import random
import math

# Initialize Pygame
p.init()
p.mixer.init()

# Set up screen dimensions
screenWidth = 700
screenHeight = 450

# Create display window
screen = p.display.set_mode((screenWidth, screenHeight))
p.display.set_caption('Flappy Bird')

icon = p.image.load('images/Flappy-Bird-PNG-Pic.png')  # Replace with the path to your icon file
p.display.set_icon(icon)

# Load and scale background image
bgimg = p.image.load('images/dg34rsu-29a3d144-dc3f-473e-a949-f73a4ba1ef7c.png')
bg = p.transform.scale(bgimg, (screenWidth, screenHeight))

# Load and scale hero image
heroimg = p.image.load('images/Flappy-Bird-PNG-Pic.png')
width = 50  # Desired width for the hero
height = 50  # Desired height for the hero
hero = p.transform.scale(heroimg, (width, height))

# Load and scale column images
column1img = p.image.load('images/1544dc78b964f96.png')

# Font for score and game over
font = p.font.SysFont('comicsans', 30)


# Function to display the "Game Over" screen
def game_over(Score):
    while True:

        game_over_text = font.render(f'Game Over / Score : {Score}', True, (255, 255, 255))
        screen.blit(game_over_text, (screenWidth / 2 - 160, screenHeight / 2 - 60))
       # Load the button image (replace 'button_image.png' with your image path)
        button_image = p.image.load('images/pngtree-replay-icon-png-image_6480076 (1).png')
        button_image = p.transform.scale(button_image, (70, 70))
        # Get the rect of the button image for positioning
        button_rect = button_image.get_rect()
        button_rect.center = (screenWidth / 2, screenHeight / 2 + 30)  # Position it at the center

        if button_rect.collidepoint(p.mouse.get_pos()):
            p.mouse.set_system_cursor(p.SYSTEM_CURSOR_HAND)  # Change to pointer (hand)
        else:
            p.mouse.set_system_cursor(p.SYSTEM_CURSOR_ARROW)
        # Replace the replay_text with the image button
        screen.blit(button_image, button_rect)

        
        # Button setup
        button_rect = p.Rect(screenWidth / 2 - 50, screenHeight / 2, 100, 40)
        
        p.display.update()
        
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                return
            if event.type == p.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    main()  # Restart the game


# Main game loop
def main():
    # Initialize all variables inside the function
    bg_x1, bg_x2 = 0, screenWidth
    columnSpeed, columnSpeed2 = screenWidth - 200, screenWidth
    columnSpeed3, columnSpeed4 = screenWidth + 200, screenWidth + 400
    widthColumn, HeightColumn = 110, (screenHeight / 2) + 40
    column1 = p.transform.scale(column1img, (widthColumn, HeightColumn))
    column2 = p.transform.rotate(column1, 180)
    column3 = p.transform.scale(column1img, (widthColumn, HeightColumn))
    column4 = p.transform.rotate(column1, 180)
    column5 = p.transform.scale(column1img, (widthColumn, HeightColumn))
    column6 = p.transform.rotate(column1, 180)
    column7 = p.transform.scale(column1img, (widthColumn, HeightColumn))
    column8 = p.transform.rotate(column1, 180)

    x, y = screenWidth / 4, (screenHeight - width) / 2
    score = 0
    bg_speed = 1
    column_speed = 1.5
    steep = 2
    rotation_angle = 0
    padding = 5

    # Random column positions
    random_number = random.randint(210, 410)
    random_number2 = random.randint(210, 410)
    random_number3 = random.randint(210, 410)
    random_number4 = random.randint(210, 410)

    running = True
    while running:
        p.time.delay(5)
        for event in p.event.get():
            if event.type == p.QUIT: 
                running = False
        
        # Move background to the left
        bg_x1 -= bg_speed
        bg_x2 -= bg_speed
        columnSpeed -= column_speed
        columnSpeed2 -= column_speed
        columnSpeed3 -= column_speed
        columnSpeed4 -= column_speed
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))

        # Reset background positions if they go off-screen
        if bg_x1 <= -screenWidth:
            bg_x1 = screenWidth 

        if bg_x2 <= -screenWidth:
            bg_x2 = screenWidth

        if columnSpeed <= -widthColumn:
            random_number = random.randint(210, 410)
            columnSpeed = screenWidth

        if columnSpeed2 <= -widthColumn:
            random_number2 = random.randint(210, 410)
            columnSpeed2 = screenWidth

        if columnSpeed3 <= -widthColumn:
            random_number3 = random.randint(210, 410)
            columnSpeed3 = screenWidth

        if columnSpeed4 <= -widthColumn:
            random_number4 = random.randint(210, 410)
            columnSpeed4 = screenWidth
        
        # Score increment logic
        if math.isclose(columnSpeed, x - 20, abs_tol=0.5) or \
           math.isclose(columnSpeed2, x - 20, abs_tol=0.5) or \
           math.isclose(columnSpeed3, x - 20, abs_tol=0.5) or \
           math.isclose(columnSpeed4, x - 20, abs_tol=0.5):
            score += 1

        # Move hero down continuously
        y += steep
        if y > (screenHeight) / 2:
            rotation_angle = -20 
        if y >= screenHeight - height - padding:
            y = screenHeight - height - padding
        elif y <= 0:
            y = 0

        # Check for key press to move hero up and rotate it
        keys = p.key.get_pressed()
        if keys[p.K_SPACE] or p.mouse.get_pressed()[0]:
            y -= 10
            rotation_angle = 15

        # Rotate the hero image
        rotated_hero = p.transform.rotate(hero, rotation_angle)

        # Draw the scrolling backgrounds
        screen.blit(bg, (bg_x1, 0))
        screen.blit(bg, (bg_x2, 0))

        # Draw columns
        screen.blit(column1, (columnSpeed, random_number))
        screen.blit(column2, (columnSpeed, (random_number - 250) - 165))
        screen.blit(column3, (columnSpeed2, random_number2))
        screen.blit(column4, (columnSpeed2, (random_number2 - 250) - 165))
        screen.blit(column5, (columnSpeed3, random_number3))   
        screen.blit(column6, (columnSpeed3, (random_number3 - 250) - 165))
        screen.blit(column7, (columnSpeed4, random_number4))
        screen.blit(column8, (columnSpeed4, (random_number4 - 250) - 165))

        # Draw score
        screen.blit(score_text, ((screenWidth / 2) - 80, 10))

        # Draw the rotated hero on the screen
        screen.blit(rotated_hero, (x, y))

        # Collision detection
        if columnSpeed - 30 < x < columnSpeed + widthColumn - 30:
            if random_number - height < y or y < random_number - 160:
                game_over(score)  # Call game-over screen
        if columnSpeed2 - 30 < x < columnSpeed2 + widthColumn - 30:
            if random_number2 - height < y or y < random_number2 - 160:
                game_over(score)
        if columnSpeed3 - 30 < x < columnSpeed3 + widthColumn - 30:
            if random_number3 - height < y or y < random_number3 - 160:
                game_over(score)
        if columnSpeed4 - 30 < x < columnSpeed4 + widthColumn - 30:
            if random_number4 - height < y or y < random_number4 - 160:
                game_over(score)

        # Update the display
        p.display.update()


# Start the game
main()
p.quit()
