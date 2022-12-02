# Day 16 Challenge: Create a "Name the Lyrics" game. Write your favorite song lyrics with a word or two missing. The user has to figure out the correct song lyric in as few attempts as possible. Find the true lyric master among you!

print("Fill in the blank lyrics! \n Type in the blank lyrics and see if you are as cool as me.\n ")
counter = 0
while True:
  print("Never going to _______ you up.")
  word=input("Enter the correct word of the above lyric:\n ")
  if word == 'give':
    counter += 1
    break
  else:
    counter += 1
    print("Nope, try again.\n")
print()
if counter == 1:
  print("Well done! it only took you",counter,"attemp to guess right.")
else:
  print("Well done! it took you",counter,"attemps to guess right.")