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

