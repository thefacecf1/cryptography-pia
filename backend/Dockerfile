FROM python:3.10.6
WORKDIR /usr/src/app/backend
COPY . /usr/src/app/backend
RUN pip install -r requirements.txt
CMD "flask" "--debug" "run" "--host=0.0.0.0"
