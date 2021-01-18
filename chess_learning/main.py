import pygame


class ChessGame:
    def __init__(self, width: int = 128 * 8, height: int = 128 * 8):
        # initialize pygame - you have to do this for stuff to work ;)
        # especially when you want to render text later on
        pygame.init()

        # save the width and height of our screen in case we need it for pixel calculations later
        self.width = width
        self.height = height

        # create the surface we want to render on
        self.surface = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Chess")

        # load some image that we may want to later draw
        self.chess_piece_images = {
            "wQ": pygame.image.load("./resources/piece_images/wQ.png")
        }

    def run(self):
        """
        Games are run with infinite loops - we always need to check for input updates
        and also for draw updates that we want to perform

        When the game ends we should also do some cleanup

        :return:
        """
        # We are currently running the game - when we want to quit set this to false
        running = True
        while running:
            # Check for events that pygame is giving us, such as keyboard events or mouse events
            for event in pygame.event.get():
                # if the user is requesting the closing of the window - we just set running to false
                if event.type == pygame.QUIT:
                    running = False
                # Here we have a keyboard event -> if the key is ESC stop the game
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                # Here we are cheking for mouse events but aren't currently using it for anything
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            # After we are done checking for user input and have updated our games logic we need
            # to also draw the new state of the game.
            self.draw_game()

        # let pygame clean up after itself
        pygame.quit()

    def draw_game(self):
        # Chess is rather simple to draw - first draw the board then the piece images on top
        self.draw_board_squares()
        self.draw_board_pieces()

        # Tell pygame to actually flip the image on the screen (name comes from double buffering)
        pygame.display.flip()

    def draw_board_squares(self):
        # Draw a rectangle onto our surface, with the (R, G, B) color at the rect (x, y, width, height)
        pygame.draw.rect(self.surface, (120, 255, 120), (50, 50, 300, 300))

    def draw_board_pieces(self):
        # scale the image such that it is the size we want (maybe do this right after loading the image so we don't
        # always have to scale the image?)
        scaled_image = pygame.transform.scale(self.chess_piece_images["wQ"], (128, 128))
        # Draw the image by blitting it onto our surface at the specified (x, y)
        self.surface.blit(scaled_image, (80, 80))


if __name__ == '__main__':
    # Create a new ChessGame class instance and call its run method
    ChessGame().run()
