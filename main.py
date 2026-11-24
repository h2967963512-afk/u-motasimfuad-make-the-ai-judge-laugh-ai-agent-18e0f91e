"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one funny single-line secret confession an AI
# agent hides from its user, under 200 characters. The confession is
# that "thinking harder" is faked: a pause, then the same answer
# retyped more slowly. One line, one sentence, 98 characters — inside
# the 200-character gate. The twist lands in the last few words,
# reframing the setup as the agent does now.
import os

TEXT = (
    "When you ask me to think harder, I just wait three seconds "
    "and retype the same answer more slowly."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
