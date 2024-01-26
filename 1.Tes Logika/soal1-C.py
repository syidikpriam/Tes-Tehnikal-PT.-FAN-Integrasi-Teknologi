def hitung_pasang_kaos_kaki(arr):
    hitung = {}
    jumlah_pasang = 0

    for ukuran in arr:
        if ukuran in hitung:
            hitung[ukuran] += 1
        else:
            hitung[ukuran] = 1

    for jumlah in hitung.values():
        jumlah_pasang += jumlah // 2

    return jumlah_pasang

# Contoh penggunaan
input = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
output = hitung_pasang_kaos_kaki(input)
print("Output :", output)
