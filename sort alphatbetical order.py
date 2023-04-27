def Func(S):
  W = S.split(" ")
  for i in range(len(W)):
      W[i]=W[i].lower() 
  S = sorted(W)
  print(' '.join(S))
S = "kanava unai vanthu sera nan ingu varam ondru ketan"
Func(S)
