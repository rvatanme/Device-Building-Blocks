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

Note the comparison of S to c2 (= dφ<sub>Bn0</sub>/dφ<sub>m</sub>). We can also plot the index S as a function of the electronegativity difference (ionicity ΔX) of the semiconductors. The electronegativity difference is defined as the difference in the Pauling electronegativities between the cation and the anion of the semiconductor. Note a sharp transition from the covalent semiconductors (such as GaAs with ΔX= 0.4) to ionic semiconductors (such as AlN with ΔX= 1.5). For semiconductors with ΔX < 1, the index S is small, indicating that the barrier height is only weakly dependent on metal electronegativity (or the work function). On the other hand, for ΔX > 1, the index S approaches 1, and the barrier height is strongly dependent on the metal electronegativity (or the work function).

For technological applications in silicon integrated circuits, an important class of Schottky barrier contacts has been developed in which a chemical reaction between the metal and the underlying silicon is induced to form silicides. The formation of metal silicides by solid-solid metallurgical reaction provides more reliable and reproducible Schottky barriers, because the interface chemical reactions are well defined and can be maintained under good control. It is thought that since the silicide interfacial properties depends on the eutectic temperature, there should be a correlation between the barrier height and the eutectic temperature.

The image-force lowering, also known as the Schottky effect or Schottky-barrier lowering, is the image-force-induced lowering of the barrier energy for charge carrier emission, in the presence of an electric field. When an electron is at a distance x from the metal, a positive charge will be induced on the metal surface. The force of attraction between the electron and the induced positive charge is equivalent to the force that would exist between the electron and an equal positive charge at distance -x. This positive charge is referred to as the image charge. The attractive force toward the metal, called the image force, and The work done to an electron in the course of its transfer from infinity to the point x is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20F%20%3D%20%5Cfrac%7B-q%5E2%7D%7B4%5Cpi%20%5Cepsilon%20_s%282x%29%5E2%7D%20%3D%20%5Cfrac%7B-q%5E2%7D%7B16%5Cpi%20%5Cepsilon%20_sx%5E2%7D%20%5C%5C%5C%5C%5C%5C%20PE%28x%29%20%3D%20%5Cint_%7B%5Cinfty%7D%5E%7Bx%7DFdx%20%3D%20%5Cfrac%7B-q%5E2%7D%7B16%5Cpi%20%5Cepsilon%20_sx%7D)

When an external field 8 is applied (in this example in the -x direction), the total potential energy PE as a function of distance is given by the sum:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20PE%28x%29%20%3D%20-%5Cfrac%7Bq%5E2%7D%7B16%5Cpi%20%5Cepsilon%20_sx%7D%20-%20q%7C%5Cxi%7Cx)

This equation has a maximum value. The image-force lowering Δφ is maximum at x<sub>m</sub> and is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20x_m%20%3D%20%5Csqrt%7B%5Cfrac%7Bq%7D%7B16%5Cpi%20%5Cepsilon%20_s%7C%5Cxi%7C%7D%7D%20%5C%5C%5C%5C%5C%5C%20%5CDelta%20%5Cphi%20%3D%20%5Csqrt%7B%5Cfrac%7Bq%7C%5Cxi%7C%7D%7B4%5Cpi%20%5Cepsilon%20_s%7D%7D%3D%202%7C%5Cxi%7Cx_m)

From the above equations, we obtain Δφ = 0.12 V and x<sub>m</sub> = 6 nm for χ = lE5 V/cm; and Δφ = 1.2 V and x<sub>m</sub> = 1 nm for χ = lE7 V/cm. Thus at high fields the Schottky barrier is considerably lowered, and the effective metal work hnction for thermionic emission (qφ<sub>B</sub>) is reduced. 

Note that inside a device such as metal-semiconductor contact, the field is not zero even without bias due to the built-in potential. Although the barrier lowering is small under no bias or forward bias, it does have a profound effect on current transport processes in metal-semi- conductor systems.

In a practical Schottky-barrier diode, the electric field is not constant with distance, and the maximum value at the surface based on the depletion approximation can be used:

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MS_Contacts/image_lower.png)

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cxi%20_m%20%3D%20%5Csqrt%7B%5Cfrac%7B2qN_D%7C%5Cpsi%20_s%7C%7D%7B%5Cepsilon_s%7D%7D%20%5C%5C%5C%5C%20%7C%5Cpsi%20_s%7C%20%3D%20%5Cphi%20_%7BBn0%7D%20-%20%5Cphi%20_n%20&plus;%20V_R%20%5C%5C%5C%5C%20%5CDelta%20%5Cphi%20%3D%20%5Csqrt%7B%5Cfrac%7Bq%5Cxi%20_m%7D%7B4%5Cpi%5Cepsilon_s%7D%7D%3D%5B%5Cfrac%7Bq%5E3N_D%7C%5Cpsi_s%7C%7D%7B8%5Cpi%5E2%5Cepsilon_s%5E3%7D%5D%5E%7B1/4%7D)

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cphi%20_%7BBn%7D%20%3D%20%5Cphi%20_%7BBn0%7D%20-%20%5CDelta%5Cphi)

By introducing a thin layer (= 10 nm or less) of controllable number of dopants on a semiconductor surface (e.g., by ion implantation), the effective barrier height for a given metal-semiconductor contact can be varied according to the image force lowers (shown in the following figure). This approach is particularly useful in order to select a metal having the most desirable metallurgical properties required for reliable device operation and at the same time to be able to adjust the effective barrier height between this metal and the semiconductor in a controlled manner.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MS_Contacts/Adjust_Barrier.png)

For Si and GaAs Schottky barriers with background doping n<sub>2</sub> of the order of 1El6 cm-3 or less, the zero-bias value of n<sub>2</sub>(W-a) is about 1E11 cm-2 where a is the thickness of the inserted thin layer for adjusting the barrier hight. Therefore, if n<sub>1</sub>a is made sufficiently larger than 1E11 cm-2 where n1 is the doping of the thin layer, then the reduced barrier hight is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%7C%5Cxi_m%7C%5Capprox%20%5Cfrac%7Bqn_1a%7D%7B%5Cepsilon%20_s%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%20%5CDelta%20%5Cphi%20%3D%20%5Cfrac%7Bq%7D%7B%5Cepsilon_s%7D%5Csqrt%7B%5Cfrac%7Bn_1a%7D%7B4%5Cpi%7D%7D)

For nla = 1El2 and 1E13 cm-2, the corresponding lowerings are 0.045 and 0.14 V, respectively. Although the image-force lowering contributes to the barrier reduction, generally the tunneling effect is more significant. For a given application, the parameters nl and a should be properly chosen so that
in the forward direction the larger Schottky-barrier lowering and the added tunneling current will not substantially degrade the ideality factor η. And in the reverse direction, they will not cause large leakage current in the required bias range.

## Current Transport Processes
The current transport in metal-semiconductor contacts is due mainly to majority carriers, in contrast to p-n junctions where the minority carriers are responsible. The following figure shows five basic transport processes under forward bias (the inverse processes occur under reverse bias).

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/MS_Contacts/Transport.png)

These five processes are (1) emission of electrons from the semiconductor over the potential barrier into the metal [the dominant process for Schottky diodes with moderately doped semiconductors (e.g., Si with ND < lE17 cm-3) operated at moderate temperatures (e.g., 300 K)], (2) quantum-mechanical tunneling of electrons through the barrier (important for heavily doped semiconductors and responsible for most ohmic contacts) (3) recombination in the
space-charge region (identical to the recombination process in a p-n junction) (4) diffusion of electrons in the depletion region, and (5) holes injected
from the metal that diffuse into the semiconductor (equivalent to recombination in the neutral region). 

Schottky diode behavior is to some extent electrically similar to a one-sided abrupt p-n junction, and yet the Schottky diode can be operated as a majority-carrier device with inherent fast response. Thus, the terminal functions of a p-n junctio diode can general be performed by a Schottky diode with one exception as a charge-storage diode. This is because the charge-storage time in a majority-carrier device is extremely small. Another difference is the larger current density in a Schottky diode due to the smaller built-in potential as well as the nature of thermionic emission compared to diffusion. This results in a much smaller forward voltage drop. By the same token, the disadvantage is the larger reverse current in the Schottky diode and a lower breakdown voltage.

The Thermionic-emission theory is derived from three assumptions: 1) the barrier hight φ<sub>Bn</sub> is much larger than kT 2) thermal equilibrium is established at the plane that determines emission, and (3) the existence of a net current flow does not affect this equilibrium so that one can superimpose two current fluxes-one from metal to semiconductor, the other from semiconductor to metal, each with a different quasi Fermi level. If thermionic emission is the limiting mechanism, then E<sub>Fn</sub> is flat throughout the depletion region.  Because of these assumptions, the shape of the barrier profile is immaterial and the current flow depends solely on the barrier is then given by height. The current density from the semiconductor to the metal J<sub>s->m</sub> the concentration of electrons with energies sufficient to overcome the potential barrier and traversing in the x-direction:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J_%7Bs%5Crightarrow%20m%7D%20%3D%20%5Cint_%7BE_%7BFn%7D&plus;%5Cphi%20_%7BBn%7D%7D%5E%7B%5Cinfty%7D%20q%5Cnu%20_xdn%20%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%20dn%20%3D%20N%28E%29F%28E%29dE)

where N(E) and F(E) are the density of states and the distribution function, respectively. If we postulate that the distribution function can be given by Boltzmann distribution, all the energy of electrons in the conduction band is kinetic energy E-Ec=m*ν<sup>2</sup>/2, and the minimum kinitic energy of electrons in the x-direction is m*ν<sub>0x</sub><sup>2</sup>=q(ψ<sub>bi</sub>-V), then J<sub>s->m</sub> yields:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J_%7Bs%5Crightarrow%20m%7D%20%3D%20A%5E*T%5E2exp%28%5Cfrac%7B-q%5Cphi_%7BBn%7D%7D%7BkT%7D%29exp%28%5Cfrac%7BqV%7D%7BkT%7D%29%20%5C%5C%5C%5C%20A%5E*%20%3D%20%5Cfrac%7B4%5Cpi%20m%5E*qk%5E2%7D%7Bh%5E3%7D)

where A* is the effective Richardson constant for thermionic emission, neglecting the effects of optical-phonon scattering and quantum mechanical reflection. Since the barrier height for electrons moving from the metal into the semiconductor remains the same under bias, the current flowing into the semiconductor is thus unaffected by the applied voltage. It must therefore be equal to the current flowing from the semiconductor into the metal when thermal equilibrium prevails (i.e., when V = 0). This corresponding current density is obtained from Eq. 52 by setting V = 0, and therefore the total current is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J_%7Bm%5Crightarrow%20s%7D%20%3D%20A%5E*T%5E2exp%28%5Cfrac%7B-q%5Cphi_%7BBn%7D%7D%7BkT%7D%29%20%5C%5C%5C%5C%20J_%7Bn%7D%20%3D%20J_%7BTE%7D%5Bexp%28%5Cfrac%7BqV%7D%7BkT%7D%29-1%5D%5C%3B%2C%20%5C%5C%5C%5C%20J_%7BTE%7D%3DA%5E*T%5E2exp%28%5Cfrac%7B-q%5Cphi_%7BBn%7D%7D%7BkT%7D%29)

An alternative approach to derive the thermionic-emission current is the following. Without decomposing the velocity components, only electrons with energy
above the barrier will contribute to the forward current. This number of electrons above the barrier is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20n%20%3D%20N_Cexp%5B%5Cfrac%7B-q%28%5Cphi%20_%7BBn%7D-V%29%7D%7BkT%7D%5D)

It is known that for a Maxwellian distribution of velocities, the current from random motion of carriers across a plane is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J%20%3D%20nq%5Cfrac%7B%5Cnu_%7Bave%7D%7D%7B4%7D)

where ν<sub>ave</sub> is the average thermal velocity,

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cnu_%7Bave%7D%3D%5Csqrt%7B%5Cfrac%7B8kT%7D%7B%5Cpi%20m%5E*%7D%7D)

By combining the above equations, the former discussed TE current is obtained.


