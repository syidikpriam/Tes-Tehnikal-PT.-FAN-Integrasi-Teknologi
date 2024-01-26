import re

def hitung_jumlah_kata(kalimat):
    kalimat_bersih = re.sub(r'[^\w\s]', '', kalimat)
    kata = kalimat_bersih.split()
    return len(kata)

# Contoh penggunaan
input_kalimat = "Berapa u(mur minimal[ untuk !mengurus ktp?"
output_jumlah_kata = hitung_jumlah_kata(input_kalimat)
print("Output:", output_jumlah_kata)
