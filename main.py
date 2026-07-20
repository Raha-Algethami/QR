import input
import QR_generator
import os


data_list = input.getData()

os.makedirs("output", exist_ok=True)
for line in data_list:
    line = line.strip()  # strips the \n character
    strings = line.split(",")
    name = strings[0]
    url = strings[1]

    file_name = f"output/{name}_QR.png"

    QR_generator.Make_qr(url, file_name)
