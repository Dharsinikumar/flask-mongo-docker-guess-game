# 1️⃣ Use official Python image
FROM python:3.11-slim

# 2️⃣ Set working directory inside the container
WORKDIR /app

# 3️⃣ Install system dependencies (needed for some Python packages like pymongo)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4️⃣ Copy requirements.txt first (caching step for faster builds)
COPY requirements.txt .

# 5️⃣ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6️⃣ Copy the rest of the app code
COPY . .

# 7️⃣ Expose the port Flask will run on
EXPOSE 5000

# 8️⃣ Set the command to run the Flask app
# Replace 'app:app' if your Flask entrypoint is named differently
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
