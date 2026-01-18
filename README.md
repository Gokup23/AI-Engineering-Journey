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

