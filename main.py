from stats import get_word_count, get_book_text, get_character_count, get_sorted_counts
import sys

def main():

    if len(sys.argv) != 2:
        print(
           'Usage: python3 main.py <path_to_book>' 
        )
        sys.exit(1)
    else:

        word_block = get_book_text(sys.argv[1])
        character_count = get_character_count(word_block)
        g = get_sorted_counts(character_count)
        print('============ BOOKBOT ============')
        print('Analyzing book found at books/frankenstein.txt...')
        print('----------- Word Count ----------')   
        print(get_word_count(word_block))
        print('--------- Character Count -------') 
        
        for d in g:
            if d['char'].isalpha():
                print(f'{d['char']}: {d['num']}' )



if __name__ == "__main__":
    main()


