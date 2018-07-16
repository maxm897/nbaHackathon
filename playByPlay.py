from astropy.table import Table, Column
#import Setup

def main():
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
    
    print(groupByGame(nested_arr)["021fd159b55773fba8157e2090fe0fe2"])
    
    
def parse2(line):
    res=[]
    copy = line +"\t"
    while copy!='':
        ind = copy.index("\t")
        res.append(copy[:ind])
        copy=copy[ind+1:]
    return res
    
def parse(line):
    """takes in a line from an array and returns an array of the elements inside in the following order: Game_id	Event_Num
    Event_Msg_Type	Period	WC_Time	PC_Time	Action_Type	Option1	Option2	Option3	Team_id	Person1	Person2	Team_id_type"""
    print(line)
    copy=line+" "
    res=[]
    while copy!='':
        k=before_space(copy)
        if k!='':
            res.append(k)
        copy=copy[copy.index(" ")+1:]
        remove_leading_space(copy)
    print(res)

    return res


def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    end=s.index(" ")
    
    return s[:end]

def remove_leading_space(s):
    """removes leading spaces from s"""
    for i in range(len(s)):
        if s[i].isalnum():
            return s[i:]
        
def groupByGame(nested_arr):
    gamesDict={}
    for arr in nested_arr:
        if arr[0] not in gamesDict:
            gamesDict[arr[0]]=[arr]
        else:
            gamesDict[arr[0]].append(arr)
    return gamesDict
            
    
if __name__=="__main__":
    main()