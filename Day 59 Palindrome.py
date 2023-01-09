# Day 59 challenge
def palindrome(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])
item = input("enter the word: ").capitalize()
print(item[1:-1])
print(palindrome(item))