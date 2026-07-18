import input
import QR_generator


url_list = input.getURL()
count = 1

for link in url_list:
    link = link.strip()  # strips the \n character
    file_name = f"QR_{count}.png"

    QR_generator.Make_qr(link, file_name)
    count += 1
