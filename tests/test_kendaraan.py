"""Unit test Kendaraan (Devi). Pertemuan 12: baru smoke test; test lengkap di Pertemuan 13-14."""
import unittest
from models import Mobil


class TestKendaraan(unittest.TestCase):
    def setUp(self):
        self.obj = Mobil("AB 1234 CD", "Toyota Avanza", 300000, 7)

    def test_objek_bisa_dibuat(self):
        self.assertIsNotNone(self.obj)

    # TODO (Pert. 13): kasus normal, kasus error (assertRaises), nilai batas. Target minimal 6 test.


if __name__ == "__main__":
    unittest.main()
