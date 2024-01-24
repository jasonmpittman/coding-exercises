__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Beserk Monsters: https://codeforces.com/problemset/problem/1922/D

Example:
    3 5 3,4,7,5,10 4,9,1,18,1

    
Started: Jan 24, 2024 @ 5:15am ET
Intervals: 1
Ended: Jan 24, 2024 @ 5:30am ET
"""
from sys import argv

def beserk(number_of_rounds: int, number_of_monsters: int, monsters_attack_values: list, monsters_hp_values: list):
    monsters_attack_values = [int(x) for x in monsters_attack_values]
    monsters_hp_values = [int(x) for x in monsters_hp_values]

    monsters = list(zip(monsters_attack_values, monsters_hp_values))

    for i in range(number_of_rounds):
        monsters_died = 0
        new_monsters = []
        for j in range(number_of_monsters):
            left = j - 1 if j - 1 >= 0 else number_of_monsters - 1
            right = j + 1 if j + 1 < number_of_monsters else 0

            attack = monsters[j][0]
            hp = monsters[j][1] - monsters[left][0] - monsters[right][0]

            if hp > 0:
                new_monsters.append((attack, hp))
            else:
                monsters_died += 1

        monsters = new_monsters
        number_of_monsters = len(monsters)

        print(f"Round {i+1}: {monsters_died} monsters died")


if __name__ == '__main__':
    number_of_rounds = int(argv[1])
    number_of_monsters = int(argv[2])
    monsters_attack_values = argv[3].split(',')
    monsters_hp_values = argv[4].split(',')

    beserk(number_of_rounds, number_of_monsters, monsters_attack_values, monsters_hp_values)
