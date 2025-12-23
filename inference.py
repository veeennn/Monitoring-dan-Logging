import requests
import json
import time
import random

def run_inference():

    url = "http://127.0.0.1:8000/predict"
    
    payload = {
        "dataframe_split": {

                #input dari cmd 20 kolom contoh:
                #-X POST http://127.0.0.1:8000/predict  -H "Content-Type: application/json" -d "{\"dataframe_split\": 
                # {\"columns\": [\"Unnamed: 0\", \"date\", \"bedrooms\", \"bathrooms\", \"sqft_living\", \"sqft_lot\", \"floors\", 
                # \"waterfront\", \"view\", \"condition\", \"grade\", \"sqft_above\", \"sqft_basement\", \"yr_built\", \"yr_renovated\", 
                # \"zipcode\", \"lat\", \"long\", \"sqft_living15\", \"sqft_lot15\"], 
                # \"data\": [[1, 20140502, 3.0, 2.25, 2570.0, 7242.0, 2.0, 0.0, 0.0, 3.0, 7.0, 2170.0, 400.0, 1951.0, 1991.0, 98125.0, 47.721, 
                # -122.319, 1690.0, 7639.0]]}}" 
                # hasil: {"predictions":[931386298014513.1]}    
        }
    }

    try:
        while True:
            start_time = time.time()
            try:
                response = requests.post(
                    url, 
                    json=payload, 
                    headers={"Content-Type": "application/json"}
                )
                latency = time.time() - start_time

                if response.status_code == 200:
                    print(f"Sukses! Prediksi: {response.json()} | Latensi: {latency:.4f}s")
                else:
                    # Menampilkan error detail jika format JSON masih salah
                    print(f"Gagal! Status: {response.status_code}")
                    print(f"Pesan Error: {response.text}")
            
            except requests.exceptions.ConnectionError:
                print("Error: Tidak dapat terhubung ke Exporter (Port 8000). Pastikan prometheus_exporter.py sudah jalan.")
            
            # Jeda agar throughput tidak terlalu liar di grafik Prometheus
            time.sleep(2)

    except Exception:
        print("\nerror")

if __name__ == "__main__":
    run_inference()