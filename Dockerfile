FROM python:3.13-slim as builder

ENV POETRY_VERSION=2.1.3
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . .

CMD ["python", "app/main.py"]