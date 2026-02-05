FROM python:3.12@sha256:75c4c2a5e2e1bd7c91c8a7f5e3c5d9e8c4e6f5d9c8e7a6b5c4d3e2f1a0b9c8
LABEL maintainer="Hugo Mrnth <hugo@example.com>"

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt && \
    useradd -m -u 1001 appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
