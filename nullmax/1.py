import sys

T = int(input())
ns = []
for _ in range(T):
    ns.append(int(input()))

for n in ns:
    cards = [i for i in range(1, n + 1)]
    while len(cards) >= 2:
        sys.stdout.write(str(cards[0])+' ')
        del cards[0]
        temp = cards[0]
        cards = cards[1:]
        cards.append(temp)
    sys.stdout.write(str(cards[0])+'\n')
