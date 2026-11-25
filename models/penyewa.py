"""Class Penyewa dan subclass-nya.

Pemilik: Neysa Alzena (60225043)
Status : SKELETON (Pertemuan 12) - atribut dan method belum berisi logika.
"""
from exceptions import PenyewaTidakTerdaftarError, SIMTidakValidError  # noqa: F401


class Penyewa:
    """Class dasar penyewa: identitas, status SIM, riwayat sewa, dan diskon."""

    def __init__(self, id_penyewa, nama, no_sim, sim_valid=False):
        self._id_penyewa = id_penyewa
        self._nama = nama
        self._no_sim = no_sim
        self._sim_valid = sim_valid
        self._riwayat_sewa = []

    # ---- Properti (encapsulation) ----
    @property
    def id_penyewa(self):
        """ID unik penyewa."""
        return self._id_penyewa

    @property
    def nama(self):
        """Nama penyewa."""
        return self._nama

    @nama.setter
    def nama(self, nilai):
        """TODO: tolak nama kosong."""
        pass

    @property
    def no_sim(self):
        """Nomor SIM penyewa."""
        return self._no_sim

    @property
    def sim_valid(self):
        """True jika SIM sudah diverifikasi."""
        return self._sim_valid

    # ---- Method ----
    def diskon(self):
        """TODO: return persentase diskon (polymorphism: di-override subclass)."""
        pass

    def tambah_riwayat(self, penyewaan):
        """TODO: catat penyewaan ke riwayat."""
        pass

    def jumlah_riwayat(self):
        """TODO: return jumlah penyewaan yang pernah dilakukan."""
        pass

    @staticmethod
    def cari_penyewa(id_penyewa, daftar):
        """TODO: return Penyewa dengan ID tersebut; raise PenyewaTidakTerdaftarError jika tidak ada."""
        pass

    def __str__(self):
        """TODO: ringkasan informasi penyewa."""
        pass


class PenyewaReguler(Penyewa):
    """Penyewa reguler: tanpa diskon."""

    def diskon(self):
        """TODO: return 0.0."""
        pass


class PenyewaMember(Penyewa):
    """Penyewa member: diskon 10%."""

    def diskon(self):
        """TODO: return 0.10."""
        pass
