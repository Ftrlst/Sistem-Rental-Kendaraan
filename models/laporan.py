"""Class Laporan: rekap transaksi memakai collection (list dan dict).

Pemilik: Aulya Deswita (60225014)
Status : SKELETON (Pertemuan 12) - atribut dan method belum berisi logika.
"""
from exceptions import LaporanKosongError  # noqa: F401


class Laporan:
    """Merekap penyewaan yang selesai dan mencetak laporan pendapatan."""

    def __init__(self):
        self._daftar_transaksi = []        # list Penyewaan
        self._pendapatan_per_jenis = {}    # {"Mobil": 0.0, ...}
        self._hitungan_kendaraan = {}      # {"B 1234 XY": 3, ...}

    def tambah_transaksi(self, penyewaan):
        """TODO: simpan ke list dan perbarui kedua dict."""
        pass

    def total_pendapatan(self):
        """TODO: jumlah total biaya dan denda."""
        pass

    def total_denda(self):
        """TODO: jumlah seluruh denda."""
        pass

    def pendapatan_per_jenis(self):
        """TODO: return salinan dict pendapatan per jenis kendaraan."""
        pass

    def kendaraan_terpopuler(self):
        """TODO: return plat kendaraan paling sering disewa (None jika kosong)."""
        pass

    def cetak_laporan(self):
        """TODO: cetak laporan terformat ke layar."""
        pass

    def simpan_ke_file(self, nama_file):
        """TODO: tulis laporan ke file teks."""
        pass
