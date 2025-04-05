FROM python:3.9

WORKDIR /app

# Copy requirements.txt first
COPY app/requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY app/ .

CMD ["python", "app.py"]