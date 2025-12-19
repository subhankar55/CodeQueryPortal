# Code Query Portal

Code Query Portal is a web-based application that allows users to search for code snippets using natural language queries. Users can log in using their Google account and get instant answers to their coding questions.

## Features

- **User Authentication:** Secure login with Google OAuth.
- **Code Search:** A simple chat interface to query for code snippets.
- **Extensible Knowledge Base:** Easily add new code solutions by updating a text file.
- **Query Logging:** All queries are logged for monitoring and analysis.
- **MySQL Integration:** User login data is stored in a MySQL database.

## Tech Stack

### Frontend

- **React:** A JavaScript library for building user interfaces.
- **Vite:** A fast build tool for modern web development.
- **Fetch API:** For making requests to the backend.

### Backend

- **Flask:** A lightweight web framework for Python.
- **MySQL:** For storing user data.
- **mysql-connector-python:** To connect to the MySQL database.
- **google-auth:** For verifying Google OAuth tokens.

## Setup and Installation

### Prerequisites

- [Node.js and npm](https://nodejs.org/en/download/)
- [Python 3](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)

### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the MySQL database:**
    -   Make sure your MySQL server is running.
    -   Create a database for the project, e.g., `codequeryportal`.
    -   Update the database credentials in `backend/database.py`. You need to replace the placeholder values for `host`, `user`, `password`, and `database`.

5.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    The backend server will start on `http://localhost:5000`.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install the npm dependencies:**
    ```bash
    npm install
    ```

3.  **Run the React application:**
    ```bash
    npm run dev
    ```
    The frontend development server will start on `http://localhost:5173`.

## Usage

1.  Open your web browser and go to `http://localhost:5173`.
2.  Log in using your Google account.
3.  You will be redirected to the chat page.
4.  Enter your coding question in the text area and click "Submit".
5.  The corresponding code snippet will be displayed if found.

## Project Structure

```
CodeQueryPortal/
├── backend/
│   ├── app.py              # Main Flask application
│   ├── auth.py             # Google OAuth verification
│   ├── matcher.py          # Logic for finding code solutions
│   ├── database.py         # MySQL database connection and operations
│   ├── solutions.txt       # The knowledge base of code snippets
│   ├── requirements.txt    # Backend dependencies
│   ├── schema.sql          # SQL schema for the users table
│   └── logs/
│       └── queries.log     # Log of all user queries
│
└── frontend/
    ├── src/
    │   ├── api.js          # Functions for API calls to the backend
    │   ├── App.jsx         # Main React component with routing
    │   ├── pages/
    │   │   ├── Chat.jsx    # The chat interface
    │   │   └── Login.jsx   # The login page
    │   └── ...
    ├── package.json        # Frontend dependencies and scripts
    └── ...
```
