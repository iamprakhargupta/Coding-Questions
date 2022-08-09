def solution(S):

  letters = ['a', 'b', 'c']
  reqLetter = 0
  count = 0
  word=S
  c = 0
  while c < len(word):
      if word[c] == letters[reqLetter]:
          c += 1
      elif word[c] != letters[reqLetter]:
          count += 1
      reqLetter = (reqLetter + 1) % 3
  return count

print(solution("bcaaa"))