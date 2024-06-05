__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Job Sequencing:
Given a list of tasks with deadlines and total profit earned on completing a task, find the maximum profit earned by executing the tasks within the specified deadlines. Assume that each task takes one unit of time to complete, and a task can’t execute beyond its deadline. Also, only a single task will be executed at a time.

Started: June 05, 2024 @ 6:25am ET
Intervals: 1
Ended: June 05, 2024 @ 6:55am ET
"""
class Job:
    def __init__(self, taskId, deadline, profit):
        self.taskId = taskId
        self.deadline = deadline
        self.profit = profit

def schedule_jobs(jobs: list, T):
    profit = 0
    time_slot = [-1] * T

    jobs.sort(key=lambda x: x.profit, reverse=True)

    for job in jobs:
         for j in reversed(range(job.deadline)):
              if j < T and time_slot[j] == -1:
                   time_slot[j] = job.taskId
                   profit += job.profit
                   break
    
    print('Schedule of jobs: ', list(filter(lambda x: x != -1, time_slot)))
    print('Profit is: ', profit)

if __name__ == "__main__":
    jobs = [
        Job(1, 9, 15), Job(2, 2, 2), Job(3, 5, 18), Job(4, 7, 1), Job(5, 4, 25),
        Job(6, 2, 20), Job(7, 5, 8), Job(8, 7, 10), Job(9, 4, 12), Job(10, 3, 5)
    ]
    
    schedule_jobs(jobs, 15)