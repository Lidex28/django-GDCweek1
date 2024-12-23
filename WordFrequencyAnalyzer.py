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

def display_word_frequencies(frequency):
    sorted_frequencies = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    print("\nWord Frequencies in Descending Order:")
    for word, count in sorted_frequencies:
        print(f"{word}: {count}")

def display_top_n_words(frequency):
    n = int(input("\nEnter the value of N to display the top N most frequent words: "))
    sorted_frequencies = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    print(f"\nTop {n} Most Frequent Words:")
    for word, count in sorted_frequencies[:n]:
        print(f"{word}: {count}")

def search_word(frequency):
    word_to_search = input("\nEnter a word to search for its frequency: ").lower()
    if word_to_search in frequency:
        print(f"'{word_to_search}' appears {frequency[word_to_search]} time(s).")
    else:
        print(f"'{word_to_search}' is not found in the text.")

def main():
    text = get_input_text()
    words = tokenize_text(text)
    word_frequencies = calculate_word_frequency(words)
    display_word_frequencies(word_frequencies)
    display_top_n_words(word_frequencies)
    search_word(word_frequencies)

if __name__ == "__main__":
    main()
