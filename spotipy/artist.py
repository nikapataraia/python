from album import Album
import song


class Artist:
    def __init__(self,firstName,lastName,birthYear,albums,singles):
        self.__firstname = firstName
        self.__lastName = lastName
        self.__birthYear = birthYear
        self.__albums = albums
        self.__singles = singles
    def getFirstName(self):
        return self.__firstname
    def getSecondName(self):
        return self.__lastName
    def getBirthYear(self):
        return self.__birthYear
    def getAlbums(self):
        return self.__albums
    def getSingle(self):
        return self.__singles
    def getallsongs(self):
        result = self.getSingle()
        for el in self.getAlbums():
            result = result + el.getSongs()
        return result 
    def mostLikedSong(self):
        fulllst = self.getSingle() + self.getAlbums().getSongs()
        likes = float('-inf')
        res = song.Song
        # resmorethanone = []
        # ismorethanone = False
        for el in fulllst:
            if(el.getLikes() > likes):
                likes = el.getLikes()
                res = el
                # resmorethanone = []
            # if(el.getLikes() == likes):
            #     resmorethanone.append(el)
            #     ismorethanone = True
        # if(ismorethanone): return resmorethanone
        return res




#there can be two songs thjat have same number of likes and i offered code for that to return list, but it is not specified that we should be able to do that so this
# is just an icorrect code. // oh, i just read the note that we can return any of them





    def leastLikedSong(self):
        fulllst = self.getSingle() + self.getAlbums().getSongs()
        likes = float('inf')
        res = song.Song
        # resmorethanone = []
        # ismorethanone = False
        for el in fulllst:
            if(el.getLikes() < likes):
                likes = el.getLikes()
                res = el
        #         resmorethanone = []
        #     if(el.getLikes() == likes):
        #         resmorethanone.append(el)
        #         ismorethanone = True
        # if(ismorethanone): return resmorethanone
        return res
    def totalLikes(self):
        result = 0
        fulllst = self.getSingle()
        for el in self.getAlbums():
            fulllst = fulllst + el.getSongs()
        for el in fulllst:
            result = result + el.getLikes()
        return result
    def __str__(self):
        return "Name: "+  str(self.__firstname) + " " + str(self.getSecondName()) + ",Birth year:" +str(self.__birthYear) + ",Total likes:" + str(self.totalLikes())



