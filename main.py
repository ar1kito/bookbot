import sys
from stats import word_cnt,char_cnt,dic_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main(path):
    print("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}...")

    text = get_book_text(path)
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


if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])