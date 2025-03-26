# **Kasidakis Projects API**

Welcome to the **Kasidakis Projects API**!  
This repository contains a modular, testable, and Dockerized Python application built using **Flask**, **SQLModel**, and **SQLite**. It allows you to manage and retrieve personal and professional projects with Swagger documentation and automated testing.

---

## ✨ Features

- 🔧 **Flask + SQLModel** for building clean, maintainable REST APIs  
- 📘 **Swagger UI** via `flask-smorest` for interactive API documentation  
- 🧪 **Pytest** testing suite with mocked DB logic (unit + integration tests)  
- 🐳 **Dockerized**, with flexible entrypoint (run app or tests)  
- 📂 Modular structure: `api/`, `business_logic/`, `data_layer/`, `tests/`

---

## 🧱 Project Structure

```bash
.
├── app.py                     # Main Flask entrypoint
├── api/                       # Flask Blueprints and Swagger schemas
├── business_logic/            # Service layer
├── data_layer/                # SQLModel tables and database logic
├── tests/                     # Pytest test suite
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker container definition
└── README.md
