class ctn:
    
    def __init__(self) -> None:
        pass

    def charToNum(self, letter):
        """
        Converts an alphabetic character to a number.

        :param letter: The letter to convert.
        :type letter: chr

        :return: The int representation of the letter.
        :rtype: int
        """

        return (ord(letter.lower()) - 97) % 26
    
    def numToChar(self, num):
        """
        Converts a number to a letter.

        :param num: The number to convert.
        :type num: int

        :return: The alphabetic representation of the letter.
        :rtype: chr
        """

        return chr(num % 26 + 97)