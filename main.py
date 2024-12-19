def count_characters(text):
    """
    Counts the frequency of each character in a given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary where keys are characters and values are their frequencies.
    """
    # Convert the text to lowercase
    text = text.lower()

    # Initialize an empty dictionary to store character counts
    char_count = {}

    # Iterate over each character in the text
    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1

    return char_count


def print_character_frequencies(char_count):
    """
    Prints the frequency of each character in a given text.

    Args:
        char_count (dict): A dictionary where keys are characters and values are their frequencies.
    """
    # Print the character frequencies
    for char, count in char_count.items():
        print(f"{char}: {count}")


def main():
    # Open the file and read its content
    with open("books/frankenstein.txt", "r") as f:
        text = f.read()

    # Count the number of words
    word_count = len(text.split())
    print(f"Number of words in the file: {word_count}")

    # Count the characters
    char_count = count_characters(text)

    # Print the character frequencies
    print_character_frequencies(char_count)


if __name__ == "__main__":
    main()
