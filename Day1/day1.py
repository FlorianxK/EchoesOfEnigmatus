from collections import deque
from typing import *

def dayOne():
    maxNum = 0

    def eni(N,EXP,MOD):
        score = 1
        arr = deque([])
        for _ in range(EXP):
            score = (score*N)%MOD
            arr.appendleft(str(score))
        return int(''.join(arr))

    #read
    with open("Day1/1_1.txt") as file:
        for line in file:
            h = {}
            vals = [ x.split('=') for x in line.strip().split() ]
            for letter,num in vals:
                h[letter] = int(num)
            res = eni(h['A'],h['X'],h['M']) + eni(h['B'],h['Y'],h['M']) + eni(h['C'],h['Z'],h['M'])
            maxNum = max(maxNum,res)
    
    return maxNum

def dayOne2():
    maxNum = 0

    def eni(N,EXP,MOD):
        val = ""
        for i in range(5):
            val += str( pow(N,EXP-i,MOD) )
        return int(val)

    #read
    with open("Day1/1_2.txt") as file:
        for line in file:
            h = {}
            vals = [ x.split('=') for x in line.strip().split() ]
            for letter,num in vals:
                h[letter] = int(num)
            res = eni(h['A'],h['X'],h['M']) + eni(h['B'],h['Y'],h['M']) + eni(h['C'],h['Z'],h['M'])
            maxNum = max(maxNum,res)
    
    return maxNum

def dayOne3():
    maxNum = 0

    def eni(N,EXP,MOD):
        cycle = []
        i = 0
        while True:
            toAdd = pow(N,EXP-i,MOD)
            if toAdd not in cycle:
                cycle.append(toAdd)
            else:
                break
            i += 1
        boundary = EXP%len(cycle)
        while pow(N,boundary,MOD) != cycle[0]:
            boundary += len(cycle)
        
        num_cycles = (EXP-boundary)//len(cycle)
        res = sum(cycle)*num_cycles
        for i in range(1,boundary+1):
            res += pow(N,i,MOD)
        return res

    #read
    with open("Day1/1_3.txt") as file:
        for line in file:
            h = {}
            vals = [ x.split('=') for x in line.strip().split() ]
            for letter,num in vals:
                h[letter] = int(num)
            res = eni(h['A'],h['X'],h['M']) + eni(h['B'],h['Y'],h['M']) + eni(h['C'],h['Z'],h['M'])
            maxNum = max(maxNum,res)
    
    return maxNum

def main():
    print("Hallo")
    print(dayOne(), "ist die Lösung von Teil 1")
    print(dayOne2(), "ist die Lösung von Teil 2")
    print(dayOne3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()