# Roman History Facts API

A simple public API that returns a daily or date-specific Roman history fact.

## Endpoints

- `/today` — Get today's fact based on UTC
- `/fact?date=MM-DD` — Get a fact for a specific date

## Usage

Run locally with:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
# roman-history-api
