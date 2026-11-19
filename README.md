# Autonomous Financial Agent

A financial assistant that actually does something instead of just showing you charts. You tell it your income, expenses, and goals. It makes a plan, watches your spending, and warns you when you are going off track.

Built for the ET AI Hackathon 2026.

## Why It Exists

Most finance apps show you dashboards. They tell you what you spent last month but do not help you do better. This one is different. It uses several AI agents working together — one makes the plan, one watches your spending, one suggests investments, and one sends alerts when something is wrong.

## How It Works

You enter your income, expenses, and what you want to save for. The planner agent creates a budget. As you spend money, the analyzer agent watches for patterns. If you are spending too much on dining out, it lets you know. The advisor agent suggests where to invest. Everything adjusts as your habits change.

## Getting Started

Start the backend:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Start the frontend:

```bash
cd frontend
npm install
npm start
```

Create a `.env` file in the backend folder with your OpenAI API key:

```
OPENAI_API_KEY=your_api_key
```

## What You Get

A budget plan based on your income. Spending alerts when you go over. Investment suggestions like SIPs. A financial health score that changes as you improve. All built with React on the frontend and FastAPI on the backend.

## What Comes Next

Banking API integration so it connects to your actual accounts. UPI support. Voice commands. Automatic investment execution.

## License

MIT
