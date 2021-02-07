FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev


COPY . /newscrawler

WORKDIR C:\Users\julie\Desktop\ESIEE_Paris\E4\Cours\Data_Engineering\Projet\ChrismasMoviesScrapper


RUN pip install Flask==0.10.1
RUN pip install elasticsearch==7.1.0

COPY . /ChrismasMoviesScrapper
ADD . .


CMD [ "python", "chrismasMovies.py" ]