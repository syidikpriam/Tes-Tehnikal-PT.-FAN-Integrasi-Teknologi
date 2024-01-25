def hitung_pasang_kaos_kaki(arr):
    pasangan = 0
    counter = {}

    # Menghitung jumlah setiap elemen dalam array
    for elemen in arr:
        if elemen in counter:
            counter[elemen] += 1
        else:
            counter[elemen] = 1

    # Menghitung pasangan untuk setiap elemen
    for jumlah in counter.values():
        pasangan += jumlah // 2

    return pasangan

# Contoh penggunaan
input_a = [10, 20, 20, 10, 10, 30, 50, 10, 20]
output_a = hitung_pasang_kaos_kaki(input_a)
print("Output a:", output_a)

input_b = [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]
output_b = hitung_pasang_kaos_kaki(input_b)
print("Output b:", output_b)

input_c = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
output_c = hitung_pasang_kaos_kaki(input_c)
print("Output c:", output_c)
