FROM python:3.9.7-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["streamlit_app.py", "model.pickle", "./"]

EXPOSE 5000

ENTRYPOINT ["streamlit", "run", "--server.port", "5000", "streamlit_app.py"]
