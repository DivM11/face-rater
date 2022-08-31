# Steps
## Install Python

## install requirements
```sh
pip install requirements.txt
```

## Run the app
```sh
streamlit run app.py
```
Navigate to `http://localhost:8501` to access the app.

### Optional Step for Ubuntu users
```
apt-get install ffmpeg libsm6 libxext6 -y
```

## Building with docker
```
docker build -t face-rater .
```

After build, one can run the container using:
```
docker run -p 8501:8501 face-rater
```
Navigate to `http://localhost:8501` to access the app.

## Optional Steps
## unzip files
Normal unzipper takes time use the inbuilt python package to unzip all the files and store in a separate directory
```sh
python unzip_data.py
```

## convert pts to txt
```sh
cd SCUT-FBP5500_v2
python pts2txt.py
cd ..
```