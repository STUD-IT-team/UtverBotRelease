FROM python:3.12-alpine

RUN rm -rf /opt/venv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./src/requirements.txt .
COPY ./src/*.py .

RUN mkdir creds
COPY ./creds/credentials.json creds

RUN mkdir data
COPY ./data/* data

RUN pip install -r requirements.txt

EXPOSE 3012

CMD ["python3.12", "./bot.py"]
