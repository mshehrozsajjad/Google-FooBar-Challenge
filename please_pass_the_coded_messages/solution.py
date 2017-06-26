def answer(L):
              L=sorted(L, reverse=True)
              L0=list(x%3 for x in L)
              k=0
              N=len(L)
              remainder=sum(L)%3
              if remainder==0:
                    return sum(x*10**i for x,i in zip(reversed(L),range(len(L))))
              for i,index in zip(reversed(L0),range(N)):
                    if i==remainder:
                          del L[N-1-index]
                          return sum(x*10**i for x,i in zip(reversed(L),range(len(L))))
              for i, index in zip(reversed(L0), range(N)):
                    if i==3-remainder:
                          k+=1
                          del L[N-1-index]
                          if k==2:
                                return sum(x*10**i for x,i in zip(reversed(L),range(len(L))))

