import os
import requests

# 1) Where you want to save your 4 car pics
OUT_DIR = r"G:\AAU Klagenfurt University\clip-demo\images"
os.makedirs(OUT_DIR, exist_ok=True)

# 2) Four direct URLs to car images
URLS = [
    # 1964 Ford Mustang (public domain)
    "https://upload.wikimedia.org/wikipedia/commons/3/3e/1964_Ford_Mustang.jpg",
    # 2018 Ford Mustang GT 5.0 (CC-BY-2.0)
    "https://upload.wikimedia.org/wikipedia/commons/3/3a/2018_Ford_Mustang_GT_5.0_%2850143712701%29.jpg",
    # Tesla Model S (public domain)
    "https://upload.wikimedia.org/wikipedia/commons/f/f0/Tesla_Model_S.JPG",
    # Tesla Model S with hood up (CC-BY-SA-3.0)
    "https://upload.wikimedia.org/wikipedia/commons/7/74/Tesla_Model_S_with_hood_up.JPG"
]

# 3) A realistic browser User-Agent so Wikimedia will serve the file
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0.0.0 Safari/537.36"
    )
}

# 4) Download each one
for url in URLS:
    fname = os.path.basename(url)
    out_path = os.path.join(OUT_DIR, fname)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        with open(out_path, "wb") as f:
            f.write(resp.content)
        print(f"✔ Saved {fname}")
    except Exception as e:
        print(f"✖ Failed {fname}: {e}")
