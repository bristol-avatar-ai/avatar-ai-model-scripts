#Script to train image classification model

import os

import numpy as np

import tensorflow as tf
assert tf.__version__.startswith('2')

from tflite_model_maker import model_spec
from tflite_model_maker import image_classifier
from tflite_model_maker.config import ExportFormat
from tflite_model_maker.config import QuantizationConfig
from tflite_model_maker.image_classifier import DataLoader
from tflite_model_maker.image_classifier import EfficientNetLite4Spec

image_path = os.path.join(os.getcwd(), 'images')

data = DataLoader.from_folder(image_path)
train_data, test_data = data.split(0.9)

model = image_classifier.create(train_data, model_spec='efficientnet_lite4', epochs=20, shuffle=True)
loss, accuracy = model.evaluate(test_data)

model.export(export_dir=image_path)
