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
    all_words = []
    full_str = f.read()
    for i in range(0, len(full_str), 6):
        all_words.append(full_str[i : i+5])
    stack = []
    stack.append(start_word)
    all_words.remove(start_word)
    q = deque([])
    q.append(stack)

    while len(q) > 0:
        current_stack = q.popleft()
        all_words_copy = copy.deepcopy(all_words)
        for word in all_words_copy:
            if _adjacent(word, current_stack[-1]):
                if word == end_word:
                    current_stack.append(word)
                    return current_stack
                new_stack = copy.deepcopy(current_stack)
                new_stack.append(word)
                q.append(new_stack)
                all_words.remove(word)
    return None


def verify_word_ladder(ladder):
    if ladder is None or len(ladder) < 1:
        return False
    elif len(ladder) == 1:
        return True
    for i in range(0, len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    if (len(word1) != len(word2)):
        return False
    count_wrong = 0
    for i in range(0, min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            count_wrong += 1
    return count_wrong == 1
