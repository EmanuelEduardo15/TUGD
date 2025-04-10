import unittest
import numpy as np
from simulations.gravitational_waves import simulate_wave

class TestEnergyConservation(unittest.TestCase):
    def test_energy(self):
        initial = np.zeros(8)
        initial[0] = 1.0  # Initial pulse
        solution = simulate_wave(initial, steps=10)
        energy = np.sum(solution.y[:, -1]**2)
        self.assertAlmostEqual(energy, 1.0, delta=0.01)
