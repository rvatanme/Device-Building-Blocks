# Simulation vs Analytical Modeling of Schottky Diode
Here, silvaco software is used to simulate the I-V curve of a Schottky diod and the results are compared with analytical results.

## I-V Characteristic of a Schottky Diode
When metal makes contact with a semiconductor, a barrier is formed at the metal-semiconductor interface. This barrier is responsible for controlling the current conduction as well as its capacitance behavior. This means that as long as the nature of metal and semicoductor remains the same, the IV characteristic of a schottky diod doesn't change with doping of semiconductor. The following schottky diode is simulated.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MS_Contacts/Simulation/schot-diode-str.png)

The input silvaco file for a schottky diode is as following:

    # (c) Silvaco Inc., 2019
    go atlas

    mesh  space.mult=1.0
    # 
    x.mesh loc=0.00 spac=0.5
    x.mesh loc=3.00 spac=0.2
    x.mesh loc=5.00 spac=0.25
    x.mesh loc=7.00 spac=0.25
    x.mesh loc=9.00 spac=0.2
    x.mesh loc=12.00 spac=0.5
    #
    y.mesh loc=0.00 spac=0.1
    y.mesh loc=1.00 spac=0.1
    y.mesh loc=2.00 spac=0.2
    y.mesh loc=5.00 spac=0.4


    region  num=1  silicon

    electr  name=anode  top
    #electr  name=anode  x.min=5  length=2
    electr  name=cathode  bot

    #....   N-epi doping 
    doping  n.type conc=1e16 uniform

    #....   Guardring doping 
    #doping   p.type conc=1e19 x.min=0  x.max=3  junc=1 rat=0.6 gauss
    #doping   p.type conc=1e19 x.min=9 x.max=12 junc=1 rat=0.6 gauss

    #....   N+ doping 
    #doping  n.type conc=1e20 x.min=0 x.max=12 y.top=2 y.bottom=5 uniform

    model    conmob  fldmob  srh  auger  bgn 
    contact    name=anode workf=4.97

    solve      init

    method newton

    solve vanode=0.0
    save outf=diodeex01_0.str
    tonyplot diodeex01_0.str -set diodeex01_0.set

    log   outfile=diodeex01.log
    solve      vanode=0.05  vstep=0.05  vfinal=1  name=anode
    tonyplot diodeex01.log -set diodeex01_log.set
    quit
   
   
This input almost the same as the input used to simulate a p-n junction, except that the anode contact is a schottky contact with the workfunction of 4.97 eV. Since the electron affinity of Si is 4.17, the schottky contact barrier is 0.8 eV. The schottky contact is defined in silvaco by "contact    name=anode workf=4.97" syntax.

The following figure a and b shows the potential profile and IV characteristic of the simulated schottky diod, respectively, from cathode to anode. As expected and concluded from analytical form, the depletion width is decreased by increasing doping concentration in the semiconductor side. The turn-on potential is found to be around 0.4 V which is half of the barrier hight.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MS_Contacts/Simulation/Schot-diode-char.png)

The following figure shows the change of build-in potential and forward IV characteristic of a shcottky diode with different work functions for schottky contact where the doping concentration of the n-doping layer remains the same.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MS_Contacts/Simulation/schot_IV_wf.png)

It is clear from the figure that both build-in potential and turn-on voltage increase with increasing the workfunction of the metal. The change of build in potential and turn-on voltage are both equal to the change in workfunction value. The same prediction is concluded from the analytical form provided in MS-Contact chapter. Since the q??</sub>n</sub> is constant and the barrier hight is increased due to increasing the workfunction, the build-in potential must be increased in order to keep the thermal equilibrium. The turn-on voltage is dependent on the barrier hight, as the barrier hight increases the turn-on voltage also increases. This voltage is 0.5, 0.75 and 1 for the workfunction of 5, 5.25 and 5.5 eV. The diode with a lower barrier hight shows highr current compared to that with higher barrier hight before the turn-on voltage. The turn-on voltage is lower than the original barrier hight due to image force lowering phenomena.

The following figure shows the depletion width of the schottky diode under three different reverse biases. The WD2 graph is corresponded to the depletion capacitance of the diode in the unit of F/cm2.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MS_Contacts/Simulation/dep_width_schot.png)

