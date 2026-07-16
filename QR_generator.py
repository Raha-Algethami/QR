import qrcode


def Make_qr(URL):
    img = qrcode.make(URL)
    img.save('qr.png')

    print("QR code generated successfully!!")
