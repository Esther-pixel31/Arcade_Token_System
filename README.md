
# 🎮 Arcade Management System

A command-line-based arcade game management system built with Python, SQLAlchemy, Typer CLI, and Alembic for database migrations.

---

## 📽️ Demo Videos

- [🎮 Gameplay Demo](https://drive.google.com/file/d/1Dm4iO1WVZpM1DYn31gDc4OKPIOhkvdK6/view?usp=sharing)

---

## 🛠️ Tech Stack

- Python 3.8+
- SQLAlchemy ORM
- SQLite (default)
- Alembic (for database migrations)
- Typer (for CLI interface)

---

## 📦 Features

- Manage **Arcades**, **Games**, **Gamers**, **Tokens**, **Prizes**
- Play mini-games (e.g., Rock-Paper-Scissors, Guessing Game)
- Track high scores
- Redeem prizes using token points
- Full CRUD operations
- Seed data support
- Schema migrations using Alembic
- Error handling & constraints enforced

---

## 🚀 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone git@github.com:Esther-pixel31/Arcade_Token_System.git
   cd arcade-system
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  
   ```

3. **Install dependencies**
   ```bash
   pip install 
   
   ```

---

## 🗄️ Database Setup

To initialize the database:

```bash
alembic upgrade head
```

If you made changes to models:

```bash
alembic revision --autogenerate -m "Describe change"
alembic upgrade head
```

To reset the database manually (for SQLite):
```bash
rm arcade.db
```

---

## 🌱 Seeding the Database

```bash
python -m db.seed
```

---

## 🕹️ Running the App

```bash
python main.py menu
```

You'll be guided through a menu where you can log in, play games, earn points, and redeem prizes.

---

## 🧪 Testing Tips

- Enter your username correctly when prompted
- Make sure your tokens and high scores are updated after each game
- Check console for helpful debug messages if things go wrong

---

## 💡 Notes

- Designed with SQLite for simplicity, but supports PostgreSQL with minimal changes
- Game logic is kept simple but extensible
- Ideal for learning SQLAlchemy, Alembic, and CLI building

---

## 👤 Author

- **Esther Mutua**
- GitHub: [@Esther-pixel31](https://github.com/Esther-pixel31/Arcade_Token_System.git)

---

## 📝 License

MIT License. See `LICENSE` file for details.
