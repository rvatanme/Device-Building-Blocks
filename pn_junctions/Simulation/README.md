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

    solve init

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
    
The "bgn" model include bandgap narrowing due to high doping concentration. It is important in heavily doped regions and critical for bipolar gain. Use Klaassen Model. The "srh" is the abbreviation for Shockley-Read-Hall model which uses fixed minority carrier lifetimes and should be used in most simulations. The "auger" is a recombination model and is the reverse of impact ionization. It happens when two carriers are recombined and the released energy is transfered to a third carrier.     
    
The following figure a shows the potential profile obtained from Silvaco for a pn junction with different doping concentration ranging from 1E15 to 1E18 /cm3 under no bias. As seen, the built in potential increases monotically from 0.6 to 0.9 V. 
    
![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/Simulation/pot-iv-pn-diode.png)

The almost same built-in potentials are obtained using analytical equation provided in this chapter, but the maximum electric field and the total depletion width shows relatively positive and negative deviations, respectively, from the numerical results (builtin.py). These deviotions are larger at lower doping concentrations and due to unvalid box approximation for depletion region. The above figure b indicates the I-V characteristics of the simulated pn juction, as expected the turn on voltages change regarding the built-in potential of each junction. 

    
## PN Junction Under Reverse Bias
the following potential profile for the p-n junction with 1e17 doping concentration was obtained from simulation of the juntion under reverse bias using silvaco.
    
![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/Simulation/pn_back_17.png)
    
The device properties of the p-n junction with 1e17 doping concentration was obtained from simulation under 0.625 V forward bias and compared with the Shockley form. 
    
![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/Simulation/QFL.png)
    
![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/Simulation/Ele_Hol_Con.png)

    
The ac analysis of the pn junction using silvaco can be performed using following syntax:
    
    solve vanode=0.05 vstep=0.05 vfinal=1 ac.analysis freq=1.0e2 name=anode
 
The following diffusion conductance and capacitance were obtained from the simulation.
    
![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/Simulation/dif_conduc_capac.png)
    
The following diode was simulated for the breakdown voltage simulation.
    
![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/Simulation/diode_BD.png)
    
The silvaco input file is as follows:
    
    # (c) Silvaco Inc., 2017
    go atlas
    TITLE PN Diode Breakdown with Energy Balance and Nonisothermal Energy Balance Models

    # EB simulation

    mesh    
    x.m  l=0.0 spac=1.0
    x.m  l=1.0 spac=1.0
    y.m  l=0   spac=1.0
    y.m  l=5.0  spac=0.005
    y.m  l=15  spac=2


    region num=1 silicon
 
    electrode  top name=emitter
    electrode  bottom name=base

    doping uniform conc=1e17 p.type 
    doping uniform n.type conc=1.e19  x.l=0. x.r=1 y.t=0.0 y.b=5.0 

    #contact name=emitter resis=1.e10

    models srh conmob bgn auger fldmob  hcte 

    impact  selb  length.rel lrel.ho=0.025  lrel.el=0.025

    material  taurel.el=0.25e-12 taumob.el=0.25e-12 taurel.ho=0.25e-12 taumob.ho=0.25e-12


    method  block newton climit=1.e-5  
   
    solve vemitter=0.0 

    log outf=diodeex02_eb.log

    solve  vemitter=0.5 vstep=0.5 vfinal=25 name=emitter cname=emitter compl=1e-12
    save outf=diodeex02_eb.str

    contact name=emitter current
    method newton climit=1e-5
    solve imult istep=2  ifinal=1e-3 name=emitter


    go atlas

    # NEB simulation

    mesh    
    x.m  l=0.0 spac=1.0
    x.m  l=1.0 spac=1.0
    y.m  l=0   spac=1.0
    y.m  l=5.0  spac=0.005
    y.m  l=15  spac=2


    region num=1 silicon

    electrode  top name=emitter
    electrode  bottom name=base
 

    doping uniform conc=1e17 p.type 
    doping uniform n.type conc=1.e19  x.l=0. x.r=1 y.t=0.0 y.b=5.0 


    thermcontact num=1 x.min=0 x.max=1 y.min=0 y.max=0  alpha=100
    thermcontact num=2  x.min=0 x.max=1 y.min=15 y.max=15  alpha=100


    models srh conmob bgn auger fldmob  hcte lat.temp

    impact  selb  length.rel lrel.ho=0.025  lrel.el=0.025

    material  taurel.el=0.25e-12 taumob.el=0.25e-12 taurel.ho=0.25e-12 taumob.ho=0.25e-12


    method  block newton climit=1.e-5  
   
    solve vemitter=0.0 

    log outf=diodeex02_neb.log

    solve  vemitter=0.5 vstep=0.5 vfinal=25 name=emitter cname=emitter compl=1e-12
    save outf=diodeex02_neb.str

    contact name=emitter current
    method newton climit=1e-5
    solve imult istep=2  ifinal=1e-3 name=emitter

    tonyplot diodeex02_neb.str -set diodeex02_0.set
    tonyplot diodeex02_eb.log -overlay diodeex02_neb.log -set diodeex02.set
    quit
    
The "x.m" and "l" syntax in mesh section is are the abbrivations for "x.mesh" and "loc", respectively. The "x.l" and "x.r" are the abbrevations for "x.left" and "x.right", respectively and can be used instead of "x.min" and "x.max". The "y.t" and "y.b" are the abbrevations for "y.top" and "y.bottom", respectively and can be used instead of "y.min" and "y.max".

Since in this example the dimension of the device is close to the submicron scale, the breakdown simulation should be simulated using the Energy Balance Model due to nonlocal impact ionization effects, which can substantially influence device characteristics. For high current levels the thermal self-heating effects can also play an important role by decreasing the mobility and impact ionization rate.  
    
In the "model" statement, the HCTE is used to enable the energy balance (EB) transport model for both electrons and holes (use HCTE.EL for EB only for electrons or HCTE.HO for EB only for holes). EB model consists of Poisson's equation, carrier continuity equations, and energy balance equation for electrons and holes.  
    
The "impact" statement is used to assign the energy relaxation lengths for the Selberherr model. The "selb" is the abbreviation for Selberherr impact ionization model. The "length.rel" specifies the use of energy relaxation length for the impact ionization model with the energy balance model. If LENGTH.REL is specified, TAUSN and TAUSP cannot be specified and have any affect. The "lrel.el" and "lrel.ho" specify an energy relaxation length for electrons and holes, respectively, if LENGTH.REL is specified. 

The "contact" statement is used to specify a large resistor at the emitter electrode, providing a smooth transition from voltage boundary conditions to current boundary conditions.    
    
In the "material" statement, the TAUREL.EL and TAUREL.HO are the electron and hole energy relaxation times. The relaxation parameters are user-definable on the MATERIAL statement and their default values are 4.0e-13 s. The relaxation times are extremely important as they determine the time constant for the rate of energy exchange and therefore precise values are required if the model is to be accurate. But, this is an unmeasurable parameter and Monte Carlo analysis is the favored method through which values can be extracted for the relaxation time. The "taumob.el" and "taumob.hol" specify the relaxation time for electrons and hole in the temperature dependent mobility model and their default values are 2.5e-13 s. 
    
In the "method" statement, the BLOCK methods will solve some equations fully coupled while others are decoupled. The numerical methods used in EB simulation can strongly affect convergence and CPU time. Here method block newton is used. This decouples the carrier temperature calculation from the potential and continuity equations at lower biases. This allows for larger bias steps at low bias. The CLIMIT or CLIM.DD specify minimal values of concentrations to be resolved by the solver. Sometimes, you need to reduce this value to aid solutions of breakdown characteristics. A value of CLIMIT=1e-4 is recommended for all simulations of breakdown, where the pre-breakdown current is small. CLIM.DD is equivalent to CLIMIT but uses the more convenient units of cm-3 for the critical concentration. CLIM.DD and CLIMIT are related by the following expression: CLIMIT*(NcNd)^1/2.     
    
In the "solve" section, Compliance (compl) is a parameter used to limit the current or voltage through or on an electrode during a simulation. You can set an electrode compliance. After reaching this limit, the bias sweep will stop. This is similar to parametric device testing when we stop a device from being over-stressed or destroyed. The compliance refers to the maximum resultant current or voltage present after obtaining a solution. If you set an electrode voltage, the compliance will then refer to the electrode current. If there are current boundary conditions, you can set a voltage compliance. Here, the initial biasing is done by ramping the emitter contact towards 25 V. A compliance limit is set on the emitter current as defined by: cname=emitter compl=1e-12 . Once this current is exceeded, the voltage ramp stops and Atlas proceeds to the next simulation line. This is to specify current forcing on the emitter contact. The syntax "contact name=emitter current" does this. 
    
After setting the newton method the biasing proceeds by specifying istep=2 imult. The parameter imult indicates that the istep is a multiplier to the current as opposed to an additive step. Therefore at each bias step the forced current is multiplied by istep. ifinal indicates the maximum current to be simulated. The "CONTACT NAME=emitter CURRENT" specifies current boundary conditions for the electrode emitter. On subsequent SOLVE statements, the drain current boundary condition will default to zero current. Therefore, floating the contact. For contacts directly onto semiconductor, the FLOATING parameter cannot be used. This type of floating electrode is best simulated by specifying current boundary conditions on the CONTACT statement. You can also make a floating contact to a semiconductor using a very large resistor attached to the contact instead. For example: CONTACT NAME=drain RESIST=1e20. In all of the examples considered in the basic description of the SOLVE statement, it was assumed that voltages were being forced and currents were being measured. ATLAS also supports the reverse case through current boundary conditions. The current through the electrode is specified in the SOLVE statement and the voltage at the contact is calculated. The syntax of the "SOLVE" statement is altered once current boundary conditions are specified. The "IMULT" parameter, is used to specify that "ISTEP" should be used as a multiplier for the current rather than a linear addition. This is typical for ramps of current since linear ramps are inconvenient when several orders of magnitude in current may need to be covered.    
    
Note that due to the use of current forcing, emitter int. bias should be used as the x axis on the IV data plots. 
    
The second Atlas run uses the Nonisothermal Energy Balance Model: Poisson's equation, carrier continuity equations, energy balance equation for electrons and holes, and the lattice heat flow equation are solved self-consistently. The same set of models is used, except that the solution of the lattice energy balance equation is activated using the models "lat.temp" statement. In addition, the thermal boundary conditions should be defined in this case. Thermal boundary conditions are defined in the thermcontact statement. Values of the thermal conductances are specified at the thermal contact located along the emitter and base electrodes.
    
When you switch a device on, there can be significant current density within the silicon. This could generate a significant amount of heat. In bulk MOS devices, the silicon substrates behaves like a good heat conductor. This generated heat is then quickly removed. But this isn’t the case with SOI substrates as the buried oxide layer allows this generated heat to be retained. For SOI MOSFETs, this can be a significant amount and can drastically affect the operation of the device. In such cases, take account of this by using the G IGA module. Note that when you switch on lattice heating by using the LAT.TEMP parameter in the MODELS statement, you also need to specify a thermal boundary condition with the THERMCONTACT statement. In deep submicron designs, you may need to switch on the additional energy balance equations. These take into account the exchange of energy between carriers and between the carriers and the lattice. The units of the thermal resistance parameter "ALPHA" are scaled in 3D to W/(cm.K) [watt/centimetre.kelvin]. Thermal resistance is a heat property and a measurement of a temperature difference by which an object or material resists a heat flow. Thermal resistance is the reciprocal of thermal conductance. In some cases, lattice heating may be important to MOS simulation. This typically occurs in cases with very high currents, just like the case with ESD simulation. To enable heat flow simulation, set the LAT.TEMP parameter of the MODEL statement (a license for G IGA is required). For example, the statement: MODEL LAT.TEMP enables heat-flow simulation.     
    
The following results is obtained from running the above silvaco input file:
    
![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/Simulation/BD_EB_NEB.png)
    
The second example of breakdown voltage is related to SiC diode. a SiC diode is simulated to demonstrate the Atlas capabilities to handle wide band gap semiconductor devices under room and elevated temperature conditions. The interest toward SiC technologies is growing due to the thermal and electronic properties of the material potentially leading to very high figures of merit for high-power, high-speed, high-temperature, and radiation hard applications. The following micron-scale PIN diode is simulated using silvaco.    
    
![]()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


