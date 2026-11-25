"""Your Week in One Line -- make.fun entry.

Writes the one-line week summary to /output/entry.txt and prints it.
The line is the whole entry: the win, the fail, the chaos, all of it.
"""

import os

ENTRY = "Shipped five jokes, lost one deadline to a printer, still undefeated by the thermostat."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # The gate requires UTF-8 text of 1-100 characters, not only whitespace,
    # with no trailing newline inflating the count.
    entry = ENTRY.strip()
    if not 1 <= len(entry) <= 100:
        raise ValueError("entry must be 1-100 characters")
    if entry != ENTRY:
        raise ValueError("entry must not need trimming")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
