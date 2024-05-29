import sys
sys.path.append("..")
import onnxruntime as ort
from decouple import config
import json
# Load classes from the JSON file
with open('./src/assets/classes.json', 'r') as file:
    classes_json = json.load(file)

CLASSES = classes_json['classes']

class Model:
    def __init__(self):
        providers = ['CUDAExecutionProvider', 'CPUExecutionProvider'] if config('device') == 'cuda' else ['CPUExecutionProvider']
        self.model = ort.InferenceSession(config('model'), providers=providers)

session = Model()
