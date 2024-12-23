def get_input_text():
    text = input("Enter a paragraph of text: ")
    return text

def tokenize_text(text):
    words = text.split()
    words = [word.strip(".,!?;:\"()[]{}").lower() for word in words]
    return words

def calculate_word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def main():
    text = get_input_text()
    words = tokenize_text(text)
    word_frequencies = calculate_word_frequency(words)
    print("\nWord Frequencies:")
    for word, count in word_frequencies.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
