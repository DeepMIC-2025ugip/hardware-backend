#/bin/bash

PYTHONPATH=src uv run uvicorn src.main:app --reload
