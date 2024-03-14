FROM python:3.11.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

COPY api/ ./api/

COPY models/ ./models/

COPY database/ ./database/

EXPOSE 8000

CMD [ "flask", "run", "--host=0.0.0.0", "--port", "8000", "--debug" ] # TODO: Disable debug mode