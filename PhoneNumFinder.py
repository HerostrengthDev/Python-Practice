import re
import pyperclip

print("Hey! Let me find the mobile numbers in your text for you.")

Textblock = input()

FindNums = re.compile(r'04\d\d\d\d\d\d\d\d'|)

FoundNums = FindNums.search(Textblock)

print(f'Phone number found: {FoundNums.group()}. Copied to clipboard')
pyperclip.copy(str(FoundNums.group()))
