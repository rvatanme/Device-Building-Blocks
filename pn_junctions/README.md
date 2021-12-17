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
 
 
 This discussion uses depletion approximation where it's assumed that n(x) ≈ p(x) ≈ 0. In reality, due to the majority-carrier distribution tail, there is a low concentration of majority carrier in both side of the juction. Therefore, a more accurate result for the depletion-layer properties can be obtained by considering this contribution in the Poisson equation, that is, ρ = q[N<sub>A</sub> - p(x)]  on the p-side and ρ = q[N<sub>D</sub> - n(x)] on the n-side. By solving Poisson equation with the new expression, it's reaveld that all the previous equation is true with this difference that the ψ<sub>bi</sub> should be replaced by ψ<sub>bi</sub> - 2kT/q and ψ<sub>bi</sub> - V - 2kT/q under no bias and bias V, respectively.
## PN Junction Under Applied Voltage
