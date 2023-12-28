FROM ubuntu:latest
LABEL authors="joaomartins"

ENTRYPOINT ["top", "-b"]

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
WORKDIR /exercise_devoteam
COPY . /exercise_devoteam
#RUN pip --no-cache-dir install -r requirements.txt
#RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install poetry fastapi uvicorn
RUN poetry install

#ENTRYPOINT ["python3", "src/main.py"]
EXPOSE 8000
ENTRYPOINT ["uvicorn", "src.main:app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]
