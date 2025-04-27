from collections import Counter

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents.lower()


def get_word_count(text_block):

    c = text_block.split()
    num_words = len(c)
    return f"Found {num_words} total words"

def get_character_count(text_block):
    count_dict = Counter(text_block)
    return count_dict

def get_sorted_counts(char_dict):
    char_list = [{'char': k, 'num': char_dict[k]} for k in char_dict]
    return sorted(char_list, key=lambda x: x['num'], reverse=True)

