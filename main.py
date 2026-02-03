import sys
from stats import word_cnt,char_cnt,dic_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")
    print ("Analyzing book found at books/frankenstein.txt...")

    text = get_book_text("./books/frankenstein.txt")
    print("----------- Word Count ----------")
    total_words = word_cnt(text)
    print(f"Found {total_words} total words")

    print("--------- Character Count -------")
    dic = char_cnt(text)
    char_counts = dic_list(dic)
    for item in char_counts:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
        else:
            pass
    print("============= END ===============")


main()