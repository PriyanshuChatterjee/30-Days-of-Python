file = open("D:/CodingChallenges/30daysofPython/day_19/michelle_obama_speech.txt", "r")

number_of_lines = 0
number_of_words = 0
for line in file:
  line = line.strip("\n")

  words = line.split()
  number_of_lines += 1
  number_of_words += len(words)

file.close()

print("lines:", number_of_lines, "words:", number_of_words)