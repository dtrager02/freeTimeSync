from datetime import datetime
import random
import time
def intersection(*events):
    maximum = max([i[0] for i in events])
    minimum = min([i[1] for i in events])
    return (maximum,minimum)

print(intersection((7,8),(7.5,10)))

person1 = [(5,6),(9,11.5),(12.5,3)]
person2 = [(4,5.5),(9,11.5),(12.5,3)]
people = [person1,person2]

def freeTime(person):
    current = 0
    free = []
    while(len(person)):
        event = person.pop(0)
        free.append((current,event[0]))
        current = event[1]
    free.append((current,current+24))
    return free

numbers = []
i = random.randint(8,9)
while i < 1000:
    numbers.append(i)
    i+= random.randint(1,5)
#print(numbers[:20])

#filters out any numbers outside the range desired
#TODO convert to work with tuples of (start time, end time)
def binaryFilter(nums,low, high):
    p1 = binary_search(nums,low)
    p2 = binary_search(nums[p1:],high)
    if p1 > low:
        p1 = p1- 1 if p1 > 0 else 0
    if p2 < high:
        p2 = p2+1 if p2 < len(nums[p1:])-1 else len(nums[p1:])-1
    return nums[p1:p1+p2]

#standard binary search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            break
 
    # If we reach here, then the element was not present
    return mid
start = time.time()
for i in range(1000):
    binaryFilter(numbers,random.randint(20,50),random.randint(100,200))
print(time.time()-start)

#print(freeTime(person1))
