FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
RUN chmod +x start.sh
CMD ["python", "-m", "bot.main"]
