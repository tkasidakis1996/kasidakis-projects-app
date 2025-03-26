# **Kasidakis Projects API**

Welcome to the **Kasidakis Projects API**!  
This repository contains a modular, testable, and Dockerized Python application built using **Flask**, **SQLModel**, and **SQLite**. It allows you to manage and retrieve personal and professional projects with Swagger documentation and automated testing.

---

## ✨ Features

- 🔧 **Flask + SQLModel** for building clean, maintainable REST APIs  
- 📘 **Swagger UI** via `flask-smorest` for interactive API documentation  
- 🧪 **Pytest** testing suite with mocked DB logic (unit + integration tests)  
- 🐳 **Dockerized**
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

```

---

## 🐳 How to Run the API

1. **Clone the repository**:

   ```bash
   git clone https://github.com/tkasidakis1996/kasidakis-projects-app
   cd kasidakis-projects-app

2. **Build the Docker image**:

   ```bash
   docker build -t kasidakis-projects-api .

3. **Run the application (default command):**

   ```bash
   docker run -p 5000:5000 kasidakis-projects-api

---

## 🧪 How to Run Tests

To run the full test suite using the Docker container:

```bash
docker run kasidakis-projects-api pytest -v tests
```

## 📘 Swagger Documentation

The Kasidakis Projects API comes with interactive **Swagger UI** powered by `flask-smorest`. You can use it to explore, test, and understand all available endpoints without writing a single line of code.

### 🔗 Accessing Swagger

Once the API is up and running, open your browser and navigate to: http://localhost:5000/docs

This will load the Swagger UI, where you can:

- 📄 View available endpoints
- 🔄 Execute live GET requests
- 🔧 Inspect request/response models
- ✅ Test inputs and check validation rules




