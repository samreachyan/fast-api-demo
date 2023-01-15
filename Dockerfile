FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /code

COPY ./requirements.txt ./

RUN python3 -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "9090", "--reload"]