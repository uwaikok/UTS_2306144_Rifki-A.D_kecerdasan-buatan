def deteksi_hama(gejala):
    hasil = []

    if "daun menguning" in gejala and "tanaman layu" in gejala:
        hasil.append("Hama A")
    if "terdapat bercak hitam" in gejala:
        hasil.append("Hama B")
    if "daun berlubang" in gejala:
        hasil.append("Hama C")
    if len(gejala) == 4:
        hasil.append("Gabungan A, B, C")
    
    return hasil

# Contoh input
gejala_input = ["daun menguning", "terdapat bercak hitam", "daun berlubang", "tanaman layu"]
print(deteksi_hama(gejala_input))
