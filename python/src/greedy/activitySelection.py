# https://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/
# Activity Selection problem
# Example 1 : Consider the following 3 activities sorted by
# by finish time.
#      start[]  =  {10, 12, 20};
#      finish[] =  {20, 25, 30};
# A person can perform at most two activities. The
# maximum set of activities that can be executed
# is {0, 2} [ These are indexes in start[] and
# finish[] ]

# Example 2 : Consider the following 6 activities
# sorted by by finish time.
#      start[]  =  {1, 3, 0, 5, 8, 5};
#      finish[] =  {2, 4, 6, 7, 9, 9};
# A person can perform at most four activities. The
# maximum set of activities that can be executed
# is {0, 1, 3, 4} [ These are indexes in start[] and
# finish[] ]

def activitySelection(start, finish):
    if (len(start) == 0 or len(finish) == 0):
        return -1
    prevFinishValue = 0
    for i in range(0,len(finish)):
        if (start[i] >= prevFinishValue):
            prevFinishValue = finish[i]
            print("[ %i , %i ]" %(start[i], finish[i]))

start  = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

pair = [(start[i],finish[i]) for i in range(0,len(finish))]
print(pair)
activitySelection(start, finish);
