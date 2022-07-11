
class Song:
    def __init__(self,title, releaseYear, duration = 60, likes = 0):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__duration = duration
        self.__likes = likes
    
    def getTitle(self):
        return self.__title
    def getReleaseYear(self):
        return self.__releaseYear
    def getDuration(self):
        return self.__duration
    def getLikes(self):
        return self.__likes
    def setDuration(self,newdur):
        if(newdur < 0 or newdur > 720 or newdur == self.__duration):
            return False
        else: 
            self.__duration = newdur 
            return True
    def like(self):
        self.__likes = self.__likes + 1
    def unlike(self):
        self.__likes = self.__likes - 1
    def durinmin(self):
        return self.__duration/60
    def __str__(self) -> str:
        return "Title:" + str(self.__title) +  ",Duration:" + str(self.durinmin()) + " minutes,Release year:" + str(self.__releaseYear) + ",Likes:" + str(self.__likes)



