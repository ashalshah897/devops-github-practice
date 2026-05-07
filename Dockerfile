#FROM python:3.12-slim

#WORKDIR /app

#RUN useradd -m -u 10001 appuser

#COPY calculator.py /app/calculator.py

#USER appuser

#CMD ["python", "calculator.py"]
FROM python:3.12-slim

WORKDIR /app

# Install the Waiter (Flask)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy EVERYTHING (including the templates folder!)
COPY . .

# Use a safe user (Good for DevSecOps!)
RUN useradd -m -u 10001 appuser
USER appuser

# Open the window for the website
EXPOSE 5000

CMD ["python", "calculator.py"]
