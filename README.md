# Material properties calculator
The repository contains a tool dedicated to interpolate and extrapolate material properties in the range of temperatures set by a user. The program has been written in Python 2.7.
<br><br>
## Application
To perform numerical simulations like FEA or CFD, a user usually have to insert to software properties of material which is used in an analysis. Simulation software often requires properties of the material in the wide range of temperatures. As there are mostly only a few temperatures for which the properties of the material have been investigated in a laboratory, the need to extrapolate this data for the wider scope of temperatures arises.
<br><br>
## How does it work?
The program consists of four files:

![Figure 1](https://github.com/MyProjectsMK/Material_properties_calculator/blob/master/README_figure1.jpg)

Its central point is the *material_properties_calculator.py* file written in Python 2.7. It is responsible for extrapolating data provided by a user in the *input_known_parameter_values.txt* and *input_known_temperatures.txt* files. If the format of provided material properties and/or temperatures is not correct, a user is asked to verify and update the data. The program saves its output to the *output_calculated_values.xlsx* file - it contains values of material properties calculated for the scope of temperatures required by a user.
<br><br>
The program utilizes the Python Shell to communicate with a user. This is how the interface of the calculator looks like:

![Figure 2](https://github.com/MyProjectsMK/Material_properties_calculator/blob/master/README_figure2.jpg)
