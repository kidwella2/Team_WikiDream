'''import for highlighted text'''
from termcolor import colored

class Search(object):
    def __init__(self): pass
    def isHighlighted(self, value):
        """
                :param value:
                    User input
                :return:
                    Boolean for true/false if highlighted

                Examples:

                >>> Search().isHighlighted('cat')
                Search: True
                >>> Search().isHighlighted('rock')
                Search: False
                """
        exampleText = 'one two cat ball house run pet shoe alpaca pizza cat'
        '''get user input'''
        value = input("Search: ")
        '''boolean for if highlighted'''
        highlighted = False
        '''loop through all the words and ignores case'''
        '''changes boolean to true if word is in the text'''
        for v in exampleText.lower().split():
            if v in value:
                highlighted = True

        '''return true or false if result is highlighted'''
        return highlighted

    def search(self, value):
        """
                :param value:
                    User input
                :return:
                    Highlighted text

                Examples:

                >>> Search().search('sock')
                Search: 'one two cat ball house run pet shoe alpaca pizza cat'
                """
        exampleText = 'one two cat ball house run pet shoe alpaca pizza cat'
        '''get user input'''
        value = input("Search: ")
        '''stores highlighted results'''
        highlightedResult = []
        '''loop through all the words and ignores case'''
        '''highlights green if match, else remains unaffected'''
        for v in exampleText.lower().split():
            if v in value:
                highlightedResult.append(colored(v, 'grey', 'on_green'))
            else:
                highlightedResult.append(v)

        '''statement that contains output with highlighted results'''
        result = " ".join(highlightedResult)
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()