# Simulation vs Analytical Modeling of a MOS Capacitor
In this section, the electrical properties of MOS capacitor obtained from numerical simulation were compared with those of obtained from the analytical 
equation.

## MOS Capacitor
A MOS capacitor (shown in the following figure) with 1e18 /cm3 p-doping concentration is simulated under different biases.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/Simulation/MOS_str.png)

The following silvaco input file was used to simulate the mentioned device. 

    # Single Gate MOS Capacitor Example

    go atlas

    mesh 

    x.m l=0 spac=1
    x.m l=1 spac=1

    y.m l=-0.0015 spac=0.0001
    y.m l=0 spac=0.0001
    y.m l=0.1 spac=0.02
    y.m l=0.5 spac=0.2

    region num=1 silicon y.min=0
    region num=2 oxide y.max=0

    electrode name=gate top
    electrode name=substrate bottom

    doping uniform conc=1e18 p.type

    save outf=quantumex02.str

    # DC analysis
    go atlas

    mesh inf=quantumex02.str

    models cvt srh print
    output con.band val.band

    method trap carr=2 maxtrap=10
    solve init

    solve vgate=0.0
    save outf=mos01_0.str
    tonyplot mos01_0.str

    solve vgate=-0.5
    save outf=mos02_0.str
    tonyplot mos02_0.str

    solve vgate=0.5
    save outf=mos03_0.str
    tonyplot mos03_0.str

    solve vgate=0 vstep=0.1 vfinal=1.5 name=gate 
    save outf=classical.str

    tonyplot classical.str

    quit


In this example, first the device structure is defined and save in the quantumex02.str file and later this file is loaded for DC analysis.

Under DC bias and no current flow, the "trap" method is used to overcome the poor convergence. One should take care of this convergence issue particulary in devices such as MOS that operate under different regimes in a wide range of voltage ramp. The effect of "trap" is to reduce the bias step if convergence problems are detected. TRAP automatically cuts the bias step in half and tries to obtain a solution for the bias that the convergence have been not achieved. If this solution does not converge, the bias step will be halved again. This procedure is repeated up to a maximum number of tries set by the
METHOD parameter MAXTRAPS. The default for MAXTRAPS is 4. 

The following figure shows the potential and electron concentration profile of the mentioned MOS along y direction in three diffent bias -2, 0, 2 V.

![]()

