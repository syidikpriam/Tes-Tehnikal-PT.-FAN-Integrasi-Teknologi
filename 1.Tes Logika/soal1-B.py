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
input = [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]
output = hitung_pasang_kaos_kaki(input)
print("Output :", output)
