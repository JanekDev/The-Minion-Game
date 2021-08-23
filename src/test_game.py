from game import minion_game

#unit tests
def test_game_diff():
    assert minion_game("BANANA")=="Stuart 12"
    assert minion_game("geek")=="Kevin 5"
def test_game_draw():
    assert minion_game("BANAASA")=="Draw"