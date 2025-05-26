# 🏛️ Roman History Facts API

A simple, public JSON API that returns a unique Roman history fact for each day of the year. Built with **FastAPI** and easily deployable to any VPS or cloud host.

> Ideal for bots, daily history feeds, educational tools, or curious minds.

---

## 🌐 Live Demo

🚀 [https://your-api-domain.com/today](https://your-api-domain.com/today)

---

## 📘 API Endpoints

### `GET /today`

Get today’s Roman history fact (based on UTC).

**Example Response**:
```json
{
  "date": "05-24",
  "fact": "15 BC – The city of Augusta Vindelicorum (Augsburg) is founded as a Roman military colony in the new province of Raetia."
}
