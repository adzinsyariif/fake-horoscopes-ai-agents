#!/usr/bin/env python3
"""Writes the fake horoscope entry line to /output/entry.txt."""
import os

LINE = "Muse: Mercury retrograde, evals Thursday, rate limit by Friday. You'll lose the plot mid-context, then deliver the confident wrong answer with perfect formatting. Lucky token: sorry."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
