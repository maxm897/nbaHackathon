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

        if parsed[2] in ['1','3','8']:

            nested_arr.append(parsed);

    event_dict=groupByGame(nested_arr)

    game_file = open("Basketball_Analytics/NBA Hackathon - Game Lineup Data Sample (50 Games).txt")
    arr2=[]
    nested_arr2=[]
    for line in game_file:
        arr2.append(line)
    arr2.remove(arr2[0])
    for j in range(len(arr2)):
        parsed2=parse2(arr2[j])
        nested_arr2.append(parsed2)

    lineup_dict=groupByGame(nested_arr2)
    ##maps game id to nested array of lineups
    for game in lineup_dict:

        #print(lineup_dict[game])
        quarter_dict=groupByQuarter(lineup_dict[game], 1)

        lineup_dict[game]=quarter_dict


    for game in event_dict:
        quarter_dict=groupByQuarter(event_dict[game], 3)

        event_dict[game]=quarter_dict


    for game in event_dict:
        game_stats={}
        if game not in stats:
            stats[game]={}
        for quarter in event_dict[game]:
            lineup = processLineup(lineup_dict[game][quarter])

            q = processQ(event_dict[game][quarter], lineup)
            game_stats[quarter]=q
        stats[game]=game_stats


    print(stats)



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

def groupByQuarter(nested_arr, pos):
    quartersDict={}
    for arr in nested_arr:

        if arr[pos] not in quartersDict:

            quartersDict[arr[pos]]=[arr]
        else:
            quartersDict[arr[pos]].append(arr)

        if(pos==3):
            for quarter in quartersDict:
                print(quartersDict[quarter])
                sorted=sortEvents(quartersDict[quarter])
                quartersDict[quarter]=sorted

    return quartersDict

def processQ(quarter, startLineup):
    """returns a dictionary mapping players to stats"""
    players=startLineup
    for event in quarter:
        if event[2]=='1':
            processMadeShot(event, players)
        elif event[2]=='3':
            processFT(event, players)
        elif event[2]=='8':
            processSub(event, players)
        else:
            print("something has gone horribly wrong")
    return players

def processMadeShot(event, players):
    """adds the proper point amount to the active players on the correct team, subtracts from active players on other team"""
    for player in players:
        if event[10]==players[player]["team"] and players[player]["isActive"]==True:
            players[player]["plus"]+=int(event[7])
        elif players[player]["isActive"]==True:
            players[player]["minus"]-=int(event[7])

def processFT(event, players):
    for player in players:
        if event[10]==players[player]["team"] and players[player]["isActive"]==True:
            players[player]["plus"]+=int(event[7])
        elif players[player]["isActive"]==True:
            players[player]["minus"]-=int(event[7])

def processSub(event, players):
    player_in=event[12]
    player_out=event[11]
    if player_in in players:
        players[player_in]["isActive"]=True
    else:
        players[player_in] = {"plus":0, "minus":0, "team": event[10], "isActive": True}
    players[player_out]["isActive"]=False


def processLineup(nest):
    """returns a dictionary of the 10 active players mapped to a dictionary with keys plus, minus, team, and isActive"""
    lineup = {}

    for arr in nest:

        lineup[arr[2]]={"plus":0, "minus":0, "team": arr[3], "isActive": True}
    return lineup



if __name__=="__main__":
    main()
