#a simple loop
with open('datasample.txt') as f:
    lines = f.readlines()
    emails1 = []
    for line in lines:
        if '@' in line:
            emails1.append(line.rstrip()) #rstripe() deteles the '\n'
print(emails1)

print('\n')

#using regular expression
import re

with open('datasample.txt') as f:
    contents = f.read()
    
    pattern = re.compile(r'.+@.+\..+')
    #re.compile(r'.+@.+\.(com|edu|net|org)')  "|" means "or"
    #re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)
        
print('\n')

#make it more readable
with open('datasample.txt') as f:
    contents = f.read()
    
    pattern = re.compile(r'(.+)(@)(.+)(\.)(.+)')
    matches = pattern.finditer(contents)
    for match in matches:
        print(match.group(1),match.group(2),match.group(3),match.group(4),match.group(5))
    #this is method is actully not very practical if needs to use these email addresses 
    #because there are blank spaces between each group.
    