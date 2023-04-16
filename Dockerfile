FROM python:3.10
#ENV PYTHONUNBUFFERED 1
RUN mkdir /bookshop_back
WORKDIR /bookshop_back
COPY requirements.txt /bookshop_back/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /bookshop_back/ 