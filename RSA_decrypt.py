import gmpy2
from gmpy2 import c_mod,mpz,powmod,f_mod
from gmpy2 import isqrt_rem,isqrt
import sys

#Challenge 1
N1 = mpz(179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581)

(A,rem) = isqrt_rem(N1)
A = A + 1       #compute the ceiling..
delta = A**2 - N1
(x,rem) = isqrt_rem(delta) 
(p,q) = (A-x,A+x)
print "Challenge 1 solution: ",min(p,q)

N2 =mpz(648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877)
A=isqrt(N2)
A = A + 1  #ceil
while(True):
	delta = A**2 - N2
	x = isqrt(delta)
	(p,q) = (A - x,A + x)
	if N2 == p*q:
		print "Challenge 2 solution",min(p,q)
		break
	A=A+1

N3 =mpz(720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929)

A = isqrt(N3*6)
A2 = 2*A + 1
res = isqrt_rem(A2**2 - 24*N3)
  