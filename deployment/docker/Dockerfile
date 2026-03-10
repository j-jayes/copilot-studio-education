FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir uv

CMD ["uv", "run", "--directory", "./mcp-servers/public-api-demo", "public-api-demo"]
