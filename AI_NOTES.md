---

# 📄 2️⃣ AI_NOTES.md


# 🤖 AI Usage Notes – Backend

## 📌 Overview

AI was used during development to assist with:

- Project structure design
- API architecture planning
- Prompt engineering refinement
- Deployment troubleshooting
- Error debugging
- Tailwind and frontend styling guidance

---

## 🧠 LLM Used in Application

### Provider:
OpenAI

### Model:
GPT-4o-mini

### Why This Model?

- Cost-efficient for structured text generation
- Good reasoning ability for breaking features into user stories and engineering tasks
- Fast response time
- Reliable Markdown formatting output

---

## 🛠 What AI Was Used For During Development

- Designing REST API structure
- Suggesting database schema
- Refining prompts for structured output
- Improving UX patterns
- Debugging Render deployment errors
- Troubleshooting Supabase connection issues
- Writing documentation

---

## 🔍 What Was Checked Manually

- Database connection validity
- Proper environment variable handling
- Correct API routing
- CORS configuration
- LLM API integration
- Deployment configuration (Render)
- Frontend-backend communication
- Cold start behavior

All deployment and runtime errors were manually verified through logs.

---

## 🎯 Design Decisions Verified Manually

- Environment-based API URL configuration
- Proper IPv4 Supabase connection for Render
- Password URL encoding
- Database model correctness
- Health endpoint accuracy
- API endpoint behavior

---

## ⚠️ AI Limitations Considered

- LLM output may vary slightly between runs
- Risk of hallucinated tasks if constraints are unclear
- Output is not validated against strict schema

Manual review was used to confirm logical structure of generated tasks.