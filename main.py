name = input("Enter file name: ")

try:
  handle = open(name)
except:
  print("There is no such file: " + name)
  quit()

count = dict()
for line in handle:
  words = line.split()
  for word in words:
    count[word] = count.get(word, 0) + 1


bigCount = None
bigWord = None
for word,counts in count.items():
  if bigCount is None or counts > bigCount:
    bigWord = word
    bigCount = counts

print(bigWord, bigCount)