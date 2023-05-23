"""ou have been recruited by your friend, a linguistics enthusiast, to create a utility tool that can perform analysis on a given piece of text. Complete the class 'analysedText' with the following methods -

    Constructor (__init__) - This method should take the argument text, make it lower case, and remove all punctuation. Assume only the following punctuation is used: period (.), exclamation mark (!), comma (,) and question mark (?). Assign this newly formatted text to a new attribute called fmtText.
    freqAll - This method should create and return dictionary of all unique words in the text, along with the number of times they occur in the text. Each key in the dictionary should be the unique word appearing in the text and the associated value should be the number of times it occurs in the text. Create this dictionary from the fmtText attribute.
    freqOf - This method should take a word as an argument and return the number of occurrences of that word in fmtText.

The skeleton code has been given to you. Docstrings can be ignored for the purpose of the exercise.
Hint: Some useful functions are replace(), lower(), split(), count()
The lower() function converts all characters in the string to lowercase.

The replace() function takes two arguments: the text to search for and the text to replace it with. Try calling this function for each punctuation you want to remove and replace it with a blank character, ''

You can define a class attribute and assign it a value with the following generic recipe: self.attribute_name = value
Try calling the <code>freqAll</code> method you implemented above and assign it to a variable. You will now have a dictionary with the unique words that appear in fmtText as the keys, and the number of times they appear as the value.

You can use this dictionary to return the number of occurrences of the word that was given as an argument to the <code>freqOf</code> method.

If the word given as an argument does not appear in the text, return 0. You can check if a string is a key in the dictionary using the following code recipe: <code>if item in my_dictionary:</code>
</details>
"""

# class analysedText(object):
#     def __init__ (self, text):
#         TODO: Remove the punctuation from <text> and make it lower case.
#         TODO: Assign the formatted text to a new attribute called "fmtText"
#         pas s
#     def freqAll(self):
#         TODO: Split the text into a list of words
#         TODO: Create a dictionary with the unique words in the text as keys
#         and the number of times they occur in the text as values
#         pass # return the created dictionary
#     def freqOf(self, word):
#         TODO: return the number of occurrences of <word> in <fmtText>
#         pass

class analysedText(object):
    """creating a class and methods"""
    def __init__ (self, text):
        """initial state"""
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        # make text lowercase
        formattedText = formattedText.lower()
        self.fmtText = formattedText

    def freqAll(self):
        """splitting"""
        # split text into words
        wordList = self.fmtText.split(' ')
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        return freqMap

    def freqOf(self,word):
        """tryng to get some stuff"""
        # get frequency map
        freqDict = self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
