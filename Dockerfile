FROM python:3.9-slim
USER root
COPY . /cs-archiver
WORKDIR /cs-archiver

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    && apt-get -y install wget

RUN wget https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb -O packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && rm packages-microsoft-prod.deb

RUN apt-get install -y apt-transport-https \
  &&  apt-get update \
  &&  apt-get install -y dotnet-sdk-6.0

RUN chgrp -R 0 /cs-archiver \
    && chmod -R g=u /cs-archiver \
    && pip install pip --upgrade \
    && pip install -r requirements.txt

CMD python3 slash_archive.py