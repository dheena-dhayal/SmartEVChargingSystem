# Smart EV Charging Station Management System

A Flask-based web application for managing EV charging stations, booking slots, and optimizing charging schedules.

## Prerequisites

1.  **Python 3.x**: Ensure Python is installed.
    *   Open a terminal and type `python --version` to check.
    *   If not installed, download it from [python.org](https://www.python.org/downloads/).
    *   **Important**: During installation, check the box **"Add Python to PATH"**.

## Installation

1.  **Navigate to the project directory**:
    ```bash
    cd C:\Users\dheena\SmartEVChargingSystem
    ```

2.  **Create a Virtual Environment** (Optional but Recommended):
    ```bash
    python -m venv venv
    ```
    *   **Activate it**:
        *   Windows (Command Prompt): `venv\Scripts\activate`
        *   Windows (PowerShell): `.\venv\Scripts\Activate`

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  **Start the Server**:
    ```bash
    python app.py
    ```

2.  **Access the App**:
    *   Open your web browser (Chrome).
    *   Go to: http://127.0.0.1:5000

## Features (Premium Version)

*   **Smart Optimization**:
    *   Real-time Grid Load analysis (Low/Medium/High).
    *   Cost-effective charging slot recommendations.
    *   Dynamic pricing estimation.
*   **Real-Time Dashboard**:
    *   Live battery simulation & status updates.
    *   Visual "Charger Grid" showing station availability.
*   **Admin Analytics**:
    *   Interactive Charts (Energy Trends, Peak Hours) using Chart.js.
    *   Key Performance Indicators (KPIs).
*   **Modern UI/UX**:
    *   **Glassmorphism Theme**: Electric Blue & Emerald Green aesthetics.
    *   **Dark Mode**: Fully supported with toggle.
    *   **Animations**: Smooth transitions & background EV motion.
*   **User/Admin Roles**: Secure authentication and role-based access.

## Default Credentials

*   **Admin**:
    *   Username: `admin`
    *   Password: `admin123`
