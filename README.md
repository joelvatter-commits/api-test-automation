# API Test Automation Framework 🚀

## About the Project
This repository contains an automated testing framework built with **Python** and **Pytest**. It is designed to validate REST API endpoints by performing CRUD (Create, Read, Update, Delete) operations.

Currently, the tests run against the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API to simulate real-world usage without triggering bot protections.

[![Run API Tests](https://github.com/joelvatter-commits/api-test-automation/actions/workflows/main.yml/badge.svg)](https://github.com/joelvatter-commits/api-test-automation/actions/workflows/main.yml)

## Tech Stack
* **Language:** Python 3.x
* **Libraries:**
  * `requests` (HTTP calls)
  * `pytest` (Test execution & assertions)
* **Environment:** Virtual Environment (venv)

## Test Scenarios
* ✅ **GET /users/{id}:** Verifies that user data is retrieved correctly (Status 200).
* ✅ **POST /users:** Verifies that a new user can be created (Status 201).
* 🛡️ **Error Handling:** Validates that the system handles invalid requests appropriately.

### 🛡️ Security & Performance Tests
In addition to functional testing, this framework includes basic security checks:
* **SQL Injection Simulation:** Attempts to inject malicious SQL payloads (`' OR 1=1 --`) into input fields to ensure the API does not crash or expose database errors (500 Internal Server Error).
* **Fuzzing / Load Test:** Sends large payloads (buffer overflow simulation) to measure API response time and stability under stress.

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/joelvatter-commits/api-test-automation.git](https://github.com/joelvatter-commits/api-test-automation.git)