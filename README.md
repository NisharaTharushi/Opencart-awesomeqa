## 🔧 Selenium Test Automation for Opencart-awesomeqa Website

### 🌐 Project Overview

This project contains automated test scripts written in Python using Selenium WebDriver and the Page Object Model (POM) design pattern for the e-commerce website:

🔗 [OpenCart Awesomeqa](https://awesomeqa.com/ui/)

Opencart-awesomeqa is an online shopping platform that allows users to browse featured products, register, log in, search for items, and complete purchases. This site is great for practicing UI automation on real-world e-commerce workflows.

### ✅ What This Project Covers

I developed automated Python test scripts following the Page Object Model (POM) design pattern. The tests cover:

    Functional and UI validations

    User registration and login flows

    Product search and browsing featured products

    Shopping cart actions and checkout-related validations

    Navigation and page element verifications

## 📄 Features and Pages Tested

The following pages are implemented as Page Objects and tested:

    Featured Products Page

    Home Page

    Login Page

    Products Page

    Register Page

    Search Page

Each page has its own Page Object class and corresponding test scripts for modularity and maintainability.

## 🧰 Tools & Technologies Used

    Language: Python 3.x

    Automation Tool: Selenium WebDriver

    Design Pattern: Page Object Model (POM)

    Testing Framework: Pytest

    Browser Drivers: ChromeDriver and GeckoDriver (Firefox)

```

## 📁 Project Structure

Opencart-awesomeqa/
│
├── pages/
│   ├── featured_products_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── register_page.py
│   └── search_page.py
│
├── tests/
│   ├── test_featured_products.py
│   ├── test_home.py
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_register.py
│   └── test_search.py
│
├── requirements.txt
├── README.md
└── .gitignore
