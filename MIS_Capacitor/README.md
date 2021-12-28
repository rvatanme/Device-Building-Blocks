# Metal-Insulator-Semiconductor Capacitor
The metal-insulator-semiconductor (MIS) capacitor is the most useful device in the study of semiconductor surfaces. Since most practical problems in the 
reliability and stability of all semiconductor devices are intimately related to their surface conditions, an understanding of the surface physics with 
the help of MIS capacitors is of great importance to device operations. Here, we are concerned primarily with the metal-oxide-silicon (MOS) system. 
This system has been extensively studied because it is directly related to most silicon planar devices and integrated circuits.

## Ideal MIS Capacitor
The metal-insulator-semiconductor (MIS) structure is shown in the following figure, where d is the thickness of the insulator and Vis the applied voltage. Here, we use the convention that the voltage Vis positive when the metal plate is positively biased with respect to the semiconductor body.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/MIS.png)

The energy-band diagram of an ideal MIS structure without bias is shown in the following figure. An ideal MIS capacitor is defined as follows: 1) The only charges that can exist in the structure under any biasing conditions are those in the semiconductor and those, with an equal but opposite sign, on the metal surface adjacent to the insulator 2) There is no carrier transport through the insulator under dc biasing conditions. For the sake of simplicity we assume the metal is chosen such that the difference between the metal work function and the semiconductor work function is zero.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/MIS-no-bias.png)

![](https://latex.codecogs.com/svg.latex?%5Cinline%20%5CLARGE%20%5Cphi%20_%7Bms%7D%20%5Cequiv%20%5Cphi_m%20-%20%28%5Cchi%20&plus;%20%5Cfrac%7BE_g%7D%7B2q%7D%20-%20%5Cpsi_%7BBn%7D%29%20%3D%20%5Cphi_m%20-%20%28%5Cchi&plus;%5Cphi_n%29%20%3D%200%20%5C%5C%5C%5C%20%5Cphi%20_%7Bms%7D%20%5Cequiv%20%5Cphi_m%20-%20%28%5Cchi%20&plus;%20%5Cfrac%7BE_g%7D%7B2q%7D%20&plus;%20%5Cpsi_%7BBp%7D%29%20%3D%20%5Cphi_m%20-%20%28%5Cchi&plus;%5Cfrac%7BE_g%7D%7Bq%7D-%5Cphi_p%29%20%3D%200)

where χ and χ<sub>i</sub> are the electron affinities for the semiconductor and insulator respectively, and ψ<sub>Bn</sub>, ψ<sub>Bp</sub>, φ<sub>n</sub>, φ<sub>p</sub> are the Fermi potentials with respect to the midgap and band edges. In other words, the band is flat (flat-band condition) when there is no
applied voltage. 

When an ideal MIS capacitor is biased with positive or negative voltages, basically three cases may exist at the semiconductor surface shown in the following figure. Consider the p-type semiconductor first. When a negative voltage (V < 0) is applied to the metal plate, the valence-band edge E , bends upward near the surface and is closer to the Fermi level. For an ideal MIS capacitor, no current flows in the structure so the Fermi level remains flat in the semiconductor. 

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/mis-bias.png)

Since the carrier density depends exponentially on the energy difference ( E<sub>F</sub>- E<sub>V</sub>), this band bending causes an accumulation of majority carriers (holes) near the semiconductor surface. This is the accumulation case. When a small positive voltage (V>0) is applied, the bands bend downward, and the majority carriers are depleted. This is the depletion case. When a larger positive voltage is applied, the bands bend even more
downward so that the intrinsic level E<sub>i</sub> at the surface crosses over the Fermi level. At this point the number of electrons (minority carriers) at the surface is larger than that of the holes, the surface is thus inverted and this is the inversion case. Similar results can be obtained for the n-type semiconductor. The polarity of the voltage, however, should be changed for the n-type semiconductor.

The following figure shows a more detailed band diagram at the surface of a p-type semiconductor. The potential in the semiconductor side is defined as:

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/MIS_Diag.png)

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cpsi%20_p%28x%29%20%5Cequiv%20-%5Cfrac%7BE_i%28x%29-E_i%28%5Cinfty%29%7D%7Bq%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%20%5Cpsi%20_p%280%29%20%5Cequiv%20%5Cpsi%20_s)

where ψ<sub>s</sub> is called the surface potential. The electron and hole concentrations are given by the following relations:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20n_p%28x%29%20%3D%20n_%7Bp0%7Dexp%28%5Cfrac%7Bq%5Cpsi_p%7D%7BkT%7D%29%20%3D%20n_%7Bp0%7Dexp%28%5Cbeta%5Cpsi_p%29%20%5C%5C%5C%5C%20p_p%28x%29%20%3D%20p_%7Bp0%7Dexp%28-%5Cfrac%7Bq%5Cpsi_p%7D%7BkT%7D%29%20%3D%20p_%7Bp0%7Dexp%28-%5Cbeta%5Cpsi_p%29%20%5C%5C%5C%5C%20n_p%280%29%20%3D%20n_%7Bp0%7Dexp%28%5Cbeta%5Cpsi_s%29%20%5C%3B%5C%3B%5C%3B%5C%3B%20p_p%280%29%20%3D%20p_%7Bp0%7Dexp%28-%5Cbeta%5Cpsi_s%29)

where n<sub>p</sub>(0) and p<sub>p</sub>(0) are the densities of electrons and holes at the surface. From the equations, the following regions can be distinguished:

1) ψ<sub>s</sub> < 0------------Accumilation of holes (upward band bending)
2) ψ<sub>s</sub> = 0------------Flat-band condition
3) ψ<sub>Bp</sub> > ψ<sub>s</sub> > 0------------Depletion of holes (bands bending downward)
4) ψ<sub>s</sub> = ψ<sub>Bp</sub>------------Fermi level at midgap, E<sub>i</sub>(0) = E<sub>F</sub>, n<sub>p</sub>(0) = p<sub>p</sub>(0) = n<sub>i</sub>
5) 2ψ<sub>Bp</sub> > ψ<sub>s</sub> > ψ<sub>Bp</sub>------------Weak inversion [electron enhancment, n<sub>p</sub>(0) > p<sub>p</sub>(0)]
6) ψ<sub>s</sub> > 2ψ<sub>Bp</sub>------------Strong inversion [n<sub>p</sub>(0) > p<sub>p</sub>(0) or N<sub>A</sub>]

The potential ψ<sub>p</sub>(x) as a function of distance can be obtained by using the one-dimensional Poisson equation:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cfrac%7Bd%5E2%5Cpsi_p%7D%7Bd%5E2x%7D%20%3D%20-%20%5Cfrac%7B%5Crho%28x%29%7D%7B%5Cepsilon_s%7D%20%5C%5C%5C%5C%20%5Crho%28x%29%20%3D%20q%28N_D%5E&plus;-N_A%5E&plus;&plus;p_p-n_p%29%20%5C%5C%5C%5C%20N_D%5E&plus;-N_A%5E&plus;%20%3D%20n_%7Bp0%7D%20-%20p_%7Bp0%7D)

Integrating the above equation from the surface to the bulk and defining the following parameters, the total space charge per unit area is derived as:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20Q_s%20%3D%20-%5Cepsilon%20_s%5Cxi%20_s%3D%20%5Cpm%20%5Cfrac%7B%5Csqrt%7B2%7D%5Cepsilon%20_skT%7D%7BqL_D%7DF%28%5Cbeta%5Cpsi_s%2C%5Cfrac%7Bn_%7Bp0%7D%7D%7Bp_%7Bp0%7D%7D%29%20%5C%5C%5C%5C%5C%5C%20L_D%20%5Cequiv%20%5Csqrt%7B%5Cfrac%7B%5Cepsilon%20_s%7D%7Bqp_%7Bp0%7D%5Cbeta%7D%7D)

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20F%28%5Cbeta%5Cpsi_p%2C%5Cfrac%7Bn_%7Bp0%7D%7D%7Bp_%7Bp0%7D%7D%29%20%5Cequiv%20%5Cpm%20%5Csqrt%7B%5Bexp%28-%5Cbeta%5Cpsi_p%29&plus;%5Cbeta%5Cpsi_p-1%5D&plus;%5Cfrac%7Bn_%7Bp0%7D%7D%7Bp_%7Bp0%7D%7D%5Bexp%28%5Cbeta%5Cpsi_p%29-%5Cbeta%5Cpsi_p-1%5D%7D)

A typical variation of the space-charge density Q<sub>s</sub>, as a function of the surface potential ψ<sub>s</sub>, is shown in the following figure, for a p-type silicon with NA = 4E15 cm-3 at room temperature. Also note that the strong inversion begins at a surface potential:

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/space_charge.png)

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cpsi_s%5Capprox%202%5Cpsi_%7BBp%7D%5Capprox%20%5Cfrac%7B2kT%7D%7Bq%7Dln%5Cfrac%7BN_A%7D%7Bn_i%7D)

The following figure shows the band diagram of a MIS in strong inversion regime. For charge neutrality of the system, it is required that:

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/strong-diag1.png)

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20Q_M%20%3D%20-%28Q_n&plus;qN_AW_D%29%20%3D%20-Q_s)

In the absence of any work-function difference, the applied voltage will partly appear across the insulator (V<sub>i</sub>) and partly across the semiconductor. Thus:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20v%20%3D%20V_i%20&plus;%20%5Cpsi%20_s%20%5C%5C%5C%5C%20V_i%20%3D%20%5Cxi%20d%20%3D%20%5Cfrac%7B%7CQ_s%7Cd%7D%7B%5Cepsilon%20_i%7D%20%3D%20%5Cfrac%7B%7CQ_s%7C%7D%7BC_i%7D)

The total capacitance C of the system is a series combination of the insulator capacitance and the semiconductor depletion-layer capacitance CD:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20C_i%20%3D%20%5Cfrac%7B%5Cepsilon%20_i%7D%7Bd%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%20C%20%3D%20%5Cfrac%7BC_iC_D%7D%7BC_i&plus;C_D%7D)

For a given insulator thickness d, the value of C<sub>i</sub>, is constant and corresponds to the maximum capacitance of the system. But the semiconductor capacitance C<sub>D</sub>, not only depends on the bias (or ψ<sub>s</sub>), it is also a function of the measurement frequency. The following figure illustrates the vastly different characteristics of C- V curves measured at different frequencies and sweep rates. The difference mainly occurs at the inversion regime, especially strong inversion.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/CV_curve_freq.png)

Weak inversion begins at ψ<sub>s</sub> = ψ<sub>Bp</sub>, and the onset of strong inversion occurs at ψ<sub>s</sub> = 2ψ<sub>Bp</sub>. The minimum low-
frequency capacitance C<sub>min</sub> occurs in between these two points.

The capacitance of the semiconductor depletion layer is obtained by differentiating the total static charge in the semiconductor side with respect to the semiconductor surface potential:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20C_D%20%5Cequiv%20%5Cfrac%7BdQ_s%7D%7Bd%5Cpsi%20_s%7D%20%3D%20%5Cfrac%7B%5Cepsilon%20_s%7D%7B%5Csqrt%7B2%7DL_D%7D%5Cfrac%7B1-exp%28-%5Cbeta%5Cpsi_s%29&plus;n_%7Bp0%7D/p_%7Bp0%7D%5Bexp%28%5Cbeta%5Cpsi_s%29-1%5D%7D%7BF%28%5Cbeta%5Cpsi_s%2Cn_%7Bp0%7D/p_%7Bp0%7D%29%7D)

Combination of the following equation gives the complete description of the ideal low-frequency C-V curve as shown in the above figure, curve (a). In describing this low-frequency curve we begin at the left side (negative voltage and ψ<sub>s</sub>), where we have an accumulation of holes and therefore a high differential capacitance of the semiconductor. As a result the total capacitance is close to the insulator capacitance. As the negative voltage is reduced to zero, we have the flat-band condition, that is, ψ<sub>s</sub> = 0. Since the function F approaches zero, C<sub>D</sub>, has to be obtained from the above equation by expanding the exponential terms into series, and we obtain:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20C_D%28flat%5C%3Bband%29%20%3D%20%5Cfrac%7B%5Cepsilon%20_s%7D%7BL_D%7D%20%5C%5C%5C%5C%20C_%7BFB%7D%28%5Cpsi%20_s%20%3D%200%29%20%3D%20%5Cfrac%7B%5Cepsilon_i%5Cepsilon_s%7D%7B%5Cepsilon_sd%20&plus;%20%5Cepsilon_iL_D%7D%20%3D%20%5Cfrac%7B%5Cepsilon_i%5Cepsilon_s%7D%7B%5Cepsilon_sd%20&plus;%20%5Cepsilon_i%5Csqrt%7BkT%5Cepsilon_s/q%5E2N_A%7D%7D)

It can be shown that under depletion and weak inversion conditions, i.e. 2 ψ<sub>Bp</sub> > ψ<sub>s</sub> > kT/q, the function F and consequently Qs can be simplified to:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20F%20%5Capprox%20%5Csqrt%7B%5Cbeta%5Cpsi_s%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%20Q_s%20%3D%20%5Csqrt%7B2%5Cepsilon_sqp_%7Bp0%7D%5Cpsi_s%7D%20%3D%20qN_AW_Dv)

We then can express the depletion width as a function of the terminal voltages. The quadratic equation gives a solution of:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20W_D%20%3D%20%5Csqrt%7B%5Cfrac%7B%5Cepsilon%20_s%5E2%7D%7BC_%7Box%7D%5E2%7D&plus;%5Cfrac%7B2%5Cepsilon_sV%7D%7BqN_A%7D%7D%20-%20%5Cfrac%7B%5Cepsilon_s%7D%7BC_%7Box%7D%7D)

Once W<sub>D</sub>, is known, C<sub>D</sub> and ψ<sub>s</sub> are deduced. The depletion capacitance can be estimated by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20C_D%20%3D%20%5Csqrt%7B%5Cfrac%7B%5Cepsilon_sqp_%7Bp0%7D%7D%7B2%5Cpsi_s%7D%7D%20%3D%20%5Cfrac%7B%5Cepsilon_s%7D%7BW_D%7D)

With further increase in positive voltage, the depletion region widens which acts as a dielectric at the semiconductor surface in series with the insulator, and the total capacitance continues to decrease. The capacitance goes through a minimum and then increases again as the inversion layer of electrons forms at the surface. The minimum capacitance and the corresponding minimum voltage are designated C<sub>min</sub> and V<sub>min</sub> respectively. Since Ci is fixed, C<sub>min</sub> can be found by the minimum value of C<sub>D</sub>. The value of ψ<sub>s</sub> corresponding to the minimum C<sub>D</sub>, can be obtained by differentiation of C<sub>D</sub> equation and setting it to zero, resulting in a transcendental equation:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Csqrt%7Bcosh%28%5Cbeta%5Cpsi_s-%5Cbeta%5Cpsi_%7BBp%7D%29%7D%20%3D%20%5Cfrac%7Bsinh%28%5Cbeta%5Cpsi_s-%5Cbeta%5Cpsi_%7BBp%7D%29-sinh%28-%5Cbeta%5Cpsi_%7BBp%7D%29%7D%7B%5Csqrt%7BN_A/n_i%7DF%28%5Cbeta%5Cpsi_%7BBp%7D%2Cn_%7Bp0%7D/p_%7Bp0%7D%29%7D)

With a known ψ<sub>s</sub>, C<sub>min</sub> and V<sub>min</sub> can be determined from the above equations. Note that the increase of the capacitance depends on the ability of the electron concentration to follow the applied ac signal. This only happens at low frequencies where the recombination-generation rates of minority carriers (in our example, electrons) can keep up with the small-signal variation and lead to charge exchange with the inversion layer in step with the measurement signal. As shown in the following figure, unlike depletion and weak inversion, at strong inversion the incremental charge is no longer at the edge of the depletion region but at the semiconductor surface inversion layer, resulting in a large capacitance. As a consequence, MIS curves measured at higher frequencies do not show the increase of capacitance in strong inversion.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/charge_inversion.png)

The high-frequency curve can be obtained using an approach analogous to a one-sided abrupt p-n junction. When the applied voltage increases, ψ<sub>s</sub> and W<sub>D</sub> increase. Eventually, strong inversion will occur. Once strong inversion occurs, the depletion-layer width reaches a maximum. When the bands are bent down far enough that ψ<sub>s</sub> = 2 ψ<sub>B</sub>, the semiconductor is effectively shielded from further penetration of the electric field by the inversion layer and even a very small increase in band bending (corresponding to a very small increase in the depletion-layer width) results in a very large increase in the charge density within the inversion layer. Accordingly, the maximum width W<sub>Dm</sub> of the depletion region under steady-state condition can be obtained from:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20W_%7BDm%7D%20%3D%20%5Csqrt%7B%5Cfrac%7B2%5Cepsilon_s%5Cpsi_s%28strong%5C%3Binv%29%7D%7BqN_A%7D%7D%20%3D%20%5Csqrt%7B%5Cfrac%7B4%5Cepsilon_skTln%28N_A/n_i%29%7D%7Bq%5E2N_A%7D%7D)

This phenomena of maximum depletion width is unique to the MIS structure, and it does not occur inp-n junctions or Schottky barriers. Another quantity of interest is the so-called turn-on voltage or threshold voltage, V<sub>T</sub> at which strong inversion occurs: 

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20V_T%20%3D%20%5Cfrac%7B%7CQ_s%7C%7D%7BC_i%7D%20&plus;%202%5Cpsi_%7BBp%7D%3D%5Cfrac%7B%5Csqrt%7B2%5Cepsilon%20_sqN_A%282%5Cpsi_%7BBn%7D%29%7D%7D%7BC_i%7D%20&plus;%202%5Cpsi_%7BBp%7D)

Note that even though the slow-varying quiescent voltage puts the additional charge at the surface inversion layer, the high-frequency small signal is too fast for the minority carriers and the incremental charge is put at the edge of the depletion region. The depletion capacitance is simply given by ε<sub>i</sub>/W<sub>D</sub>, with a minimum value corresponding to the maximum depletion width W<sub>Dm</sub>:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20C_%7Bmin%7D%27%3D%5Cfrac%7B%5Cepsilon_i%5Cepsilon_s%7D%7B%5Cepsilon_sd&plus;%5Cepsilon_iW_%7BDm%7D%7D)

Complete ideal C-V curves of the metal-SiO2-Si system have been computed for various oxide thicknesses and semiconductor doping densities. The following figure shows typical ideal C-V curves for p-type silicon. Note that as the oxide film becomes thinner, larger variation of the capacitance is obtained. Also the curves are sharper, reducing the threshold voltage V<sub>T</sub>. The figure shows the dependence of ψ<sub>s</sub>, on the applied voltage for the same systems. Similarly, modulation of ψ<sub>s</sub> is more effective with thinner oxides.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/CV_Volt.png)

The critical parameters C<sub>FB</sub>, C<sub>min</sub>, C<sub>min</sub>', V<sub>T</sub>, and V<sub>min</sub> are calculated and plotted in the following figure. These ideal MIS curves will be used to compare with experimental results and to understand practical MIS systems. The conversion to
n-type silicon is achieved simply by changing the sign of the voltage axes. Converting to other insulators requires scaling the oxide thickness with the ratio of the permittivities of SiO2, and the other insulator:

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/C_thickness.png)

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20d_c%20%3D%20d_i%5Cfrac%7B%5Cepsilon%28SiO_2%29%7D%7B%5Cepsilon%28insulator%29%7D)

where d<sub>c</sub>, is the equivalent SiO<sub>2</sub>, thickness to be used in these curves, d<sub>i</sub> and ε<sub>i</sub> are the thickness and permittivity of the new insulator. 

At high frequency and with a fast sweeping ramp in the direction toward strong inversion, the semiconductor does not have enough time to come to equilibrium even with the large-signal variation. Deep depletion is said to occur when the depletion width is wider than the maximum value at equilibrium. This is the condition which CCDs are operated under when they are driven with large bias pulses. At even higher voltages, impact ionization can occur in the semiconductor. Under light illumination, however, extra minority carriers can be generated quickly and curve (d) will collapse to curve (c).

## Silicon MOS Capacitor
Of all the MIS capacitors, the metal-oxide-silicon (MOS) capacitor is by far the most practical and important. For a practical MOS capacitor, interface traps and oxide charges exist that will, in one way or another, affect the ideal MOS characteristics. As shown in the following figure, the basic classifications of these traps and charges are: 1) Interface traps of density D<sub>it</sub>, and trapped charges Q<sub>it</sub>. Interface traps can possibly be produced by excess silicon (trivalent silicon), broken Si-H bonds, excess oxygen and impurities. 2) Fixed oxide charges Q<sub>f</sub> which are located at or near the interface and are immobile under an applied electric field. (3) Oxide trapped charges Q<sub>ot</sub>, which can be created, for example, by X-ray radiation or hot-electron injection; these traps are distributed inside the oxide layer. (4) Mobile ionic charges Q<sub>m</sub>, such as sodium ions, which are mobile within the oxide under bias-temperature stress conditions.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/trap_fig.png)

Interface traps that are historically also called interface states, fast states or surface states exists exists within the forbidden gap due to the interruption of the periodic lattice structure at the surface of a crystal. It has been exprimentally found that the Dit in a clean surface of Si can be as high as 1E15 /cm2, on the order of density of surface atoms (1E15/cm3). For the present MOS capacitors having thermally grown SiO2 on Si, The total surface traps can be as low as 1E10 cm-2, which amounts to about one interface trap per lE5 surface atoms.

Similar to bulk impurities, an interface trap is considered a donor if it is neutral and can become positively charged by donating (giving up) an electron. An acceptor interface trap is neutral and becomes negatively charged by accepting an electron. The distribution functions (occupancy) for the interface traps are govern by Fermi-Dirac distribution:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20F_%7BSD%7D%28E_t%29%20%3D%20%5Cfrac%7B1%7D%7B1&plus;g_Dexp%5B%28E_F-E_t%29/kT%5D%7D%20%5C%5C%5C%5C%5C%5C%20F_%7BSA%7D%20%3D%20%5Cfrac%7B1%7D%7B1&plus;g_Aexp%5B%28E_t-E_F%29/kT%5D%7D)

where FSD, FSA, and Et are distribution fuction for donor type trap states, distribution function for acceptor type trap states, and the energy of trap stated, respectively. Here the degeneracy for donors gD is 2 and for acceptors gA is 4. Presumably every insulater-semiconductor interface has both kinds of traps. A convenient notation is to interpret the sum of these by an equivalent Dit, distribution, with an energy level called neutral level E0 above which the states are of acceptor type, and below which are of donor type, as shown in the following figure.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/Accep_dono_trap.png)

When EF is above (below) E0, net charge is - (+). To calculate the trapped charge, it can also be assumed that at room temperature, the occupancy takes on the value of 0 and 1 above and below EF With these assumptions, the interface-trapped charge can now be easily calculated by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20Q_%7Bit%7D%20%3D%20-q%20%5Cint_%7BE_0%7D%5E%7BE_F%7DD_%7Bit%7DdE%20%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%20for%20%5C%3B%20E_F%20%5C%3B%20above%20%5C%3BE_0%2C%20%5C%5C%5C%5C%20%3D%20&plus;q%20%5Cint_%7BE_0%7D%5E%7BE_F%7DD_%7Bit%7DdE%20%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%20for%20%5C%3B%20E_F%20%5C%3B%20below%20%5C%3BE_0%2C)

The foregoing charges are the effective net charges per unit area (i.e. C/cm2). Because interface-trap levels are distributed across the energy bandgap, they are characterized by an interface-trap density distribution:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20D_%7Bit%7D%20%3D%20%5Cfrac%7B1%7D%7Bq%7D%5Cfrac%7BdQ_%7Bit%7D%7D%7BdE%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%20Number%5C%3Bof%5C%3Btraps%20%28/cm2.eV%29)

This is the concept used to determine Dit experimentally-from the change of Q<sub>it</sub>, in response to the change of E<sub>F</sub> or surface potential ψ<sub>s</sub>. On the other hand, the above equation cannot distinguish whether the interface traps are of donor type or acceptor type but only determine the magnitude of Di<sub>it</sub>.

The basic equivalent circuit incorporating the interface-trap effect is shown in the following figure a. C<sub>it</sub>, and R<sub>it</sub>, are the capacitance and resistance associated with the interface traps and, thus, are also functions of energy. The product C<sub>it</sub>R<sub>it</sub>, is
defined as the interface-trap lifetime τ<sub>it</sub>, which determines the frequency behavior of the interface traps. The parallel branch of the equivalent circuit in Fig. 14a can be converted into a frequency-dependent capacitance C<sub>p</sub> in parallel with a frequency-dependent conductance G<sub>p</sub>, as shown in the following figure b, where:

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/equivalent_circuit.png)

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20C_P%20%3D%20C_D%20&plus;%20%5Cfrac%7BC_%7Bit%7D%7D%7B1&plus;%5Comega%5E2%20%5Ctau%20_%7Bit%7D%5E2%7D%20%5C%5C%5C%5C%5C%5C%20%5Cfrac%7BG_p%7D%7B%5Comega%7D%20%3D%20%5Cfrac%7BC_%7Bit%7D%5Comega%20%5Ctau%20_%7Bit%7D%7D%7B1&plus;%5Comega%5E2%20%5Ctau%20_%7Bit%7D%5E2%7D)

Also of particular interest are the equivalent circuits in the low-frequency and high-frequency limits, included in the above figure c and d. In the low-frequency limit, R<sub>it</sub>, is set to zero and C<sub>D</sub>, is in parallel to C<sub>it</sub>. In the high-frequency limit, the C<sub>it</sub>-R<sub>it</sub> branch is ignored or open. Physically it means that the traps are not fast enough to respond to the fast signal. The total terminal capacitance for these two cases (low-frequency C<sub>LF</sub>, and high-frequency C<sub>HF</sub>) are:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20C_%7BLF%7D%20%3D%20%5Cfrac%7BC_%7Bi%7D%28C_D&plus;C_%7Bit%7D%29%7D%7BC_i&plus;C_D&plus;C_%7Bit%7D%7D%20%5C%5C%5C%5C%5C%5C%20C_%7BLF%7D%20%3D%20%5Cfrac%7BC_%7Bi%7DC_D%7D%7BC_i&plus;C_D%7D)

Either capacitance measurement or conductance measurement can be used to evaluate the interface-trap density, because both the input conductance and the input capacitance of the equivalent circuit contain similar information about the interface traps. It will be shown that the conductance technique can give more accurate results, especially for MOS capacitors with relatively low interface-trap density (=1El0 /cm2.eV). The capacitance measurement, however, can give rapid evaluation of flat-band shift and the total interface-trapped charge.

The following figure a shows qualitatively the high-frequency and low-frequency C-V characteristics with and without interface traps. A very noticeable effect of the interface traps is that the curves are stretched out in the voltage direction. This is due to the fact that extra charge has to fill the traps, so it takes more total charge or applied voltage to accomplish the same surface potential ψ<sub>s</sub> (or band bending). This is demonstrated more clearly in below figure b where ψ<sub>s</sub> is plotted against the apply voltage directly, with and without interface traps.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/CV_trap_ideal.png)

One other helpful point is that interface traps affect the total capacitance in two ways. A direct impact is through the extra circuit elements Cit and R<sub>it</sub>. A second impact is indirectly on C<sub>D</sub>. For a fixed bias, since some charge will be needed to fill the interface traps, the remaining charge to be put in the depletion layer is reduced and this will reduce the surface potential or band bending. But since the relationship
between C<sub>D</sub> and ψ<sub>s</sub> is fixed (Eq. 22 or 28), changing ψ<sub>s</sub> means changing C<sub>D</sub> also. This explains that for the high-frequency limit, even though the equivalent circuit does not contain the C<sub>it</sub> element, the high-frequency C-V curve is still affected by interface traps, through C<sub>D</sub>.

Before discussing the capacitance method to measure Dit, we derive some useful equations to extrat this information from a C-V curve. First the relationship between C<sub>it</sub>, and D<sub>it</sub>, is derived as follows. Since dQ<sub>it</sub> = qD<sub>it</sub>dE, and dE = qdψ<sub>s</sub>, we obtain:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20C_%7Bit%7D%20%5Cequiv%20%5Cfrac%7BdQ_%7Bit%7D%7D%7Bd%5Cpsi_s%7D%20%3D%20q%5E2D_%7Bit%7D)

Next we will derive the stretch out of the ψ<sub>s</sub>-V curve in relationship to interface traps. Using the low-frequency equivalent circuits, the applied voltage is partitioned between the oxide layer and the semiconductor layer. The portion of the voltage across the semiconductor ψ<sub>s</sub> is simply given by the voltage divider of the capacitor network, i.e.:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cfrac%7Bd%5Cpsi_s%7D%7BdV%7D%20%3D%20%5Cfrac%7BC_i%7D%7BC_i&plus;%28C_D&plus;C_%7Bit%7D%29%7D%20%5C%5C%5C%5C%5C%5C%20D_%7Bit%7D%20%3D%20%5Cfrac%7BC_i%7D%7Bq%5E2%7D%5B%28%5Cfrac%7Bd%5Cpsi_s%7D%7BdV%7D%29%5E%7B-1%7D-1%5D-%5Cfrac%7BC_D%7D%7Bq%5E2%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%20%281%29)

In the high frequancy capacitance method, first the total capacitance (CHF) of MOS is measured and since the equivalent circuit does not contain Cit, CD can be easly calculated from CHF. Once C<sub>D</sub> is known, ψ<sub>s</sub> can be calculated from theory and the ψ<sub>s</sub>-V relationship is obtained. Equation 1 is then used to determine D<sub>it</sub>.

In the low frequency method, the following equations are used:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cfrac%7Bd%5Cpsi_s%7D%7BdV%7D%20%3D%20%5Cfrac%7BC_i%7D%7BC_i&plus;C_D&plus;C_%7Bit%7D%7D%20%3D%201%20-%5Cfrac%7BC_D&plus;C_%7Bit%7D%7D%7BC_i&plus;C_D&plus;C_%7Bit%7D%7D%20%5C%5C%5C%5C%20%3D%201%20-%20%5Cfrac%7BC_%7BLF%7D%7D%7BC_i%7D%20%5C%5C%5C%5C%20%5Cpsi_s%28V_2%29%20-%20%5Cpsi_s%28V_1%29%20%3D%20%5Cint_%7BV_1%7D%5E%7BV_2%7D%281%20-%20%5Cfrac%7BC_%7BLF%7D%7D%7BC_i%7D%29dV%20&plus;%20Cons.)

The integrand constant can be the starting point at accumulation or strong inversion where w, is known and it has weak dependence on the applied voltage. Once ψ<sub>s</sub> is known, D<sub>it</sub> can be calculated from Eq. 1, provided that the doping profile is known. One disadvantage of the low-frequency capacitance method is the measurement difficulty in the presence of increased dc leakage for thinner oxides.

In the High-Low-Frequency capacitance method, the following equation is used:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20D_%7Bit%7D%3D%5Cfrac%7B%5CDelta%20C%7D%7Bq%5E2%7D%281%20-%20%5Cfrac%7BC_%7BHF%7D&plus;%5CDelta%20C%7D%7BC_i%7D%29%5E%7B-1%7D%281%20-%20%5Cfrac%7BC_%7BHF%7D%7D%7BC_i%7D%29%5E%7B-1%7D)

where ΔC is the capacitance gap as CHF - CLF for each bias point. As shown in this equation, the trap density, on the first order, is proportional to the capacitance gap ΔC. If the energy spectrum of Dj, is to be determined, either the low-frequency capacitance integration approach or the high-frequency method can be applied to determine ψ<sub>s</sub>.

The simplified equivalent circuit in the above figure b illustrates the principle of the MIS conductance technique. The impedance of the MIS capacitor is measured by a bridge across the capacitor terminals. The insulator capacitance C<sub>i</sub> is also measured in the region of strong accumulation. The reactance of the insulator capacitance is subtracted from this impedance and the resulting impedance converted into an admittance. This leaves C<sub>D</sub> in parallel with the series R<sub>it</sub>C<sub>it</sub>, network of the interface traps (Fig. 14b). The equivalent parallel conductance G<sub>p</sub> divided by ω is given by Eq. 40 which does not contain C<sub>D</sub> and depends only on the interface-trap branch of the equivalent circuit. An expression to convert the measured admittance to the conductance of the interface-trap branch is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cfrac%7BG_p%7D%7B%5Comega%7D%20%3D%20%5Cfrac%7B%5Comega%20C_i%5E2G_%7Bin%7D%7D%7BG_%7Bin%5E2%7D&plus;%5Comega%20%5E2%28C_i-C_%7Bin%7D%29%5E2%7D%20%3D%20%5Cfrac%7BC_%7Bit%7D%5Comega%20%5Ctau%20_%7Bit%7D%7D%7B1&plus;%5Comega%5E2%20%5Ctau%20_%7Bit%7D%5E2%7D)

At a given bias, G<sub>p</sub>/ω can be measured as a function of frequency. A plot of G<sub>p</sub>/ω versus ω goes through a maximum when
ωτ<sub>it</sub> = 1, and gives τ<sub>it</sub> directly. The value of G<sub>p</sub>/ω at the maximum is C<sub>it</sub>/2. Thus, the equivalent parallel conductance corrected for C<sub>i</sub> gives C<sub>it</sub>, and τ<sub>it</sub> (= R<sub>it</sub>C<sub>it</sub>) directly from the measured conductance. Once C<sub>it</sub> is known, the interface-trap density is obtained by using the relation D<sub>it</sub> = C<sub>it</sub> /q<sup>2</sup>.

Typical results in a Si-SiO2 system show that near the midgap D<sub>it</sub>, is relatively constant, but it increases toward the conduction- and valence-band edges. Orientation dependence is particularly important. In (100) orientation D<sub>it</sub>, is about an order of magnitude smaller than that in (111). This result has been correlated with the available bonds per unit area on the silicon. It is apparent that the (111) surface has the largest number of available bonds per area, and the (100) surface has the smallest. One would also expect that the (100) surface has the lowest oxidation rate which is advantageous for thin oxides. If we assume that the origin of interface traps is due to excess silicon in the oxide, then the lower the oxidation rate
the smaller the amount of the excess silicon; thus the (100) surface should have the smallest interface-trap density. Therefore, all modern silicon MOSFETs are fabricated on (100)-oriented substrates.

Interface traps in the Si-SiO, system comprise of many levels. These are so closely spaced in energy that they cannot be distinguished as separate levels and actually appear as a continuum over the bandgap of the semiconductor. The equivalent circuit for an MIS capacitor with a single-level time constant (Fig. 14a) should, therefore, be interpreted as for a certain bias or trap level.

The following figure shows the variation of the time constant τ<sub>it</sub>, versus surface potential (or trap level) for MOS capacitors with steam-grown oxides on (100) silicon substrates, where is the average surface potential. These curves can be fitted by the following expressions:

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/time_constant.png)

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Ctau%20_%7Bit%7D%20%3D%20%5Cfrac%7B1%7D%7B%5Cbar%7B%5Cnu%7D%5Csigma_pn_i%7Dexp%5B-%5Cfrac%7Bq%28%5Cpsi_%7BBp%7D-%5Cbar%7B%5Cpsi_s%7D%29%7D%7BkT%7D%5D%20%5C%3B%5C%3B%5C%3B%5C%3B%20for%5C%3Bp%5C%3Btype%20%5C%5C%5C%5C%20%5Ctau%20_%7Bit%7D%20%3D%20%5Cfrac%7B1%7D%7B%5Cbar%7B%5Cnu%7D%5Csigma_nn_i%7Dexp%5B-%5Cfrac%7Bq%28%5Cpsi_%7BBn%7D-%5Cbar%7B%5Cpsi_s%7D%29%7D%7BkT%7D%5D%20%5C%3B%5C%3B%5C%3B%5C%3B%20for%5C%3Bn%5C%3Btype)

where σ<sub>p</sub> and σ<sub>n</sub>, are the capture cross sections of holes and electrons respectively, and ν is the average thermal velocity. These results indicate that the capture cross section is independent of energy. The capture cross sections obtained from the above figure are σ<sub>p</sub> =
4.3E-16 cm2 and σ<sub>n</sub> = 8.1E-16 cm2, where the value of ν = lE7 cm/s has been used. For (111)-oriented silicon the variation of time constant versus surface potential is similar to that of (100) and the measured capture cross sections are smaller with σ<sub>p</sub> = 2.2E-16 cm2 and σ<sub>n</sub> = 5.9E-16 cm2. We must also consider the statistical fluctuation of surface potential due to surface charges which include the fixed oxide charges Q<sub>f</sub> and the interface-trapped charges Q<sub>it</sub>. From the above equation, a small fluctuation in ψ<sub>s</sub> causes a large fluctuation in τ<sub>it</sub>. Assuming that surface charges are randomly distributed in the plane of the interface, the electric field at the semiconductor surface will fluctuate over the plane of the interface. 

Oxide charges, other than that of the interface traps, include the fixed oxide charge Q<sub>f</sub>, the mobile ionic charge Q<sub>m</sub>, and the oxide trapped charge Q<sub>ot</sub>. In general, unlike interface-trapped charges, these oxide charges are independent of bias, so they cause a parallel shift in
the gate-bias direction including workfunction difference, given by (obtained from Guass's law):

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/Shift_FB.png)

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5CDelta%20V%20_%7BFB%7D%3D%20V_%7BFB%7D%20%3D%20%5Cphi_%7Bms%7D%20-%20%5Cfrac%7BQ_f&plus;Q_m&plus;Q_%7Bot%7D%7D%7BC_i%7D%20%5C%5C%5C%5C%20%5Cphi%20_%7Bms%7D%20%3D%20%5Cphi%20_m%20&plus;%20%28%5Cchi%20&plus;%20%5Cfrac%7BE_g%7D%7B2q%7D%20-%20%5Cphi_%7BBn%7D%29)

The fixed oxide charge Q<sub>f</sub> has the following properties: It is located very close to the Si-SiO2, interface; it is generally positive; its density is not greatly affected by the oxide thickness or by the type or concentration of impurities in the silicon, but it depends on oxidation and annealing conditions, and on silicon surface orientation. It has been suggested that excess silicon (trivalent silicon) or the loss of an electron from excess oxygen centers (nonbridging oxygen) near the Si-SiO, interface is the origin of fixed oxide charge.

Mobile ionic charges can move back and forth through the oxide layer, depending on biasing conditions, and thus give rise to voltage shifts. The shift usually is enhanced at elevated temperature.In severe cases, hysteresis can be seen when the gate voltage is swept in opposite polarities. Alkali ions, such as sodium, in thermally grown SiO2 films are mainly responsible for the instability of the oxide-passivated devices. Reliability problems in semiconductor devices operated at high temperatures and voltages may be related to trace contamination by alkali metal ions. To prevent mobile ionic charge contamination of the oxide during device life, one can protect it with a film impervious to mobile ions such as amorphous or small-crystallite silicon nitride. For amorphous Si3N4, there is very little sodium penetration. Other sodium barrier layers include Al2O3, and phosphosilicate glass.

Oxide trapped charge is associated with defects in SiO,. The oxide traps are usually initially neutral and are charged by introducing electrons and holes into the oxide layer. This can occur from any current passing through the oxide layer, hot-carrier injection, or by photon excitation.

In modern integrated-circuit processing, heavily doped polysilicon has been used to replace Al as the gate electrode. For an n+-polysilicon gate, the Fermi level essentially coincides with the bottom of the conduction band EC, and the effective work function φm is equal to the Si electron affinity (χsi = 4.05 V). For a p+-polysilicon gate, the Fermi level coincides with the top of the valence band EV, and the effective workfunction φm is equal to the sum of χsi and Eg/q (5.17 V). This is one of the advantages of using poly-Si gates in MOSFETs since the same material can give different work functions by doping.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/Workfun.png)

## Carrier Transport
In an ideal MIS capacitor the conductance ofthe insulating film is assumed to be zero. Real insulators, however, show some degree of carrier conduction when the electric field or temperature is sufficiently high. The below table summarizes the basic conduction processes in insulators. It also emphasizes the voltage and temperature dependence of each process that are used often to identify the exact conduction mechanism experimentally.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/Table.png)

Tunneling is the most-common conduction mechanism through insulators under high fields. The tunnel emission is a result of quantum mechanics by which the electron wave function can penetrate through a potential barrier. It has the strongest dependence on the applied voltage but is essentially independent of the temperature. According to the following figure tunneling can be divided into direct tunneling and Fowler-Nordheim tunneling where carriers tunnel through only a partial width of the barrier.

The Schottky emission process is similar to the process discussed in the Schottky diode. In the table, the term subtracting from φB is due to image-force lowering. A plot of In(J/T2) versus 1/T yields a straight line with a slope determined by the net barrier height.

The Frenkel-Poole emission shown in the following figure, is due to emission of trapped electrons into the conduction band. The supply of electrons from the traps is through thermal excitation. For trap states with Coulomb potentials, the expression is similar to that of the Schottky emission. The barrier height, however, is the depth of the trap potential well. The barrier reduction is larger than in the case of Schottky emission by a factor of 2, since the barrier lowering is twice as large due to the immobility of the positive charge.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/Carrier_Transport.png)

At low voltage and high temperature, current is carried by thermally excited electrons hopping from one isolated state to the next. This mechanism yields an ohmic characteristic exponentially dependent on temperature.

The ionic conduction is similar to a diffusion process. Generally, the dc ionic conductivity decreases during the time the electric field is applied because ions cannot be readily injected into or extracted from the insulator. After an initial current flow, positive and negative space charges will build up near the metal-insulator and the semiconductor-insulator interfaces, causing a distortion of the potential distribution. When the applied field is removed, large internal fields remain which cause some, but not all, ions to flow back toward their equilibrium position. Because of this, hysteresis results in I-V traces.

The space-charge-limited current results from carriers injected into a lightly doped semiconductor or an insulator, where no compensating charge is present. The current for the unipolar trap-free case is proportional to the square of the applied voltage. Notice that the mobility regime is relevant here  since mobility is typically very low in insulators. 

For ultra-thin insulators, tunneling increases such that the conduction approaches that of the metal-semiconductor contact where the barrier is measured at the semiconductor surface instead of the insulator and the thermionic-emission current is multiplied by a tunneling factor.

For a given insulator, each conduction process may dominate in certain temperature and voltage range. The processes are also not exactly independent of one another and should be carefully examined. For example, for the large space-charge effect, the tunneling characteristic is found to be very similar to the Schottky-type emission. At high temperatures (and high fields), the current J , is due to Frenkel-Poole emission. At low temperatures, the conduction is tunneling limited (J2) which is temperature insensitive. One can also observe that the tunneling current strongly depends on the barrier height, which is related to the energy gap of the insulators. At intermediate temperatures, the current J3 is ohmic in nature.

## Nonequilibrium and Avalanche
In a nonequilibrium condition, the depletion width is larger than the maximum value W<sub>Dm</sub> at equilibrium. This condition is called deep depletion. As the bias is swept from depletion to strong inversion, a large concentration of minority carriers is needed at the semiconductor surface. This supply of minority camers is limited by the thermal generation rate. For a fast sweep rate, the thermal generation rate cannot keep up with the demand and deep depletion occurs. The energy-band diagram for deep depletion is shown in the following figure a. Equilibrium condition in the Fig. b can be restored by slowing or stopping the voltage ramp, by raising the temperature for larger thermal generation rate, or by shining light to produce additional electron-hole pairs. When switched to equilibrium, the field is redistributed, most of which is across the oxide layer.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/Non_equi.png)

If driven into deep depletion with a sufficiently large bias, avalanche multiplication and breakdown can occur in the semiconductor side (Fig. 26c), similar to that in a p-n junction. The breakdown voltage is defined as the gate voltage that makes the ionization integral equal to unity, when integrated along a path from the semiconductor surface to the depletion-layer boundary. For similar fields within the semiconductor, an MOS structure takes a higher bias compared to a p-n because of the additional voltage taken up in the oxide layer. The breakdown voltage VBD, as a function of doping level,
has a valley before it goes up again. The decrease of VBD is the same trend as in a p-n junction due to the increased field with doping. The rise after the minimum is because at high doping levels, the higher field at the semiconductor surface at breakdown induces a larger voltage across the oxide layer, leading to a higher terminal voltage. Another point is that for lower impurity concentrations, the MOS breakdown is actually smaller than those of p-n junctions. This is due to the inclusion of the edge effect in this study. Near the perimeter of the gate electrode, the field is higher due to the two-dimensional effect which leads to a lower breakdown voltage.

Because of avalanche multiplication, reliability also becomes an issue due to the injection of carriers,39 shown in Fig. 26c. Carriers generated by avalanche multiplication in the surface depletion layer, electrons in this example, will have enough energy to surmount the interfacial energy barrier and enter into the oxide layer. The passage of hot electrons into the oxide layer generally create fixed charge, bulk and interface traps in the oxide.

Hot-carrier or avalanche injection is closely related to many MOS device operations. For example, in a MOSFET, channel carriers can be accelerated by the source-to-drain electric field to have sufficient energy to surmount the Si-SiO, interfacial energy barrier. These effects are undesirable because they create a change in device characteristics during operation. On the other hand, these phenomena can be utilized in nonvolatile semiconductor memories.

Another source of hot carriers is ionization radiation such as X-ray or γ-ray. Ionization radiation creates electron-hole pairs in the oxide by breaking Si-O bonds. The electric field applied across the oxide during radiation exposure drives the generated carriers in opposite directions. The electrons are considerably more mobile than the holes as they rapidly drift toward the positive electrode where most flow out into the external circuit; the holes drift much more slowly toward the negative electrode and some become trapped. The trapped holes constitute the radiation-induced positive oxide charge often observed. These trapped holes may also be responsible for the increased interface-trap density usually associated with ionizing radiation.

Under optical illumination, the main effect on the MIS capacitance curves is that the capacitance in the strong-inversion region approaches the low-frequency value as the intensity of illumination is increased. Two basic mechanisms are responsible for this effect. The first is the decrease in the time constant of minority-carrier generation in the inversion layer. The second is the generation of electron-hole pairs by photons, which causes a decrease of the surface potential tys under constant applied voltage. This decrease of (vs results in a reduction of the depletion width with a corre-
sponding increase of the capacitance. The second mechanism is dominant when the measurement frequency is high. Also under the condition of deep depletion caused by a fast gate sweep [curve-(d) in Fig. 71, the extra electron-holes pairs can supply carriers for maintaining equilibrium and curve-(d) will collapse to curve-(c)]

## Accumulation- and Inversion-Layer Thickness
For an MIS capacitor, the maximum capacitance is equal to εi/d which implies that charges on both sides of the electrodes cling to the two interfaces of the insulator. While such an assumption is valid on the metal-insulator interface, detailed examination on the insulator-semiconductor interface reveals that it can lead to considerable error, especially for thin oxides. This is due to charges on the semiconductor side, either accumulation or strong-inversion charges, have a distribution as a hnction of distance from the interface. Effectively this would reduce the maximum capacitance given by εi/d.

In the classical physics, the charge distribution is controlled by the Poisson equation. Using Boltzmann statistics, the Poisson equation become:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Crho%28x%29%20%3D%20N_Aexp%28-%5Cfrac%7Bq%5Cpsi_p%7D%7BkT%7D%29%20%5C%5C%5C%5C%20%5Cfrac%7Bd%5E2%5Cpsi%7D%7Bdx%5E2%7D%20%3D%20-%5Cfrac%7B%5Crho%28x%29%7D%7B%5Cepsilon%20_s%7D%20%3D%20-%5Cfrac%7BqN_A%7D%7B%5Cepsilon%20_s%7Dexp%28-%5Cfrac%7Bq%5Cpsi_p%7D%7BkT%7D%29)

The solution of the above equation is:

![](https://latex.codecogs.com/svg.latex?%5Cinline%20%5CLARGE%20%5Cpsi_p%28x%29%20%3D%20-%5Cfrac%7BkT%7D%7Bq%7Dln%28sec%5E2%5C%7Bcos%5E%7B-1%7D%5Bexp%28-%5Cfrac%7Bq%5Cpsi_p%7D%7B2kT%7D%5D-%5Cfrac%7Bx%7D%7B%5Csqrt2L_D%7D%5C%7D%29%20%5C%5C%5C%5C)

The total accumulation layer thickness where y, approaches zero is equal to πLD/sqrt(2) which is in the order of a few tens of nm. However, most of the carriers are confined very close to the surface. Figure 28 shows the potential and carrier distributions for two different biases. It shows that although the concentration peaks at the surface, it spreads out with an effective distance of the order of a few nm. This spread is also a function of the bias; higher bias forces the carriers to be closer to the interface.

In quantum mechanics, the wavefunction associated with the carriers is near zero at the insulator-semiconductor interface because of the high barrier of the insulator. As a consequence, the carrier concentration peaks at some finite distance from the interface. This distance is approximately 10 Ang. Macroscopically, this effect can be interpreted as a degradation in oxide capacitance (or thicker oxide). Ten ang of Si is equivalent to 3 ang of SiO2,
taking into account the difference in dielectric constant. This amount adds to the oxide thickness and lowers the capacitance. Also shown in the figure is the classical calculation. The quantum effect is shown to cause more pronounced degradation than the classical model. Another factor that
causes further reduction of the capacitance is the polysilicon gates widely used in commercial technologies. Even if the polysilicon is degenerately doped, the depletion-layer and accumulation-layer thicknesses are still finite.

## Dielectric Breakdown
One common concern for an MOS device is reliability. Under a large bias, some current will conduct through the insulator, most commonly a tunneling current. These energetic carriers cause defects in the bulk of the dielectric film. When these defects reach a critical density level, catastrophic breakdown occurs. Microscopically, a percolation theory is used to explain breakdown (the following figure). On the passage of energetic
carriers, defects are generated randomly. When defects are dense enough to form a continuous chain connecting the gate to the semiconductor, a conduction path is created and catastrophic breakdown occurs.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MIS_Capacitor/diele_break.png)

A measure to quantify reliability is time to breakdown, tBD, which is the total stress time until breakdown occurs. An alternate quantity is called charge to break-down qBD, which is the total charge (integrating the current) passed through the device within tBD. Obviously tBD and q B D are both function of applied bias. The plots of qBD would show similar shapes and trend. A few key points can be noticed in this figure. First, tBD is a function of bias. Even for a small bias, eventually the oxide will break down, taking a very long time. Conversely, a large field can be sustained for a very short time without breaking down. To search for the breakdown field quickly, typically a voltage ramp is applied until a large current is detected. For a common measurement, the ramping rate is typically in the order of 1 V/s. The figure shows that for this time frame, the breakdown field is around 10 MV/cm. As the
oxide thickness becomes thinner, the breakdown field increases. More-recent results, however, show that this breakdown field would drop for thicknesses below = 4 nm, due to an increase of tunneling current.
