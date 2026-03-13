import random
import datetime

pertanyaan = [
    ("Siapa nama kahim Informatika 2026?", "Ergi"),
    ("Apa divisi paling keren di HMIF 2026", "PSDM"),
    ("Apa nama kabinet HMIF 2026?", "Adhirasatya")
]
score = 0

waktu_mulai = datetime.datetime.now()
print("Kuis dimulai pada:", waktu_mulai)
print("--------------------------")

for soal in pertanyaan:
    q, jawaban_benar = soal

    print("Pertanyaan:", q)
    jawaban = input("Masukan Jawaban: ")

    if jawaban.lower() == jawaban_benar:
        print("Jawaban benar!")
        score += 1
    else:
        print("Jawaban salah!")

    print()

ulang = input("Ingin melihat skor? (y/n): ")
while ulang.lower() not in ["y", "n"]:
    ulang = input("Masukkan hanya y atau n: ")

if ulang == "y":
    print("Skor kamu:", score, "dari", len(pertanyaan))

print("Terima kasih sudah bermain kuis infor")
