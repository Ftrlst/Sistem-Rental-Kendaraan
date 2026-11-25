class RentalError(Exception):
    """Induk semua exception proyek."""


class KendaraanSedangDisewaError(RentalError):
    """Dipicu saat kendaraan yang sedang disewa dicoba disewa lagi."""


class TarifTidakValidError(RentalError):
    """Dipicu saat tarif kendaraan bernilai nol atau negatif."""


class SIMTidakValidError(RentalError):
    """Dipicu saat penyewa dengan SIM tidak valid mencoba menyewa."""


class PenyewaTidakTerdaftarError(RentalError):
    """Dipicu saat ID penyewa tidak ditemukan di daftar."""


class SewaSudahSelesaiError(RentalError):
    """Dipicu saat penyewaan yang sudah selesai dikembalikan lagi."""


class LamaSewaTidakValidError(RentalError):
    """Dipicu saat lama sewa nol atau negatif."""


class LaporanKosongError(RentalError):
    """Dipicu saat meminta statistik dari laporan yang belum berisi data."""
