import json
import pickle
import sys
from typing import List


def get_lexicon_from_file(filename: str) -> List[str]:
    """extract lexicon from binary file
    
    Args:
        filename: path to binary file with the lexicon.pkl

    Returns: list of all the words in the lexicon
    """
    try:
        with open(filename, 'rb') as lexicon_file:
            data = pickle.load(lexicon_file)
            return list(data)
    except FileNotFoundError as e:
        print(f"file does not exist: {e}")
        sys.exit()

def is_phrase_valid(phrase: str, lexicon: List[str]) -> bool:
    """checks if a phrase is a valid one
    do that by checking if all the words in that phrase are valid ones

    Args:
        phrase: the phrase to check
        lexicon: list of all the words in a specific language
    
    Returns: whether the phrase is valid or not

    """
    words_in_phrase = phrase.split()
    for word in words_in_phrase:
        if not (word in lexicon):
            return False
    return True

def offset_character(char, characters, offset):
    """offset a character by a specific index (roll characters if offset extends the end of the characters)
    
    Args:
        char: the char to change
        characters: all the characters in a specific language in order
        offset: the amount of characters to move the current one backwards
    Returns: the character after offset
    """
    return characters[(characters.index(char) - offset)%len(characters)]

def get_characters_from_file(filename) -> List[str]:
    """get all characters of the language from file
    
    Args:
        filename: path to the characters file
    
        Returns: list with all of the characters within the file in the same order
    """
    characters = list()
    try:
        with open(filename, 'r', encoding='utf-8') as characters_file:
            for character in characters_file:
                characters.append(character[0])
            return characters
    except FileNotFoundError as e:
        print(f"file does not exist: {e}")
        sys.exit()

def decipher_phrase(phrase, lexicon_filename, abc_filename) -> dict:
    """decipher a phrase and return it can or cannot be deciphered.
    this function only checks movement of characters by a specific offset
    
    Args:
        phrase: the sentence to decipher
        lexicon_filename: path to lexicon.pkl file 
        abc_filename: path to a file with all of the english characters
    
    Returns: dictionary with all the data needed about the phrase in the following format:
    {"status": (int) if can be decipher or not, "orig_phrase": phrase, "K": the offset of characters}
    """
    print(f'starting deciphering using {lexicon_filename} and {abc_filename}')
    if phrase == "":
        return {"status": 0, "orig_phrase": '', "K": -1}
    lexicon = get_lexicon_from_file(lexicon_filename)
    characters = get_characters_from_file(abc_filename)
    for offset in range(len(characters)):
        modified_phrase = ''.join(c if c == ' ' else offset_character(c, characters, offset) for c in phrase)
        if is_phrase_valid(modified_phrase, lexicon):
            return {"status": 1, "orig_phrase": modified_phrase, "K": offset}
    return {"status": -1, "orig_phrase": phrase, "K": -1}

students = {'id1': '315155531', 'id2': '000000000'}

if __name__ == '__main__':
    with open('config-decipher.json', 'r') as json_file:
        config = json.load(json_file)

    # note that lexicon.pkl is a serialized list of 10,000 most common English words
    result = decipher_phrase(config['secret_phrase'],
                             config['lexicon_filename'],
                             config['abc_filename'])

    assert result["status"] in {1, -1, 0}

    if result["status"] == 1:
        print(f'deciphered phrase: {result["orig_phrase"]}, K: {result["K"]}')
    elif result["status"] == -1:
        print("cannot decipher the phrase!")
    else:  # result["status"] == 0:
        print("empty phrase")
