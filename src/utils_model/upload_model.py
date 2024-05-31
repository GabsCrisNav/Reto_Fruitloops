import sys
sys.path.append("..")
import onnxruntime as ort
import boto3
from decouple import config
import json
# Load classes from the JSON file
with open('./src/assets/classes.json', 'r') as file:
    classes_json = json.load(file)

CLASSES = classes_json['classes']

class Model:
    def __init__(self):
        s3_client = boto3.client('s3', aws_access_key_id=config('access-key'), aws_secret_access_key=config('secret-access-key'))
        response = s3_client.get_object(Bucket=config('bucket'), Key=config('model'))
        object_content = response['Body'].read()
        providers = ['CUDAExecutionProvider', 'CPUExecutionProvider'] if config('device') == 'cuda' else ['CPUExecutionProvider']
        self.model = ort.InferenceSession(object_content, providers=providers)

session = Model()
