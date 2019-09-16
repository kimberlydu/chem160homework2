from random import choices
ntrials=10000
player1wins=0
nplayer1dice=3
nplayer2dice=2
for i in range(ntrials):
    dice=choices(range(1,7),k=ndice)
    player1wins=player1wins+dice[0]+dice[1]
    if dice[0]==dice[1]:
        player1wins+=1
        continue
    else
        dice=choices(range(1,7),k=ndice)
        dice.sort(reverse=True)
        player1wins=player1wins+dice[0]+dice[1]
    if player1wins>player1wins
print("Average roll=",player1wins/ntrials)
