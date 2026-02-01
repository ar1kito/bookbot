from stats import word_cnt 

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def path():
    x = "./books/frankenstein.txt"
    return get_book_text(x)

word_cnt()