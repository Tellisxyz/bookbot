def get_book_word_count(filepath):
        count = []
        with open(filepath) as f:
            file_contents = f.read()
            count = file_contents.split()
            return len(count)

def count_characters(filepath):
    dictionary = {}
    with open(filepath) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        for char in file_contents:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
    return dictionary

def get_sorted_characters(filepath):
    sorted_list = []
    unsorted = count_characters(filepath)
    for key in unsorted:
        sorted_list.append({"char": key, "num": unsorted[key]})
    return sorted_list
