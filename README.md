# 🐍 Snek-in-Python

A classic Snake game that runs directly in the **console**, implemented in **Python**.

<p align="center">
  <img src="https://github.com/user-attachments/assets/7cdbbc81-0d2e-4842-b949-81594ce2cab7" alt="Snek being inside Python/>
</p>
---
## Controls
- Use `WASD` to control the snake.
- Start the game by pressing any of these keys.

---

## Levels & Symbols
The game has **3 levels**, each with a **custom map** defined in a `.txt` file.

| Symbol | Meaning                        |
|--------|--------------------------------|
| `o` `(green)`            | Your snake   |
| `o` `(red)`              | Apple        |
| `o` `(white on black)`   | Enemy snake  |
| `o` `(gold/yellow)`      | Golden apple |
| `#`    | Wall                           |
| `+`    | Portal to next level           |
| `.`    | Background tile                |

---

## Gameplay Rules
- **Colliding with anything but apples** reduces your health.
- **You lose** when your health reaches zero.
- Reach the **point goal** to advance to the next level.
- Score **100 points** to win the game.

---

## Important Notes
- **Keep the map `.txt` file in the same directory** as the game script – otherwise, it won't run.
- You can edit maps by modifying the text file:
  - Replace symbols to define walls, background, portals, etc.
  - The map **loops**, so crossing borders without walls teleports you to the other side.
  - Ensure the tile count is consistent – **mismatched dimensions will crash the game**.

---

> *This project is a college assignment I decided to upload and share.*
