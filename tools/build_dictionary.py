import csv
import json
import os
import sys

# Konfigurasi Path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, 'colloquial-indonesian-lexicon.csv') # Pastikan file csv ada di root
OUTPUT_PATH = os.path.join(BASE_DIR, 'data', 'slang_dict.json')

def build():
    print(f"🚀 Memulai proses build dictionary dari: {CSV_PATH}")
    
    slang_map = {}

    # 1. Load dari CSV (Dataset Riset)
    try:
        with open(CSV_PATH, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                slang = row['slang'].strip().lower()
                formal = row['formal'].strip().lower()
                
                # Validasi sederhana: jangan masukkan jika kosong
                if slang and formal:
                    slang_map[slang] = formal
                    count += 1
            print(f"✅ Berhasil memuat {count} kata dari CSV.")
            
    except FileNotFoundError:
        print(f"❌ Error: File {CSV_PATH} tidak ditemukan.")
        print("Pastikan kamu sudah menaruh file CSV di folder root project.")
        sys.exit(1)

    # 2. Tambahan Manual (High Priority Slang)
    # Kadang CSV akademik agak kaku, kita tambahkan slang internet modern di sini
    manual_additions = {
        "gws": "lekas sembuh",
        "kpn": "kapan",
        "sy": "saya",
        "otw": "sedang jalan",
        "ygy": "ya guys ya",
        "tbl": "takut banget loh",
        "fomo": "takut ketinggalan zaman",
        "jastip": "jasa titip",
        "mager": "malas gerak",
        "baper": "bawa perasaan"
    }
    
    # Update dictionary (kata manual akan menimpa CSV jika ada duplikat)
    slang_map.update(manual_additions)
    print(f"✅ Menambahkan {len(manual_additions)} kata slang modern manual.")

    # 3. Sorting agar rapi (Reviewer suka file yang urut abjad)
    sorted_map = dict(sorted(slang_map.items()))

    # 4. Save ke JSON
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(sorted_map, f, indent=2, ensure_ascii=False)
    
    print(f"🎉 SUKSES! Dictionary tersimpan di: {OUTPUT_PATH}")
    print(f"📊 Total Kosakata: {len(sorted_map)} kata.")

if __name__ == "__main__":
    build()