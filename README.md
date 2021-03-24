# Word Ladders with Stacks and Queues
[![](https://github.com/ohorban/word_ladder/workflows/tests/badge.svg)](https://github.com/ohorban/word_ladder/actions?query=workflow%3Atests)

I will implement a solution to Lewis Carroll's [word ladder game](https://en.wikipedia.org/wiki/Word_ladder).

**Learning Objectives:**

1. implement a complex algorithm involving both queues and stacks
1. understand python memory management
1. practice translating pseudocode into python

## Background

A word ladder is a list of words where each word differs by only a single letter from the previous word.
For example, we can convert a `stone` into `money` using the following ladder:

```
stone
shone
shote
shots
soots
moots
motts
motes
motey
money
```

A function `word_ladder` generates these word ladders.
There are many possible algorithms to generate word ladders,
but a simple one uses a combination of stacks and queues as shown in the following pseudocode.

```
Create a stack
Push the start word onto the stack
Create a queue
Enqueue the stack onto the queue

While the queue is not empty
    Dequeue a stack from the queue
    For each word in the dictionary
        If the word is adjacent to the top of the stack
            If this word is the end word
                You are done!
                The front stack plus this word is your word ladder.
            Make a copy of the stack
            Push the found word onto the copy
            Enqueue the copy
            Delete word from the dictionary
```
