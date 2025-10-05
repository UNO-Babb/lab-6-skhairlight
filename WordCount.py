#WordCount.py
#Name: Salsabiel Khair Allah
#Date: Oct.5
#Assignment: Lab 6

def main():
  textFile = open("gettysberg.txt", 'r')

  lineCount = 0
  wordCount = 0
  charCount = 0
  
  for line in textFile:
    lineCount += 1
    words = line.split()
    wordCount += len(words)
    charCount += len(line)
  textFile.close()

  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Characters:", charCount)
  

if __name__ == '__main__':
  main()
