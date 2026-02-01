from main import path

def word_cnt():
    num = 0 
    words = path().split()
    for word in words:
        num += 1
    print(f"Found {num} total words")