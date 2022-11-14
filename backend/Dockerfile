FROM python:3.9.15-alpine3.16
WORKDIR /usr/src/app/backend
COPY . /usr/src/app/backend
RUN . venv/bin/activate
RUN pip install -r requirements.txt
CMD "flask" "--debug" "run" "--host=0.0.0.0"
