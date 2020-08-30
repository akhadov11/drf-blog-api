FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /src/
ENTRYPOINT ["/src/entrypoint.sh"]