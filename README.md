# Windchill REST Service Generator

## Version 1.0

Generates Windchill REST Service projects automatically.

### Features

- Generates config JSON
- Generates Domain JSON
- Generates import.js
- Generates import.json
- Generates Java Helper
- Generates Output Schema
- Placeholder-based templates
- Shared Folder deployment support

Status: Version 1.0 (UI Generation Complete)

## UI stack decision (final, 2026-08-27)

**FastAPI + Jinja2 + HTMX is the product direction going forward.** Not
Flutter, and not Streamlit long-term. Reasoning:

- The generator engine (`core/`, `config/`, `models/`) is Python and stays
  Python regardless of frontend choice. A Flutter frontend wouldn't remove
  a language from this project, it would add one (Dart) on top of the
  Python already required for the engine -- keeping the frontend in Python
  too (via Jinja2/HTMX) keeps the whole stack in one language.
- This may be sold to other companies doing Windchill customization as a
  product, not just used personally. A buyer evaluating a tool like this
  expects a fast, ordinary web page -- not an app-like Flutter Web load,
  which has already caused real problems in an unrelated project
  (HomeBee's Vendor Portal: heavy cold-load, less "webby").
- Streamlit is fine for an internal tool but has real ceilings for a
  brandable, multi-tenant product (hard to skin, rerun-on-every-interaction
  model doesn't fit SaaS well).

**Streamlit (`app.py`) stays for now as a fallback only**, until the
FastAPI+HTMX UI has actually been run and verified end-to-end (it hasn't
yet -- built and reviewed, but not executed, since no Python interpreter
was available on the machine it was built on). Remove `app.py` and the
`streamlit` dependency once the FastAPI UI is confirmed working.

## Running it

**Streamlit** (fallback, until the FastAPI UI is verified):
```
streamlit run app.py
```

**FastAPI + HTMX** (the product direction):
```
uvicorn web.main:app --reload
```
Run from the project root in both cases, after `pip install -r requirements.txt`.