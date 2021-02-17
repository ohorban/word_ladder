#!/bin/python3
from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    if start_word == end_word:
        return [start_word]
    if len(start_word) != len(end_word):
        return None
    if _adjacent(start_word, end_word):
        return [start_word, end_word]
    f = open(dictionary_file, 'r')
    allWords = []
    fullStr = f.read()
    for i in range(0, len(fullStr), 6):
        allWords.append(fullStr[i:i+5])
    stack = []
    stack.append(start_word)
    allWords.remove(start_word)
    q = deque([])
    q.append(stack)

    while len(q) > 0:
        currentStack = q.popleft()
        allWords_copy = copy.deepcopy(allWords)
        for word in allWords_copy:
            if _adjacent(word, currentStack[-1]):
                if word == end_word:
                    currentStack.append(word)
                    return currentStack
                newStack = copy.deepcopy(currentStack)
                newStack.append(word)
                q.append(newStack)
                allWords.remove(word)
    return None


def verify_word_ladder(ladder):
    if ladder is None or len(ladder) < 1:
        return False
    elif len(ladder) == 1:
        return True
    for i in range(0, len(ladder)-1):
        if not _adjacent(ladder[i], ladder[i+1]):
            return False
    return True


def _adjacent(word1, word2):
    if (len(word1) != len(word2)):
        return False
    countWrong = 0
    for i in range(0, min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            countWrong += 1
    return countWrong == 1
