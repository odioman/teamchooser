from random import choice

players = ['Bilbo', 'Gandalf', 'Thorin',
           'Dwalin', 'Balin', 'Bifur', 'Bombur',
           'Bofur', 'Oin', 'Gloin', 'Ori', 'Nori']
print(players)

teamA = []
teamB = []
teamC = []
teamD = []

while len(players) > 0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)

    if players == []:
        break

    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)

    if players == []:
        break

    playerC = choice(players)
    teamC.append(playerC)
    players.remove(playerC)

    if players == []:
        break

    playerD = choice(players)
    teamD.append(playerD)
    players.remove(playerD)

    if players == []:
        break

print('Team A:', teamA)
print('Team B:', teamB)
print('Team C:', teamC)
