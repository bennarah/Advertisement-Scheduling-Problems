ads = [
    {'id': 'A', 'deadline': 2, 'profit': 100},
    {'id': 'B', 'deadline': 1, 'profit': 19},
    {'id': 'C', 'deadline': 2, 'profit': 27},
    {'id': 'D', 'deadline': 1, 'profit': 25},
    {'id': 'E', 'deadline': 3, 'profit': 15},
]

# Sort by profit descending
ads.sort(key=lambda ad: ad['profit'], reverse=True)
