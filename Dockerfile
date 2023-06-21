FROM python:3.11.4-alpine
LABEL authors="boristoboltsov"

ENV TZ="Europe/Moscow"

WORKDIR /knowledge_support

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements_dev.txt
RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime
RUN echo "Europe/Moscow" > /etc/timezone

CMD ["python", "main.py"]
