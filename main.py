def getLetterOccurences(my_text):
    my_dict = {} 
    my_lower_text = my_text.lower()
    for my_letter in my_lower_text:
        if my_letter in  my_dict:
            my_dict[my_letter] += 1
        else:
            my_dict[my_letter] = 1
    
    return my_dict

def book_report(path,word_count,book_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()

    my_symbols = list(book_dict.keys())



    my_symbols.sort()

    print(my_symbols)
    for my_symbol in my_symbols:
        if my_symbol.isalpha():
            print(f" The '{my_symbol}' character was found {book_dict[my_symbol]} times")
    

path = "books/frankenstein.txt"
with open(path) as f:
    file_contents = f.read()
    my_word_count = len(file_contents.split())
    my_dict = getLetterOccurences(file_contents)
    print(my_dict)
    book_report(path,my_word_count,my_dict)


