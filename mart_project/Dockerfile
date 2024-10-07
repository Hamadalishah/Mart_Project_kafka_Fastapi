FROM python:3.12

RUN pip install poetry

WORKDIR /app
COPY . /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev 

EXPOSE 8000

CMD [ "poetry","run","uvicorn","mart_project.main:app","--host","0.0.0.0","--reload" ]