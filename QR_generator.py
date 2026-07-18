import qrcode


def Make_qr(URL, file_name):
    img = qrcode.make(URL)
    img.save(file_name)

    print(f"{file_name} QR code generated successfully!!")
