"""
Database layer – Firebase Firestore with local JSON fallback.

If FIREBASE_CREDENTIALS_PATH is set and valid, uses Firestore.
Otherwise, falls back to a local JSON file for easy hackathon demos.
"""

from __future__ import annotations

import json
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

load_dotenv()

# ── Globals ────────────────────────────────────────────────────────────
_firestore_db = None
_use_firestore = False
_LOCAL_DB_PATH = Path(__file__).parent / "local_db.json"


def _init_firebase():
    global _firestore_db, _use_firestore
    cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
    if cred_path and Path(cred_path).exists():
        try:
            import firebase_admin
            from firebase_admin import credentials, firestore

            if not firebase_admin._apps:
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)
            _firestore_db = firestore.client()
            _use_firestore = True
            print("✅ Connected to Firebase Firestore")
        except Exception as e:
            print(f"⚠️  Firebase init failed ({e}), using local JSON fallback")
            _use_firestore = False
    else:
        print("ℹ️  No Firebase credentials found, using local JSON fallback")
        _use_firestore = False


_init_firebase()


# ── Local JSON helpers ─────────────────────────────────────────────────
def _load_local() -> dict:
    if _LOCAL_DB_PATH.exists():
        return json.loads(_LOCAL_DB_PATH.read_text(encoding="utf-8"))
    return {"users": {}, "transactions": {}, "plans": {}, "alerts": {}}


def _save_local(data: dict):
    _LOCAL_DB_PATH.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")


def _gen_id() -> str:
    return uuid.uuid4().hex[:12]


# ── CRUD: Users ────────────────────────────────────────────────────────
def save_user(user_data: dict) -> str:
    uid = user_data.get("id") or _gen_id()
    user_data["id"] = uid
    now = datetime.utcnow().isoformat()
    user_data.setdefault("created_at", now)
    user_data["updated_at"] = now

    if _use_firestore:
        _firestore_db.collection("users").document(uid).set(user_data)
    else:
        db = _load_local()
        db["users"][uid] = user_data
        _save_local(db)
    return uid


def get_user(uid: str) -> dict | None:
    if _use_firestore:
        doc = _firestore_db.collection("users").document(uid).get()
        return doc.to_dict() if doc.exists else None
    else:
        return _load_local()["users"].get(uid)


def list_users() -> list[dict]:
    if _use_firestore:
        return [d.to_dict() for d in _firestore_db.collection("users").stream()]
    else:
        return list(_load_local()["users"].values())


# ── CRUD: Transactions ────────────────────────────────────────────────
def save_transactions(user_id: str, txns: list[dict]):
    if _use_firestore:
        batch = _firestore_db.batch()
        for t in txns:
            t["id"] = t.get("id") or _gen_id()
            t["user_id"] = user_id
            ref = _firestore_db.collection("transactions").document(t["id"])
            batch.set(ref, t)
        batch.commit()
    else:
        db = _load_local()
        if user_id not in db["transactions"]:
            db["transactions"][user_id] = []
        for t in txns:
            t["id"] = t.get("id") or _gen_id()
            t["user_id"] = user_id
        db["transactions"][user_id].extend(txns)
        _save_local(db)


def get_transactions(user_id: str) -> list[dict]:
    if _use_firestore:
        docs = (
            _firestore_db.collection("transactions")
            .where("user_id", "==", user_id)
            .stream()
        )
        return [d.to_dict() for d in docs]
    else:
        return _load_local()["transactions"].get(user_id, [])


def clear_transactions(user_id: str):
    if _use_firestore:
        docs = (
            _firestore_db.collection("transactions")
            .where("user_id", "==", user_id)
            .stream()
        )
        batch = _firestore_db.batch()
        for d in docs:
            batch.delete(d.reference)
        batch.commit()
    else:
        db = _load_local()
        db["transactions"][user_id] = []
        _save_local(db)


# ── CRUD: Plans ────────────────────────────────────────────────────────
def save_plan(plan_data: dict) -> str:
    pid = plan_data.get("id") or _gen_id()
    plan_data["id"] = pid
    plan_data["created_at"] = datetime.utcnow().isoformat()

    if _use_firestore:
        _firestore_db.collection("plans").document(pid).set(plan_data)
    else:
        db = _load_local()
        db["plans"][plan_data["user_id"]] = plan_data
        _save_local(db)
    return pid


def get_plan(user_id: str) -> dict | None:
    if _use_firestore:
        docs = (
            _firestore_db.collection("plans")
            .where("user_id", "==", user_id)
            .order_by("created_at", direction="DESCENDING")
            .limit(1)
            .stream()
        )
        for d in docs:
            return d.to_dict()
        return None
    else:
        return _load_local()["plans"].get(user_id)


# ── CRUD: Alerts ───────────────────────────────────────────────────────
def save_alerts(user_id: str, alerts: list[dict]):
    if _use_firestore:
        batch = _firestore_db.batch()
        for a in alerts:
            a["id"] = a.get("id") or _gen_id()
            a["user_id"] = user_id
            ref = _firestore_db.collection("alerts").document(a["id"])
            batch.set(ref, a)
        batch.commit()
    else:
        db = _load_local()
        if user_id not in db["alerts"]:
            db["alerts"][user_id] = []
        for a in alerts:
            a["id"] = a.get("id") or _gen_id()
            a["user_id"] = user_id
        db["alerts"][user_id].extend(alerts)
        _save_local(db)


def get_alerts(user_id: str) -> list[dict]:
    if _use_firestore:
        docs = (
            _firestore_db.collection("alerts")
            .where("user_id", "==", user_id)
            .stream()
        )
        return [d.to_dict() for d in docs]
    else:
        return _load_local()["alerts"].get(user_id, [])


def clear_alerts(user_id: str):
    if _use_firestore:
        docs = (
            _firestore_db.collection("alerts")
            .where("user_id", "==", user_id)
            .stream()
        )
        batch = _firestore_db.batch()
        for d in docs:
            batch.delete(d.reference)
        batch.commit()
    else:
        db = _load_local()
        db["alerts"][user_id] = []
        _save_local(db)
