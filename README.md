# Selenium UI Automation Testing

This repository contains a modular and scalable Selenium-based UI automation framework designed for testing open-source websites. The framework is built using **Python**, **pytest**, and the **Page Object Model (POM)** design, ensuring maintainability and scalability.

---

## 🚀 Features
- Automated testing for:
  - Search functionality.
  - Language switching.
  - Section navigation within articles.
- Configurable test setup via `config.yaml`.
- Modular framework using the **Page Object Model (POM)**.
- Detailed HTML reports for test results.
- Easy integration with CI/CD pipelines.

---

## 📖 User Stories

### 1. **Search Functionality**
**As a user**, I want to search for a topic on a website (e.g., Wikipedia) so that I can quickly access relevant information.

### 2. **Language Switching**
**As a user**, I want to switch the language of the homepage so that I can browse content in my preferred language.

### 3. **Navigation to a Specific Section**
**As a user**, I want to navigate to a specific section of an article so that I can find detailed information easily.

---

## 📂 Project Structure
```plaintext
selenium-ui-automation-testing/
├── src/
│   ├── tests/
│   │   ├── test_search.py       # Test for search functionality
│   │   ├── test_language.py     # Test for language switching
│   │   └── test_navigation.py   # Test for section navigation
│   ├── pages/
│   │   ├── homepage.py          # Page Object Model for the homepage
│   │   └── article_page.py      # Page Object Model for article pages
├── config/
│   └── config.yaml              # Configuration file for test setup
├── reports/                     # HTML test reports
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation


# Installation Instructions

Follow these steps to set up and run the Selenium UI Automation Testing framework on your local machine.

---

## Prerequisites

1. **Python 3.7 or higher**: Ensure Python is installed on your system.
   - Download: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   
2. **Google Chrome**: Install the latest version of Google Chrome.
   - Download: [https://www.google.com/chrome/](https://www.google.com/chrome/)

3. **ChromeDriver**: Download the ChromeDriver compatible with your Chrome version.
   - Download: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)

4. **Git**: Ensure Git is installed to clone the repository.
   - Download: [https://git-scm.com/](https://git-scm.com/)

---

## Step-by-Step Installation

### 1. Clone the Repository
```bash
git clone https://github.com/kgandhi04/selenium-ui-automation-testing.git
cd selenium-ui-automation-testing

