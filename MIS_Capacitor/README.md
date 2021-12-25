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

    ψ<sub>s</sub> < 0    Accumilation of holes (upward band bending)
    ψ<sub>s</sub> = 0    Flat-band condition
    ψ<sub>Bp</sub> > ψ<sub>s</sub> > 0  Depletion of holes (bands bending downward)
    ψ<sub>s</sub> = ψ<sub>Bp</sub>      Fermi level at midgap, E<sub>i</sub>(0) = E<sub>F</sub>, n<sub>p</sub>(0) = p<sub>p</sub>(0) = n<sub>i</sub>
    2ψ<sub>Bp</sub> > ψ<sub>s</sub> > ψ<sub>Bp</sub> Weak inversion [electron enhancment, n<sub>p</sub>(0) > p<sub>p</sub>(0)]
    ψ<sub>s</sub> > 2ψ<sub>Bp</sub>     Strong inversion [n<sub>p</sub>(0) > p<sub>p</sub>(0) or N<sub>A</sub>]


