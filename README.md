# Material properties calculator
The repository contains a tool dedicated to interpolate and extrapolate material properties in the range of temperatures set by a user. The program has been written in Python 2.7.
<br><br>
## Application
To perform numerical simulations like FEA or CFD, a user usually have to insert to software properties of material which is used in an analysis. Simulation software often requires properties of the material in the wide range of temperatures. As there are mostly only a few temperatures for which the properties of the material have been investigated in a laboratory, the need to extrapolate this data for the wider scope of temperatures arises.
<br><br>
## How does it work?
The program consists of four files:

![Figure 1](https://github.com/MyProjectsMK/Material_properties_calculator/blob/master/README_figure1.jpg)

Its central point is the *material_properties_calculator.py* file written in Python 2.7. It utilizes 
