#WordIndex.py
#Name: Salsabiel Khair Allah
#Date: Oct.5
#Assignment: Lab 6

def main():
  textFile = open("fish.txt", 'r')
  
  words = {} #create an empty dictionary

  lineNum = 0
  for line in textFile:
    lineNum += 1
    lineWords = line.strip().split()

    for word in lineWords:
      word = word.strip(".,!?;:\"'()[]{}").lower()
      if word == "":
        continue

      if word not in words:
        words[word] = [lineNum]
      else:
        if lineNum not in words[word]:
          words[word].append(lineNum)

  textFile.close()

  for word in sorted(words):
    print(word, ":", words[word])
    

if __name__ == '__main__':
  main()
