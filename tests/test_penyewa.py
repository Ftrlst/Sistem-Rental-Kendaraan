"""Unit test Penyewa (Neysa). Pertemuan 12: baru smoke test; test lengkap di Pertemuan 13-14."""
import unittest
from models import PenyewaMember


class TestPenyewa(unittest.TestCase):
    def setUp(self):
        self.obj = PenyewaMember("P001", "Rina", "SIM-001", sim_valid=True)

    def test_objek_bisa_dibuat(self):
        self.assertIsNotNone(self.obj)

    # TODO (Pert. 13): kasus normal, kasus error (assertRaises), nilai batas. Target minimal 6 test.


if __name__ == "__main__":
    unittest.main()
