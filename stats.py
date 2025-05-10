def count_words(file):
    words = file.split()
    return len(words)


def count_chars(file):
    file_content = file.lower()
    counts = {}
    for c in file_content:
        if c in counts:
            counts[c] +=1
        else:
            counts[c] = 1
    return counts


def sort_key(dict):
    return dict["num"]


def sort_dict(dict):
    char_num = []
    for key in dict:
        char_num.append({"char": key, "num": dict[key]})

    char_num.sort(reverse=True, key=sort_key)
    return char_num

