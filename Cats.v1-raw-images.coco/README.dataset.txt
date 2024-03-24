# undefined > raw-images
https://public.roboflow.ai/object-detection/undefined

Provided by undefined
License: CC BY 4.0

## About this Dataset
This dataset was created by exporting the [Oxford Pets dataset from Roboflow Universe](https://universe.roboflow.com/brad-dwyer/oxford-pets), generating a version with [Modify Classes](https://docs.roboflow.com/image-transformations/image-preprocessing#modify-classes) to drop all of the classes for the labeled dog breeds and consolidating all cat breeds under the label, "cat." The bounding boxes were also modified to incude the entirety of the cats within the images, rather than only their faces/heads.

![Annotated image of a cat from the dataset](https://i.imgur.com/3IEzlCf.png)

### Oxford Pets
* The Oxford Pets dataset (also known as the "dogs vs cats" dataset) is a collection of images and annotations labeling various breeds of dogs and cats. There are approximately 100 examples of each of the 37 breeds. This dataset contains the object detection portion of the original dataset with bounding boxes around the animals' heads.

* Origin: This dataset was collected by the [Visual Geometry Group](https://www.robots.ox.ac.uk/~vgg/data/pets/) (VGG) at the University of Oxford.