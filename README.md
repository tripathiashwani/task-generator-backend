# 🚀 Tasks Generator – Backend

## 📌 Required Project Files

This repository includes:

- `README.md` — Setup instructions and project overview
- `AI_NOTES.md` — Explanation of AI usage in development
- `ABOUTME.md` — Author information and resume
- `PROMPTS_USED.md` — Prompts used during development (without responses or API keys)

---

## ⚙️ How to Run Locally

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=your_database_url
OPENAI_API_KEY=your_openai_key
```

---

### 3️⃣ Run the Server

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

## 📦 API Endpoints

### `POST /generate/`

Generate structured user stories and engineering tasks.

---

### `GET /specs/`

Retrieve the last 5 generated specifications.

---

### `GET /health/`

Check backend and LLM configuration status.

---

## ✅ Features Implemented

- LLM-powered task generation
- Structured prompt design
- Database persistence
- History retrieval (last 5 specs)
- Health check endpoint
- Environment-based configuration
- CORS middleware support
- Deployed on Render

---

## ⚠️ Not Implemented / Known Limitations

- No authentication
- No user-specific specification storage
- No pagination
- No rate limiting
- No advanced request validation schema
- No automated tests
- No structured JSON output from LLM (currently Markdown output)
- No background job queue

---

## 🌍 Deployment

Backend is deployed on:

- **Render** (Web Service)
- **Supabase** (PostgreSQL Database)

---

### ⚠️ Note

Render free tier may experience cold start delays.