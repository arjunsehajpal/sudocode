FROM ubuntu:18.04

RUN mkdir -p /sudoku-solver/



RUN apt-get update && apt-get install -y python3-pip \
    python3-dev \
    git

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

COPY requirements.txt /sudoku-solver/requirements.txt
RUN pip3 install -r /sudoku-solver/requirements.txt

COPY ./ /sudoku-solver/

WORKDIR /sudoku-solver/