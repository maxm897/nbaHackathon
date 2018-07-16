from astropy.table import Table, Column
import numpy as np

# dictionary structure
# {"gameID":{"playerID": {"plus": 3, "minus": 2, "isActive": true}}, "gameID2": {etc}}

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