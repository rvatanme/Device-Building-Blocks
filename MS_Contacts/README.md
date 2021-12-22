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
