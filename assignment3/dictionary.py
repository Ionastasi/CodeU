class Dictionary:
    """Implementation of a Dictionary using trie. Not case-sensitive."""
    def __init__(self):
        self._root = {}
        self._end = "_end"

    def _getLastNode(self, prefix):
        """Internal helper function, that return the next node after this
        prefix in the trie, if this trie contains such prefix.

        Args:
            prefix: a string, prefix that we want to find in the trie.

        Returns:
            `None` if the trie doesn't contain such prefix, or the next node
            of the trie after the last letter of the given prefix.
        """
        prefix = prefix.lower()
        cur_dict = self._root
        for letter in prefix:
            if letter in cur_dict:
                cur_dict = cur_dict[letter]
            else:
                return None
        return cur_dict

    def addWords(self, words):
        """Add new words to the dictionary.

        Args:
            words: a list of strings, words that we want to add.

        Returns:
            None.
        """
        for word in words:
            word = word.lower()
            cur_dict = self._root
            for letter in word:
                cur_dict = cur_dict.setdefault(letter, {})
            cur_dict[self._end] = self._end


    def isWord(self, word):
        """Check if the given word contains in the dictionary.

        Args:
            word: a string, the word that we want to find.

        Returns:
            True if the given word contains in the dictionary, False otherwise.
        """
        last_node = self._getLastNode(word)
        return (last_node is not None and self._end in last_node)

    def isPrefix(self, prefix):
        """Check if the dictionary contains the word with such prefix.

        Args:
            prefix: a string, the prefix that we want to find.

        Returns:
            True if such word contains in the dictionary, False otherwise.
        """
        last_node = self._getLastNode(prefix)
        return (last_node is not None)
