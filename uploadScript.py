import ibm_boto3
from ibm_botocore.client import Config, ClientError

def read_config(file_path):
    config_dict = {}
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if '=' not in line:
                    continue
                key, value = line.strip().split('=')
                config_dict[key] = value
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    return config_dict

file_path = 'config.properties'
config = read_config(file_path)

if config is not None:
    COS_ENDPOINT = config.get('dbEndpointURL')
    COS_API_KEY_ID = config.get('dbAPIKey')
    COS_AUTH_ENDPOINT = "https://iam.cloud.ibm.com/identity/token"
    COS_SERVICE_CRN = config.get('dbServiceInstanceID')
    COS_BUCKET = config.get('dbBucketName')
    USERNAME = config.get('vmUsername')

    # Create resource
    cos = ibm_boto3.resource("s3",
        ibm_api_key_id=COS_API_KEY_ID,
        ibm_service_instance_id=COS_SERVICE_CRN,
        ibm_auth_endpoint=COS_AUTH_ENDPOINT,
        config=Config(signature_version="oauth"),
        endpoint_url=COS_ENDPOINT
    )

    def upload_file(bucket_name, item_name, file_path):
        try:
            print("Starting file upload")
            with open(file_path, "rb") as file_data:
                cos.Object(bucket_name, item_name).upload_fileobj(file_data)
            print("Upload complete")
        except Exception as e:
            print(f"An error occurred while uploading: {e}")

    upload_file(COS_BUCKET, 'model.tflite', f'/home/{USERNAME}/images/model.tflite')

