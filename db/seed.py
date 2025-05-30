from .engine import Session, engine
from models import Arcade, Gamer, Token, Game, Play, Prize, Redemption
from models import Base  


def seed():

    Base.metadata.create_all(engine)

    session = Session()

    # Clear existing data if you want (optional)
    session.query(Redemption).delete()
    session.query(Play).delete()
    session.query(Token).delete()
    session.query(Prize).delete()
    session.query(Game).delete()
    session.query(Gamer).delete()
    session.query(Arcade).delete()
    session.commit()

    # Create some Arcades
    arcade1 = Arcade(name="Pixel Palace", location="Downtown")
    arcade2 = Arcade(name="Retro Realm", location="Uptown")

    session.add_all([arcade1, arcade2])
    session.commit()

    # Create some Gamers
    gamer1 = Gamer(username="joystick_king")
    gamer2 = Gamer(username="pixel_master")
    session.add_all([gamer1, gamer2])
    session.commit()

    # Create some Tokens
    token1 = Token(type="Gold Token", points=100, arcade=arcade1, gamer=gamer1)
    token2 = Token(type="Silver Token", points=50, arcade=arcade2, gamer=gamer2)
    session.add_all([token1, token2])
    session.commit()

    # Create some Games
    game1 = Game(name="Guessing Game", genre="Puzzle", arcade=arcade1)
    game2 = Game(name="Rock Paper Scissors", genre="Strategy", arcade=arcade1)
    game3 = Game(name="Space Invaders", genre="Shooter", arcade=arcade1)
    game4 = Game(name="Pac-Man", genre="Maze", arcade=arcade2)
    session.add_all([game1, game2, game3, game4])

    # Create some Plays
    play1 = Play(gamer=gamer1, game=game1, score=9000)
    play2 = Play(gamer=gamer2, game=game2, score=12000)
    session.add_all([play1, play2])
    session.commit()

    # Create some Prizes
    prize1 = Prize(name="Arcade T-Shirt", token_cost=150, arcade=arcade1)
    prize2 = Prize(name="Game Poster", token_cost=75, arcade=arcade2)
    session.add_all([prize1, prize2])
    session.commit()

    # Create some Redemptions
    redemption1 = Redemption(gamer=gamer1, prize=prize1)
    redemption2 = Redemption(gamer=gamer2, prize=prize2)
    session.add_all([redemption1, redemption2])
    session.commit()

    print("Seed data added!")

if __name__ == "__main__":
    seed()
