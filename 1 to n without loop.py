from typing import List
def printNos(x: int) -> List[int]: 
    if x==0:
        return []
    ans=printNos(x-1)
    ans.append(x)
    return ans
