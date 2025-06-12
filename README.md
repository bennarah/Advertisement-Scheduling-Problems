# Advertisement Scheduling Problem
Bassma Ennarah bennarah@csu.fullerton.edu


This project solves the Advertisement Scheduling Problem using a greedy algorithm.

Each advertisement has:
- An ID
- A deadline (the latest time it can be scheduled)
- A profit (earned if scheduled on or before its deadline)

Each ad takes 1 unit of time. The goal is to schedule ads to maximize total profit without overlapping ads.

## How the Algorithm Works

1. Sort the ads in decreasing order of profit.
2. For each ad, try to schedule it in the latest available time slot before its deadline.
3. If a time slot is free, schedule the ad and add its profit to the total.
4. Return the list of scheduled ad IDs and the total profit.

## Time Complexity

- Sorting: O(n log n)
- Scheduling: O(n × d), where d is the maximum deadline
- Worst-case time complexity: O(n²)

## Example Input

```python
ads = [
    {'id': 'A', 'deadline': 2, 'profit': 100},
    {'id': 'B', 'deadline': 1, 'profit': 19},
    {'id': 'C', 'deadline': 2, 'profit': 27},
    {'id': 'D', 'deadline': 1, 'profit': 25},
    {'id': 'E', 'deadline': 3, 'profit': 15},
]
