def word_count(file_contents):
    words = file_contents.split()
    return len(words)  # Just return the count, don't print it

def count_characters(file_contents):
    counts = {}
    for character in file_contents.lower():
        if character.isalpha():  # Only count letters
            if character in counts:
                counts[character] = counts[character] + 1
            else:
                counts[character] = 1  
    return counts

def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    num_words = word_count(file_contents)  # Save the count
    characters_count = count_characters(file_contents)


    chars_to_sort = []
    for char, count in characters_count.items():
            if char.isalpha():
                chars_to_sort.append({"character": char, "num": count})


    chars_to_sort.sort(key=sort_on, reverse=True)

    for char_dict in chars_to_sort:
        print("The '" + char_dict['character'] + "' character was found " + str(char_dict['num']) + " times")
if __name__ == "__main__":
    main()