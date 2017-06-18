from dictionary import Dictionary


class GridWord:
    """ A class that represents a path in the grid and a corresponding word.

    Fields:
        _last_position:    a tuple of length 2 that represents the coordinates
                           of the last position in the path;
        _visited_position: a set of tuples that contains all coordinates
                           in this path;
        _word:             a string, the word that corresponds to the path.
    """
    def __init__(self, last = None, visited = None, word = ''):
        self._last_position = last
        if visited is None:
            self._visited_positions = set()
        else:
            self._visited_positions = visited
        self._word = word

    def getLastPosition(self):
        return self._last_position

    def getWord(self):
        return self._word

    def appendPosition(self, i, j, symbol):
        self._last_position = (i, j)
        self._visited_positions.add(self._last_position)
        self._word += symbol

    def containsPosition(self, i, j):
        return (i, j) in self._visited_positions

    def copy(self):
        return GridWord(self._last_position,
                        self._visited_positions.copy(), self._word)


def wordSearch(rows, cols, grid, dictionary):
    """Given a grid of letters and a dictionary, find all the words from the
    dictionary that can be formed in the grid. Not case-sensitive.

    Args:
        rows: an int, number of rows in the grid;
        cols: an int, number of columns in the grid;
        grid: 2-dimensional array of chars, a grid of letters;
        dictionary: a Dictionary, that contains possible words.

    Returns:
        set of all words found.
    """

    # find all possible chars in the grid, that can be a prefix of some word
    current_words = list()
    for i in range(rows):
        for j in range(cols):
            if dictionary.isPrefix(grid[i][j]):
                tmp = GridWord()
                tmp.appendPosition(i, j, grid[i][j])
                current_words.append(tmp)

    found = set()

    # bfs
    while current_words:
        gridWord = current_words.pop()
        word = gridWord.getWord()
        if dictionary.isWord(word):
            found.add(word)
        i, j = gridWord.getLastPosition()
        # iterate through all adjacent cells (i+di, j+dj)
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                ii, jj = i+di, j+dj
                if (ii in range(rows) and jj in range(cols)
                                    and not gridWord.containsPosition(ii, jj)):
                    symbol = grid[ii][jj]
                    if not dictionary.isPrefix(word + symbol):
                        continue
                    tmp = gridWord.copy()
                    tmp.appendPosition(ii, jj, symbol)
                    current_words.append(tmp)
    return found
