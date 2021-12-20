# PN Junctioins
p-n junctions are of great importance both in modern electronic applications and in understanding other semiconductor devices. The p-n junction theory serves as the foundation of the physics of semiconductor devices. 

## PN Junctions at Thermal Equilibrium
At thermal equilibrium under no bias, Boltzmann statistics and Poisson equation can be employed together in order to model a pn junction. First, let's consider a parallel abrupt pn junction where the acceptor doping concentration of the P side abruptly changes to the donor concentration of the n side. In this case, a layer named depletion layer is created at the interface where negligble free carrier exists, n(x) ≈ p(x) ≈ 0. Assumming complete ionization, depletion layer contains a pile of fixed negative and positive charges at the p and n side, respectively.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/ab_pn_equi.png)

 The depletion layer reslts in a  built in potential that is the fundumental characteristic of any pn junction. Using Boltzmann equation, the build in potential, under complete ionization, is obtained as follows: 
 
![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/biuld_in.png)


![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/pn_diagram.png)


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cpsi_%7Bbi%7D%20%3D%20%5Cfrac%7BkT%7D%7Bq%7Dln%28%5Cfrac%7BN_DN_A%7D%7Bn_i%5E2%7D%29)
 
 
Other Characteristic physical properties of a pn junction including maximum electric field at the juctuin and the depletion width can be expressed based on build in potential. By applying Poisson equation in the p and n sides of the depletion layer in the sketched pn junction, we get:
 
 ![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cfrac%7Bd%5E2%5Cpsi_i%7D%7Bdx%5E2%7D%20%3D%20%5Cfrac%7BqN_A%7D%7B%5Cepsilon_s%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%20for%20%5C%3B%5C%3B%20-W_%7BDp%7D%20%5Cleq%20x%20%5Cleq%200%20%5C%5C%5C%5C%20-%5Cfrac%7Bd%5E2%5Cpsi_i%7D%7Bdx%5E2%7D%20%3D%20%5Cfrac%7BqN_D%7D%7B%5Cepsilon_s%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%20for%20%5C%3B%5C%3B%200%20%5Cleq%20x%20%5Cleq%20W_%7BDn%7D)
 
where ψ<sub>i</sub> is the potential. The electric field is then obtained by integrating the above equations, as follows:
 
 ![](https://latex.codecogs.com/svg.latex?%5Clarge%20%5Cxi%20%28x%29%20%3D%20-%5Cfrac%7BqN_A%7D%7B%5Cepsilon_s%7D%28x&plus;W_%7BDp%7D%29%20%5C%3B%5C%3B%5C%3B%5C%3B%20for%20%5C%3B%5C%3B%20-W_%7BDp%7D%20%5Cleq%20x%20%5Cleq%200%20%5C%5C%5C%5C%20%5Cxi%20%28x%29%20%3D%20-%5Cfrac%7BqN_D%7D%7B%5Cepsilon_s%7D%28W_%7BDn%7D-x%29%20%5C%3B%5C%3B%5C%3B%5C%3B%20for%20%5C%3B%5C%3B%200%20%5Cleq%20x%20%5Cleq%20W_%7BDn%7D)
 
 
 ![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/ele_field_pn.png)
 
 where ξ is the electric field. Integrating from the above equation once again gives the potential distribution as follows:
 
 ![](https://latex.codecogs.com/svg.latex?%5Clarge%20%5Cpsi_i%20%28x%29%20%3D%20%5Cfrac%7BqN_A%7D%7B2%5Cepsilon_s%7D%28x&plus;W_%7BDp%7D%29%5E2%20%5C%3B%5C%3B%5C%3B%5C%3B%20for%20%5C%3B%5C%3B%20-W_%7BDp%7D%20%5Cleq%20x%20%5Cleq%200%20%5C%5C%5C%5C%20%5Cpsi_i%20%28x%29%20%3D%20%5Cpsi_i%20%280%29%20&plus;%20%5Cfrac%7BqN_D%7D%7B2%5Cepsilon_s%7D%28W_%7BDn%7D-%5Cfrac%7Bx%7D%7B2%7D%29x%20%5C%3B%5C%3B%5C%3B%5C%3B%20for%20%5C%3B%5C%3B%200%20%5Cleq%20x%20%5Cleq%20W_%7BDn%7D)
 
 Finally, by some mathematical simplification, the following equations are obtained:
 
 
 ![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%7C%5Cxi%20_m%7C%20%3D%20%5Cfrac%7B2%5Cpsi%20_%7Bbi%7D%7D%7BW_D%7D%20%3D%20%5Csqrt%7B%5Cfrac%7B2qN_AN_D%5Cpsi%20_%7Bbi%7D%7D%7B%5Cepsilon%20_s%28N_A&plus;N_D%29%7D%7D)
 
 
 ![](https://latex.codecogs.com/svg.latex?%5CLARGE%20W_D%20%3D%20W_%7BDp%7D%20&plus;%20W_%7BDn%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%20%5Cfrac%7BW_%7BDn%7D%7D%7BW_D%7D%20%3D%20%5Cfrac%7BN_A%7D%7BN_A%20&plus;%20N_D%7D)
 
 
 ![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cpsi%20_bi%20%3D%20%5Cpsi%20_%7BBp%7D%20&plus;%20%5Cpsi%20_%7BBn%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%20%5Cfrac%7B%5Cpsi%20_%7BBn%7D%7D%7B%5Cpsi%20_%7Bbi%7D%7D%20%3D%20%5Cfrac%7BN_A%7D%7BN_A%20&plus;%20N_D%7D)
 
 
 This discussion uses depletion approximation where it's assumed that n(x) ≈ p(x) ≈ 0. In reality, due to the majority-carrier distribution tail, there is a low concentration of majority carrier in both sides of the junction. Therefore, a more accurate result for the depletion-layer properties can be obtained by considering this contribution in the Poisson equation, that is, ρ = q[N<sub>A</sub> - p(x)]  on the p-side and ρ = q[N<sub>D</sub> - n(x)] on the n-side. By solving Poisson equation with the new expression, it's reaveld that all the previous equation is true with this difference that the ψ<sub>bi</sub> should be replaced by ψ<sub>bi</sub> - 2kT/q and ψ<sub>bi</sub> - V - 2kT/q under no bias and bias V, respectively.
 
 
 The net potential at zero bias is near 0.8 V for Si and 1.3 V for GaAs. This net potential will be decreased under forward bias and increased
under reverse bias. These results can also be used for GaAs since both Si and GaAs have approximately the same static dielectric constants. To obtain the depletion-layer width for other semiconductors such as Ge, one must multiply the results of Si by the (\epsilon_Ge / \epsilon_Si)^1/2 (= 1.16) factor. The simple model above can give adequate predictions for most abrupt p-n junctions.

The depletion-layer capacitance per unit area is defined as C<sub>D</sub> = dQ<sub>D</sub>/dV = ε<sub>s</sub>/W<sub>D</sub>, where Q<sub>D</sub> is the incremental change of depletion charge in each side of the junction (total charge is zero) upon the incremental change of the applied voltage dV. By plugging the former derived expression for W<sub>D</sub> and rearranging the equation, depletion capacitance for a one-side abrupt junction is given by:


![](https://latex.codecogs.com/svg.latex?%5CLARGE%201/C_D%5E2%20%3D%20%5Cfrac%7B2%7D%7Bq%5Cepsilon%20_sN%7D%28%5Cpsi%20_%7Bbi%7D%20-%20V%20-%202kT/q%29)


Therefore by plotting 1/C<sub>D</sub><sup>2</sup> versus a straight line should result from a one-sided abrupt junction (Fig. 3). The slope gives the impurity concentration of the substrate (N), and the extrapolation gives (ψ<sub>bi</sub> - 2kT/q). Note that, for the forward bias, a diffusion capacitance exists in addition to the depletion capacitance.

Note that the semiconductor potential and the capacitance-voltage data are insensitive to changes in the doping profiles that occur in a distance less than a Debye length. The Debye length L, is a characteristic length for semiconductors and is defined as:


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20L_D%20%3D%20%5Csqrt%7B%5Cfrac%7BkT%5Cepsilon%20_s%7D%7Bq%5E2N%7D%7D%20%3D%20%5Csqrt%7B%5Cfrac%7B%5Cepsilon%20_s%7D%7BqN%5Cbeta%20_%7Bth%7D%7D%7D)


In another words, the bare Coulomb potential of an ionized impurity is exponentially screened by the medium, over a distance of the Debye length, therefore the effect of that impurity on the potential of a carrier is considerable only outside the Deby length. At thermal equilibrium the depletion-layer widths of abrupt junctions are about 8L<sub>D</sub>, for Si, and 10L<sub>D</sub>, for GaAs. For a doping density of 1E16 cm-3, the Debye length is 40 nm; for other dopings, L<sub>D</sub> will vary as N^-1/2, that is, a reduction by a factor of 3.16 per decade.


Now let's consider a linearly graded pn junction. In this case, the form of Poisson equation is as follows:


![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/graded_junc.png)


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20-%5Cfrac%7Bd%5E2%5Cpsi%20_i%7D%7Bdx%5E2%7D%20%3D%20%5Cfrac%7Bd%5Cxi%7D%7Bdx%7D%20%3D%20%5Cfrac%7Bq%7D%7B%5Cepsilon%20_s%7D%28p-n&plus;ax%29%20%5C%5C%5C%5C%5C%5C%20%5Capprox%20%5Cfrac%7Bqax%7D%7B%5Cepsilon%20_s%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%20-%5Cfrac%7BW_D%7D%7B2%7D%20%5Cleq%20x%20%5Cleq%20%5Cfrac%7BW_D%7D%7B2%7D)


where a is the doping gradient in cm-4 unit. By integrating the above equation once and twice, the electric field and potential is obtained as follows:


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cxi%28x%29%20%3D%20-%5Cfrac%7Bqa%7D%7B2%5Cepsilon%7D%5B%7B%28%5Cfrac%7BW_D%7D%7B2%7D%29%5E2%7D-x%5E2%5D)


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cpsi%20_i%28x%29%20%3D%20%5Cfrac%7Bqa%7D%7B6%5Cepsilon%20_s%7D%5B2%28%5Cfrac%7BW_D%7D%7B2%7D%29%5E3&plus;3%28%5Cfrac%7BW_D%7D%7B2%7D%29%5E2x-x%5E3%5D)


![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/ele_fie_gra.png)


Using the above equation, maximum electric field and deplation width can be derived as a function of build in potential: 

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%7C%5Cxi%20_m%7C%20%3D%20%5Cfrac%7BqaW_D%5E2%7D%7B8%5Cepsilon%20_s%7D%20%5C%5C%5C%5C%20W_D%20%3D%20%28%5Cfrac%7B12%5Cepsilon_s%5Cpsi%20_%7Bbi%7D%7D%7Bqa%7D%29%5E%7B1/3%7D)

Since the values of the impurity concentrations at the edges of the depletion region (-W<sub>D</sub>/2 and W<sub>D</sub>/2) are the same and equal to aW<sub>D</sub>/2, the built-in potential for a linearly graded junction can be approximated by an expression:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cpsi%20_%7Bbi%7D%20%5Capprox%20%5Cfrac%7BkT%7D%7Bq%7Dln%5B%5Cfrac%7B%28aW_D/2%29%28aW_D/2%29%7D%7Bn_i%5E2%7D%5D%20%5Capprox%20%5Cfrac%7B2kT%7D%7Bq%7Dln%5B%5Cfrac%7BaW_D%7D%7B2n_i%7D%5D)

By plugging W<sub>D</sub> as a function of ψ<sub>bi</sub> in the above equation, the built-in potential can be calcu-
lated explicitly by an expression as a gradient voltage V<sub>g</sub>:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20V_g%20%3D%20%5Cfrac%7B2kT%7D%7B3q%7Dln%5B%5Cfrac%7Ba%5E2%5Cepsilon%20_skT%7D%7B8n_i%5E3q%5E2%7D%5D)

The depletion-layer capacitance for a linearly graded junction is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20C_D%20%3D%20%5Cfrac%7B%5Cepsilon%20_s%7D%7BW_D%7D%20%3D%20%5B%5Cfrac%7Bqa%5Cepsilon%20_s%5E2%7D%7B12%28%5Cpsi%20_%7Bbi%7D%20-%20V%29%7D%5D%5E%7B1/3%7D)


In the case of any arbitray doping profile near the junction, the potenial on the n side and the total depletion-layer charge of a one-side pn junctioin is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cpsi%20_n%20%3D%20%5Cfrac%7Bq%7D%7B%5Cepsilon%20_s%7D%5Cint_%7B0%7D%5E%7BW_%7BDn%7D%7DxN_D%28x%29dx)


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20Q_D%20%3D%20q%5Cint_%7B0%7D%5E%7BW_%7BDn%7D%7DN_D%28x%29dx)

Differentiating the above quantities with respect to the depletion width gives:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cfrac%7BdV%7D%7BdW_D%7D%20%3D%20-%5Cfrac%7Bd%5Cpsi%20_n%7D%7BdW_D%7D%20%3D%20-%20%5Cfrac%7BqN_D%28W_D%29W_D%7D%7B%5Cepsilon%20_s%7D%20%5C%5C%5C%5C%5C%5C%20%5Cfrac%7BdQ_D%7D%7BdW_D%7D%20%3DqN_D%28W_D%29%20%5C%5C%5C%5C%5C%5C%20C_D%3D%7C%5Cfrac%7BdQ_D%7D%7BdW_D%7D%7C%3D%7C%5Cfrac%7BdQ_D%7D%7BdW_D%7D%5Cfrac%7BdW_D%7D%7BdV%7D%7C%3D%5Cfrac%7B%5Cepsilon%20_s%7D%7BdW_D%7D)

Therefore, the general expression of ε<sub>s</sub>/W<sub>D</sub> is obtained and is applicable to depletion layer capacitance for any arbitrary doping profile. From this we can derive the following equation for a general nonuniform profile:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20%5Cfrac%7Bd%281/C_D%5E2%29%7D%7BdV%7D%20%3D%20-%5Cfrac%7B2%7D%7Bq%5Cepsilon%20_sN_D%28W_D%29%7D)

This C-V technique can be used to measure nonuniform doping profile. The 1/C<sub>D</sub><sup>2</sup>-V plot would deviate from a straight line if the doping is not constant.

## PN Junction Under Bias
Let's first consider an ideal case where the following conditions hold: 1) deplation-layer approximation which states that all the drop potential happens in depletion layer and therefore electric field is zero outside the depletion layer 2) Boltzmann equation is valid 3) low injection regime holds 4) no generation and recombination takes place in the depletion region.

We first define the quasi-Fermi levels as follows:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20E_%7BFn%7D%20%5Cequiv%20E_i%20&plus;%20kTln%28%5Cfrac%7Bn%7D%7Bn_i%7D%29%20%5C%5C%5C%5C%20E_%7BFp%7D%20%5Cequiv%20E_i%20-%20kTln%28%5Cfrac%7Bp%7D%7Bn_i%7D%29)

where n and p are the electron and hole concentration in any region of interest in the pn junction, under bias. Therefore the product of pn, unlike thermal equilibrium, is not n<sub>i</sub><sup>2</sup>:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20pn%20%3D%20n_i%5E2exp%28%5Cfrac%7BE_%7BFn%7D-E_%7BFp%7D%7D%7BkT%7D%29)

where for a forward bias pn > n<sub>i</sub><sup>2</sup> and for a reverse bias pn < n<sub>i</sub><sup>2</sup>, inside the depletion layer and near its boundary.  


![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/ideal_diod.png)
Inside the depletion region, E<sub>Fn</sub> and E<sub>Fp</sub> remain relatively constant. This comes about because the injected carrier concentrations are relatively much higher inside the depletion region, but since the currents remain fairly constant, the gradients of the quasi-Fermi levels have to be
small. In addition, the depletion width is typically much shorter than the diffusion length, so the total drop of quasi-Fermi levels inside the depletion width is not significant. With these arguments, it follows that within the depletion region:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20qV%20%3D%20E_%7BFn%7D-E_%7BFp%7D)

The above equations can be combined to give the electron density at the boundary of the depletion-layer region on the p-side and the hole density at the boundary of the depletion-layer region on the n-side:


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20n_p%28-W_%7BDp%7D%29%20%3D%20%5Cfrac%7Bn_i%5E2%7D%7Bp_p%7Dexp%28%5Cfrac%7BqV%7D%7BkT%7D%29%5Capprox%20n_%7Bp0%7Dexp%28%5Cfrac%7BqV%7D%7BkT%7D%29%20%5C%5C%5C%5C%5C%5C%20p_n%28W_%7BDn%7D%29%20%3D%20p_%7Bn0%7Dexp%28%5Cfrac%7BqV%7D%7BkT%7D%29)


Using the continuity equations for both electrons and holes for the steady-state condition in the n-side of the junction and assuming that there is no electric field outside the depletion region and only a net recommbination happens outside the depletion region, the following electron and hole current densities are obtained for an ideal diode:


![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/contiuity.png)


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J_p%28W_%7BDn%7D%29%3D%5Cfrac%7BqD_pp_%7Bn0%7D%7D%7BL_n%7D%5Bexp%28%5Cfrac%7BqV%7D%7BkT%7D%29-1%5D%20%5C%5C%5C%5C%5C%5C%20J_n%28-W_%7BDp%7D%29%3D%5Cfrac%7BqD_nn_%7Bp0%7D%7D%7BL_p%7D%5Bexp%28%5Cfrac%7BqV%7D%7BkT%7D%29-1%5D)


It is interesting to note that the hole current is due to injection of holes from thep-side to the n-side, but the magnitude is determined by the properties in the n-side only (Dp, Lp, pn0). The analogy holds for the electron current. The total current is given by the sum of above equations:


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J%20%3D%20J_p%20&plus;%20J_n%20%3D%20J_0%5Bexp%28%5Cfrac%7BqV%7D%7BkT%7D%29-1%5D%2C%20%5C%5C%5C%5C%5C%5C%20J_0%20%5Cequiv%20%5Cfrac%7BqD_pp_%7Bn0%7D%7D%7BL_n%7D%20&plus;%20%5Cfrac%7BqD_nn_%7Bp0%7D%7D%7BL_p%7D)


The above equation is the well-known Shockley equation, which is the ideal diode law. In the forward direction (positive bias on the p-side) for
V > 3kT/q, the rate of current rise is constant (Fig. lob); at 300 K for every decade change of current, the voltage changes by only 0.06 V (= 2.3kT/q). In the reverse direction, the current density saturates at -J0. The saturation current density depends on temperature as follows:


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J_0%20%5Cpropto%20T%5E%7B%283&plus;%5Cgamma%20/2%29%7Dexp%28%5Cfrac%7B-E_g%7D%7BkT%7D%29)


Therefore the slope of a plot J, versus l/T is determined mainly by the energy gap Eg. It is expected that in the reverse direction, where |JR| = J0, the current will increase approximately as exp(-Eg/kT) with temperature; and in the forward direction, where JF = J0exp(qV/kT), the current will increase approximately as exp[-(Eg - qV)/kT] with temperature. 

The Shockley equation adequately predicts the current-voltage characteristics of germanium p-n junctions at low current densities. For Si and GaAs p-n junctions, however, the ideal equation can only give qualitative agreement. The departures from the ideal are mainly due to: (1) the generation and recombination of carriers in the depletion layer, (2) the high-injection condition that may occur even at relatively small forward bias, (3) the parasitic IR drop due to series resistance, (4) the tunneling of carriers between states in the bandgap, and (5) the surface effects. In addition, under sufficiently larger field in the reverse direction, the junction will breakdown as a result, for example, of avalanche multiplication.

We first consider the generation current under the reverse-bias condition. Because of the reduction in carrier concentration under reverse bias (pn << n<sub>i</sub><sup>2</sup>) the dominant generation processes are those of trap assisted emission. With n << n<sub>i</sub> and p << n<sub>i</sub> condition, the generation rate is given by:


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20U%20%3D%20-%5C%7B%5Cfrac%7B%5Csigma%20_n%20%5Csigma%20_p%20%5Cnu%20_%7Bth%7DN_t%7D%7B%5Csigma%20_nexp%5B%28E_t-E_i%29/kT%5D&plus;%5Csigma%20_pexp%5B%28E_i-E_t%29/kT%5D%7D%5C%7Dn_i%3D%20%5C%5C-%5Cfrac%7Bn_i%7D%7B%5Ctau%20_g%7D)


The current due to generation in the depletion region is thus given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J_%7Bge%7D%20%3D%20%5Cint_%7B0%7D%5E%7BW_D%7Dq%7CU%7Cdx%5Capprox%20%5Cfrac%7Bqn_iW_D%7D%7B%5Ctau%20_g%7D)

At a given temperature, J<sub>ge</sub> is proportional to the depletion-layer width, which in turn is dependent on the applied reverse bias. It is thus expected that:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J_%7Bge%7D%20%5Cpropto%20%28%5Cpsi%20_%7Bbi%7D%20&plus;%20V%29%5E%7B1/2%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%20for%5C%3Babrupt%5C%3Bjunction%20%5C%5C%5C%5C%20J_%7Bge%7D%20%5Cpropto%20%28%5Cpsi%20_%7Bbi%7D%20&plus;%20V%29%5E%7B1/3%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%20for%5C%3Blinearly%5C%3Bjunction)

The total reverse current (for pn0 >> np0 and |V| > 3kT/q) can be approximated by the sum of the diffusion component in the neutral region and the generation current in the depletion region:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J_R%20%3D%20q%5Csqrt%7B%5Cfrac%7BD_p%7D%7B%5Ctau_p%7D%7D%5Cfrac%7Bn_i%5E2%7D%7BN_D%7D%20&plus;%20%5Cfrac%7Bqn_iW_D%7D%7B%5Ctau%20_g%7D)

For semiconductors with large values of ni (such as Ge), the diffusion component will dominate at room temperature and the reverse current will follow the Shockley equation; but if yli is small (such as for Si), the generation current may dominate.

At forward bias, where the major recombination-generation processes in the depletion region are the capture processes, we have a recombination current J,, in addition to the diffusion current. In this case, under the assumption Et = Ei and σp = σn = σ and Ei = (EFn+EPn)/2 and V > kT/q, the recommbination rate is as follows:


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20U%20%5Capprox%20%5Cfrac%7B1%7D%7B2%7D%5Csigma%20%5Cnu%20_%7Bth%7DN_tn_iexp%28%5Cfrac%7BqV%7D%7BkT%7D%29)


Then the recommbination current density is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J_%7Bge%7D%20%3D%20%5Cint_%7B0%7D%5E%7BW_D%7Dq%7CU%7Cdx%5Capprox%20%5Cfrac%7Bqn_iW_D%7D%7B2%5Ctau%7Dexp%28%5Cfrac%7BqV%7D%7B2kT%7D%29)


The above approximation assumes that most part of the depletion layer has this maximum recombination rate, and Jre is thus somewhat an overestimate. A more rigorous derivation gives:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J_%7Bge%7D%20%3D%20%5Cint_%7B0%7D%5E%7BW_D%7Dq%7CU%7Cdx%20%3D%20%5Csqrt%7B%5Cfrac%7B%5Cpi%7D%7B2%7D%7D%20%5Cfrac%7BkTn_i%7D%7B2%5Ctau%20%5Cxi%20_0%7Dexp%28%5Cfrac%7BqV%7D%7B2kT%7D%29%20%5C%5C%5C%5C%5C%5C%20%5Cxi%20_0%20%3D%20%5Csqrt%7B%5Cfrac%7BqN%282%5Cpsi%20_%7Bbi%7D-V%29%7D%7B%5Cepsilon%20_s%7D%7D)

Similar to the generation current in reverse bias, the recombination current in forward bias is also proportional to ni. The total forward current can be approximated by the sum of diffusion and recommbination current. For a p+-n junction (pn0 >> np0) and V >> kT/q:


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J_F%20%3D%20q%5Csqrt%7B%5Cfrac%7BD_p%7D%7B%5Ctau_p%7D%7D%5Cfrac%7Bn_i%5E2%7D%7BN_D%7Dexp%28%5Cfrac%7BqV%7D%7BkT%7D%29%20&plus;%20%5Csqrt%7B%5Cfrac%7B%5Cpi%7D%7B2%7D%7D%20%5Cfrac%7BkTn_i%7D%7B2%5Ctau%20%5Cxi%20_0%7Dexp%28%5Cfrac%7BqV%7D%7B2kT%7D%29)


The experimental results in general can be represented by an empirical form:


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J_F%20%5Cpropto%20exp%28%5Cfrac%7BqV%7D%7B%5Ceta%20kT%7D%29)


where the ideality factor η equals 2 when the recombination current dominates and η equals 1 when the diffusion current dominates. When both currents are comparable, η has a value between 1 and 2.

At high current densities (under the forward-bias condition) such that the injected minority-carrier density is comparable to the majority concentration, both drift and diffusion current components must be considered. Since Jp, q, μp, and p are positive, the quasi-Fermi level for holes E increases monotonically to the right as shown in Fp following figure. Similarly, the quasi-Fermi level for electrons EF,, decreases monotonically to the left. Thus, everywhere the separation of the two quasi-Fermi levels must be equal to or less than the applied voltage, and therefore:


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20pn%20%5Cleq%20n_i%5E2exp%28%5Cfrac%7BqV%7D%7BkT%7D%29)

Following figure shows the energey band diagram of a p+n junction at three different current densities 10 (a), 1000 (b), 10000 (c) A/cm2. At 10 A/cm2 the diode is in the low-injection regime. Almost all of the potential drop occurs across the junction. The hole concentration in the n-side is small compared to the electron concentration. At l000 A/cm2 the electron concentration near the junction exceeds the donor concentration appreciably (bear in mind that from charge neutrality, injected carriers Ap = An). An ohmic potential drop appears on the n-side. At l0000 A/cm2 we have very high injection; the potential drop across the junction is insignificant compared to ohmic drops on both sides of the neutral regions.


![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/High_injection.png)


For the case b and c, since n and p carreir concentrations are comparable (n=p), by substituting this condition in the above equation p(x=W<sub>D</sub>) = n<sub>i</sub>exp(qV/2kT). Therefore in the high injection condition, the current density is roughly proportional to exp(qV/2kT). 
At high-current levels we should consider another effect associated with the finite resistivity in the quasi-neutral regions. This resistance absorbs an appreciable amount of the applied voltage between the diode terminals. One can estimate the series resistance from comparing the experimental curve to the ideal curve (AV= IR). The series resistance effect can be substantially reduced by the use of epitaxial materials (p+-n-n+).


The depletion-layer capacitance considered previously accounts for most of the junction capacitance when the junction is reverse-biased. When forward-biased, there is, in addition, a significant contribution to junction capacitance from the rearrangement of minority carrier density, the so-called diffusion capacitance. In other words, the latter is due to the injected charge, while the former to the depletion-layer charge.
When a small ac signal is applied to a junction that is forward-biased at a dc voltage V0 and current density J0 the total voltage and current are defined by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20V%20%3D%20V_0%20&plus;%20V_1exp%28j%5Comega%20t%29%20%5C%5C%5C%5C%20J%20%3D%20J_0%20&plus;%20J_1exp%28j%5Comega%20t%29)

where V1 and J1 are the small-signal voltage and current density, respectively. The imaginary part of the admittance J1/V1 will give the diffusion conductance and diffuision capacitance:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20Y%5Cequiv%20%5Cfrac%7BJ_1%7D%7BV_1%7D%20%5Cequiv%20G_d%20&plus;%20j%5Comega%20C_d)

The electron and hole densities at the depletion region boundaries can be obtained from the master equation by using [V0 + V1exp(jwt)] instead of V. We obtain for the n-side of the junction and V1 << V0,


![](https://latex.codecogs.com/svg.latex?%5CLARGE%20p_n%28W_%7BDn%7D%29%20%3D%20p_%7Bn0%7Dexp%5B%5Cfrac%7Bq%28V_0&plus;V_1exp%28j%5Comega%20t%29%29%20%7D%7BkT%7D%5D%20%5C%5C%5C%5C%5C%5C%20%5Capprox%20p_%7Bn0%7Dexp%5B%5Cfrac%7BqV_0%7D%7BkT%7D%5D%20&plus;%20%5Cfrac%7Bp_%7Bn0%7DqV_1%7D%7BkT%7Dexp%5B%5Cfrac%7BqV_0%7D%7BkT%7D%5Dexp%28j%5Comega%20t%29%20%5C%5C%5C%5C%5C%5C%20%5Capprox%20p_%7Bn0%7Dexp%5B%5Cfrac%7BqV_0%7D%7BkT%7D%5D%20&plus;%20%5Ctilde%7Bp_n%7D%28t%29)

Substituting p<sub>n</sub>(t) in the continuity equation and assuming that Gp = E = dE/dx = 0, we can then obtain the alternating current density as:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J%20%3D%20qp_%7Bn0%7D%5Csqrt%7B%5Cfrac%7BD_p%7D%7B%5Ctau%20_p%5E*%7D%7D&plus;qn_%7Bp0%7D%5Csqrt%7B%5Cfrac%7BD_n%7D%7B%5Ctau%20_n%5E*%7D%7D%5Bexp%28qV_0/kT%29%5D%5B1&plus;%5Cfrac%7BqV_1%7D%7BkT%7Dexp%28j%5Comega%20t%29%5D)

with the ac component being:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20J_1%20%3D%20%5B%5Cfrac%7Bqp_%7Bn0%7DD_p%5Csqrt%7B1&plus;j%5Comega%20%5Ctau%20_p%7D%7D%7BL_p%7D&plus;%5Cfrac%7Bqn_%7Bp0%7DD_n%5Csqrt%7B1&plus;j%5Comega%20%5Ctau%20_n%7D%7D%7BL_n%7D%5Dexp%28%5Cfrac%7BqV_0%7D%7BkT%7D%29%5Cfrac%7BqV_1%7D%7BkT%7D)

From J1/Vl, both Gd and Cd can be found and they are frequency dependent. For relatively low frequencies (ωτ<sub>n</sub>, ωτ<sub>p</sub> << l), the diffusion conductance GdO is given by:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20G_%7Bd0%7D%20%3D%20%5B%5Cfrac%7Bqp_%7Bn0%7DD_p%7D%7BL_p%7D&plus;%5Cfrac%7Bqn_%7Bp0%7DD_n%7D%7BL_n%7D%5Dexp%28%5Cfrac%7BqV_0%7D%7BkT%7D%29%5Cfrac%7Bq%7D%7BkT%7D)

The low-frequency diffusion capacitance Cdo can be obtained by using the approximation (1+jωτ)^0.5= (1 + 0.5jωτ). This diffusion capacitance is proportional to the forward current. For an n+-p one-sided junction, it can shown that:

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20C_%7Bd0%7D%20%3D%20%5Cfrac%7Bq%5E2%7D%7B2kT%7D%28p_%7Bn0%7DL_p&plus;n_%7Bp0%7DL_n%29exp%28%5Cfrac%7BqV_0%7D%7BkT%7D%29)

![](https://latex.codecogs.com/svg.latex?%5CLARGE%20C_%7Bd0%7D%3D%5Cfrac%7BqL_n%5E2%7D%7B2kTD_n%7DJ_F)


Cd is especially important at low frequencies and under forward-bias conditions.

##JUNCTION BREAKDOWN
Breakdown occurs only in the reverse-bias regime because high voltage can be applied resulting in high field. There are basically three breakdown mechanisms: (1) thermal instability, (2) tunneling, and (3) avalanche multiplication.

Breakdown due to thermal instability is responsible for the maximum dielectric strength in most insulators at room temperature, and is also a major effect in semiconductors with relatively small bandgaps (e.g., Ge). Because of the heat dissipation caused by the reverse current at high reverse voltage, the junction temperature increases. This temperature increase, in turn, increases the reverse current in comparison with its value at lower voltages. This positive feedback is responsible for breakdown.

