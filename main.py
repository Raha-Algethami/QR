import input
from QRuser import QRuser
import os

data_list = input.getData()
os.makedirs("output", exist_ok=True)

user = QRuser("name")

for line in data_list:
    line = line.strip()
    if not line or "," not in line:
        continue
    name, url = line.split(",", 1)
    user.Make_qr(url.strip(), f"output/{name.strip()}.png")

user.summary()
