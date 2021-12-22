# Metal-Semiconductor Contacts
Metal-Semiconductor contacts have been found many applications in different devices as photodetectors, solar cells, as the gate electrode of the MESFET,
etc. Most importantly, the metal contact on heavily doped semiconductor forms an ohmic contact that is required for every semiconductor 
device in order to pass current in and out of the device.

## Formation of Barrier
When metal makes contact with a semiconductor, a barrier is formed at the metal- semiconductor interface. This barrier is responsible for 
controlling the current conduction as well as its capacitance behavior. In this section, we consider the basic energy-band diagrams leading to 
the formation of the barrier height and some effects that can modify the value of this barrier.

Let's first consider an ideal metal-semiconductor (MS) contact where there is no surface states or any other abnomalis it its junction. If a high work functioin metal and n-type semiconductor are allowed to communicate with each other, charge will follow from the semiconductor to the metal and thermal equilibrium will be estabilished whose peoperties depends on the physical gap between the metal and semiconductor as shown in the following figure. In the equilibrium, Fermi levels will line up and a depletion layer is created in the semiconductor side. Relative to the metal fermi level, the fermi level of the semiconductor is lowered by the amount of equal to the difference between the two work functions.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MS_Contacts/Band_diag_MS.png)

The potential difference between the two work functions φ<sub>m</sub> - (χ+φ<sub>n</sub>) is called the contact potential. As the gap distance δ decreases, the electric field in the gap increases and an increasing negative charge is built up at the metal surface. The potential variation within the depletion layer is similar to that in one side of a p-n junction. When δ is small enough to be comparable to the inter-atomic distances, the gap becomes transparent to electrons and the barrier hight is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20q%5Cphi%20_%7BBn0%7D%20%3D%20q%28%5Cphi%20_m%20-%20%5Cchi%29)

Conversely, for an ideal contact between a metal and ap-type semiconductor, the barrier height qφ<sub>Bp0</sub> is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20q%5Cphi%20_%7BBp0%7D%20%3D%20E_g%20-%20q%28%5Cphi%20_m%20-%20%5Cchi%29)

In practice, however, simple expressions for the barrier heights as given by above equations are never realized experimentally. The main deviations of experimental barrier heights from the ideal condition are: (1) an unavoidable interface layer, δ is not exactly zero, and (2) the presence of interface
states. Furthermore, the barrier height can be modified due to image-force lowering. These effects will be discussed in the following sections.

The depletion layer of a metal-semiconductor contact is similar to that of the one-sided abrupt (e.g., p<sup>+</sup>-n) junction. The energy-band diagrams for metals on both n-type and p-type materials are shown, under different biasing conditions, in the following figure.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MS_Contacts/MS_bias.png)

For contacts on n-type semiconductors, under the abrupt approximation that ρ = qN<sub>D</sub>, for x < W<sub>D</sub>, ρ = 0 and ξ(x) = 0 for x > W<sub>D</sub>, where WD is the depletion width, we obtain:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20W_D%20%3D%20%5Csqrt%7B%5Cfrac%7B2%5Cepsilon%20_s%7D%7BqN_D%7D%28%5Cpsi%20_%7Bbi%7D%20-%20V%20-%20kT/q%29%7D%20%5C%5C%5C%5C%5C%5C%20%7C%5Cxi%20%28x%29%7C%20%3D%20%5Cfrac%7BqN_D%7D%7B%5Cepsilon%20_s%7D%28W_D-x%29%3D%7C%5Cxi%20_m%7C%20-%20%5Cfrac%7BqN_Dx%7D%7B%5Cepsilon%20_s%7D%20%5C%5C%5C%5C%5C%5C%20E_c%28x%29%20%3D%20q%5Cphi%20_%7BBn0%7D%20-%20%5Cfrac%7Bq%5E2N_D%7D%7B%5Cepsilon%20_s%7D%28W_Dx%20-%20%5Cfrac%7Bx%7D%7B2%7D%29)

where the term kT/q arises from the contribution of the majority-carrier distribution tail (electrons in n-side) and ξ<sub>m</sub> is the maximum field
strength which occurs at x = 0:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cxi%20_m%20%3D%20%5Cxi%20%28x%3D0%29%20%3D%20%5Csqrt%7B%5Cfrac%7B2qN_D%7D%7B%5Cepsilon%20_s%7D%28%5Cpsi%20_%7Bbi%7D%20-%20V%20-%20kT/q%29%7D%20%3D%20%5C%5C%20%5Cfrac%7B2%28%5Cpsi%20_%7Bbi%7D%20-%20V%20-%20kT/q%29%7D%7BW_D%7D)

The space charge Q<sub>sc</sub>, per unit area of the semiconductor and the depletion-layer capacitance C, per unit area are given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20C_D%20%5Cequiv%20%5Cfrac%7B%5Cepsilon%20_s%7D%7BW_D%7D%20%5C%5C%5C%5C%5C%5C%20%5Cfrac%7B1%7D%7BC_D%5E2%7D%20%3D%20%5Cfrac%7B2%28%5Cpsi%20_%7Bbi%7D%20-%20V%20-%20kT/q%29%7D%7BqN_D%5Cepsilon%20_s%7D%20%5C%5C%5C%5C%5C%5C%20N_D%20%3D%20%5Cfrac%7Bq%5Cepsilon_s%7D%7B2%7D%5B-%5Cfrac%7B1%7D%7Bd%281/C%5E2%29/dV%7D%5D)

If N<sub>D</sub> is constant throughout the depletion region, one should obtain a straight line by plotting 1/C<sup>2</sup> versus voltage. If N<sub>D</sub> is not a constant, the differential capacitance method can be used to determine the doping profile from deferential form of above equation.  

The C-V measurement can also be used to study deep impurity levels. the following figure shows a semiconductor with one shallow donor level and one deep donor. While all the shallow donors above the Fermi level will be ionized, only deep impurities near the surface are above the Fermi level and ionized, giving a higher effective doping concentration near the interface. In a C-V measurement where a small ac signal is superimposed on the dc bias, there will be a frequency dependence on capacitance since the deep impurities can only follow slow signals, i.e. dNT/dV is absent at high frequencies. Comparing C-V measurements at various frequencies can reveal the properties of these deep-level impurities.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MS_Contacts/CV_imp.png)

The barrier heights of metal-semiconductor systems are, in general, determined by both the metal work function and the interface states. A general expression of the barrier height can be obtained on the basis of the following two assumptions: 1) with intimate contact between the metal and the semiconductor, and with an interfacia1 layer of atomic dimensions, this layer will be transparent to electrons but can withstand potential across it, and (2) the interface states per unit area per energy at the interface are a property of the semiconductor surface and are independent of the metal. A more detailed energy-band diagram of a practical metal-n-semiconductor contact is shown in the following figure. 

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MS_Contacts/Detail_Band_diag.png)

The first quantity of interest in the above figure is the energy level qφ<sub>0</sub> above E<sub>V</sub>, at the semiconductor surface. It is called the neutral level above which the states are of acceptor type (neutral when empty, negatively charged when full) and below which the states are of donor type (neutral when full of electrons, positively charged when empty). Consequently, when the Fermi level at the surface coincides with this neutral level, the net interface-trap charge is zero. This energy level also tends to pin the semiconductor Fermi level at the surface before the metal contact was formed.

We consider a semiconductor with acceptor interface traps (since in this particular example E<sub>F</sub> is above the neutral level) whose density is D<sub>it</sub>, states/cm2-eV, and is a constant over the energy range from qφ<sub>0</sub> + E , to the Fermi level. The interface-trap charge density on the semiconductor Q<sub>ss</sub> is therefore negative and is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20Q_%7Bss%7D%20%3D%20-qD_%7Bit%7D%28E_g-q%5Cphi%20_0%20-q%5Cphi%20_%7BBn0%7D%29%20%5C%3B%5C%3B%5C%3B%5C%3B%20C/cm%5E2)

The space charge that forms in the depletion layer of the semiconductor at thermal equilibrium is given as:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20Q_%7Bsc%7D%20%3D%20qN_DW_D%20%3D%20%5Csqrt%7B2q%5Cepsilon%20_sN_D%28%5Cphi%20_%7BBn0%7D%20-%20%5Cphi%20_n%20-%20kT/q%29%7D)

In the absence of any space-charge effects in the interfacial layer, an exactly equal and opposite charge, Q<sub>M</sub> (C/cm2), develops on the metal surface. For thin interfacial layers such space-charge effects are negligible and Q<sub>M</sub> and the potential across the interface can be written as:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20Q_M%20%3D%20-%28Q_%7Bss%7D%20&plus;%20Q_%7Bsc%7D%29%20%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%20%5Cbigtriangleup%20%3D%20-%5Cfrac%7B%5Cdelta%20Q_M%7D%7B%5Cepsilon%20_s%7D)

where ε<sub>i</sub> is the permitivity of the interfacial layer and δ its thickness. Another relation for interficial potential can be obtained by inspection of the energy-band diagram of the above figure:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cbigtriangleup%20%3D%20%5Cphi%20_m%20-%20%28%5Cchi%20&plus;%20%5Cphi%20_%7BBn0%7D%29)

By combining all the above equation, the following expression of barrier hight can be given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cphi%20_%7BBn0%7D%20%3D%20c_2%28%5Cphi%20_m%20-%20%5Cxi%29%20&plus;%20%281-c_2%29%28%5Cfrac%7BE_g%7D%7Bq%7D-%5Cphi%20_0%29%20%5C%5C%20%5Cequiv%20c_2%5Cphi%20_m%20&plus;%20c_3%20%5C%5C%5C%5C%20c_2%20%5Cequiv%20%5Cfrac%7B%5Cepsilon%20_i%7D%7B%5Cepsilon%20_i%20&plus;%20q%5E2%20%5Cdelta%20D_%7Bit%7D%7D)

With known c2 and c3 from experiments of varying φ<sub>m</sub> , the interfacial properties are given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cphi%20_%7B0%7D%20%3D%20%5Cfrac%7BE_g%7D%7Bq%7D-%5Cfrac%7Bc_2%5Cchi%20&plus;%20c_3%7D%7B1-c_2%7D%20%5C%5C%5C%5C%20D_%7Bit%7D%20%3D%20%5Cfrac%7B%281-c_2%29%5Cepsilon%20_s%7D%7Bc_2%5Cdelta%20q%5E2%7D)

Using the previous assumptions for δ and ε<sub>i</sub>, we obtain D<sub>it</sub> = 1.1E13(1-c2) /c2 states/cm2-eV. There are two limiting cases which can be obtained directly from the above equations: 1) When D<sub>it</sub> --> inf, then c2 --> 0 and qφ<sub>Bn0</sub> = E<sub>g</sub> - qφ<sub>0</sub>. In this case the Fermi level at the interface is pinned by the surface states at the value qφ<sub>0</sub> above the valence band. The barrier height is independent of the metal work function and is determined entirely by the surface properties of the semiconductor. 2) When D<sub>it</sub> --> 0, then c2 --> 1 and qφ<sub>Bn0</sub> = q(φ<sub>m</sub> - X) that is the barrier height of an ideal Schottky barrier. We note that the values of qφ<sub>0</sub>, for Si, GaAs, and GaP are very close to one-third of the bandgap. Similar results are obtained for other semiconductors. This fact indicates that most covalent semiconductor surfaces have a high peak density of surface states or defects near the neutral level and that the neutral level is about one-
third of the bandgap from the valence-band edge.

for most III-V compounds, the barrier height is essentially independent of metal work function. For ionic semiconductors such as CdS and ZnS, the barrier height generally depends strongly on the metal and a correlation has been found between interface behavior and the electronegativity of the metal. From the following figure that is a plot of the barrier height versus the electronegativity of metals deposited on Si, GaSe, and SiO2. From the plot we define the slope as an index of interface behavior:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20S%20%5Cequiv%20%5Cfrac%7Bd%5Cphi_%7BBn0%7D%7D%7BdX_M%7D)
