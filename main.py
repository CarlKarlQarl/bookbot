def main():
    book_location = "books/frankenstein.txt"
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(book_location)} words found in the document")
    for char_count_dict in sort_dict_list(convert_to_char_dict_list(char_count(book_location))):
        print("The '%s' character was found %d times"%(char_count_dict["char"],char_count_dict["count"]))
    print("--- End report ---")

def print_whole_book(book):
    with open(book) as f:
        return f.read()
         
def word_count(book):
    count_list = print_whole_book(book).split()
    count = len(count_list)
    return count

def char_count(book):
    lowercase_book = print_whole_book(book).lower()
    char_dict = {}
    for char in lowercase_book:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] = char_dict[char] + 1
            else:
                char_dict[char] = 1
    return char_dict

def convert_to_char_dict_list(char_dict):
    char_dict_list = []
    for char, count in char_dict.items():
        char_dict_list.append({
            "char": char,
            "count": count
        })

    return char_dict_list

def sort_dict_list(dict_list):
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(dict):
    return dict["count"]

main()