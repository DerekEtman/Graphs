# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.
# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None

# Here are steps to solve (almost) any graph problems:
    # 1.Translate the problem into graph terminology
    # 2.Build your graph
    # 3.Traverse your graph

def find_ladders(begin_word, end_word):
    '''
    Find a word transformation between beginning word and end word
    use BFS
    '''

    q = Queue()
    # Enqueue path to starting word
    q.enqueue([begin_word])
    visited = set()
    # while queue is not empty...
    while q.size() > 0:
        # Dequeue path
        path = q.dequeue()
        # Grab  last word form __path__
        # chevk if its been visited, if not...
            # mark it visited
            # enqueue a path to each neighbor
