# 🤖 FinAgent — Autonomous Financial Agent for Young Indian Professionals

An AI-powered, multi-agent financial system that **takes actions, not just gives advice**.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│              React + Tailwind UI             │
│    (Dashboard, Charts, Alerts, Forms)        │
└────────────────────┬────────────────────────┘
                     │ REST API
┌────────────────────▼────────────────────────┐
│              FastAPI Backend                  │
│  ┌──────────┐ ┌──────────┐ ┌──────────────┐ │
│  │ Planner  │ │ Analyzer │ │   Advisor    │ │
│  │  Agent   │ │  Agent   │ │   Agent      │ │
│  └──────────┘ └──────────┘ └──────────────┘ │
│  ┌──────────┐ ┌──────────────────────────┐  │
│  │  Alert   │ │    Memory System         │  │
│  │  Agent   │ │  (Cross-session state)   │  │
│  └──────────┘ └──────────────────────────┘  │
│              Gemini AI + Firebase             │
└──────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Google Gemini API key ([Get one free](https://aistudio.google.com/apikey))

### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment
copy .env.example .env       # Windows
# cp .env.example .env       # macOS/Linux

# Edit .env and add your GEMINI_API_KEY
```

### 2. Frontend Setup

```bash
cd frontend
npm install
```

### 3. Run the App

**Terminal 1 – Backend:**
```bash
cd backend
# Make sure venv is activated
uvicorn backend.main:app --reload --port 8000
```
> Run this from the project root directory (ET folder), NOT from inside the backend folder.

**Terminal 2 – Frontend:**
```bash
cd frontend
npm run dev
```

Open **http://localhost:5173** in your browser.

## 🔑 API Key Setup

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Click "Create API Key"
3. Copy the key and paste it in `backend/.env`:
   ```
   GEMINI_API_KEY=your-key-here
   ```

> **No API key?** The app works without one — it uses deterministic fallback logic for all agents. You just won't get personalized AI insights.

## 📊 Demo Flow

1. **Onboard** — Fill in your income, expenses, risk level, and goals
2. **Generate Plan** — AI creates budget allocation + SIP suggestions
3. **Simulate Transactions** — Realistic mock spending data is generated
4. **View Dashboard** — Charts, health score, insights, and alerts appear
5. **Re-Analyze** — Agent adapts the plan based on actual spending
6. **Alerts** — Overspending warnings with corrective actions

## 🧠 Multi-Agent System

| Agent | Purpose |
|-------|---------|
| **Planner** | Creates budget allocation, savings targets, SIP suggestions |
| **Analyzer** | Detects overspending, category-wise breakdown |
| **Advisor** | SIP recommendations based on risk level & income |
| **Alert** | Generates warnings with corrective actions + escalation |
| **Memory** | Cross-session continuity, context retrieval |

## 📁 Project Structure

```
ET/
├── backend/
│   ├── agents/
│   │   ├── planner.py      # Budget planning agent
│   │   ├── analyzer.py     # Spending analysis agent
│   │   ├── advisor.py      # Investment advice agent
│   │   ├── alert.py        # Alert & action agent
│   │   └── memory.py       # Memory system
│   ├── routes/
│   │   ├── user.py          # User CRUD
│   │   ├── transactions.py  # Transaction simulation
│   │   ├── insights.py      # Agent orchestration
│   │   └── dashboard.py     # Aggregated dashboard
│   ├── main.py              # FastAPI entry point
│   ├── models.py            # Pydantic models
│   ├── database.py          # Firebase/local JSON storage
│   └── requirements.txt
├── frontend/
│   └── src/
│       ├── components/
│       │   ├── InputForm.jsx
│       │   ├── Dashboard.jsx
│       │   ├── Alerts.jsx
│       │   ├── HealthScore.jsx
│       │   ├── ExpenseChart.jsx
│       │   └── InsightsPanel.jsx
│       ├── api.js
│       ├── App.jsx
│       └── index.css
└── README.md
```

## 🧪 Sample Test Data

After running the app, the onboarding form comes pre-filled with:
- **Income:** ₹60,000
- **Rent:** ₹12,000
- **Age:** 25
- **Risk:** Medium

Click "Simulate Transactions" to auto-generate 25-40 realistic Indian transactions (Zomato, Uber, BigBasket, etc.).

## ⚡ Adaptive Behavior

- **Overspend detected** → Next budget allocates less to that category
- **Income increases** → Agent suggests higher savings & SIP amounts
- **Alerts ignored** → Escalation: normal → elevated → critical tone
