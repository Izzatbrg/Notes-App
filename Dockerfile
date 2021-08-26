# pull official base image
FROM python:3.6-buster

# set work directory
WORKDIR D:/users/Desktop/Notes-app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .

CMD ["python", "UI.py"]