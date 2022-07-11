def frequency(text):
  retdict = {}
  for let in text:
    if let in retdict:
      x = int(retdict[let])
      retdict.update({let : x+1})
    else :
      retdict[let] = 1
  return retdict