FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV $(cat .env | xargs)


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
