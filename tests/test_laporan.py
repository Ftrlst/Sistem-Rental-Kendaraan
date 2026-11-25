"""Unit test Laporan (Aulya). Pertemuan 12: baru smoke test; test lengkap di Pertemuan 13-14."""
import unittest
from models import Laporan


class TestLaporan(unittest.TestCase):
    def setUp(self):
        self.obj = Laporan()

    def test_objek_bisa_dibuat(self):
        self.assertIsNotNone(self.obj)

    # TODO (Pert. 13): kasus normal, kasus error (assertRaises), nilai batas. Target minimal 6 test.


if __name__ == "__main__":
    unittest.main()
