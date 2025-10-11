FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl libsnappy-dev make gcc g++ libc6-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && ln -s /root/.local/bin/uv /usr/local/bin/uv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY . . 

EXPOSE 8000

# Run the application with uv
CMD ["uv", "run", "uvicorn", "--app-dir", "src", "app:app", "--host", "0.0.0.0", "--port", "8000"]