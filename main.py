import input
from QRuser import QRuser
import os


data_list = input.getData()
os.makedirs("output", exist_ok=True)

user = QRuser("name")

user.Make_qr("cisco.com", "cisco")
user.Make_qr("iherb.com", "iherb")

for line in data_list:
    name, url = line.strip().split(",")
    user.Make_qr(url.strip(), name.strip())
user.summary()
