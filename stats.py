def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
        word_list = text.split()
        return len(word_list)

def get_chars_dictionary(text):
    chars = {}
    for c in text.lower():
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    return chars

def get_filtered_char_list(chars_dictionary):
    sorted_list = []
    
    for char in chars_dictionary:
         sorted_list.append({
              "char": char,
              "num": chars_dictionary[char]
         })
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(items):
    return items["num"]