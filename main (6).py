word = ['c','o','m','p','u','t','e','r']
goodlist = ['-',"-","-","-","-","-","-","-"]
badlist = []
while len (badlist)<6:
  print("guess a letter")
  letter = input()
  if letter in word:
    word.index(letter)
    position=word.index(letter)
    goodlist[position]=letter 
    print(goodlist)
  else: 
    badlist.append(letter)
    print(badlist)

  if (goodlist == word):
    print ('congrats game complete')
    break


