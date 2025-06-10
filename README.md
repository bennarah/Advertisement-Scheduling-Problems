# Advertisement-Scheduling-Problems

# Instructions

Assume that you are giving 𝑛 advertisement slots. Each slot has:
• A unique ID
• A deadline (the latest time by which it must be completed)
• A profit (earned if the job is completed before or on its deadline)
The goal is to schedule advertisements slots or jobs such that the total profit is maximized and
each slot takes 1 unit of time. Each slot is scheduled as late as possible before its deadline (if a slot
is available). An example is given below:
Sample Input:
Jobs = [
{id: 'A', deadline: 2, profit: 100},
{id: 'B', deadline: 1, profit: 19},
{id: 'C', deadline: 2, profit: 27},
{id: 'D', deadline: 1, profit: 25},
{id: 'E', deadline: 3, profit: 15}, ]
Sample Output:
Scheduled Jobs: ['A', 'C', 'E']
Total Profit: 142
Design an algorithm that returns the maximum number of advertisements jobs to be aired, subject
to the latest deadline (3). Your algorithm must ensure maximization of profit.
