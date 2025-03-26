FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ENV PYTHONPATH="/app"

# Copy the project code
COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["python", "app.py"]
