from astropy.table import Table, Column
from setup import *


def main():
    stats = {}
    file = open("Basketball_Analytics/NBA Hackathon - Play by Play Data Sample (50 Games).txt", "r")
    arr = []
    nested_arr=[]
    for line in file:
        arr.append(line)
    arr.remove(arr[0])
    for k in range(len(arr)):
        parsed=parse2(arr[k])
        print(parsed[2])
        if parsed[2] in ['1','3','8']:

            nested_arr.append(parsed);

    dict=groupByGame(nested_arr)

    for game in dict:
        quarter_dict=groupByQuarter(dict[game])

        dict[game]=quarter_dict


    for game in dict:
        if game not in stats:
            stats[game]={}
        for quarter in dict[game]:
            processQ(dict[game][quarter])





def parse2(line):
    res=[]
    copy = line +"\t"
    while copy!='':
        ind = copy.index("\t")
        res.append(copy[:ind])
        copy=copy[ind+1:]
    return res



def groupByGame(nested_arr):
    gamesDict={}
    for arr in nested_arr:
        if arr[0] not in gamesDict:
            gamesDict[arr[0]]=[arr]
        else:
            gamesDict[arr[0]].append(arr)
    return gamesDict

def groupByQuarter(nested_arr):
    quartersDict={}
    for arr in nested_arr:
        if arr[3] not in quartersDict:
            quartersDict[arr[3]]=[arr]
        else:
            quartersDict[arr[3]].append(arr)

        for quarter in quartersDict:
            sorted=sortEvents(quartersDict[quarter])
            quartersDict[quarter]=sorted

        return quartersDict

def processQ(quarter):
    for event in quarter:
        if event[2]=='1':
            processMadeShot(event)
        elif event[2]=='3':
            processFT(event)
        elif event[2]=='8':
            processSub(event)
        else:
            print("something has gone horribly wrong")

def processMadeShot(event):


if __name__=="__main__":
    main()
