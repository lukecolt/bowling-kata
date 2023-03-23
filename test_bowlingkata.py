from BowlingGame import BowlingGame

class TestBowlingkata:
    # tests 1,2,3 test cases from codingdojo.org, rest from article Adventures in C#: The Bowling Game
    # also from this site, and some mine
    
    def test_1(self): #perfect situation
        game1 = BowlingGame()
        frameNumber = 0
        while frameNumber < 10:
            game1.strike()
            frameNumber += 1
        game1.roll(10)
        game1.roll(10)
        assert game1.score() == 300

    def test_2(self):
        game2 = BowlingGame()
        frameNumber = 0
        while frameNumber < 10:
            game2.open(9,0)
            frameNumber += 1
        assert game2.score() == 90 

    def test_3(self):
        game3 = BowlingGame()
        frameNumber = 0
        while frameNumber < 10:
            game3.spare(5,5)
            frameNumber += 1
        game3.roll(5)
        assert game3.score() == 150

    def test_all_zeroes(self): #zero
        game4 = BowlingGame()
        frameNumber = 0
        while frameNumber < 10:
            game4.open(0,0)
            frameNumber += 1
        assert game4.score() == 0

    def test_threes(self):
        game5 = BowlingGame()
        frameNumber = 0
        while frameNumber < 10:
            game5.open(3,3)
            frameNumber += 1
        assert game5.score() == 60

    def test_strike(self):
        frameNumber = 0
        game6 = BowlingGame()
        game6.strike()
        game6.open(5,3)
        while frameNumber < 8:
            game6.open(0,0)
            frameNumber += 1
        assert game6.score() == 26

    def test_spare(self):
        frameNumber = 0
        game7 = BowlingGame()
        game7.spare(4,6)
        game7.open(3,5)
        while frameNumber < 8:
            game7.open(0,0)
            frameNumber += 1
        assert game7.score() == 21

    def test_open(self):
        frameNumber = 0
        game8 = BowlingGame()
        game8.open(3,3)
        while frameNumber < 9:
            game8.open(0,0)
            frameNumber += 1
        assert game8.score() == 6

    def test_alt(self):
        frameNumber = 0
        game9 = BowlingGame()
        while frameNumber < 5:
            game9.strike()
            game9.spare(4,6)
            frameNumber += 1
        game9.roll(10)
        assert game9.score() == 200

    def test_spare_final_frame(self):
        frameNumber = 0
        game10 = BowlingGame()
        while frameNumber < 9:
            game10.open(0,0)
            frameNumber += 1
        game10.spare(4,6)
        game10.roll(5)
        assert game10.score() == 15


        
