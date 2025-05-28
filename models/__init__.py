from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .arcade import Arcade
from .gamer import Gamer
from .token import Token
from .game import Game
from .play import Play
from .prize import Prize
from .redemption import Redemption
