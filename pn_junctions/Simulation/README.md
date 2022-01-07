# Simulation vs Analytical Modeling of a pn Junction
Here different characteristic of different pn junctions are simulated and are compared to the analytical results.

## Abrupt Parallel pn Junction
In this section, the plan is to simulate a parrallel abrupt Si pn diode where the acceptor and donor concentrations are the same at the both side of the junction. The schematic of the mentioned junction is shown in the following figure. 

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/Simulation/pn_diode_str.png)

Silvaco-2017 software were used in order to simulate the diode. The input file is as following:

    # (c) Silvaco Inc., 2019
    go atlas

    mesh  space.mult=1.0
    # 
    y.mesh loc=0.00 spac=0.01 
    y.mesh loc=1.29 spac=0.01
    #
    x.mesh loc=0.00 spac=0.01
    x.mesh loc=0.4 spac=0.01


    region  num=1  silicon

    electr  name=anode  top
    electr  name=cathode  bot

    #....   N-epi doping
    doping  p.type conc=1e17 x.min=0 x.max=0.4 y.top=0.0 y.bottom=0.6 uniform 
    doping  n.type conc=1e17 x.min=0 x.max=0.4 y.top=0.6 y.bottom=1.29 uniform

    solve vanode=0.0
    save outf=pn01_0.str
    tonyplot pn01_0.str -set pn01_0.set

    solve vanode=0.5
    save outf=pn02_0.str
    tonyplot pn02_0.str -set pn02_0.set


    model    conmob  fldmob  srh  auger  bgn

    solve      init

    method newton

    log   outfile=pn01.log
    solve      vanode=0.05  vstep=0.05  vfinal=1  name=anode
    tonyplot pn01.log -set pn01_log.set
    quit

The first line "go atlas" specifies which subrouting the user desire to call. The "atlas" is a subroutin that simulate the electrical properties of a given semicodutor device. 

The "mesh space.mult=1.0" line gives the factor that mesh sizes should be multiplied by. For this case, when its value is one, the mesh sizes given after this line remains unchanged.

The line "y.mesh loc=0.00 spac=0.01" specifies the mesh size (0.01 um) in the y direction [from top (y=0) to bottom] starting from 0 to the next start location of the next "mesh" syntax line. Here, the next mesh line is "y.mesh loc=1.29 spac=0.01", therefore the mesh size from 0 to 1.29 um is 0.01 um. The mesh size of the last "mesh" syntax line should be the same as the mesh size of the one before last "mesh" syntax one, otherwise the mesh size of the one before the last one would be gradualy increased or decreased in order to match the last mesh size. 
