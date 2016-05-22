"""
Connect 4 Server for Software Craftsmanship
"""

from . import board

class ConnectFourServer():
    def __init__(self, bot_list):
        self.Alive = True
        self.board = board.Board()

def initialise_server(bot_list):
    print("Initialising Server")
    return ConnectFourServer(bot_list)

def register_game():
    pass

def prompt_for_move():
    pass

def CurrentBoard():
    return SERVER.board


def main():
    """
    Entry point for command line invocation.
    """
    initialise_server([])

if __name__ == '__main__':
    main()
else:
    SERVER = initialise_server([])
