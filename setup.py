from astropy.table import Table, Column
import numpy as np

# dictionary structure
# {"gameID": {quarter: {"playerID": {"plus": 3, "minus": 2, "isActive": true}}}, "gameID2": {etc}}

# t = Table()
# table['Game_ID'] = Column()
# table['Player_ID'] = Column()
# table['Plus'] = Column()
# table['Minus'] = Column()
# table['Is_Active'] = Column()

def updateActive(dict, gameID, playerID, activity):
    """Changes a players Is_Active column to the activity value"""
    dict[gameID][playerID]["isActive"] = activity

def isActive(dict, gameID, playerID):
    """Returns true if player is currently active, false otherwise"""
    return dict[gameID][playerID]["isActive"]

def addPlus1(dict, gameID, playerID):
    dict[gameID][playerID]["plus"] += 1

def addPlus2(dict, gameID, playerID):
    dict[gameID][playerID]["plus"] += 2

def addPlus3(dict, gameID, playerID):
    dict[gameID][playerID]["plus"] += 3

def addMinus1(dict, gameID, playerID):
    dict[gameID][playerID]["minus"] += 1

def addMinus2(dict, gameID, playerID):
    dict[gameID][playerID]["minus"] += 2

def addMinus3(dict, gameID, playerID):
    dict[gameID][playerID]["minus"] += 3

def sortEvents(gameArr):
    """Given: an array containing all the events belonging to a given quarter where
    each event is, itself, an array (that array is a line of the events.txt file).
    Returns: the same array, now reorded so that each event array is sorted by game
    clock time"""
    result = [];
    
    result.append(gameArr[0])
    for i in range(1, len(gameArr)):
        if(type(i)!=int):
            inserted = False
            for j in range(0, len(result)):
                if ((gameArr[i][6] <= result[j][6]) and (not inserted)):
                    result.insert(j, gameArr[i][6])
                    inserted = True
            if not inserted:
                result.append(gameArr[i][6])

    return result;
