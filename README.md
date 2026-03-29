# Autonomous Financial Agent for Young Indian Professionals

An AI powered, agent based financial assistant that analyzes, adapts, and takes action to improve users’ financial health in real time.

---

## Problem

Young professionals in India are earning their first stable incomes but struggle with:

* Unconscious overspending
* Delayed savings and investments
* Financial anxiety due to lack of guidance

Existing applications focus on dashboards and tracking rather than actionable intelligence.

---

## Solution

This project introduces an autonomous financial agent that:

* Understands income, expenses, and financial goals
* Generates personalized financial plans
* Continuously monitors spending behavior
* Detects financial issues such as overspending and missed savings
* Recommends corrective actions and adapts strategies over time

This is not a chatbot. It is a multi agent AI system designed for continuous decision support.

---

## Key Features

### Smart Financial Planning

* Generates budget allocation and savings targets
* Suggests investment plans such as SIPs based on user profile

### Spending Intelligence

* Tracks and analyzes transaction patterns
* Identifies overspending across categories

### Real Time Alerts

* Notifies users when budgets are exceeded
* Provides actionable recommendations

### Adaptive AI Behavior

* Adjusts plans based on user activity
* Learns from historical financial behavior

### Financial Health Score

* Provides a dynamic score indicating financial stability

---

## System Architecture

The system is built using a multi agent architecture:

### Planner Agent

Creates the initial financial plan based on user input

### Spending Analyzer Agent

Analyzes transaction data and identifies behavioral patterns

### Investment Advisor Agent

Recommends and adjusts investment strategies

### Alert and Action Agent

Triggers alerts and suggests corrective measures

### Memory System

Stores user data and enables continuity across sessions

---

## Tech Stack

Frontend: React with Tailwind CSS
Backend: FastAPI with Python
AI Engine: OpenAI or Gemini API
Database: Firebase or Supabase
Visualization: Recharts or Chart.js

---

## Project Structure

/backend
/agents
planner.py
analyzer.py
advisor.py
alert.py
/routes
user.py
insights.py
main.py

/frontend
/components
Dashboard.jsx
Alerts.jsx
InputForm.jsx
App.jsx

---

## Getting Started

### Clone the Repository

git clone https://github.com/your-username/financial-agent
cd financial-agent

---

### Backend Setup

cd backend
pip install -r requirements.txt
uvicorn main:app --reload

---

### Frontend Setup

cd frontend
npm install
npm start

---

### Environment Variables

Create a .env file in the backend directory:

OPENAI_API_KEY=your_api_key

---

## Demo Flow

1. User enters income, expenses, and goals
2. The system generates a financial plan
3. Mock transaction data simulates real usage
4. The system detects overspending patterns
5. Alerts are generated
6. The plan is adjusted dynamically

---

## Impact Model

* Reduces financial planning time from hours to minutes
* Reduces overspending by an estimated 20 to 30 percent
* Improves savings rate by approximately 25 percent

---

## What Makes It Different

* Multi agent architecture instead of a single model response
* Action oriented system rather than passive advice
* Continuous adaptation based on user behavior
* Designed specifically for Indian financial habits

---

## Future Scope

* Integration with banking APIs and UPI systems
* Automated investment execution
* Voice enabled financial assistant
* Advanced risk profiling and personalization

---

## Demo Video

Add your 3 minute demo link here

---

## License

MIT License

---

## Team

Your Name
Teammate Name

---

## Final Note

This project presents a shift from passive financial tracking to an active AI driven system that helps users make better financial decisions and build long term stability.

Built for ET AI Hackathon 2026
