FROM python:3.9-slim
WORKDIR /app
# This line tells Python to print everything immediately
ENV PYTHONUNBUFFERED=1 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
CMD ["python", "main.py"]