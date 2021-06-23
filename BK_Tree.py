from EditDistance import editDistance
from collections import deque
# class BK_Tree:
#     def __init__(self,list,DistanceFunction):
#         self.df = DistanceFunction
#         self.root = list[0]
#         self.tree = (list[0],{})
#     def builder(self,list):
#         for word in list[1:]:
#             self.tree = self.insert(self.tree,word)
#
#     def insert(self,node,word):
#         dist = self.df(word,node[0])
#         if dist not in node[1]:
#             node[1][dist] = (word,{})
#         else:
#             self.insert(node[1][dist],word)
#         return node
#
#     def spell_checker(self,testword, n):
#         def search(node):
#             dist = self.df(testword,node[0])
#             output=[]
#             if dist<=n:
#                 output.append(node[0])
#             for i in range(dist-n,dist+n+1):
#                 child = node[1]
#                 if i in child:
#                     output.extend(search(node[1][i]))
#             return output
#         root = self.tree
#         return search(root)
# if __name__ == '__main__':
#     file = open('words_alpha.txt')
#     list = file.read().split()
#     tree = BK_Tree(list, editDistance)
#     tree.builder(list)
    # print(tree.spell_checker('hell',2))

class BKTree:
    def __init__(self,DistanceFunction):
        self.tree = None
        self.DistanceFunction = DistanceFunction

    def insert(self,node):
        if self.tree is None:
            self.tree = (node,{})
            return
        current,children = self.tree
        while True:
            dist = self.DistanceFunction(node,current)
            target = children.get(dist)
            if target is None:
                children[dist] = (node,{})
                break
            current,children = target
    def search(self, node, radius):
        if self.tree is None:
            return []

        candidates = deque([self.tree])
        result = []
        while candidates:
            candidate, children = candidates.popleft()
            dist = self.DistanceFunction(node, candidate)
            if dist == 0:
                return 0
            if dist <= radius:
                result.append(candidate)
            low, high = dist - radius, dist + radius
            candidates.extend(c for d, c in children.items()
                              if low <= d <= high)

        return result

# tree = BKTree(editDistance)
# file = open('google-10000-english.txt')
# list = file.read().split()
# for item in list:
#     tree.insert(item.lower())
# print(tree.search('hello',1))

