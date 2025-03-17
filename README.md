# Wallet API Automation Framework

## 📌 Overview
This is an API automation framework for testing the **Wallet API**. It covers:
- **Authentication**
- **Wallet Retrieval**
- **Transactions Processing**
- **Negative & Edge Cases**
- **Concurrency & Load Handling**
- **Allure Reporting Integration**

---

## ⚙️ **Project Structure**
```
WalletAPIAutomation/
│── tests/                  # API test cases
│   ├── test_auth.py        # Authentication tests
│   ├── test_wallet.py      # Wallet retrieval tests
│   ├── test_transactions.py # Transaction processing tests
│   ├── test_negative_cases.py # Negative test cases
│   ├── test_edge_cases.py  # Edge case test cases
│── utils/                  # Utility functions
│   ├── api_client.py       # API request handler
│   ├── config.py           # Configuration settings
│   ├── __init__.py         # Marks utils as a Python package
│── reports/                # Stores Allure reports
│── requirements.txt        # Dependencies
│── pytest.ini              # Pytest configuration
│── README.md               # Documentation
│── TESTPLAN.md             # Test plan with implemented/unimplemented cases
│── .gitignore              # Git ignore file
```

---

## 🚀 **Setup Instructions**

### **1️⃣ Clone the Repository**
```sh
git clone git@github.com:logifuture-task/wallet-api-automation.git
cd WalletAPIAutomation
```

### **2️⃣ Create a Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## 🛠 **Running Tests**

### **1️⃣ Run All Tests**
```sh
pytest
```

### **2️⃣ Run Specific Test File**
```sh
pytest tests/test_wallet.py
```

### **3️⃣ Run Tests with Allure Reporting**
```sh
pytest --alluredir=reports/allure-results
```

---

## 📊 **Allure Reporting**
### **1️⃣ Generate Allure Report**
After running tests, serve the report:
```sh
allure serve reports/allure-results
```
This will open an **interactive HTML report**.

### **2️⃣ Save Allure Report as HTML**
```sh
allure generate reports/allure-results -o reports/allure-report --clean
```
Then open:
```sh
open reports/allure-report/index.html  # Mac
start reports/allure-report/index.html # Windows
```

---

## ✅ **Best Practices**
- **Run tests from the project root** (`pytest`).
- **Ensure `utils/` has `__init__.py`** (`touch utils/__init__.py`).
- **Use a virtual environment** to avoid dependency conflicts.
- **Review Allure reports** to analyze test failures.

---

## ❗ Troubleshooting

### **1️⃣ `ModuleNotFoundError: No module named 'utils'`**
**Solution:**
Run tests from the root directory:
```sh
cd /path/to/WalletAPIAutomation
pytest
```
Or explicitly set `PYTHONPATH`:
```sh
PYTHONPATH=$(pwd) pytest
```

### **2️⃣ `pytest: command not found`**
Ensure you **activated your virtual environment**:
```sh
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### **3️⃣ `allure: command not found`**
Install **Allure CLI**:
```sh
brew install allure  # Mac
scoop install allure # Windows
```
Or manually download from: [https://github.com/allure-framework/allure2](https://github.com/allure-framework/allure2)

---

## 📌 **Author**
- **hkasarjyan**
- **hovhanneskasarjyan@gmail.com**
- **https://github.com/hkasarjyan**

🚀 Happy Testing! 🚀
