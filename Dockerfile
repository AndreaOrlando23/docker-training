## base image to start
FROM python:3.6.13

## install the dependencies
RUN pip install -U Flask

# Copy your application to the image
COPY app.py /myapp/app.py
WORKDIR /myapp

## when execute the container the following commands are executed
ENTRYPOINT ["python3", "app.py"]
