import sys


"""Where import statements and any variables should be declared.And if necessary manipulated for global use."""


def find_anagrams(word_for_search, search_list_dictionary):
    """Find dictionary palingrams."""
    pass


def find_palingrams(dictionary_list):
    """Find dictionary palingrams."""
    pass


def print_generic_list(list_items_category_name, list_to_print):
    """Print a list of the items in any list passed to the function. Use the first parameter to describe the list."""
    pass


def find_palindromes(anagram_list):
    """Find palindromes in the anagrams list."""
    pass


def print_pairs_of_twos(dictionary_of_pairs):
    """Print the keywords and values of an dictionary passed to the method."""
    pass


def print_explanation():
    print(
        '''
        An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        typically using all the original letters exactly once. It can however us on a few of the letters.    
        A palindrome is a word, number, phrase, or other sequence of characters which reads the same 
        backward as forward, such as "madam" or "racecar".
    
        A palingram – a letter palingram. A palingram can also be created using syllables
        or words, in addition to individual letters. An example of this using words is, “He was, was he?” 
        Notice that the words can be reversed and the sentence still reads the same. 
        A sentence that is a palingram and a palindrome is, “I did, did I”  
        
        This application allows three activities.
    
          Activity A: Finds the anagrams for any word you enter. Then identifies palindromes, if there are any, 
                      in the identified anagrams. 
    
          Activity B: Finds all the word pairs in the dictionary list which form palingrams. 
                      The palingrams ignore spaces and hyphens.   
                      
          Activity C: Find all the palindromes in the dictionary.
          ''')


def write_anagrams_palindromes_to_file(original_word, anagrams_list, palindromes_list):
    """Write the lists of anagrams and the palindromes to a file.
    Use the original word in the file names and descriptions ."""
    pass


def write_palingrams_to_file(palingram_list):
    """Write the lists of palingrams to a file."""
    pass


def main():
    """The main method with primary functionality of the application."""
    running = True
    pass

# ______________________________________________________________________________


if __name__ == '__main__':
    main()
