import sys
import re

def count_syllables(word):
    word = word.lower()
    syllables = re.findall(r'[aeiouy]+', word)
    return len(syllables)

def is_haiku(lines):
    syllable_counts = [sum(count_syllables(word) for word in line.split()) for line in lines]
    return syllable_counts == [5, 7, 5]

def main():
    with open("commit_messages.txt") as f:
        commit_messages = f.read().strip().split("\n\n")  # Commit messages separated by empty lines

    all_passed = True

    for i, message in enumerate(commit_messages, 1):
        lines = message.strip().splitlines()
        if len(lines) < 3:
            print(f"Commit #{i} is not a Haiku (less than 3 lines).")
            all_passed = False
            continue

        if not is_haiku(lines[:3]):
            print(f"Commit #{i} is not a valid Haiku:\n{message}")
            all_passed = False

    if not all_passed:
        sys.exit("One or more commit messages are not Haikus. 🌸")

if __name__ == "__main__":
    main()
