#!/bin/bash

# Argument: VM username
USERNAME=$1

#Get bucket name
BUCKET=$(grep -w "cloudBucketName" /home/${USERNAME}/config.properties | cut -d'=' -f2)

# Download uploaded images from the Cloud Bucket
gsutil cp gs://${BUCKET}/images.zip .

# Unzip the file and rename the resulting directory to 'images'
unzip images.zip -d temp_folder
mv temp_folder/* images
rm -r temp_folder

# Start the Docker container
docker run --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 -v /home/${USERNAME}/images:/app/images --gpus all recognition

#Save newly created model externally
python uploadScript.py

#Remove images
rm images.zip
rm -rf images/

# Shutdown the machine
sudo shutdown now
