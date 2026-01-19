# ⚡ Cipher Engine
A small Python project using **Dictionaries** to map characters to custom symbols for basic encryption.

##  Concept
- Uses a **Hash Map (Dictionary)** for $O(1)$ lookup speed.
- Practice with string manipulation and user input.

##  Output

<img width="1567" height="716" alt="Screenshot 2026-01-13 at 6 59 42 AM" src="https://github.com/user-attachments/assets/66ff3264-444b-499e-97cf-b16a61fc8946" />

🌐 Vector-Vision: 3D Linear Combination Visualizer

A Python-based tool built to visualize the Geometry of Linear Equations, specifically focusing on the concepts of Span, Linear Independence, and Subspaces as taught in MIT’s 18.06 (Gilbert Strang).
🎯 Purpose

This project was developed during my GATE DA 2026 preparation to bridge the gap between abstract Linear Algebra theory and practical Data Science implementation. It visualizes how two vectors in R3 combine to form a 2D plane (the Column Space).
🛠️ Tech Stack

    Python 3.9+

    NumPy: Used for vector operations and generating the coordinate meshgrid.

    Matplotlib: Used for 3D rendering and surface plotting.

🧠 Core Concepts Visualized

    The Column Picture: Visualizing Ax as a linear combination of the columns of A.

    Linear Independence: * If vectors v and w are independent, they span a 2D Plane.

        If they are dependent (e.g., w=2v), the span collapses into a 1D Line.

    Span: Every point on the rendered "surface" represents a possible solution to the system cv+dw.

🚀 How to Run

    Clone the repo:
    Bash
    
<img width="993" height="748" alt="Screenshot 2026-01-16 at 11 08 18 AM" src="https://github.com/user-attachments/assets/6c251a0b-242c-484e-924d-03ddfb93583f" />


  The Skyline Generator:
  Code Logic (How it works)

    Canvas Setup: Creates a file in w mode and writes the HTML headers.

    The Algorithm: * Uses a while loop to traverse the X-axis (0 to 800px).

        Randomizes width and height for each building.

        Calculates y coordinates using 400 - height (since SVG coordinates start from top-left).

    Detailing: * Generates "Cyberpunk" RGB colors using random.randint.

        Uses nested loops to calculate window positions based on the building's dimensions.

    Finalization: Closes the SVG tags and saves the file.
    
<img width="847" height="512" alt="Screenshot 2026-01-17 at 7 40 22 AM" src="https://github.com/user-attachments/assets/533a6b9b-2b23-4691-a502-91a6254daca2" />


# 💼 TradeBot: Automated Portfolio Auditor

A Python-based Data Engineering tool designed to validate, clean, and analyze high-frequency trading data.

## 🔍 Problem Solved
Raw trading logs often contain corrupted data (missing prices, string errors) or logical impossibilities (negative quantities). Manually checking thousands of rows is impossible. This script automates the audit process.

## 🛠️ Technical Implementation
* **csv.DictReader:** Used for robust, column-based data parsing.
* **Exception Handling:** Implemented `try-except` blocks to catch `ValueError` (Data Type mismatches).
* **Business Logic Validation:** Manually raises errors for logical fallacies (e.g., Negative Quantity).
* **Logging:** Separates clean data (`verified_trades.csv`) from corrupted entries (`audit.log`).

<img width="1200" height="479" alt="Screenshot 2026-01-18 at 8 33 57 AM" src="https://github.com/user-attachments/assets/a7e0ca20-586f-45c5-a69b-49bfc505984a" />

IMAGE GLITCHER
A Python tool that performs "digital lobotomies" on image files to create cyberpunk glitch art.

This project bypasses standard image libraries (like PIL/OpenCV) to manipulate raw file bytes directly. It opens images in binary mode, injects random noise into the data stream, and stitches the file back together—creating unpredictable visual artifacts.
How It Works (The "Under the Hood" Logic)

Most image editors work with Pixels (R, G, B values). This tool works with Bytes (Hex Data).
1. Binary Surgery (rb Mode)

We open the file using Python's rb (Read Binary) mode. This treats the image not as a picture, but as a raw stream of data (e.g., \xFF\xD8\xFF...).
2. Mutable Memory (bytearray)

Python's standard bytes objects are immutable (cannot be changed). To modify the file in-memory without saving it 1000 times, we convert the stream into a mutable bytearray:
Python

with open(filename, "rb") as f:
    data = f.read()
    mutable_data = bytearray(data)  # Now we can edit specific bytes!

3. Header Protection (The "Brain" of the File)

Every file (JPG, PNG) starts with a Header—a specific sequence of bytes that tells the OS "I am an image."

    If we corrupt the header, the file breaks and won't open.

    Solution: We implement a Dynamic Safe Zone that skips the first 10-15% of the file bytes, ensuring we only glitch the pixel data, not the metadata.

4. Noise Injection

We randomly select byte addresses and overwrite them with random integers (0-255). This corrupts the compression algorithms (like Huffman coding in JPGs), forcing the decoder to "guess" the colors, resulting in cool visual tears and color shifts.
🚀 How to Run

    Clone the Repo:
    Bash

git clone https://github.com/YourUsername/Binary-Surgeon.git
cd Binary-Surgeon

Add a Target: Place any .jpg or .png image in the folder.

Run the Script:
Bash

    python glitcher.py

    Check the Output: A new file named glitched_filename.jpg will appear in your folder.

⚙️ Configuration (Tweak the Chaos)

You can adjust the parameters inside glitcher.py to get different artistic effects:
Parameter	Recommended Value	Effect
intensity	0.005 - 0.02	Controls what % of bytes get destroyed. Warning: Go too high (>0.05) and the file may die.
header_safe_zone	int(file_size * 0.10)	Percentage of the file start to protect. Increase this if your output files are blank/broken.
⚠️ Disclaimer

This script corrupts data. While it creates a copy (glitched_), never run this on your only copy of an important photo. The output is random—some files may look cool, others may break completely.

![Untitled design(1)](https://github.com/user-attachments/assets/e5ce8412-7e81-4e69-a6c8-8fb1f5aaf643)

