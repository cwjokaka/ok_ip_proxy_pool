FROM python:3.7
MAINTAINER cwjokaka <cwjokaka@gmail.com>
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
COPY . /code/
#WORKDIR /proxy_app
#COPY . ./
#RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
EXPOSE 8080
#CMD ["python", "main.py"]
