# It's tournament time for your volleyball league, but many of your teammates are out of town for the long weekend.
# Sounds like we'll have to make some substitutions! Tasks (3): Use a list operation to replace "Iliana" with "Jack"
# ( sub_1 ). Replace "Anders" with "Celeste" ( sub_2 ). Replace "Gabrielle" with "Mary" ( sub_3 ). It's match time.
# Go team!

players = ["Iliana", "Samuel", "Anders", "Teresa", "Gabrielle", "Alejandro"]
sub1 = "Jack"
players.pop(0)
players.insert(0, sub1)
sub2 = "Celeste"
players.pop(2)
players.insert(2, sub2)
sub3 = "Mary"
players.pop(4)
players.insert(4, sub3)

print(players)
