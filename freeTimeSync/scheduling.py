from datetime import datetime
import random
import time
from icalendar import Calendar, Event
from pytz import UTC
def parseCal(file):
    g = open(file,'rb')
    gcal = Calendar.from_ical(g.read())
    for component in gcal.walk():
        if component.name == "VEVENT":
            print(component.get('summary'))
            print(component.get('dtstart').dt > component.get('dtend').dt)
            #print(component.get('dtstamp'))
    g.close()


def intersection(*events):
    maximum = max([i[0] for i in events])
    minimum = min([i[1] for i in events])
    return (maximum,minimum)

#print(intersection((7,8),(7.5,10)))

person1 = [(0,.5),(1,2),(2.1,2.4),(5,6),(6.2,7.2),(9,11.5),(12.5,3)]
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
def binaryFilter(tuples,low, high):
    ends = [i[1] for i in tuples]
    starts = [i[0] for i in tuples]
    p1 = binary_search(ends,low) #this could either be a real start time too high or too low
    p2 = binary_search(starts[p1:],high) #this could either be a real start time too high or too low
    #we want start times after the largest end time, and end times lower than the lowest start
    print(tuples[p1:p1+p2])
    if ends[p1] > low:
        p1 = p1- 1 if p1 > 0 else 0
    if starts[p1+p2] < high:
        p2 = p2+1 if p2 < len(tuples[p1:])-1 else len(tuples[p1:])-1
    return tuples[p1:p1+p2]

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

#parseCal('basic.ics')

t = freeTime(person1)
print(t)
print(binaryFilter(t,1.5,11.5))
#l = [1,2,4,5,7,8,9,11,15,17,20,21]
#print(l[binary_search(l,10)])
