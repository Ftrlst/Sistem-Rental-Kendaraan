"""Unit test Penyewaan (Fitriani). Pertemuan 12: baru smoke test; test lengkap di Pertemuan 13-14."""
import unittest
from datetime import date
from models import Motor, PenyewaReguler, Penyewaan


class TestPenyewaan(unittest.TestCase):
    def setUp(self):
        motor = Motor("AB 1234 CD", "Honda Beat", 80000)
        penyewa = PenyewaReguler("P001", "Rina", "SIM-001", sim_valid=True)
        self.obj = Penyewaan(motor, penyewa, date(2026, 11, 20), 3)

    def test_objek_bisa_dibuat(self):
        self.assertIsNotNone(self.obj)

    # TODO (Pert. 13): kasus normal, kasus error (assertRaises), nilai batas. Target minimal 6 test.


if __name__ == "__main__":
    unittest.main()
