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

## Running it

Two UIs currently exist, side by side, both driving the same generator core:

**Streamlit** (original):
```
streamlit run app.py
```

**FastAPI + HTMX** (new -- server-rendered, no build tooling, meant to
grow into something brandable if this becomes a product):
```
uvicorn web.main:app --reload
```
Run from the project root in both cases, after `pip install -r requirements.txt`.