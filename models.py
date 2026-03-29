"""Pydantic models for the Autonomous Financial Agent."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ── Enums ──────────────────────────────────────────────────────────────
class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class AlertSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class TransactionCategory(str, Enum):
    FOOD = "Food"
    TRAVEL = "Travel"
    BILLS = "Bills"
    ENTERTAINMENT = "Entertainment"
    SHOPPING = "Shopping"
    HEALTH = "Health"
    EDUCATION = "Education"
    OTHER = "Other"


# ── User ───────────────────────────────────────────────────────────────
class FinancialGoal(BaseModel):
    name: str = Field(..., example="Emergency Fund")
    target_amount: float = Field(..., example=100000)
    timeline_months: int = Field(..., example=12)


class UserProfileCreate(BaseModel):
    name: str = Field(..., example="Rahul Sharma")
    age: int = Field(..., example=26)
    monthly_income: float = Field(..., example=60000)
    rent: float = Field(0, example=15000)
    emi: float = Field(0, example=5000)
    utilities: float = Field(0, example=3000)
    other_fixed: float = Field(0, example=2000)
    risk_level: RiskLevel = RiskLevel.MEDIUM
    goals: list[FinancialGoal] = []


class UserProfile(UserProfileCreate):
    id: str
    created_at: str = ""
    updated_at: str = ""


# ── Transactions ───────────────────────────────────────────────────────
class Transaction(BaseModel):
    id: str = ""
    user_id: str
    amount: float
    category: TransactionCategory
    description: str = ""
    date: str = ""


# ── Financial Plan ─────────────────────────────────────────────────────
class BudgetAllocation(BaseModel):
    category: str
    amount: float
    percentage: float


class SIPSuggestion(BaseModel):
    fund_type: str = ""
    monthly_amount: float = 0
    reasoning: str = ""


class FinancialPlan(BaseModel):
    id: str = ""
    user_id: str
    budget_allocations: list[BudgetAllocation] = []
    total_savings_target: float = 0
    sip_suggestions: list[SIPSuggestion] = []
    summary: str = ""
    created_at: str = ""


# ── Insights ───────────────────────────────────────────────────────────
class SpendingInsight(BaseModel):
    category: str
    spent: float
    budgeted: float
    status: str  # "on_track", "overspent", "under_budget"
    message: str


class InsightsResponse(BaseModel):
    spending_insights: list[SpendingInsight] = []
    investment_advice: str = ""
    sip_suggestions: list[SIPSuggestion] = []
    overall_summary: str = ""


# ── Alerts ─────────────────────────────────────────────────────────────
class Alert(BaseModel):
    id: str = ""
    user_id: str
    severity: AlertSeverity
    title: str
    message: str
    suggested_action: str = ""
    created_at: str = ""
    is_read: bool = False


# ── Dashboard ──────────────────────────────────────────────────────────
class HealthScore(BaseModel):
    score: int = Field(..., ge=0, le=100)
    label: str  # "Excellent", "Good", "Needs Improvement", "Poor"
    breakdown: dict = {}


class ImpactMetrics(BaseModel):
    savings_improvement_pct: float = 0
    overspending_reduction_pct: float = 0
    health_score: int = 0


class DashboardData(BaseModel):
    user: Optional[UserProfile] = None
    plan: Optional[FinancialPlan] = None
    alerts: list[Alert] = []
    insights: Optional[InsightsResponse] = None
    health_score: Optional[HealthScore] = None
    impact_metrics: Optional[ImpactMetrics] = None
    expense_breakdown: dict = {}
    total_spent: float = 0
    total_income: float = 0
