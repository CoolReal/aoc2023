import re
from functools import cmp_to_key
use_real_data = True

file = open('Day7/{}_data7.1.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = raw_data.split('\n')

hands = []

cardTypes = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def getHandType(cardCount):
    if 5 in cardCount:
        return 14
    if 4 in cardCount:
        return 12
    if 3 in cardCount and 2 in cardCount:
        return 10
    if 3 in cardCount:
        return 8
    if cardCount.count(2) == 2:
        return 6
    if 2 in cardCount:
        return 4
    if cardCount.count(1) == 5:
        return 2
    return 0

for line in per_line_data:
    split = line.strip().split(' ')
    cardCount = [0] * len(cardTypes)
    for card in split[0]:
        cardCount[cardTypes.index(card)] += 1
    cardCount[cardCount.index(max(cardCount[:-1]))] += cardCount[-1]
    cardCount[-1] = 0
    handType = getHandType(cardCount)
    hands.append({'hand': split[0], 'bid': split[1], 'handType': handType})

def sortHands(a, b):
    if a['handType'] > b['handType']:
        return 1
    if a['handType'] < b['handType']:
        return -1
    for index, card in enumerate(a['hand']):
        if cardTypes.index(card) > cardTypes.index(b['hand'][index]):
            return -1
        if cardTypes.index(card) < cardTypes.index(b['hand'][index]):
            return 1
    return 0

hands.sort(key=cmp_to_key(sortHands))
totalValue = 0
for index, hand in enumerate(hands):
    totalValue += int(hand['bid']) * (index + 1)
print(totalValue)