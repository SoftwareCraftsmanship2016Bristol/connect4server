"""
Tests for server.py
"""

from .context import connect4server

import pytest
server = connect4server.server
board = connect4server.board

A6x7Board = board.Board()

@pytest.fixture()
def blankserver():
    return server.initialise_server([])

@pytest.fixture()
def blankboard():
    return board.Board()

def test_WhenInitialiseIsCalledABoardOf6x7IsCreated():
   #arrange
    expected = A6x7Board
   #act
    actual = server.CurrentBoard()
   #assert
    assert expected == actual

def test_CheckInitWorks():
    #arrange
    expected = True
    #act
    actual = server.initialise_server([])
    #assert
    assert expected == actual.Alive

def test_WhenIDropCoinInEmptyBoardInFirstColumnCoinEndsInBottomRow():
    #arrange
    expected = 1
    my_server = server.initialise_server([])
    #act
    actual = my_server.board.MakeMove(1)
    #assert
    assert expected == actual[0][0]

def test_WhenCoinAlredyInColumn1ANewCoinWillEndUpInColumn1Row2():
    #arrange
    expected = 1
    my_server = server.initialise_server([])
    my_server.board.MakeMove(1)
    #act
    actual = my_server.board.MakeMove(1)
    #assert
    assert expected == actual[0][1]

def test_WhenColumn1IsFullItThrowsExcpetion():
    #arrange
    expected = 1
    my_server = server.initialise_server([])
    for i in range(6):
        my_server.board.MakeMove(1)
    #act
    with pytest.raises(ValueError):
        actual = my_server.board.MakeMove(1)
    #assert

def test_WinSinglePlayerBy4CoinsInColumn1():
    #arrange
    my_server = server.initialise_server([])
    for i in range(3):
        my_server.board.MakeMove(1)
    #act
    actual = my_server.board.MakeMove(1)
    #assert
    assert actual.win == True

def test_WinSinglePlayerBy4CoinsInRow1(blankserver):
    #arrange
    for i in range(1,4):
        blankserver.board.MakeMove(i)
    #act
    board = blankserver.board.MakeMove(4)
    #assert
    assert board.win == True

def test_Player1DropsCoinInFirstColumnPlayer2InSecondOutcomeIs1Then2(blankserver):
    #act
    blankserver.board.MakeMove(1,player = 1)
    blankserver.board.MakeMove(2,player = 2)

    #assert
    assert blankserver.board[0][0] == 1 and blankserver.board[1][0] == 2

@pytest.mark.parametrize(('column'), range(2))
def test_If4CoinsDiagonallyThenAPlayerWins(blankserver, column):
    #arrange
    blankserver.board.MakeMove(column+1,player = 1)
    blankserver.board.MakeMove(column+2,player = 2)
    blankserver.board.MakeMove(column+3,player = 2)
    blankserver.board.MakeMove(column+4,player = 2)
    blankserver.board.MakeMove(column+3,player = 2)
    blankserver.board.MakeMove(column+4,player = 2)
    blankserver.board.MakeMove(column+4,player = 2)
    blankserver.board.MakeMove(column+2,player = 1)
    blankserver.board.MakeMove(column+3,player = 1)
    blankserver.board.MakeMove(column+4,player = 1)
    #act
    assert blankserver.board.win == True
    #assert


# def test_4inColumnIsAWin(blankserver, column):
#     #act
#     for i in range(4):
#         blankserver.board.MakeMove(column)

#     #assert
#     assert blankserver.board.win == True

# Diagonal win condition required
# Test if column is already full
# Test if board is full.
# Test for coordinates e.g. is [0,0] top or bottom
# Agree rendering routine for board with bot team
# Make allowance for two colours
