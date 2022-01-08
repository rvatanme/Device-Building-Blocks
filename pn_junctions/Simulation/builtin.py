import math
ni = 1.08e10   #/cm3
Eth = 0.0259    #eV
Vth = 0.0259    #V
ND = NA = 1e18
eps0 = 8.85e-14  #C/V.cm
di = 11.7
q = 1.6e-19   #C
psi_bi = Vth*math.log(ND*NA/(ni**2))
for i in range(4):
    ND = NA = 10**(15+i)
    psi_bi = Vth*math.log(ND*NA/(ni**2))
    xi_m = math.sqrt(2*q*NA*ND*psi_bi/(eps0*di*(NA+ND)))
    WD = (2*psi_bi/xi_m)*(1e3)   #um
    WDp = WDn = WD/2
    print ("NA=ND=%s   psi_bi=%s   xi_m=%s   WD=%s"% (ND,psi_bi,xi_m,WD))
