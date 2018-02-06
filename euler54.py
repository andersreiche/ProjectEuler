#Project euler problem 54
import time
start = time.time()

cards = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

def cardvalue(card):
    if card == "2":
        return 2
    if card == "3":
        return 3
    if card == "4":
        return 4
    if card == "5":
        return 5
    if card == "6":
        return 6
    if card == "7":
        return 7
    if card == "8":
        return 8
    if card == "9":
        return 9
    if card == "T":
        return 10
    if card == "J":
        return 11
    if card == "Q":
        return 12
    if card == "K":
        return 13
    return 14

def checkrank(hand = []):
    #Royal Flush check
    #Same suit check
    if hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] and hand[2][1] == hand[3][1] and hand[3][1] == hand[4][1]:
        #Trickle through T, J, Q, K, A checks
        for a in range(len(hand)):
            if "T" in hand[a]:
                for b in range(len(hand)):
                    if "J" in hand[b]:
                        for c in range(len(hand)):
                            if "Q" in hand[c]:
                                for d in range(len(hand)):
                                    if "K" in hand[d]:
                                        for e in range(len(hand)):
                                            if "A" in hand[e]:
                                                return 10
    
    #Straight Flush check
    #Same suit check
    if hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] and hand[2][1] == hand[3][1] and hand[3][1] == hand[4][1]:
        #Consecutive values check
        for a in range(len(cards)-4):
            for b in range(len(hand)):
                if hand[b][0] == cards[a+1]:
                    for c in range(len(hand)):
                        if hand[c][0] == cards[a+2]:
                            for d in range(len(hand)):
                                if hand[d][0] == cards[a+3]:
                                    for e in range(len(hand)):
                                        if hand[e][0] == cards[a+4]:
                                            return 9
    
    #Straight check
    for a in range(len(cards)-4):
            for b in range(len(hand)):
                if hand[b][0] == cards[a+1]:
                    for c in range(len(hand)):
                        if hand[c][0] == cards[a+2]:
                            for d in range(len(hand)):
                                if hand[d][0] == cards[a+3]:
                                    for e in range(len(hand)):
                                        if hand[e][0] == cards[a+4]:
                                            return 5
    
    #Flush check
    if hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] and hand[2][1] == hand[3][1] and hand[3][1] == hand[4][1]:
        return 6
    
    #Multiple of a kind checks
    kinds = ""
    pairs = 0
    for i in range(len(hand)):
        kinds += hand[i][0]
        kl = list(kinds)
        
    if len(set(kinds)) == 2:          #Four of a kind check
        for i in range(len(cards)):
            if kl.count(str(i)) == 3: #Full house check
                return 7        
        return 8
    elif len(set(kinds)) <= 3:        #Three of a kind check
        for i in range(len(cards)):
            if kl.count(str(i)) == 2:
                pairs += 1
                if pairs == 2:
                    return 3
        return 4
    elif len(set(kinds)) <= 4:        #Two of a kind check
        return 2       
    return 1

def tiebreaker(hand = []):
    res = 0
    for i in range(len(hand)):
        res += cardvalue(hand[i][0])
    return res


player1_score = 0
with open("poker_hands.txt", "r") as f:
    content = f.read()

for row in content.split('\n'):
    if row != "":
        L = row.split()
        player1_hand = L[0:5]
        player2_hand = L[5:10]
        p1_rank = checkrank(player1_hand)
        p2_rank = checkrank(player2_hand)

        if p1_rank > p2_rank:
            player1_score += 1
        if p1_rank == p2_rank:
            if tiebreaker(player1_hand) > tiebreaker(player2_hand):
                player1_score += 1

print(player1_score)
elapsed = (time.time() - start)
print(f"time elapsed: {elapsed} seconds")