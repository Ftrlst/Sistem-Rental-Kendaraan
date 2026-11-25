"""Class Penyewaan: proses sewa, pengembalian, biaya, dan denda.

Pemilik: Fitriani Lestari (60225030)
Status : SKELETON (Pertemuan 12) - atribut dan method belum berisi logika.
"""
from exceptions import (  # noqa: F401
    KendaraanSedangDisewaError,
    SIMTidakValidError,
    SewaSudahSelesaiError,
    LamaSewaTidakValidError,
)


class Penyewaan:
    """Penghubung Kendaraan dan Penyewa; hasilnya dikirim ke Laporan."""

    def __init__(self, kendaraan, penyewa, tanggal_sewa, lama_sewa):
        self._kendaraan = kendaraan
        self._penyewa = penyewa
        self._tanggal_sewa = tanggal_sewa
        self._lama_sewa = lama_sewa
        self._tanggal_jatuh_tempo = None   # TODO: tanggal_sewa + lama_sewa hari
        self._tanggal_kembali = None
        self._status = "belum_mulai"       # "belum_mulai" | "berjalan" | "selesai"
        self._total_biaya = 0.0
        self._denda = 0.0
        # TODO (Pert. 13): raise LamaSewaTidakValidError jika lama_sewa <= 0.

    # ---- Properti ----
    @property
    def kendaraan(self):
        """Kendaraan yang disewa."""
        return self._kendaraan

    @property
    def penyewa(self):
        """Penyewa."""
        return self._penyewa

    @property
    def status(self):
        """Status penyewaan."""
        return self._status

    @property
    def total_biaya(self):
        """Biaya sewa setelah diskon."""
        return self._total_biaya

    @property
    def denda(self):
        """Denda keterlambatan."""
        return self._denda

    # ---- Method ----
    def proses_sewa(self):
        """TODO: cek SIM valid, tandai kendaraan disewa, hitung total, catat riwayat penyewa."""
        pass

    def proses_kembali(self, tanggal_kembali):
        """TODO: tandai kendaraan tersedia, hitung denda, status selesai; return total akhir.

        Raise SewaSudahSelesaiError jika sudah dikembalikan.
        """
        pass

    def hitung_total(self):
        """TODO: kendaraan.hitung_tarif_sewa(lama) dikurangi diskon penyewa."""
        pass

    def hitung_denda(self):
        """TODO: hari terlambat x kendaraan.tarif_denda_per_hari()."""
        pass

    def apakah_terlambat(self):
        """TODO: True jika tanggal kembali melewati jatuh tempo."""
        pass
