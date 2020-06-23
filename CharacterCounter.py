import pprint
import pyperclip

message = 'The quick brown fox jumped over the lazy dog'
count = {}
for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
pyperclip.copy(str(count))
