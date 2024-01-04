# 1
"""
import random

def generate_random_number():
    return str(random.randint(1, 100))


def files():
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        name = i + ".txt"
        file = open(name, "w")
        file.write(generate_random_number())
        file.close()


files()

file_summary = open("summary.txt", "w")

for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    name = i + ".txt"
    file = open(name, "r")
    txt = file.read()
    file_summary.write(f"name:{name} txt:{txt}\n")
    file.close()
file_summary.close()
"""
# 2
"""
file1 = open("file1.txt", "r")
txt = file1.read()
file1.close()

file2 = open("file2.txt", "w")
file2.write(txt)
"""
# 3
"""
import random
import csv

players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

with open('game_scores.csv', mode='w') as file:
    writer = csv.writer(file)

    for i in range(1, 101):
        for j in players:
            score = random.randint(0, 1000)
            writer.writerow([f'{j}, {score}'])
"""
# 4
"""
import csv

def last_list(reader):
    all_scores = []
    for i in reader:
        if i != []:
            all_scores.append(i)
    return all_scores


def max_score(all_scores, writer):
    players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

    for i in range(len(players)):
        temp_list = []
        for j in range(i, len(all_scores), 5):
            txt = str(all_scores[j][0])
            txt = txt.split()
            temp_list.append(int(txt[1]))
        max_score = max(temp_list)
        writer.writerow([f"{players[i]}, {max_score}"])


with open('high_scores.csv', 'w') as file1:
    writer = csv.writer(file1)
    with open('game_scores.csv', 'r') as file2:
        reader = csv.reader(file2)
        all_scores = last_list(reader)
        max_score(all_scores, writer)
"""
