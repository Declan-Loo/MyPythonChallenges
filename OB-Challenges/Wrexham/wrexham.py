class Wrexham:
    def __init__(self, playernumber, forename, surname, position, communityinvolvement = 0, injured = False):
        self.__playernumber = playernumber
        self.__forename = forename
        self.__surname = surname
        self.__position = position
        self.__communityinvolvement = communityinvolvement
        self.__injured = injured
        
    def GetPlayerInfo(self):
        return 'NAME: ' + self.__forename  + ' ' + self.__surname + '\nPOSITION: ' + self.__position
    
    def ChangeCommunityInvolvement(self, change):
        self.__communityinvolvement += change
    
    def ChangeInjured(self):
        if self.__injured == False:
            self.__injured = True
        else:
            self.__injured = False
            
import os
wrexham_database = []
try:
    with open('wrexham.txt','r') as f:
        num_lines = len(f.readlines())
        f.seek(0)
        
        for i in range(num_lines//4):
            playernum = f.readline().strip()
            firstname = f.readline().strip()
            lastname = f.readline().strip()
            position = f.readline().strip()
            wrexham_database.append(Wrexham(playernum,firstname,lastname,position))
            
except IOError:
    print("Cannot find file. Current directory:",os.getcwd())

for i in wrexham_database:
    print(i.GetPlayerInfo())
    print()
