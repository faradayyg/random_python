def make_word_dict(word):
  word_dict = dict()
  for letter in word:
    word_count = word_dict.get(letter, 0)
    word_dict[letter] = word_count + 1

  return word_dict

def is_anagram(word1, word2):
  word1_dict = make_word_dict(word1)
  word2_dict = make_word_dict(word2)
  return word1_dict == word2_dict


def CountingAnagrams(input):
  words = input.split(" ")
  distinct_words = list(set(words))
  anagram_count = 0
  word_pair  = []
  for outer_index, outer_word in enumerate(distinct_words):
    for inner_index, inner_word in enumerate(distinct_words):
      if is_anagram(inner_word, outer_word) and outer_index != inner_index:
        anagram_count += 1

  print(anagram_count)
  return anagram_count//2


print('Test 1 passed: {}'.format(CountingAnagrams('cars are very cool so are arcs and my os') == 2))
print('Test 2 passed: {}'.format(CountingAnagrams('a b c d run urn urn') == 1))
print('Test 3 passed: {}'.format(CountingAnagrams('arcs cars casr racs') == 6))
print('Test 3 passed: {}'.format(CountingAnagrams('arcs are really nice') == 0))
print('Test 3 passed: {}'.format(CountingAnagrams('a b b b') == 0))
print('Test 3 passed: {}'.format(CountingAnagrams('') == 0))


"""
Have the function  CountingAnagrams(str) take
the str parameter and determine how many anagrams
exist in the string. An anagram is a new word that is
produced from rearranging the characters in a different word,
for example: cars and arcs are anagrams.
Your program should determine how many anagrams exist in a
given string and return the total number.
For example: if str is "cars are very cool so are arcs and my os"
then your program should return 2 because "cars" and "arcs"
form 1 anagram and "so" and "os" form a 2nd anagram.
The word "are" occurs twice in the string but it isn't an
anagram because it is the same word just repeated.
The string will contain only spaces and lowercase letters,
no punctuation, numbers, or uppercase letters
"""