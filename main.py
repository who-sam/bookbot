from stats import count_words 



def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents



def main():
    file_content = get_book_text("./books/frankenstein.txt")
    num_words = count_words(file_content)
    print(f"{num_words} words found in the document")



main()
