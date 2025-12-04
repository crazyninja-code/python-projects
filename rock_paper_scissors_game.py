from __future__ import annotations

import argparse
import random
import sys
from typing import Tuple


CHOICES = ("rock", "paper", "scissors")
WINNING_PAIRS = {
    ("rock", "scissors"),
    ("scissors", "paper"),
    ("paper", "rock"),
}


def decide_winner(player: str, computer: str) -> str:
    """Return 'player', 'computer', or 'tie'."""
    if player == computer:
        return "tie"
    if (player, computer) in WINNING_PAIRS:
        return "player"
    return "computer"


def play_round(player_choice: str) -> Tuple[str, str, str]:
    """Play a single round and return (player, computer, result)."""
    computer_choice = random.choice(CHOICES)
    result = decide_winner(player_choice, computer_choice)
    return player_choice, computer_choice, result


def interactive_mode() -> None:
    print("Welcome to Rock-Paper-Scissors (new game file)!")
    print("Type 'quit' to exit or 'score' to see current score.\n")

    player_score = 0
    computer_score = 0

    while True:
        try:
            raw = input("Your move (rock/paper/scissors): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not raw:
            print("Please enter a move or 'quit'.")
            continue

        if raw == "quit":
            print("Thanks for playing!")
            break

        if raw == "score":
            print(f"Score -> You: {player_score}  Computer: {computer_score}")
            continue

        if raw not in CHOICES:
            print(f"'{raw}' is not a valid move.")
            continue

        player, computer, result = play_round(raw)
        print(f"You: {player}  Computer: {computer}")
        if result == "tie":
            print("Result: tie")
        elif result == "player":
            print("Result: you win")
            player_score += 1
        else:
            print("Result: computer wins")
            computer_score += 1

        print(f"Current -> You: {player_score}  Computer: {computer_score}\n")

    print(f"Final -> You: {player_score}  Computer: {computer_score}")


def demo_mode(rounds: int = 5) -> None:
    print(f"Demo mode: {rounds} rounds")
    player_score = 0
    computer_score = 0
    for i in range(1, rounds + 1):
        player_choice = random.choice(CHOICES)
        _, computer_choice, result = play_round(player_choice)
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        print(f"Round {i}: player={player_choice} computer={computer_choice} -> {result}")

    print(f"Demo final -> You: {player_score}  Computer: {computer_score}")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Rock-Paper-Scissors game (new file)")
    p.add_argument("--demo", "-d", action="store_true", help="Run non-interactive demo")
    p.add_argument("--rounds", "-r", type=int, default=5, help="Rounds for demo mode")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.demo:
        demo_mode(args.rounds)
        return 0
    interactive_mode()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
