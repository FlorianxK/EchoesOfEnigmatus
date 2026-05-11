from math import lcm
from typing import *

def dayThree():
    points = []
    #read
    with open("Day3/3_1.txt") as file:
        for line in file:
            x,y = [ int(a.split('=')[1]) for a in line.strip().split() ]
            points.append( (x,y) )

    def move(x,y,days):
        diag = x+y-1
        newX = ((x-1+days)%diag)+1
        newY = diag-newX+1
        return newX,newY
    
    res = 0
    for x,y in points:
        newX,newY = move(x,y,100)
        res += newX+(100*newY)
    return res

def dayThree2():
    points = []
    #read
    with open("Day3/3_2.txt") as file:
        for line in file:
            x,y = [ int(a.split('=')[1]) for a in line.strip().split() ]
            points.append( (x,y) )

    days = 0
    step = 1
    for x,y in points:
        mod = x+y-1
        rem = y-1

        while days%mod != rem:
            days += step

        step = lcm(step,mod)
    
    return days

def dayThree3():
    points = []
    #read
    with open("Day3/3_3.txt") as file:
        for line in file:
            x,y = [ int(a.split('=')[1]) for a in line.strip().split() ]
            points.append( (x,y) )

    days = 0
    step = 1
    for x,y in points:
        mod = x+y-1
        rem = y-1

        while days%mod != rem:
            days += step

        step = lcm(step,mod)
    
    return days

def main():
    print("Hallo")
    print(dayThree(), "ist die Lösung von Teil 1")
    print(dayThree2(), "ist die Lösung von Teil 2")
    print(dayThree3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()