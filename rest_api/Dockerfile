FROM python:3
MAINTAINER Victor Shamakov <sva1.0@mail.ru>
COPY . /docker
WORKDIR /docker
RUN pip install -r requirements.txt
EXPOSE 9999
CMD python ./api.py
