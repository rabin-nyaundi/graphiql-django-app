FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# RUN apt install -y  apturl

COPY . .

EXPOSE 8060


CMD ["python","manage.py","runserver","0.0.0.0:8000"]

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]