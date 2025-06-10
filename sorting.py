ads = [
    {'id': 'A', 'deadline': 2, 'profit': 100},
    {'id': 'B', 'deadline': 1, 'profit': 19},
    {'id': 'C', 'deadline': 2, 'profit': 27},
    {'id': 'D', 'deadline': 1, 'profit': 25},
    {'id': 'E', 'deadline': 3, 'profit': 15},
]

# Sort by profit descending
ads.sort(key=lambda ad: ad['profit'], reverse=True)

# Find the max deadline
max_deadline = max(ad['deadline'] for ad in ads)

# create schedule with empty slots
slots = [None] * max_deadline

total_profit = 0

for ad in ads:
    # place ad in latest available slot before its deadline
    for t in range(ad['deadline'] - 1, -1, -1):  
        if slots[t] is None:
            slots[t] = ad  # Schedule the ad
            total_profit += ad['profit']
            break  # Move on to the next ad

scheduled_ads = [ad['id'] for ad in slots if ad is not None]

print("Scheduled Ads:", scheduled_ads)
print("Total Profit:", total_profit)
