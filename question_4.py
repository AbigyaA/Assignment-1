from collections import deque

def word_ladder(beginWord, endWord, wordList):
    word_set = set(wordList)  
    if endWord not in word_set:
        return 0, []  

    queue = deque([(beginWord, [beginWord])])  
    visited = set([beginWord]) 

    while queue:
        current_word, path = queue.popleft()

        if current_word == endWord:
            return len(path), path

        for i in range(len(current_word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                transformed = current_word[:i] + char + current_word[i + 1:]

                if transformed in word_set and transformed not in visited:
                    queue.append((transformed, path + [transformed]))
                    visited.add(transformed)

    return 0, []  


# Example 
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
steps, sequence = word_ladder(beginWord, endWord, wordList)
print("Steps:", steps)
print("Sequence:", sequence)
