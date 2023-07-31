FROM python:3

WORKDIR /project

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
RUN echo "America/Sao_Paulo" > /etc/timezone

COPY . .

ENV SSL_CERT=''
ENV SSL_KEY=''

CMD ["python3", "main.py", "--env=production"]