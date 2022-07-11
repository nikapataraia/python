import os
from turtle import st
from artist import Artist
import album
import artist
import song
from song import Song
from album import Album

# def buildsong(str):
#         startind = 0
#         endind = 0
#         invar = 0
#         title = ""
#         releaseyear = ""
#         duration = ""
#         likes = ""
#         for let in str:
#             if(let == ','):
#                 var = str[startind:endind]
#                 startind = endind + 1
#                 if(invar == 0):
#                     title = var
#                 if(invar == 1):
#                     for ind in range(len(var)):
#                         if(var[ind] == " "):
#                             var = var[0:ind]
#                             break
#                     duration = float(var) * 60
#                 if(invar == 2):
#                     releaseyear = int(var)
#                 invar = invar + 1
#             endind = endind + 1
#         likes = int(str[startind:endind])
#         return Song(title,releaseyear,duration,likes)

# def buildsonglst(str):
#     res = []
#     startind = 0
#     for ind in range(len(str)):
#         if(str[ind] == "|"):
#             res.append(buildsong(str[startind:ind]))
#             startind = ind + 1
#     res.append(buildsong(str[startind:len(str)]))
#     return res 



# def buildalbum(str):
#     title = ""
#     releaseyear = 0
#     increm = 0
#     startind = 0
#     for ind in range(len(str)):
#         if(str[ind] == ","):
#             if(increm == 0):
#                 title = str[startind:ind]
#                 startind = ind + 1
#             if(increm == 1):
#                 releaseyear = int(str[startind:ind])
#                 startind = ind + 1
#                 break
#             increm = increm + 1
#     res = Album(title,releaseyear)
#     for el in buildsonglst(str[startind+7:len(str)-1]):
#         res.addSongs(el)
#     return res

# def buildalbumlst(str):
#     lst = []
#     startind = 8
#     for ind in range(len(str)):
#         if(str[ind] == "%"):
#             lst.append(buildalbum(str[startind:ind-1]))
#             startind = ind + 1
#     lst.append(buildalbum(str[startind:len(str)]))
#     return lst

# def shred(str):
#     lstofop = [':', '{', '}', ',', '#', '%', '|','[',']','(',')'] #there should not be [,],(,) the simbols but on data3 there were some insistencies so i had to make an exception
#     leftind = 0
#     rightind = 0
#     res = str
#     for ind in range(len(str)):
#         if(str[ind] in lstofop):
#             leftind = ind
#             rightind = ind
#             for left in range(1,ind):
#                 if(str[ind - left] == " "):
#                     leftind = ind - left
#                 else :
#                     break
#             for right in range(1,len(str) - ind):
#                 if(str[ind + right] == " "):
#                     rightind = ind + right
#                 else:
#                     break
#             res = str[0:leftind] + str[ind] + shred(str[rightind+1:len(str)])
#             break
#     return res
    
# def buildartist(str):
#         artname = ""
#         artsurname = ""
#         artbirth = 0
#         artalbums = []
#         singles = []
#         firstind = 0
#         onvar = 0
#         ind = 0
#         for el in str:
#             if(el == ','):
#                 if(onvar == 0):
#                     artname = str[firstind:ind]
#                     firstind = ind + 1

#                 if(onvar == 1):
#                     artsurname = str[firstind:ind]
#                     firstind = ind + 1
#                 if(onvar == 2):

#                     artbirth = int(str[firstind:ind])
#                     firstind = ind + 1
#                     break
#                 onvar = onvar + 1
#             ind = ind + 1    
#         inrec = 0
#         lastofalbumlst = 0
#         for ind in range(firstind,len(str)):
#             if(str[ind] == '{' or str[ind] == '['):
#                 inrec = inrec + 1
#             if(str[ind] == '}' or str[ind] == ']'):
#                 inrec = inrec - 1
#                 if(inrec == 0):
#                     lastofalbumlst = ind
#                     break
#         artalbums = buildalbumlst(str[firstind:lastofalbumlst])
#         singles = buildsonglst(str[(lastofalbumlst+11):len(str)-1])

#         return Artist(artname,artsurname,artbirth,artalbums,singles)

# def buildartistlst(str):
#         lastind = 9
#         lst = []
#         for ind in range(10,len(str)):
#             if(str[ind] == '#'):
#                 lst.append(buildartist(str[lastind:ind]))
#                 lastind = ind + 1
#         lst.append(buildartist(str[lastind:len(str)-1]))
#         return lst

class SpotiPy:
    def __init__(self):
        self.__artists = []

    def getArtists(self):
        return self.__artists
    def addArtists(self,*artists):
        containtsart = False
        for el in artists:
            for lstel in self.getArtists():
                if(el.getFirstName() == lstel.getFirstName() and el.getSecondName() == lstel.getSecondName() and el.getBirthYear() == lstel.getBirthYear()):
                    containtsart = True
            if(not containtsart):
             self.__artists.append(el)
    def getTopTrendingArtist(self):
        likes = float('-inf')
        res = artist.Artist
        for el in self.getArtists():
            if(el.totalLikes() > likes):
                likes = el.totalLikes()
                res = el
        return (res.getFirstName(),res.getSecondName())
    def getTopTrendingAlbum(self):
        likes = float('-inf')
        res = album.Album
        for artel in self.getArtists():
            for alel in artel.getAlbums():
                if(alel.getLikes() > likes):
                    res = alel
                    likes = alel.getLikes()
        return res.getTitle()
    def getTopTrendingSong(self):
        likes = float('-inf')
        res = song.Song
        for arel in self.getArtists():
            for alel in arel.getallsongs():
                if(alel.getLikes() > likes):
                    res = alel
                    likes = alel.getLikes()
        return res.getTitle()

    @classmethod
    def loadFromFile(cls,path):
        def buildsong(str):
         startind = 0
         endind = 0
         invar = 0
         title = ""
         releaseyear = ""
         duration = ""
         likes = ""
         for let in str:
             if(let == ','):
                 var = str[startind:endind]
                 startind = endind + 1
                 if(invar == 0):
                     title = var
                 if(invar == 1):
                     for ind in range(len(var)):
                         if(var[ind] == " "):
                             var = var[0:ind]
                             break
                     duration = float(var) * 60
                 if(invar == 2):
                     releaseyear = int(var)
                 invar = invar + 1
             endind = endind + 1
         likes = int(str[startind:endind])
         return Song(title,releaseyear,duration,likes)

        def buildsonglst(str):
         res = []
         startind = 0
         for ind in range(len(str)):
          if(str[ind] == "|"):
             res.append(buildsong(str[startind:ind]))
             startind = ind + 1
         res.append(buildsong(str[startind:len(str)]))
         return res 

        def buildalbum(str):
          title = ""
          releaseyear = 0
          increm = 0
          startind = 0
          for ind in range(len(str)):
              if(str[ind] == ","):
                  if(increm == 0):
                      title = str[startind:ind]
                      startind = ind + 1
                  if(increm == 1):
                      releaseyear = int(str[startind:ind])
                      startind = ind + 1
                      break
                  increm = increm + 1
          res = Album(title,releaseyear)
          for el in buildsonglst(str[startind+7:len(str)-1]):
              res.addSongs(el)
          return res

        def buildalbumlst(str):
         lst = []
         startind = 8
         for ind in range(len(str)):
           if(str[ind] == "%"):
            lst.append(buildalbum(str[startind:ind-1]))
            startind = ind + 1
         lst.append(buildalbum(str[startind:len(str)]))
         return lst

        def shred(str):
         lstofop = [':', '{', '}', ',', '#', '%', '|','[',']','(',')'] #there should not be [,],(,) the simbols but on data3 there were some insistencies so i had to make an exception
         leftind = 0
         rightind = 0
         res = str
         for ind in range(len(str)):
             if(str[ind] in lstofop):
                 leftind = ind
                 rightind = ind
                 for left in range(1,ind):
                     if(str[ind - left] == " "):
                         leftind = ind - left
                     else :
                         break
                 for right in range(1,len(str) - ind):
                     if(str[ind + right] == " "):
                         rightind = ind + right
                     else:
                         break
                 res = str[0:leftind] + str[ind] + shred(str[rightind+1:len(str)])
                 break
         return res

        def buildartist(str):
         artname = ""
         artsurname = ""
         artbirth = 0
         artalbums = []
         singles = []
         firstind = 0
         onvar = 0
         ind = 0
         for el in str:
            if(el == ','):
                if(onvar == 0):
                    artname = str[firstind:ind]
                    firstind = ind + 1

                if(onvar == 1):
                    artsurname = str[firstind:ind]
                    firstind = ind + 1
                if(onvar == 2):

                    artbirth = int(str[firstind:ind])
                    firstind = ind + 1
                    break
                onvar = onvar + 1
            ind = ind + 1    
         inrec = 0
         lastofalbumlst = 0
         for ind in range(firstind,len(str)):
            if(str[ind] == '{' or str[ind] == '['):
                inrec = inrec + 1
            if(str[ind] == '}' or str[ind] == ']'):
                inrec = inrec - 1
                if(inrec == 0):
                    lastofalbumlst = ind
                    break
         artalbums = buildalbumlst(str[firstind:lastofalbumlst])
         singles = buildsonglst(str[(lastofalbumlst+11):len(str)-1])

         return Artist(artname,artsurname,artbirth,artalbums,singles)

        def buildartistlst(str):
         lastind = 9
         lst = []
         for ind in range(10,len(str)):
            if(str[ind] == '#'):
                lst.append(buildartist(str[lastind:ind]))
                lastind = ind + 1
         lst.append(buildartist(str[lastind:len(str)-1]))
         return lst

        # dir_path = os.path.dirname(os.path.realpath(__file__)) #path to current file.
        res = SpotiPy()
        allartist = []
        templst = []
        strfordata =""
        with open(path) as file:
            for line in file:
                strfordata = strfordata + line.rstrip()
        strfordata = shred(strfordata)
        templst = buildartistlst(strfordata)
        for el in templst:
            res.addArtists(el)
        templst = []
        strfordata = ""
        return res