FROM python:3
MAINTAINER Victor Shamakov <sva1.0@mail.ru>
COPY /classiriers/rest_api
WORKDIR .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py
