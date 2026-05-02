FROM python:3.12-slim

WORKDIR /app

RUN useradd -m -u 10001 appuser

COPY calculator.py /app/calculator.py

USER appuser

CMD ["python", "calculator.py"]
