from pybedtools import *

a = BedTool('PAC4GC.524-PAC2_0.308_5.bed')
b = BedTool('PAC4GC.524-PAC2_0.312_5.bed')
c = BedTool('PAC4GC.524-PAC2_0.383_5.bed')

# figure this out


ab = a.intersect(b, wa = True,wb=True)
abc = ab.intersect(c , wa = True, wb = True)
ac = a.intersect(c, wa = True, wb = True)
bc = b.intersect(c, wa = True, wb = True)

ab=ab.sort()
abc=abc.sort()
ac=ac.sort()
bc= bc.sort()


print (abc).sort().merge()
print (a+b+c).sort()

print a.sort() == (abc).sort().merge()

