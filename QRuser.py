import qrcode

class QRuser:

    def __init__(self, name):
        self.name = name
        self.qr_codes_made = 0

    def Make_qr(self, URL, file_name):
        img = qrcode.make(URL)
        img.save(file_name)
        self.qr_codes_made += 1

        print(f"{file_name} QR code generated successfully!!")

    def summary(self):
        print(f"{self.qr_codes_made} were made")
