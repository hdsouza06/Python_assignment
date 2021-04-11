FROM python:3.6

WORKDIR /app

COPY requirements.txt /app/

#COPY ./models/. /app/

COPY ./*.py /app/

COPY ./* ./app

RUN pip install -r requirements.txt

EXPOSE 8040


CMD ["uvicorn", "Ziro_todo_main:app", "--host=0.0.0.0", "--port=8040", "--reload" ]





