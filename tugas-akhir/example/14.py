# OCP
from abc import ABC, abstractmethod


def cekNama(nama):
  for i in nama:
    if i.isdigit():
      return False
  return True


class absHasil(ABC):
  @abstractmethod
  def hasil(self):
    pass


class simpanData(absHasil):
  def hasil(nama):
    if cekNama(nama):
      print("Data berhasil disimpan")
    else:
      print("Data gagal disimpan")


class loginNama(absHasil):
  def hasil(nama):
    if cekNama(nama):
      print("Berhasil login")
    else:
      print("Gagal login")


if __name__ == "__main__":
  nama = "Rizky"
  for proses in absHasil.__subclasses__():
    print(proses)
    proses.hasil(nama)
  nama = "123"
  for proses in absHasil.__subclasses__():
    print(proses)
    proses.hasil(nama)
