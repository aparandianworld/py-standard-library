#!/usr/bin/env python3

players = [
    {"name": "Alex", "scores": [85, 92, 78, 95]},
    {"name": "Emma", "scores": [88, 87, 91, 99]},
    {"name": "Jordan", "scores": [72, 80, 85, 78]},
    {"name": "Sam", "scores": [95, 94, 96, 93]},
    {"name": "Taylor", "scores": [80, 85, 88, 82]},
    {"name": "Casey", "scores": [90, 92, 89, 91]},
]

players_with_avg = []
average_score = 0

for player in players:
    average_score = sum(player["scores"]) / len(player["scores"])
    players_with_avg.append({"name": player["name"], "scores": average_score})

# print(players)
# print(players_with_avg)

print(sorted(players_with_avg, key = lambda x: x["scores"], reverse = True))