# ML Vehicle Image CAPTCHA Project


## Team Members
- Stewart Geisz
- Arnav Chahal
- Zack Silver
- Augusto Lee

## Project Overview
In our Machine Learning Final Report, we aimed to process and distinguish vehicles from images in the style of a CAPTCHA. The motivation behind our work is to explore the challenges that computers face in solving problems that are typically easy for humans, and to gain a deeper understanding of machine learning systems.

## Dataset
Our dataset comprised images of various vehicle types. We performed an analysis on the distribution of image types and their corresponding counts.


## Preprocessing
For our neural network to process the images effectively, we standardized our data by:
- Resizing images to 224x224 pixels
- Normalizing color values from a range of 0-255 to 0-1

## Model Training and Evaluation
We experimented with different architectures and hyperparameters, using an 80/20 split for training and testing to evaluate the model's performance. We monitored accuracy, precision, recall, and F1 score.

### CNN with ResNet-18
Our best-performing model was a CNN using ResNet-18 architecture. The model was trained from scratch on the HCaptcha dataset over 20 epochs, achieving a final accuracy of 95.10% on our testing data.


## Comparison with Other Models
We compared our approach with similar datasets and competitions found on Kaggle. Our custom-built CNN performed competitively with top models, achieving comparable accuracies. We also discussed the potential advantages of incorporating transfer learning in future work.

## Ethics in Machine Learning
We discussed the ethical implications of training models that could potentially bypass CAPTCHA security, recognizing the balance between advancing technology and maintaining responsible use.

## Conclusion
Our project successfully identified CAPTCHA images of vehicles with an impressive accuracy rate. Although not perfect, our model demonstrated the capability to solve CAPTCHAs in many cases, which could prompt improvements in CAPTCHA technology.

## Future Work
For future enhancement, we would consider applying transfer learning, testing our model in real-world CAPTCHA scenarios, and exploring further ethical considerations.

## Contributions
- **Zack Silver:** Data preprocessing and management
- **Arnav Chahal:** Neural network implementation and optimization
- **Stewart Geisz:** Research on image processing techniques and project coordination
- **Augusto Lee:** Repository management and data visualization

## Bibliography
- TensorFlow Core Image classification
- Neural Networks in Python
- Object Detection Algorithms and Libraries

## Repository
[GitHub Project Repository](https://github.com/gutoleeofficial/mlvehicleproject)

---

_Disclaimer: The provided project link is fictional and for demonstration purposes only._
