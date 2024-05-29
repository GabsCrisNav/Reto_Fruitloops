from PIL import Image
import json
import cv2
import random
import numpy as np
from .upload_model import session
import matplotlib.pyplot as plt

from decouple import config

# Load classes from the JSON file
with open('./src/assets/classes.json', 'r') as file:
    classes_json = json.load(file)

CLASSES = classes_json['classes']
colors = {name:[random.randint(0, 255) for _ in range(3)] for i,name in enumerate(CLASSES)}

# Load and preprocess the image
def load_and_preprocess_image(image_path, input_shape):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (input_shape[3], input_shape[2]))
    image = np.transpose(image, (2, 0, 1))  # Change data layout from HWC to CHW
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = image.astype(np.uint8)
    return image

# Visualize the predictions
def visualize_predictions(image, num_detections, pred_boxes, pred_scores, pred_classes, class_names, confidence_score = 0.5):
    #plt.figure(figsize=(10, 10))
    #plt.imshow(image)
    results = []
    num_detections = int(num_detections[0])  # Convert to integer
    for i in range(num_detections):
        
        x_min, y_min, x_max, y_max = pred_boxes[0, i]
        confidence = pred_scores[0, i]
        class_id = int(pred_classes[0, i])
        
        if confidence > confidence_score:  # Only visualize predictions with confidence > 0.5
            color = (0, 255, 0)
            cv2.rectangle(image, (int(x_min), int(y_min)), (int(x_max), int(y_max)), color, 2)
            label = f"{class_names[class_id]}: {confidence:.2f}"
            results.append([class_names[class_id], int(confidence*100)])
            cv2.putText(image, label, (int(x_min), int(y_min) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    
    if len(results) < 1:
        results = [['nothing',0]]
    
    return results
    
    #plt.imshow(image)
    #plt.axis('off')
    #plt.show()

def get_class(im, conf_needed=0.8):
    
    inputs = [o.name for o in session.model.get_inputs()]
    outputs = [o.name for o in session.model.get_outputs()]

    input_image = load_and_preprocess_image(im, (1, 3, 640, 640))

    predictions = session.model.run(outputs, {inputs[0]: input_image})

    num_detections, pred_boxes, pred_scores, pred_classes = predictions
    print(conf_needed)
    results = visualize_predictions(input_image[0].transpose(1, 2, 0), num_detections, pred_boxes, pred_scores, pred_classes, CLASSES, conf_needed)

    return results