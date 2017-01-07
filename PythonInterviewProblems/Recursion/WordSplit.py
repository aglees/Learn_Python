def word_split(phrase, list_of_words, output = None):

    # find word in string
    # lannch function again to find words in input string
    # return None if can't be found
    # whole string function needs to be covered to be good

    if list_of_words == []:
        return []

    output = []

    for word in list_of_words:

        if word in phrase:

            list_of_words.remove(word)
            newphrase = phrase.replace(word, '')
            output.append(word)
            output.extend(word_split(newphrase, list_of_words))

            for outputword in output:
                phrase = phrase.replace(outputword, '')

            if phrase == '':
                return output
            else:
                return []
    return []

def word_split2(phrase, list_of_words, output=None):
    '''
    Note: This is a very "python-y" solution.
    '''

    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []

    # For every word in list
    for word in list_of_words:

        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):

            # Add the word to the output
            output.append(word)

            # Recursively call the split function on the remaining portion
            # of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split2(phrase[len(word):], list_of_words, output)

    # Finally return output if no phrase.startswith(word) returns True
    return output

print(word_split2('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']))
#print(word_split('themanran',['clown','ran','man']))
