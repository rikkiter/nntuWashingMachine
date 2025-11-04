FROM python:3.13-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy dependency files
COPY poetry.lock pyproject.toml ./

# Install all dependencies (including dev)
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy project
COPY . .

# For development with auto-reload
CMD ["python", "app/main.py"]