deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4


def deal(deck):
  hand = []
  for i in range(2):
     random.shuffle(deck)
     card = deck.pop()
     hand.append(card)
  return hand

def blackjack:
  print("Start")
  
   Dhand = deal(deck)
   Phand = deal(deck)


if __name__ == "__main__":
   blackjack()
