# 0/1 Knapsack Problem Solver

This is a web application built with **Flask** and **Tailwind CSS** that allows users to solve the **0/1 Knapsack Problem**. It features a visual representation of the selected items within the knapsack, a detailed explanation of the solution steps, and an improved user interface.

---

## 🚀 Features
- User-friendly UI with a clean Tailwind CSS design.
- Visual representation of the knapsack container and selected items.
- Progress bar to indicate capacity usage.
- Step-by-step explanation dropdown for clear understanding.

---

## 📋 Requirements
Ensure you have the following installed:
- Python 3.8+
- Flask
- Tailwind CSS (via CDN)

---

## ⚙️ Installation & Setup
1. **Clone the repository**
```bash
git clone https://github.com/your-repo/knapsack-solver.git
cd knapsack-solver
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install flask
```

4. **Run the application**
```bash
python app.py
```

5. **Access the web app**
- Open your browser and go to: **`http://localhost:5000`**

---

## 📄 How It Works
1. **Enter Values:** Provide the values of items (comma-separated). Example: `60, 100, 120`
2. **Enter Weights:** Provide the weights of the items (comma-separated). Example: `10, 20, 30`
3. **Enter Capacity:** Specify the maximum capacity of the knapsack.
4. **Submit the Form:** The application calculates the maximum possible value and visually represents the selected items in the knapsack container.
5. **View Explanation Steps:** Click the "Explanation Steps" dropdown to see the step-by-step calculation process.

---

## 🖥️ Example Usage
- **Input Values:** `60, 100, 120`
- **Input Weights:** `10, 20, 30`
- **Capacity:** `50`

**Result:** Maximum Value = **220**

---

## 🐞 Troubleshooting
- Ensure all dependencies are properly installed.
- If Tailwind CSS styling doesn't load, check your network connection since the CDN is used.
- If the server doesn't start, ensure your `app.py` is correctly configured with Flask.

---

## 📧 Support
If you encounter any issues or have suggestions for improvement, feel free to reach out or open an issue on GitHub.

Happy Coding! 😊

