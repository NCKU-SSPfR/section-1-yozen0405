from judge_code import game_over

def test_game_over_0():
    """Test when health is 0"""
    assert game_over(0) is True

def test_game_over_666():
    """Test when health is 666"""
    assert game_over(666) is True

def test_game_over_other():
    """Test when health is not 0 or 666"""
    assert game_over(3) is False