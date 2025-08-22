# Pygame Minesweeper

A classic Minesweeper game implementation using Pygame with emoji support.

## Features

- 9x9 grid with 10 mines
- Left click to reveal cells
- Right click to cycle through flag/question mark states
- Shift+Left click for chording (reveal surrounding cells when flags match mine count)
- Visual feedback with emojis (💣, 🚩, ❓)
- Game over and victory screens
- Click anywhere to restart after game ends

## Requirements

- Python 3.x
- Pygame

## Installation

```bash
pip install pygame
```

## Usage

```bash
python main.py
```

## Game Sections

### Section 1 – Basic Environment Setup and Board Creation
- Pygame initialization and display setup
- Game loop structure with event handling
- Basic board grid rendering system

### Section 2 – Initial Structure and Mine Placement  
- Random mine placement algorithm
- Adjacent mine counting logic
- Board state management (hidden/open/flagged/question)

### Section 3 – Object-Oriented Design and Click Actions
- Board class implementation
- Click position to grid coordinate conversion
- Left/right click event handling

### Section 4 – Advanced Logic Implementation
- Recursive cell opening for empty areas
- Chording functionality (Shift+Left click)
- Flag counting and validation

### Section 5 – Win/Loss Handling and Additional Features
- Game over detection and mine revelation
- Victory condition checking
- Game restart functionality
- Emoji rendering system

## Controls

- **Left Click**: Reveal cell
- **Right Click**: Flag/Question mark/Clear
- **Shift + Left Click**: Chord (reveal surrounding cells)
- **Click after game ends**: Restart

## File Structure

- `main.py` - Game loop and display logic
- `board.py` - Board class with game logic
- `const.py` - Constants and configuration
- `font/NotoEmoji-Medium.ttf` - Emoji font file