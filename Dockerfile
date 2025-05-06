# 1. Use official Python image
FROM python:3.12.2-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set work directory
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copy project files into container
COPY . .

# 6. Expose port (Django default)
EXPOSE 8000

# 7. Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
