from random import choices
ntrials=10000
player1wins=0
nplayer1dice=3
nplayer2dice=2
player1total=0
player2total=0
for i in range(ntrials):
    dice2=choices(range(1,7),k=nplayer2dice)
    player1wins=player1wins+dice2[0]+dice2[1]
    if dice2[0]==dice2[1]:
        player1wins+=1
        continue
    player1total=player2total+dice2[0]+dice2[1]
    dice1=choices(range(1,7),k=nplayer1dice)
    dice1.sort(reverse=True)
    player1total=player1total+dice1[0]+dice1[1]
    if player1total>player2total:
        player1wins = player1wins+1
print("Average player 1 will win=",player1wins/ntrials)
