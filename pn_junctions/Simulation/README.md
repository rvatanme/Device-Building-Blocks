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
    

    model    conmob  fldmob  srh  auger  bgn

    method newton

    solve      init

    solve vanode=0.0
    save outf=pn01_0.str
    tonyplot pn01_0.str -set pn01_0.set

    solve vanode=0.5
    save outf=pn02_0.str
    tonyplot pn02_0.str -set pn02_0.set

    log   outfile=pn01.log
    solve      vanode=0.05  vstep=0.05  vfinal=1  name=anode
    tonyplot pn01.log -set pn01_log.set
    quit

The first line "go atlas" specifies which subrouting the user desire to call. The "atlas" is a subroutin that simulate the electrical properties of a given semicodutor device. 

The "mesh space.mult=1.0" line gives the factor that mesh sizes should be multiplied by. For this case, when its value is one, the mesh sizes given after this line remains unchanged.

The line "y.mesh loc=0.00 spac=0.01" specifies the mesh size (0.01 um) in the y direction [from top (y=0) to bottom] starting from 0 to the next start location of the next "mesh" syntax line. Here, the next mesh line is "y.mesh loc=1.29 spac=0.01", therefore the mesh size from 0 to 1.29 um is 0.01 um. The mesh size of the last "mesh" syntax line should be the same as the mesh size of the one before last "mesh" syntax one, otherwise the mesh size of the one before the last one would be gradualy increased or decreased in order to match the last mesh size. The same syntax meaning is applied for the mesh size in the x direction where x=0 stats from the left side of the device. Here, very fine mesh is defined for this example which is not neccesary. 

Once the mesh is specified, every part of it should be assigned to a material. The syntax is something like "region mum=1 x.min=0.0 x.max=0.1 y.min=0.0 y.max=0.2 silicon". Region numbers should be started from 1. Upto 15000 regions can be assigned. 

Then, at least one electrode should be defined using the syntax of "electr name=source <position>". the position can be given by x.min, x.max, y.min and y.max or the right, left, top and bottom parameters for example "electrode name=source left length=0.5". If no location is defined for a region, it's assumed that the whole device is defined by that region.  
 
The final step for defining the device structure is to specify doping concentration and type for each region using the syntax of "doping <doping type> conc <location> <distribution function>". Example: "doping  p.type conc=1e17 x.min=0 x.max=0.4 y.top=0.0 y.bottom=0.6 uniform".
    
Once the device structure and properties are defined, one can modify the characteristic of electrodes (CONTACT syntax), change the defualt materials (MATERIAL syntax), and choose physical models (MODEL syntax) the models that Atlas use during the device simulation. Impact ionization model can be enabled by "IMPACT" syntax and the interface properties can be defined by "INTERFACE" syntax. Example: "model  conmob  fldmob  srh  auger  bgn". 

The following figure a shows the potential profile obtained from Silvaco for a pn junction with different doping concentration ranging from 1E15 to 1E18 /cm3 under no bias. As seen, the built in potential increases monotically from 0.6 to 0.9 V. 
    
![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/Simulation/pot-iv-pn-diode.png)

The almost same built-in potentials are obtained using analytical equation provided in this chapter, but the maximum electric field and the total depletion width shows relatively positive and negative deviations, respectively, from the numerical results (builtin.py). These deviotions are larger at lower doping concentrations and due to unvalid box approximation for depletion region. The above figure b indicates the I-V characteristics of the simulated pn juction, as expected the turn on voltages change regarding the built-in potential of each junction. 
    
yt
