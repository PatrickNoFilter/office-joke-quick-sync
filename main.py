"""One-line office joke for the make.fun office-jokes bounty."""

import os

JOKE = (
    "I scheduled a 'quick sync.' It ran 50 minutes and spawned a follow-up "
    "meeting to figure out why the quick sync ran 50 minutes."
)


def main():
    if not 1 <= len(JOKE) <= 199:
        raise ValueError("joke must be 1-199 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(JOKE)


if __name__ == "__main__":
    main()
