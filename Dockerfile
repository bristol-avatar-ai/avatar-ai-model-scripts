FROM nvcr.io/nvidia/tensorflow:21.05-tf2-py3
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN apt-get update
RUN pip install tflite-model-maker
RUN pip install numpy==1.21.0
RUN apt-get install -y libusb-1.0-0
COPY ./trainingScript.py /app/trainingScript.py
CMD ["python", "/app/trainingScript.py"]
