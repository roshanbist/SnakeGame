# SnakeGame

A classic Snake game implemented in Python using the `turtle` graphics library. Control the snake, eat food, and grow longer, just be careful not to hit the walls or yourself!

## 🐍 Features

- Move the snake using arrow keys (Up, Down, Left, Right)
- Eat the food to grow the snake and increase your score
- Real-time score display
- Game resets when the snake hits the wall or itself
- Food appears at random locations on the screen
- 100% Python

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed

### Installation

The only required library is `turtle`, which comes with standard Python installations.

**Clone the repository:**

```bash
git clone https://github.com/roshanbist/SnakeGame.git
cd SnakeGame
```

### Running the Game

```bash
python main.py
```

## 🎮 How to Play

- Use **arrow keys** to control the snake’s direction.
- Eat the food to grow longer.
- Avoid colliding with the walls or your own body.
- Try to achieve the highest score!

## 📁 Project Structure

```
SnakeGame/
└── food.py
└── main.py
└── README.md
└── score_file.txt
└── scoreboard.py
└── snake.py
```

## File Descriptions

- main.py: Entry point, handles the game loop and user input.
- snake.py: Contains the Snake class for snake behavior.
- food.py: Contains the Food class for food placement.
- scoreboard.py: Contains the Scoreboard class for score display and high score logic.
- score_file.txt: The highest score is saved in score_file.txt. The file is updated automatically when you beat the previous high score..

## 📝 Customization

You can tweak the speed, grid size, or add new features like sound effects, or obstacles by editing the Python files.

## 📄 License

This project is for educational purposes.
