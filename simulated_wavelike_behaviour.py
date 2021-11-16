from math import *
from cmath import *
import matplotlib.pyplot as plt
from random import *

# Initialise the random number generator
seed()

##################################################
# Functions and preliminaries
##################################################

# Phases are normalised to the interval [0,2]
# for simplicity. Variable phase for first
# beamsplitter, xi_1, starts from a random value.
xi_1 = 2.0 * random()

# Variable phase for second beamsplitter, xi_2,
# starts from a random value.
xi_2 = 2.0 * random()

# Measure of how beamsplitter atom is heavier
# than photon.
ratio = 20.0

# Function describing the effect of a beamsplitter.
def beamsplitter(phase, xi):

    # Difference between photon phase (phase), and
    # beamsplitter phase (xi).
    delta = (phase - xi) % 2
    reflection = (abs(delta - 1.0) < 0.5)

    if reflection:  # Reflection condition.

        # Both phases are transformed by the interaction:

        # Beamsplitter phase is changed.
        xi = (xi + delta / (1.0 + ratio)) % 2

        # Photon phase is changed, with a 0.5 offset.
        phase = (phase + .5 - delta * ratio / (1.0 + ratio)) % 2

    return phase, xi, reflection

# Function to check the distribution in a single beamsplitter.
def photon_in_one_bs(phase):

    global xi_1

    _, xi_1, reflection = beamsplitter(phase, xi_1)

    if reflection:
        return 1
    else:
        return 0

# Function to simulate two consecutive beamsplitters by
# running the beamsplitter() procedure twice, introducing
# an optical difference if the simulated photon is
# reflected by the first beamsplitter.
def photon_in_two_bs(phase, optical_difference):

    global xi_1
    global xi_2

    # First beamsplitter.
    phase, xi_1, reflection = beamsplitter(phase, xi_1)

    # Add the optical path difference for reflected photon.
    if reflection:
        phase = (phase + optical_difference) % 2

    # The same rules are applied to the second beamsplitter
    # but the outgoing phase is not needed.
    _, xi_2, reflection = beamsplitter(phase, xi_2)

    if reflection:
        return 1
    else:
        return 0

##################################################
# Simulated experiment
##################################################

# Number of photons in each experiment.
N = 100000

# Count of reflections.
reflection_count1 = 0.0

# Using photon_in_one_bs() to check the distribution of
# single photons under these rules. Simulate a sequence
# of N photons interacting with a single beamsplitter:
for i in range(N):

    # Count of photons leaving 'reflected' output
    # of beamsplitter.
    reflection_count1 = reflection_count1 + photon_in_one_bs(2.0 * random())

print('Percentage of reflections in one beamsplitter', reflection_count1 / N)

# Using photon_in_two_bs() to simulate the two beamsplitter
# experiment for a range of optical path differences.

# Subdivisions of the optical path difference.
steps = 50

# Array of results.
reflection_percentages = []

# Run through all possible optical path differences:
for j in range(steps):

    # Count of reflections.
    reflection_count2 = 0.0

    # Randomly re-initialise phase xi_1 for first beamsplitter.
    xi_1 = 2.0 * random()

    # Randomly re-initialise phase xi_2 for second beamsplitter.
    xi_2 = 2.0 * random()

    # Simulate a sequence of N photons:
    for i in range(N):

        # Count of photons leaving given output of
        # second beamsplitter.
        reflection_count2 = reflection_count2 + photon_in_two_bs(2.0 * random(), 2.0 * j / steps)

    # Log reflection rate for given optical path difference
    reflection_percentages.append(reflection_count2 / N)

    print(j, reflection_count2 / N)

# Plotting the results of two beamsplitter simulation.
plt.plot(reflection_percentages)
plt.ylabel('% of reflections')
plt.show()
