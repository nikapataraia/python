from song import Song

class Album:
    def __init__(self,title,releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []
    def getTitle(self):
        return self.__title
    def getReleaseYear(self):
        return self.__releaseYear
    def getSongs(self):
        return self.__songs
    def addSongs(self, *songlst):
        num = 0
        for arr in songlst:
            if(arr in self.__songs): pass
            else: 
                self.__songs.append(arr)
                num = num+1
        return num
    def sortBy(self, bykey, reverse):
        return sorted(self.getSongs(), key=bykey, reverse= not reverse)
    def sortByName(self,reverse):
        return self.sortBy(lambda x : x.getTitle,reverse)
    def sortByPopularity(self,reverse):
        return self.sortBy(lambda x : x.getLikes(),reverse)
    def sortByDuration(self,reverse):
        return self.sortBy(lambda x: x.getDuration(),reverse)
    def sortByReleaseYear(self,reverse):
        return self.sortBy(lambda x: x.getReleaseYear(),reverse)
    def __str__(self):
        stri = "Title:" + str(self.__title) + ",Release year:" + str(self.__releaseYear)+ ",songs:{"
        for el in self.getSongs():
            stri = stri + el.__str__() + "|"
        return stri.rstrip(stri[-1]) + "}"
    def str(self):
        stri = "Title:" + str(self.__title) + ",Release year:" + str(self.__releaseYear)+ ",songs:{"
        for el in self.getSongs():
            stri = stri + el.__str__() + "|"
        return stri.rstrip(stri[-1]) + "}"
    def getLikes(self):
        res = 0
        for el in self.getSongs():
            res = res = el.getLikes()
        return res 


# rattlestarSong = song.Song('Snake Jazz', 9)
# majorSong = song.Song('Space Oddity', 10, 315)
# queenSong = song.Song('Teo Torriatte', 20, 355, 132178)
# snakeJazz = song.Song('Snake Jazz', 30, 30)
# a = song.Song("lol" , 100)
# b = song.Song("L" , 200)
# greenSide = Album("Green side",1976)
# greenSide.getTitle()
# greenSide.addSongs(snakeJazz)
# greenSide.addSongs(majorSong, rattlestarSong, a,b)
# lst = greenSide.sortByReleaseYear(reverse=True)
# lst = sorted(greenSide.getSongs(),key= lambda x : x.getReleaseYear(), reverse= False)
# for el in lst:
#     print(el.getReleaseYear())

# snakeJazz = song.Song('Snake Jazz', 1989, 30)
# majorSong = song.Song('Space Oddity', 1969, 60, 12000)
# greenSide = Album("Green side",1976)
# greenSide.addSongs(snakeJazz,majorSong)
# print(greenSide)





    
