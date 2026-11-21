
# Python Playwright Test Automation Framework

### End-to-End Web Automation | Python | Playwright | Pytest

A web UI test automation framework developed using Python,
Playwright and Pytest to test the SauceDemo e-commerce application.

## Technologies

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Pytest Fixtures
- Data-Driven Testing
- HTML Test Reporting

## Test Scenarios

- Valid user login
- Invalid login and error message validation
- Add product to shopping cart
- Complete checkout workflow
- Reusable fixtures for test setup
- Parameterised login test cases

## Framework Architecture

- `pages/` - Page Object Model classes
- `tests/` - Automated test cases
- `conftest.py` - Shared Pytest fixtures
- `pytest.ini` - Pytest configuration
- `requirements.txt` - Python dependencies

## Installation

Clone the repository and open its folder.

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Execute Tests

Run all framework tests:

```bash
python -m pytest tests/ -v
```

Run tests with a visible browser:

```bash
python -m pytest tests/ --headed --slowmo 1000 -v
```

Generate an HTML report:

```bash
python -m pytest tests/ -v --html=report.html --self-contained-html
```

## Test Execution Results

Latest local execution: **9 passed, 0 failed**.

## Future Enhancements

- GitHub Actions CI/CD integration
- Expanded cross-browser testing
- Additional negative test scenarios
- Automated failure screenshots and traces

## Author

**Veera Manikanta Sai Kaja**

Software QA Engineer | Python & Playwright Automation

Based in Ireland | Open to QA and Graduate Engineering Roles

[GitHub](https://github.com/Veeramanikantasai)
