import re

def hitung_jumlah_kata(kalimat):
    kalimat_bersih = re.sub(r'[^\w\s]', '', kalimat)
    kata = kalimat_bersih.split()
    return len(kata)

# Contoh penggunaan
input_kalimat = "Saat meng*ecat tembok, Agung dib_antu oleh Raihan."
output_jumlah_kata = hitung_jumlah_kata(input_kalimat)
print("Output:", output_jumlah_kata)