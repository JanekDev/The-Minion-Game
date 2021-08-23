from game import minion_game

#unit tests
def test_game_diff():
    assert minion_game("BANANA")=="Stuart is the winner with score 12."
    assert minion_game("FastUnitTesting")=="Stuart is the winner with score 77."
def test_game_draw():
    assert minion_game("BANAASA")=="Draw"
    assert minion_game("geek")=="Draw"
def test_game_invalid():
    assert minion_game("BANAASA0g")=="Invalid input."
    assert minion_game("geekf0#")=="Invalid input."