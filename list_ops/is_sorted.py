def isSorted(lst):
  checker = 0
  if len(lst)==0 : return 1
  if lst[0]<lst[1]: checker = 1
  else : checker = -1
  for index in range(len(lst) - 1) :
    if(checker == 1):
      if(lst[index + 1] < lst[index]) :
        return 0
    else:
      if(lst[index + 1] > lst[index]) :
        return 0
  return checker 