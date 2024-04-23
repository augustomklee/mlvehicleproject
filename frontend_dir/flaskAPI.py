from flask import Flask, request, jsonify
import torch
from torchvision import models, transforms
from PIL import Image
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
# Load the pre-trained model
model = models.resnet18(pretrained=False)
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, 8)  # Adjust the final fully connected layer
model.load_state_dict(torch.load('model_state_dict.pth'))
model.eval()  # Set the model to evaluation mode

# Define the image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize images to match model input expectations
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


def split_image(image_path, grid_size, save_dir, margin_ratio=0.1, cond=3):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)  # Create save directory if it doesn't exist

    image = Image.open(image_path)
    image_width, image_height = image.size

    # Calculate margins to be cropped from each side
    x_margin = int(image_width * .03)
    y_margin = int(image_height * .175)

    # Adjust width and height with margins
    adj_width = image_width - (2 * x_margin)  # Subtract the margin from both sides for width
    adj_height = image_height - (2 * y_margin)  # Subtract the margin from both sides for height


    tile_width = adj_width // grid_size[0]
    tile_height = adj_height // grid_size[1]
    if cond ==1:
        for i in range(grid_size[1]):  # Number of rows
            for j in range(grid_size[0]):  # Number of columns
                if i == 2:
                    left = j * tile_width + x_margin
                    top = i * tile_height + (1.2*y_margin)
                    right = left + tile_width
                    bottom = top + (1.05*tile_height)
                elif i==1:
                    left = j * tile_width + x_margin
                    top = i * tile_height + (1.15*y_margin)
                    right = left + (.9*tile_width)
                    bottom = top + (tile_height)
                else:
                    left = j * tile_width + x_margin
                    top = i * tile_height + y_margin
                    right = left + tile_width
                    bottom = top + tile_height

            # Crop the image tile from the adjusted coordinates
                tile = image.crop((left, top, right, bottom))
                tile_name = f'tile_{i}_{j}.jpg'
                tile_path = os.path.join(save_dir, tile_name)
                tile.save(tile_path)

    else:
        for i in range(grid_size[1]):  # Number of rows
            for j in range(grid_size[0]):  # Number of columns
                if i == 2:
                    left = j * tile_width + x_margin
                    top = i * tile_height + (1.2*y_margin)
                    right = left + tile_width
                    bottom = top + (1.05*tile_height)
                elif i==1:
                    left = j * tile_width + x_margin
                    top = i * tile_height + (1.3*y_margin)
                    right = left + (.8*tile_width)
                    bottom = top + (tile_height)
                else:
                    left = j * tile_width + x_margin
                    top = i * tile_height + (1.3 *y_margin)
                    right = left + tile_width
                    bottom = top + tile_height

            # Crop the image tile from the adjusted coordinates
                tile = image.crop((left, top, right, bottom))
                tile_name = f'tile_{i}_{j}.jpg'
                tile_path = os.path.join(save_dir, tile_name)
                tile.save(tile_path)

# Assuming the CAPTCHA is a 3x3 grid
tiles = split_image('highCat.jpg', (3, 3),"sea",3)


@app.route('/api/predict')
def predict():
    class_labels = ['Airplane', 'Bike', 'Boat', 'motorbus', 'motorcycle', 'seaplane', 'train', 'truck']
    predictions = []

    # Iterate over the tiles and predict each one
    for tile_name in os.listdir('otherImgs'):
        if tile_name.endswith('.jpg'):  # Check file extension
            tile_path = os.path.join('otherImgs', tile_name)
            image = Image.open(tile_path).convert('RGB')
            image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

            with torch.no_grad():
                output = model(image_tensor)

            prediction = output.argmax(dim=1).item()
            predictions.append((tile_name, class_labels[prediction]))
    
    return jsonify({'predictions': predictions})

@app.route('/')
def hello():
    return "Hello!"

if __name__ == '__main__':
    app.run(debug=True)
