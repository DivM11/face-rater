# base image
FROM ubuntu:22.04

# apt-get packages
RUN apt-get update -y && apt-get install ffmpeg libsm6 libxext6 -y

# Installing python
RUN apt-get install python3-pip -y

# Installing python packages
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copying all the code and data
COPY . face-rater/.

# Expose port for to be access externally
EXPOSE 8501

# Change dir to app folder
WORKDIR /face-rater/

# RUN CMD
CMD ["streamlit", "run", "app.py", "--server.port", "8501"]