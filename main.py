from stats import * 
import sys



def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents



def main():
    try:
        file_path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    file_content = get_book_text(file_path)
    num_words = count_words(file_content)
    num_chars, total = count_chars(file_content)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    listed_chars = sort_dict(num_chars)

    for item in listed_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
        else:
            pass

    print("============= END ===============")



main()
