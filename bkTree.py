from editDistance import levenshtein_distance
def memoize(f):
    memo = {}

    def wrapper(*args):
        key = ''.join(map(str, args))
        if key not in memo:
            memo[key] = f(*args)
        return memo[key]
    return wrapper


class Node:
    def __init__(self, word, distance):
        """
        :param word: node word
        :param distance: node distance from parent node
        """
        self.word = word
        self.distance = distance
        self.children = {}

    def add_node(self, node):
        """
        Adds node to children nodes
        :param node: node to add to children list
        """
        if node.distance in self:
            self.children[node.distance].add_node(node)
        else:
            self.children[node.distance] = node

    def get_node(self, distance):
        """
        Gets node child based on distance
        :param distance: distance of node and child node
        :return: child node
        """
        return self.children[distance]

    def get_children(self):
        """
        :return: all node children
        """
        return self.children

    def __contains__(self, item):
        """
        Checks for node child of distance
        :param item: distance to check for children
        :return: True if child with distance exists else False
        """
        return item in self.children

    def __len__(self):
        """
        :return: number of node children
        """
        return len(self.children)


class BKTree:
    def __init__(self, words=None, distance_func=levenshtein_distance):
        """
        :param words: list of words to add to tree
        :param distance_func: distance function to use, Levenshtein by default
        """
        self.tree = None

        self.distance_func = distance_func

        if words:
            self.load_words(words)



    def load_words(self, words):
        """
        Adds list of words to BK-tree
        :param words: list of words
        """
        words_iterator = iter(words)
        root_word = next(words_iterator)

        self.tree = Node(root_word, 0)

        # NO RECURSION
        for w in words_iterator:
            self.add_word(w)


    def add_word(self, word):
        """
        Adds single word to BK tree
        :param word: single word
        """
        if self.tree is None:
            self.tree = Node(word, 0)
            return

        current_node = self.tree

        while True:
            distance = self.distance_func(word, current_node.word)

            if distance in current_node:
                current_node = current_node.get_node(distance)
            else:
                if word != current_node.word:
                    current_node.add_node(Node(word, distance))
                break

        # NO RECURSION

    @memoize
    def search(self, word, max_distance):
        """
        Performs BK-tree search for word with max distance
        :param word: word to search in BK-tree
        :param max_distance: max distance allowed
        :return: sorted list of tuples of distance and Node (distance, Node)
        """
        if self.tree is None:
            return []

        result = []
        node_buffer = [self.tree]

        while node_buffer:
            node = node_buffer.pop()
            distance = self.distance_func(word, node.word)
            if distance <= max_distance:
                result.append((distance, node))

            low, high = distance - max_distance, distance + max_distance
            node_buffer.extend(n for d, n in node.get_children().items() if low <= d <= high)

        return sorted(result, key=lambda x: x[0])

#
# file = open('google-10000-english.txt')
# list = file.read().split()
# tree = BKTree(words=list)
# while True:
#     t = input('Input: ')
#     result = tree.search(t, 2)
#     if len(result) == 0:
#         print('Not found')
#
#     for i in result[0:5]:
#         if i[0]==0:
#             print('Correct')
#             break
#         else:
#             print(i[1].word)

# list = ['hi','hello','test','help','hold''man']
# tree = BKTree(words=list)

# di = Node('hello',0)
# di.add_node(Node('hi',3))
# test = [di]
# print(di)
# print(test.pop())


