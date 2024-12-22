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
```

---

## 🛠️ Installation Instructions

### Prerequisites
1. Install **Python 3.7+**.
2. Install **Google Chrome** and the corresponding **ChromeDriver** for Selenium.
   - Download ChromeDriver: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/selenium-ui-automation-testing.git
   cd selenium-ui-automation-testing
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the test environment:
   - Update `config/config.yaml` with the desired base URL and language settings.

---

## ▶️ How to Run Tests

1. Run all tests and generate an HTML report:
   ```bash
   pytest src/tests/ --html=reports/report.html
   ```

2. Run a specific test:
   ```bash
   pytest src/tests/test_search.py
   ```

3. View the HTML report:
   - Open `reports/report.html` in your browser.

---

## 🌟 Example Test Case

### Search Functionality Test
The following test checks if searching for "Python (programming language)" on Wikipedia returns the correct page:

```python
def test_search_functionality(self):
    self.home_page.load("https://www.wikipedia.org")
    self.home_page.search("Python (programming language)")
    assert "Python" in self.driver.title
```

---

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🙋‍♂️ Contact
For any questions or feedback, please reach out to [your-email@example.com](mailto:your-email@example.com).
