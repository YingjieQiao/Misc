#For a text in English, check how many words are in the text and how many times each word has occurred.
with open('file_1.rtf') as f:
    lines = f.readlines()
    d = {}
    for line in lines:
        thisline = line.split()
        for word in thisline:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1

s = 0
for num in d.values():
    s = s + num


print('There are '+str(s)+' words in this text.')
print(d)

