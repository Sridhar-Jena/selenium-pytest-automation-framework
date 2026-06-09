# 🧪 Selenium PyTest Automation Framework

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.18-green?logo=selenium)
![PyTest](https://img.shields.io/badge/PyTest-8.1-orange?logo=pytest)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A production-ready, scalable **UI Test Automation Framework** built with Python, Selenium WebDriver, and PyTest — following the **Page Object Model (POM)** design pattern.

---

## 🚀 Key Features

- ✅ **Page Object Model (POM)** — clean separation of test logic and UI interactions
- ✅ **Data-Driven Testing** — test inputs loaded from JSON files; easily extensible to Excel
- ✅ **Parallel Execution** — via `pytest-xdist` to reduce regression run time
- ✅ **Auto Screenshot on Failure** — captures and saves PNG on every failed test
- ✅ **HTML & Allure Reporting** — detailed visual test reports out of the box
- ✅ **Headless Mode Support** — run in CI/CD pipelines without a display
- ✅ **Jenkins Ready** — plug directly into any CI/CD pipeline

---

## 🗂️ Project Structure

```
selenium-pytest-automation-framework/
│
├── pages/                  # Page Object classes
│   ├── base_page.py        # Reusable Selenium wrapper methods
│   ├── login_page.py       # Login page interactions & locators
│   └── dashboard_page.py   # Dashboard page interactions & locators
│
├── tests/                  # Test suites
│   └── test_login.py       # Login feature: positive, negative, UI tests
│
├── utils/                  # Utilities and config
│   ├── config.py           # Centralized environment config
│   └── test_data.json      # External test data (data-driven)
│
├── reports/                # Auto-generated test reports & screenshots
├── conftest.py             # PyTest fixtures (driver, test data, hooks)
├── pytest.ini              # PyTest configuration
└── requirements.txt        # Python dependencies
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Browser Automation | Selenium WebDriver 4.x |
| Test Framework | PyTest |
| Design Pattern | Page Object Model (POM) |
| Parallel Execution | pytest-xdist |
| Reporting | pytest-html, Allure |
| API Testing | Python Requests |
| Data Management | JSON, openpyxl (Excel) |
| CI/CD | Jenkins |

---

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.10+
- Google Chrome browser
- Git

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/selenium-pytest-automation-framework.git
cd selenium-pytest-automation-framework
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running Tests

### Run all tests
```bash
pytest
```

### Run with HTML report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run in parallel (4 workers)
```bash
pytest -n 4
```

### Run headless (for CI/CD)
```bash
HEADLESS=true pytest
```

### Run only smoke tests
```bash
pytest -m smoke
```

---

## 📊 Test Report

After running, open `reports/report.html` in your browser to see a full test report with pass/fail status, execution time, and screenshots for failures.

---

## 🧩 Test Cases Covered

| TC ID | Description | Type |
|---|---|---|
| TC001 | Valid login with correct credentials | Positive |
| TC002 | Dashboard loads after successful login | Positive |
| TC003 | Logout flow works correctly | Positive |
| TC004 | Login fails with wrong username & password | Negative |
| TC005 | Login fails with wrong password only | Negative |
| TC006 | Login fails with empty username & password | Negative |
| TC007 | Login fails with empty password | Negative |
| TC008 | Login page title is correct | UI Validation |
| TC009 | Login page URL is correct | UI Validation |

---

## 👤 Author

**Sridhar Jena**
QA Automation Engineer | Python | Selenium | PyTest | Robot Framework

📧 jenasridhar2002@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/sridhar-jena)

---

## 📄 License

This project is licensed under the MIT License.
