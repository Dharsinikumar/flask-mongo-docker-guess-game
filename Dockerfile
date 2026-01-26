FROM python:3.9-alpine
WORKDIR /app
COPY app.py .
RUN pip install -r requirements.txt
EXPOSE 6000
CMD ["python", "app.py"]
