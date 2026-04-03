# SauceDemo — Automation Testing

Automated end-to-end test suite for [SauceDemo](https://www.saucedemo.com), a demo e-commerce site.  
Built with **Playwright + PyTest** using the **Page Object Model (POM)** design pattern.

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| Playwright | Browser automation |
| PyTest | Test framework |
| Python 3.x | Language |
| GitHub Actions | CI/CD pipeline |

---

## 📁 Project Structure

```
saucedemo-automation/
├── tests/
│   ├── pages/
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   └── cart_page.py
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_checkout.py
├── conftest.py
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

## ✅ Test Coverage

- **Login** — valid login, invalid credentials, locked user
- **Inventory** — product listing, sorting, add to cart
- **Cart** — add/remove items, cart count
- **Checkout** — complete purchase flow, empty cart validation

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/afridi15/saucedemo-automation.git
cd saucedemo-automation

# 2. Install dependencies
pip install -r requirements.txt
playwright install

# 3. Run all tests
pytest tests/ -v

# 4. Run a specific test file
pytest tests/test_login.py -v
```

---

## ⚙️ CI/CD

Tests run automatically on every push and pull request via **GitHub Actions**.  
See `.github/workflows/ci.yml` for configuration.
