import input
import QR_generator


data_list = input.getData()


for line in data_list:
    line = line.strip()  # strips the \n character
    strings = line.split(",")
    name = strings[0]
    url = strings[1]

    file_name = f"{name}_QR.png"

    QR_generator.Make_qr(url, file_name)
