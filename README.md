# simulated-wavelike-behaviour
Toy Python model demonstrating deterministic stochastic actions replicating quantum interference effects.

When executed, prints percentage reflection result from photon_in_one_bs() function; then prints fifty percentage reflection results from photon_in_two_bs() function executed over a range of phase differences, displays a graph of the results.


# Variables

xi_1, xi_2
Randomly initialised when script is run.

ratio = 20.0
The weighting between particle phase and apparatus phase used in beamsplitter() function.
Can be changed to any positive float to explore different behaviours.

N = 100000
The number of simulated particles in each experiment.
Can be altered depending on desired experimental precision and computer memory available.

reflection_count1 = 0.0
Used to count reflection results from multiple runs of photon_in_one_bs() function. Set to 0.0 when script is run and increased by photon_in_one_bs() function.

reflection_count2 = 0.0
Used similarly for photon_in_two_bs(). Reset to 0.0 for each new optical_difference value tested.

steps = 50
The amount of divisions betwen 0.0--2.0 over which photon_in_two_bs() functions is tested.
Can be altered to change the precision of the final graph output.

reflection_percentages = []
Creates an empty array to be populated by simulated experiment results and displayed by plot(reflection_percentages).


# FUNCTIONS

beamsplitter(phase, xi)
Accepts two floats and returns phase, xi, reflection as float, float, bool.
Used in photon_in_one_bs() and photon_in_two_bs().

photon_in_one_bs(phase)
Accepts a single float and returns a boolean value.
Run N times to calculate a percentage reflection.

photon_in_two_bs(phase, optical_difference)
Accepts two floats and returns a boolean value.
Is run (N * steps) times to calculate a percentage reflection over a range of optical_difference values.

