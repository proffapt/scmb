FROM python:3.11.8

# Configure IST Timezone
ENV TZ="Asia/Kolkata"

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

COPY models/ ./models/

COPY database/ ./database/

COPY middleware/ ./middleware/

COPY api/ ./api/

EXPOSE 8000

CMD [ "flask", "run", "--host=0.0.0.0", "--port", "8000" ]