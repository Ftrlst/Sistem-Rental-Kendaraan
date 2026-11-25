from datetime import date

from exceptions import RentalError
from models import Motor, PenyewaReguler, Penyewaan, Laporan


def main():
    motor = Motor("AB 1234 CD", "Honda Beat", 80000)
    penyewa = PenyewaReguler("P001", "Rina", "SIM-001", sim_valid=True)
    sewa = Penyewaan(motor, penyewa, date.today(), 3)
    laporan = Laporan()

    try:
        # TODO (Pert. 13): sewa.proses_sewa(); sewa.proses_kembali(...);
        #                  laporan.tambah_transaksi(sewa); laporan.cetak_laporan()
        print("Skeleton siap: semua class berhasil di-import dan dibuat.")
    except RentalError as err:
        print(f"Terjadi kesalahan: {err}")


if __name__ == "__main__":
    main()
