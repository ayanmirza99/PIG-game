# Pig Dice Game

Welcome to the Pig Dice Game! This is a simple and fun two-player dice game where the first player to reach a predetermined score (default is 50 points) wins.

## Game Rules

1. **Players take turns** to roll a single die as many times as they wish, adding the roll's value to a temporary total (called the "turn total").
2. **If the player rolls a 1**, their turn ends, and they score nothing for that turn (their turn total is reset to 0).
3. **If the player rolls any other number (2-6)**, they can either:
   - **Add the roll to their turn total and roll again**.
   - **Add the roll to their turn total and hold** (end their turn), adding their turn total to their overall score.
4. **The first player to reach or exceed the predetermined winning score (default is 50 points) wins**.
5. Each player will get equal number of turns.

## Strategy

- Deciding when to roll and when to hold is crucial. Rolling too many times increases the risk of rolling a 1 and losing the turn's points.

## How to Play

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/pig-dice-game.git
    ```

2. Navigate to the project directory:
    ```bash
    cd pig-dice-game
    ```

3. Run the game:
    ```bash
    python index.py
    ```

4. Follow the on-screen instructions. Players will be prompted to roll or hold after each roll. The game continues until one player reaches the winning score.