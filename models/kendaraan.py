"""Class Kendaraan dan subclass-nya.

Pemilik: Devi Augustin Umpriana Syaputri (60225047)
Status : SKELETON (Pertemuan 12) - atribut dan method belum berisi logika.
"""
from exceptions import KendaraanSedangDisewaError, TarifTidakValidError  # noqa: F401


class Kendaraan:
    """Class dasar kendaraan: data, status ketersediaan, dan aturan tarif."""

    def __init__(self, plat, merk, tarif_dasar, tersedia=True):
        self._plat = plat
        self._merk = merk
        self._tarif_dasar = tarif_dasar
        self._tersedia = tersedia
        # TODO (Pert. 13): arahkan assignment lewat setter agar divalidasi.

    # ---- Properti (encapsulation) ----
    @property
    def plat(self):
        """Nomor polisi kendaraan."""
        return self._plat

    @plat.setter
    def plat(self, nilai):
        """TODO: tolak plat kosong."""
        pass

    @property
    def merk(self):
        """Merek/model kendaraan."""
        return self._merk

    @property
    def tarif_dasar(self):
        """Tarif sewa per hari."""
        return self._tarif_dasar

    @tarif_dasar.setter
    def tarif_dasar(self, nilai):
        """TODO: raise TarifTidakValidError jika nilai <= 0."""
        pass

    @property
    def tersedia(self):
        """True jika kendaraan sedang tersedia untuk disewa."""
        return self._tersedia

    # ---- Method ----
    def tandai_disewa(self):
        """TODO: ubah status menjadi disewa; raise KendaraanSedangDisewaError jika sudah disewa."""
        pass

    def tandai_tersedia(self):
        """TODO: ubah status menjadi tersedia."""
        pass

    def hitung_tarif_sewa(self, hari):
        """TODO: return total tarif untuk `hari` hari (polymorphism: boleh di-override)."""
        pass

    def tarif_denda_per_hari(self):
        """TODO: return denda keterlambatan per hari (polymorphism: di-override subclass)."""
        pass

    def __str__(self):
        """TODO: ringkasan informasi kendaraan."""
        pass


class Motor(Kendaraan):
    """Motor. Tarif Rp 80.000/hari, denda Rp 20.000/hari."""

    def tarif_denda_per_hari(self):
        """TODO: return 20000."""
        pass


class Mobil(Kendaraan):
    """Mobil. Tarif Rp 300.000/hari, denda Rp 75.000/hari."""

    def __init__(self, plat, merk, tarif_dasar, jumlah_kursi, tersedia=True):
        super().__init__(plat, merk, tarif_dasar, tersedia)
        self._jumlah_kursi = jumlah_kursi

    def tarif_denda_per_hari(self):
        """TODO: return 75000."""
        pass


class Bus(Kendaraan):
    """Bus. Tarif Rp 1.200.000/hari (termasuk sopir), denda Rp 300.000/hari."""

    def __init__(self, plat, merk, tarif_dasar, kapasitas, tersedia=True):
        super().__init__(plat, merk, tarif_dasar, tersedia)
        self._kapasitas = kapasitas

    def hitung_tarif_sewa(self, hari):
        """TODO: tarif per hari sudah termasuk biaya sopir."""
        pass

    def tarif_denda_per_hari(self):
        """TODO: return 300000."""
        pass
