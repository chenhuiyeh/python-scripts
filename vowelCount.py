import re, pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

# counts number of vowels in a message/string
def vowelCount(message):
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    vowelList = vowelRegex.findall(message)

    count = {}

    for i in range(len(vowelList)):
        count.setdefault(vowelList[i], 0)
        count[vowelList[i]] = count[vowelList[i]] + 1

    pprint.pprint(count)

# counts number of consonants in a string message
def consonantCount(message):
    consonantRegex = re.compile(r'[^aeiouAEIOU\s,.]')
    consonantList = consonantRegex.findall(message)

    count = {}

    for i in range(len(consonantList)):
        count.setdefault(consonantList[i], 0)
        count[consonantList[i]] = count[consonantList[i]] + 1
    pprint.pprint(count)

consonantCount(message)
vowelCount(message)
