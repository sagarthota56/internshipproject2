def count_words(text):
    """
    Counts the number of words in the input text.

    Args:
        text (str): The input sentence or paragraph.

    Returns:
        int: The total number of words.
    """
    
    words = text.split()

    
    return len(words)

def main():
    try:
        user_input = input("Enter a sentence or paragraph: ")
        if not user_input.strip():
            print("Error: Please provide a non-empty input.")
        else:
            word_count = count_words(user_input)
            print(f"Word count: {word_count}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()