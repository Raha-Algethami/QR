#  Qr code generator Engine- using the qrcode library

A lightning fast. terminal based python application that handles a website link form the user, and instantly turn it into a scannable qr code png file in seconds,this tool is designed to be reliable, scalable, and easy to read.
With implemented OS-level directory management (os.makedirs) to automatically generate and route QR images into a dedicated output folder.

##  How to use

1. **Installations:** Ensure you have the required libraries included the file `requirements.txt`. (You can install them by running `pip install -r requirements.txt` in your terminal).
2. **Running the program:** in your terminal type:
   `python main.py`


##  Features

-* **[modularity]** This program can be used in other complex programs without ever touching the core logic.
-* **[Built to Scale]** Designed with a controller-based execution model(main). If you suddenly need to generate 1000 QR codes from a .csv spreadsheet, you only have to loop the controller..the underlying engine stays exactly the same.
-* **[Lightweight]** Strict version control hygiene keeps this repository completely free of bloated cache files and localized machine environments. You only download the code you actually need.
- * **[Easy to understand]** Explicit namespace routing prevents code collisions, making it incredibly easy for other developers to read, debug, and contribute to the codebase.
-* **[Smart Data Parsing & File Naming]** Upgraded the input system to process structured, CSV-style text data. The generator now automatically slices inputs to assign custom, descriptive file names (e.g., `Instagram_QR.png`) during bulk generation. it makes it easier not to get your files mixed up.
-* **[Automated Output Routing]** Integrates directly with the operating system to dynamically generate an isolated `output/` directory. All generated QR codes are automatically routed to this folder, keeping the main project directory completely organized and free of image pollution.

### Programming Language
- python


### Development Tools
- Visual Studio Code
- Git
- GitHub
- requirements.txt

---

## 📂 Project Structure

```text
QR
│
├── input.py
├── QR_generator.py
├── main.py
└── links.txt
└── README.md
```

---

##  Author

**Raha Algethami**

Computer Engineering Student  
Taif University  
Saudi Arabia 🇸🇦
