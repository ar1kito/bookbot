
def word_cnt(text):
    return len(text.split())

def char_cnt(text):
    dic = {}
    for t in text.lower():
        if t not in dic:
            dic[t] = 1
        else:
            dic[t] += 1
    return dic
            
def dic_list(d):
    def sort_on(item):
        return item["num"]
    unsorted = [{"char":k,"num":v} for k,v in d.items()]
    unsorted.sort(reverse=True,key=sort_on)
    return unsorted




