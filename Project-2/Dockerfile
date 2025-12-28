FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files safely
COPY . .

# Create directories and move files if they exist
RUN mkdir -p templates static
RUN [ -f index.html ] && mv index.html templates/ || true
RUN [ -f "Project-2_Architecture_Diagram.png" ] && mv "Project-2_Architecture_Diagram.png" static/ || true

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
