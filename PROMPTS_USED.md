# 📝 Prompts Used – Backend

This file documents the core prompts used during application development.

No API keys or agent responses are included.

---

## 🔹 Primary Task Generation Prompt

```text
You are a senior product manager and software architect.

Generate:

- User stories
- Engineering tasks grouped by frontend/backend/database
- Risks and unknowns

Goal:
{goal}

Users:
{users}

Constraints:
{constraints}

Template:
{template_type}

Output in clean Markdown format.
```

---

## 🔹 Enhanced Version (Structured Emphasis)

```text
You are an experienced SaaS architect.

Break down the following feature idea into:

- Clear user stories (role-based format)
- Frontend engineering tasks
- Backend engineering tasks
- Database tasks
- Risks and unknowns

Be practical, realistic, and production-aware.

Goal:
{goal}

Users:
{users}

Constraints:
{constraints}

Template:
{template_type}

Output must be structured and grouped clearly.
```

---

## 🔹 Health Endpoint Prompt (Internal Use)

Not applicable — the health endpoint does not use an LLM.

---

## 🔹 Prompt Design Principles

- Role-based user stories
- Clear separation of frontend/backend/database
- Production-aware risks
- Markdown formatting
- Concise but structured output
- Avoid over-engineering
- Encourage scalability awareness