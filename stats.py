def read_book(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    num_words = 0
    word_list = book_text.split()
    for word in word_list:
        num_words +=1
    return f"Found {num_words} total words"

def unique_character_count(book_text):
    lower_book_text = book_text.lower()
    #word_list = lower_book_text.split()
    word_dictionary = {}
    for character in lower_book_text:
        if character in word_dictionary:
            word_dictionary[character] += 1
        else:
            word_dictionary[character] = 1
    return word_dictionary

def sort_on(dict):
    return dict["num"]

def sorting_dict(dict):
    """
    1. You're given a big dictionary. This dictionary lists keys (characters) and the number of times they
    appear on the book(i.e. {b:5803})
    2. You need to create a dictionary for every instance of this dictionary.
        Each of this new dictionary will:
            a. take the key/chracter, add it as a value whose key is simply "char"
            b. take the value/count, add it as a value whose key is simply "num"
        Now, you append this dictionary to a list.
    3. Sort the list with list.sort(). Sort by greatest to list by count, meaning the value of the key "num"
        This can be done by using list.sort(reverse=True, key=sort_on)
        key=sort_on looks for the key with numbers, while reverse tells him to count from greatest to least.
    """
    list_dict = []
    for key in dict:
        temp_dict = {}
        temp_dict["char"] = key
        temp_dict["num"]= dict[key]
        list_dict.append(temp_dict)
    list_dict.sort(reverse=True,key=sort_on)
    return list_dict

