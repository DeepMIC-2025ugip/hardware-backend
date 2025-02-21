FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv pip

COPY pyproject.toml poetry.lock* ./
RUN uv pip install --system --no-cache-dir --requirements pyproject.toml

COPY . .

ENV PYTHONPATH=src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
