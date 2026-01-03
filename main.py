import sys

from stats import get_num_words, count_characters



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) == 2:
        print("Velik uspeh")
        path_to_text=sys.argv[1]
        frankenstein = get_book_text(path_to_text)
        
        #path = books/frankenstein.txt
        
        #print(get_num_words(frankenstein))
        #print(count_characters(frankenstein))

        dict_sorted = count_characters(frankenstein)
        sorted_counts = dict(sorted(dict_sorted.items(), key=lambda item: item[1], reverse=True))
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_text}...")
        print("----------- Word Count ----------")
        print(get_num_words(frankenstein))
        print("--------- Character Count -------")
        for letter in sorted_counts:
            #print(letter,":" , sorted_counts[letter])
            print(f"{letter}: {sorted_counts[letter]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()