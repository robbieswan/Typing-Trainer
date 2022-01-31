"""

"""

import pygame
import random

# RGB Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Word:
    """
    A class that contains a random moving word. 
    """
    # Init with random word and y value
    def __init__(self, word_list, start_x, start_y):
        self.word_list = word_list
        self.word = word_list[random.randint(0, 9999)]

        self.start_x = start_x
        self.start_y = start_y

        self.x = start_x
        self.y = start_y

        self.velocity = 0.5

    # Draws word to the screen if it is in bounds
    def draw(self, screen):
        if self.x > -100:
            self.x -= 3
            font = pygame.font.Font(None, 42)
            text = font.render(self.word, True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = (self.x, self.y)
            screen.blit(text, text_rect)
        else:
            self.new_word()

    # Moves word left based on velocity
    def move_left(self):
        self.x -= self.velocity

    # Getter: Returns current word
    def get_word(self):
        return self.word

    # Loads a new word and resets x and y
    def new_word(self):
        # New random word
        self.word = self.word_list[random.randint(0, 9999)]
        # Resets x and y to orginal values
        self.x = self.start_x
        self.y = self.start_y


class Score:
    """
    A that contains a random moving word. 
    """
    # Init 
    def __init__(self):
        self.score_int = 0
        self.score_str = "Score: " + str(self.score_int)
        self.x = 800
        self.y = 100

    #
    def get_score(self):
        return self.score

    def draw(self, screen):
        font = pygame.font.Font(None, 50)
        score_text = font.render(self.score_str, True, BLACK)
        score_rect = score_text.get_rect()
        score_rect.center = (900, 50)
        screen.blit(score_text, score_rect)

"""
def draw_level(screen, level):
    font = pygame.font.Font(None, 50)
    level_text = font.render(str(level), True, BLACK)
    level_rect = level_text.get_rect()
    score_rect.center = (900, 50)
    screen.blit(score_text, score_rect)
"""


# 
def level_up(words):
    for word in words:
        word.velocity += 1


def main():
    # Initaialize pygame
    pygame.init() 
    clock = pygame.time.Clock()

    # Load a file of a words into a list
    file_name = "word_list.txt"
    with open(file_name) as file:
        word_list = file.read().splitlines()

    # Init 3 words
    word1 = Word(word_list, 1100, 150)
    word2 = Word(word_list, 1500, 225)
    word3 = Word(word_list, 1900, 300)
    screen_words = [word1, word2, word3]

    # Set screen dimensions
    screen_width = 1000
    screen_height = 461
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Load the background image
    background = pygame.image.load("jungle.jpg")
    pygame.display.set_caption('Jungle Typer')


    # Draws input box
    font = pygame.font.Font(None, 32)
    input_rect = pygame.Rect(250, 365, 500, 32)

    # Loop Variables
    running = True
    user_text = ""
    score = Score()
    lives = 3

    # While loop for running
    while running:

        #TODO: Dely

        # Draws Background
        screen.blit(background, (0, 0)) # Background

        # Draws input box and text
        pygame.draw.rect(screen, WHITE, input_rect) 
        text_surface = font.render(user_text, True, BLACK)  
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        # Lives Counter

        

        # Score Counter
        score.draw(screen)

        
        # Draws and moves words
        for word in screen_words:
            word.draw(screen)
            word.move_left()

        # Handles events 
        for event in pygame.event.get():

            # Quits program
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            # If key is pressed
            if event.type == pygame.KEYDOWN:

                # TODO: Handles backspace
                if event.key == pygame.K_BACKSPACE:
                    print(user_text)
                    user_text = user_text[-1]
                    print(user_text)

                # If return is pressed, 
                if event.key == pygame.K_RETURN:
                    for word in screen_words:
                            if user_text == word.get_word():
                                #score += len(word.get_word()) * 10
                                word.new_word()
                    user_text = ""

                # Adds character to user_text
                else:
                    user_text += event.unicode

            # If lives
            if lives <= 0:
                pygame.quit()
                quit()

                
        clock.tick(60)
        pygame.display.update()


# Start progam
main()
