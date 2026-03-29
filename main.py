"""
Autonomous Financial Agent – FastAPI Entry Point
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import user, transactions, insights, dashboard

app = FastAPI(
    title="Autonomous Financial Agent",
    description="AI-powered financial assistant for young Indian professionals",
    version="1.0.0",
)

# CORS – allow frontend dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(user.router)
app.include_router(transactions.router)
app.include_router(insights.router)
app.include_router(dashboard.router)


@app.get("/")
async def root():
    return {
        "name": "Autonomous Financial Agent API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health")
async def health():
    return {"status": "ok"}
