
# 🦠 Epidemiological Data Dashboard

A web-based interactive dashboard to visualize and simulate the spread of diseases using the SIR model. Built with **Dash**, **Plotly**, **pandas**, and **matplotlib**.

---

## 📊 Features

- 📈 Visualize total cases over time by country
- 🧮 Predict disease spread using the **SIR model**
- 🌍 Support for multiple regions
- 🔄 Easy to extend with SEIR models or real-world datasets

---

## 🧱 Project Structure
```bash
Epidemiological_Dashboard_Project/
├── app.py # Main Dash application
├── data/
│ └── sample_data.csv # Sample dataset (date, location, total_cases)
├── models/
│ └── sir_model.py # SIR simulation model logic
├── venv/ # Optional: virtual environment folder (not included in Git)
├── assets/ # Optional: add CSS/JS here for custom styling
└── README.md # Project instructions

```

---


## ⚙️ Prerequisites

- Python 3.7+
- `pip` package manager

---


## 💻 Setup Instructions

### 🪟 Windows

```bash
# 1. Open Command Prompt and navigate to the project folder
cd path\\to\\Epidemiological_Dashboard_Project

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
venv\\Scripts\\activate

# 4. Install dependencies
pip install dash pandas plotly scipy

# 5. Run the app
python app.py
```

## 🍎 macOS / Linux

```bash
# 1. Open Terminal and navigate to the project folder
cd ~/Downloads/Epidemiological_Dashboard_Project

# 2. Create a virtual environment
python3 -m venv venv

# 3. Activate the virtual environment
source venv/bin/activate

# 4. Install dependencies
pip install dash pandas plotly scipy

# 5. Run the app
python app.py
🌐 View the Dashboard
After running app.py, open your browser and go to:


http://127.0.0.1:8050/

```


## 📁 Sample Dataset Format (data/sample_data.csv)
```bash
date,location,total_cases
2020-01-01,CountryA,0
2020-01-02,CountryA,3
```
...
## 🚀 Future Ideas
Add SEIR model support

Integrate real-time COVID or dengue datasets

Deploy to Heroku, Render, or Streamlit Cloud

## 🤝 Contributions
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.


