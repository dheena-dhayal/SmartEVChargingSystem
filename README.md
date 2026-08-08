⚡ Smart EV Charging Optimization System

A web-based Electric Vehicle (EV) charging management and optimization platform that intelligently allocates charging slots and optimizes charging decisions based on vehicle requirements, station availability, and charging conditions.

The system combines a **priority-based scheduling algorithm** with a **Deep Q-Network (DQN) reinforcement learning model** to improve charging efficiency and demonstrate the application of AI in EV charging management.

📌 Project Overview

The increasing adoption of Electric Vehicles creates a growing demand for efficient charging infrastructure. Poor allocation of charging slots can result in:

- Long waiting times
- Uneven utilization of charging stations
- Inefficient charging schedules
- Increased operational complexity

This project addresses these challenges by developing a centralized platform for **EV users, charging stations, and administrators**, while incorporating intelligent scheduling and optimization techniques.

🎯 Objectives

The primary objectives of this project are to:

- Efficiently allocate EV charging slots.
- Reduce unnecessary waiting time for users.
- Improve charging station utilization.
- Provide intelligent charging schedules.
- Monitor charging activities and station performance.
- Apply reinforcement learning to EV charging optimization.
- Provide administrators with useful operational analytics.

🚀 Key Features

### 👤 User Management

- User registration and authentication
- Vehicle management
- View available charging stations
- Check charging slot availability
- Book charging slots
- View booking history
- Monitor charging sessions
- View billing information

### 🔌 Charging Management

- Charging station management
- Slot availability management
- Intelligent slot allocation
- Priority-based scheduling
- Charging session monitoring
- Simulated charging telemetry

### 🧠 Intelligent Optimization

The system implements two optimization approaches:

**1. Priority-Based Greedy Scheduling**

A fast scheduling approach that assigns charging slots based on factors such as vehicle requirements, priority, station availability, and charging conditions.

**2. Deep Q-Network (DQN)**

A reinforcement learning approach that learns charging decisions through interaction with a simulated charging environment.

The DQN module is designed to optimize charging decisions while considering available charging resources.

### 📊 Admin Dashboard

Administrators can:

- Manage users
- Manage vehicles
- Manage charging stations
- Manage charging slots
- Configure tariffs
- Monitor bookings
- Monitor charging activity
- View system statistics and analytics

 🏗️ System Architecture

 Architecture:



 
                         ┌─────────────────┐
                         │      Users      │
                         └────────┬────────┘
                                  │
                                  ▼
                     ┌────────────────────────┐
                     │     Web Interface      │
                     │     HTML / CSS / JS    │
                     └────────────┬───────────┘
                                  │
                                  ▼
                     ┌────────────────────────┐
                     │      Flask Backend     │
                     │     Application Logic  │
                     └────────────┬───────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
      ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
      │  Scheduling  │    │     DQN      │    │   Billing &  │
      │    Engine    │    │  Optimizer   │    │  Management  │
      └──────┬───────┘    └──────┬───────┘    └──────┬───────┘
             │                   │                   │
             └───────────────────┼───────────────────┘
                                 │
                                 ▼
                       ┌──────────────────┐
                       │    SQLite DB     │
                       └──────────────────┘


                       
🧠 Optimization Methodology:

Priority-Based Scheduling
The initial scheduling mechanism uses a priority-based greedy strategy.
Charging requests are evaluated using parameters such as:
Charging priority
Vehicle requirements
Available charging slots
Station availability
This provides an efficient baseline scheduling solution.
Deep Q-Network (DQN)
The project also includes a reinforcement learning module based on Deep Q-Networks.
The DQN agent interacts with a simulated charging environment and learns which charging actions provide better outcomes.



Conceptually:


Charging Environment
        │
        ▼
   Current State
        │
        ▼
   DQN Agent
        │
        ▼
    Action
        │
        ▼
 Charging Decision
        │
        ▼
     Reward
        │
        └──────────► Learning
This approach demonstrates how reinforcement learning can be applied to intelligent EV charging management.
🛠️ Technology Stack
Layer
Technologies
Frontend
HTML5, CSS3, JavaScript (ES6)
UI
Glassmorphism, Chart.js
Backend
Python, Flask
Database
SQLite
ORM
SQLAlchemy
Machine Learning
PyTorch
AI Technique
Deep Q-Network (DQN)
Version Control
Git, GitHub
Development
Visual Studio Code


📂 Project Structure:

SmartEVChargingSystem/
│
├── models/
│   ├── __init__.py
│   ├── booking.py
│   ├── graph_network.py
│   ├── station.py
│   ├── user.py
│   └── vehicle.py
│
├── routes/
│   └── admin.py
│
├── services/
│
├── static/
│
├── templates/
│
├── app.py
├── config.py
├── database.py
├── demo_dqn.py
├── EV_Project_Report.md
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation & Setup:

1. Clone the Repository
git clone https://github.com/dheena-dhayal/SmartEVChargingSystem.git
2. Navigate to the Project Directory
cd SmartEVChargingSystem
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment
Windows:
venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt
6. Run the Application
python app.py
The application can then be accessed at:
http://127.0.0.1:5000
🔐 Security & Configuration
Sensitive configuration values should be stored in environment variables.
Example:
SECRET_KEY=your-secret-key
Sensitive files such as .env, virtual environments, database files, and Python cache files should not be committed to the repository.

📈 Future Enhancements:

The project can be further extended with:
Real-time IoT integration
Real-time charger monitoring
Mobile application
Cloud deployment
Vehicle-to-Grid (V2G) support
Real-time electricity pricing
Multi-station optimization
EV charging demand prediction
Advanced reinforcement learning algorithms

💡 What This Project Demonstrates:

This project demonstrates practical experience in:
Full-stack web application development
RESTful/backend application design
Database management
Algorithm design
Reinforcement learning
Machine learning with PyTorch
Data visualization
Git and GitHub
Software project organization

👨‍💻 Author
Dheena Dhayal M
MCA Student | PSG College of Technology
Interested in Software Development, Artificial Intelligence, Data Structures & Algorithms, and Intelligent Systems.
GitHub: dheena-dhayal
⁠
LinkedIn:https://www.linkedin.com/in/dheena-dhayal-m-41b714292?utm_source=share_via&utm_content=profile&utm_medium=member_android


📜 License
This project was developed for academic and educational purposes.
