FROM --platform=linux/amd64 python:3.10

WORKDIR /src

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /src

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
