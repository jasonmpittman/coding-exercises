__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Activity Selection:
Given a set of activities, along with the starting and finishing time of each activity, find the maximum number of activities performed by a single person assuming that a person can only work on a single activity at a time.

Input : [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: {(1, 4), (5, 7), (8, 11), (12, 14)}

Input : [(3, 7), (1, 3), (2, 9), (2, 7), (1, 2), (7, 8)]
Output: {(1, 3), (3, 7), (7, 8)} or {(1, 2), (3, 7), (7, 8)} or {(1, 2), (2, 7), (7, 8)}

Started: Mar 27, 2024 @ 4:50am ET
Intervals: 1
Ended: March 27, 2024 @ 5:20am ET
"""
from sys import argv

def select_activities(activities: list) -> list:
    sorted_activities = sorted(activities, key = lambda x: x[1])

    selected_activities = [sorted_activities[0]]
    prev_finish_time = sorted_activities[0][1]

    # Iterate through sorted activities and select sequential activities
    for activity in sorted_activities[1:]:
        start_time, finish_time = activity
        if start_time >= prev_finish_time:
            selected_activities.append(activity)
            prev_finish_time = finish_time

    return selected_activities


if __name__ == "__main__":
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)] 

    selected = select_activities(activities)
    print(selected)