# Snake Game

A classic Snake game implemented in Python using the curses library. This terminal-based game features colorful graphics, score tracking, and an intuitive interface.

## Features

- Colorful terminal-based UI
- Score and high score tracking
- Direction-aware snake appearance
- Game over screen with restart option
- Persistent high score storage

## Requirements

- Python 3.x (Python 2 is not supported)
- curses library (included in standard Python distribution)

## Installation

Clone the repository:
```bash
git clone git@github.com:SwetaTanwar/snake-game.git
cd snake-game
```

Make the game executable (optional):
```bash
chmod +x snake_game.py
```

## How to Play

You can run the game in any of these ways:

1. Using Python 3 explicitly:
   ```bash
   python3 snake_game.py
   ```

2. If the file is executable (after running chmod):
   ```bash
   ./snake_game.py
   ```

### Controls
- Use arrow keys (↑ ↓ ← →) to control the snake
- Eat ★ to grow and score points
- Press 'q' to quit
- Press 'r' to restart after game over

## Game Elements

- 🐍 Snake head shows direction (▶ ◀ ▲ ▼)
- ◆ Snake body
- ★ Food
- Score and high score display at the top
- Control instructions at the bottom 