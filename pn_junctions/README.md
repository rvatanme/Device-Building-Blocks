# PN Junctioins
p-n junctions are of great importance both in modern electronic applications and in understanding other semiconductor devices. The p-n junction theory serves as the foundation of the physics of semiconductor devices. 

## PN Junctions at Thermal Equilibrium
At thermal equilibrium under no bias, Boltzmann statistics and Poisson equation can be employed together in order to model a pn junction. First, let's consider a parallel abrupt pn junction where the acceptor doping concentration of the P side abruptly changes to the donor concentration of the n side. In this case, a layer named depletion layer is created at the interface where negligble free carrier exists, n(x) ≈ p(x) ≈ 0. Assumming complete ionization, depletion layer contains a pile of fixed negative and positive charges at the p and n side, respectively.

![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/ab_pn_equi.png)

 The depletion layer reslts in a  built in potential that is the fundumental characteristic of any pn junction. Using Boltzmann equation, the build in potential, under complete ionization, is obtained as follows: 
 
![](https://github.com/rvatanme/Device-Building-Blocks/blob/main/pn_junctions/biuld_in.png)


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


