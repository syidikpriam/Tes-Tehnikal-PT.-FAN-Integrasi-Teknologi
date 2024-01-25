import re

def hitung_jumlah_kata(kalimat):
    # Mengganti special karakter dengan spasi
    kalimat_bersih = re.sub(r'[^a-zA-Z0-9\s]', ' ', kalimat)

    # Memisahkan kata-kata
    kata_kata = kalimat_bersih.split()

    # Menghitung jumlah kata
    jumlah_kata = len(kata_kata)

    return jumlah_kata

# Contoh penggunaan
input_a = "Saat meng*ecat tembok, Agung dib_antu oleh Raihan."
output_a = hitung_jumlah_kata(input_a)
print("Output a:", output_a)

input_b = "Berapa u(mur minimal[ untuk !mengurus ktp?"
output_b = hitung_jumlah_kata(input_b)
print("Output b:", output_b)

input_c = "Masing-masing anak mendap(atkan uang jajan ya=ng be&rbeda."
output_c = hitung_jumlah_kata(input_c)
print("Output c:", output_c)
