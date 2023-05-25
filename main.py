import random

wordsfile = open("valid-wordle-words.txt")
wordlewordslist = wordsfile.readlines()
wordsfile.close()
for i in range(len(wordlewordslist)):
  wordlewordslist[i] = wordlewordslist[i].strip()
generatednumber = random.randint(0, len(wordlewordslist))
chosenword = wordlewordslist[generatednumber]

print("WORDLE")
print()
i = 0
while i < 6:
  word = str(input("Insert a five letter word: "))
  result = ""
  if word.isalpha() == False:
    print("Your word can only have letters from the alphabet!")
    i -= 1
  elif len(word) != 5:
    print("Your word is not 5 letters long!")
    i -= 1
  elif word not in wordlewordslist:
    print("That's not a valid word!")
    i -= 1
  elif word in wordlewordslist:
    for j in range(len(word)):
      if word[j] == chosenword[j]:
        result += "G-"
      elif word[j] in chosenword:
        result += "Y-"
      else:
        result += "B-"
    result = result[:-1]
    if result == "G-G-G-G-G":
      print(result)
      print("You win!")
      i = 6
    else:
      print(result)
  result = ""
  print()
  i += 1

print("The word was "+chosenword+"!")