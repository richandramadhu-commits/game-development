sS={"badminton","racket","net","file","soccer"}
SsS={"soccer","goal","ball","badminton"}
#students who play both
print(sS.intersection(SsS))
print(sS&SsS)
#students who play either but not both
print(sS.symmetric_difference(SsS))
print(sS^SsS)
#students who play only badminton
print(sS.difference(SsS))
print(sS-SsS)