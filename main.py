import typer
from db.engine import Session
from models import Gamer, Game, Prize, Token
from models.redemption import Redemption
from models.play import Play
from models import games

app = typer.Typer()

# --- Helper Function ---
def get_gamer(session, username):
    gamer = Gamer.get_by_username(session, username)
    if not gamer:
        typer.echo(f"Gamer '{username}' not found.")
    return gamer

# --- Interactive Menu Command ---
@app.command()
def menu():
    """Interactive Arcade System Menu."""
    session = Session()

    while True:
        typer.echo("\n🎮 Arcade Menu")
        typer.echo("1. Create Gamer")
        typer.echo("2. View All Gamers")
        typer.echo("3. View Gamer Details")
        typer.echo("4. Add Tokens to Gamer")
        typer.echo("5. List Prizes")
        typer.echo("6. Redeem Prize")
        typer.echo("7. Play a Game")
        typer.echo("0. Exit")

        choice = typer.prompt("Select an option")

        if choice == "1":
            username = typer.prompt("Enter username")
            gamer = Gamer.create(session, username)
            typer.echo(f"Gamer '{gamer.username}' created.")

        elif choice == "2":
            gamers = session.query(Gamer).all()
            for g in gamers:
                typer.echo(str(g))

        elif choice == "3":
            username = typer.prompt("Enter username")
            gamer = get_gamer(session, username)
            if gamer:
                typer.echo(f"{gamer} | Total Tokens: {gamer.total_tokens()}")

        elif choice == "4":
            username = typer.prompt("Enter username")
            gamer = get_gamer(session, username)
            if gamer:
                points = int(typer.prompt("Enter token amount"))
                token = Token(gamer_id=gamer.id, points=points)
                session.add(token)
                session.commit()
                typer.echo(f"Added {points} tokens to {username}.")

        elif choice == "5":
            prizes = session.query(Prize).all()
            for prize in prizes:
                typer.echo(f"{prize.id}: {prize.name} - Cost: {prize.token_cost} tokens")

        elif choice == "6":
            username = typer.prompt("Enter username")
            gamer = get_gamer(session, username)
            if gamer:
                prize_id = int(typer.prompt("Enter prize ID"))
                prize = session.get(Prize, prize_id)
                if prize and gamer.total_tokens() >= prize.token_cost:
                    redemption = Redemption(gamer_id=gamer.id, prize_id=prize.id)
                    session.add(redemption)
                    session.commit()
                    typer.echo(f"{username} redeemed {prize.name}.")
                else:
                    typer.echo("Cannot redeem. Either prize not found or not enough tokens.")

        elif choice == "7":
            username = typer.prompt("Enter username")
            gamer = get_gamer(session, username)
            if gamer:
                typer.echo("Choose a game:")
                typer.echo("1. Guessing Game")
                typer.echo("2. Rock, Paper, Scissors")
                game_choice = typer.prompt("Enter game choice")

                if game_choice == "1":
                    game = session.query(Game).filter_by(name="Guessing Game").first()
                    score = games.guessing_game()
                elif game_choice == "2":
                    game = session.query(Game).filter_by(name="Rock Paper Scissors").first()
                    score = games.rock_paper_scissors()
                else:
                    typer.echo("Invalid game choice.")
                    return

                if game:
                    play = gamer.play_game(session, game, score)
                    session.add(play)
                    session.commit()
                    typer.echo(f"{username} played {game.name} with score {score}.")
                else:
                    typer.echo("Game not found in database.")

        elif choice == "0":
            typer.echo("Goodbye!")
            break

        else:
            typer.echo("Invalid option.")

    session.close()

# --- Additional Typer Commands (Optional/Non-Interactive) ---
@app.command("create-gamer")
def create_gamer(username: str):
    """Create a new gamer."""
    session = Session()
    gamer = Gamer.create(session, username)
    typer.echo(f"Gamer '{gamer.username}' created.")
    session.close()

@app.command("list-gamers")
def list_gamers():
    """List all gamers."""
    session = Session()
    gamers = session.query(Gamer).all()
    for gamer in gamers:
        typer.echo(f"{gamer.id}: {gamer.username} - {gamer.total_tokens()} tokens")
    session.close()

@app.command("add-tokens")
def add_tokens(username: str, amount: int):
    """Add tokens to a gamer."""
    session = Session()
    gamer = get_gamer(session, username)
    if gamer:
        token = Token(gamer_id=gamer.id, points=amount)
        session.add(token)
        session.commit()
        typer.echo(f"{amount} tokens added to {username}.")
    session.close()

@app.command("list-prizes")
def list_prizes():
    """List all available prizes."""
    session = Session()
    prizes = session.query(Prize).all()
    for prize in prizes:
        typer.echo(f"{prize.id}: {prize.name} - Cost: {prize.token_cost}")
    session.close()

@app.command("play-game")
def play_game(username: str, game_id: int, score: int):
    """Log that a gamer played a game."""
    session = Session()
    gamer = get_gamer(session, username)
    if gamer:
        game = session.query(Game).get(game_id)
        if game:
            play = gamer.play_game(game, score)
            session.add(play)
            session.commit()
            typer.echo(f"{username} played {game.name} with score {score}.")
        else:
            typer.echo("Game not found.")
    session.close()
@app.command("create-game")
def create_game(name: str, desc: str = "No description"):
    """Create a new game."""
    session = Session()
    game = Game(name=name, description=desc)
    session.add(game)
    session.commit()
    typer.echo(f"Game '{name}' added.")
    session.close()


if __name__ == "__main__":
    app()
