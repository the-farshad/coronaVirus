# Alpine base image that contains python 3.10
FROM python:3-slim
# define the directory to work in
WORKDIR /src
# copy the requirements.txt file to the work directory
COPY requirements.txt .
# Install some system deps in a virtual environment named .build-deps, you can name it what ever you want
# install pip dependencies in the same layer
RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt 
# Copy rest of the source code

COPY . .
CMD ["python", "./app.py"]
