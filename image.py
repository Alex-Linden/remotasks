import numpy as np
from PIL import Image

class MyImage:
    def __init__(self, image_name, description, date_created):
        self.image_name = image_name
        self.description = description
        self.date_created = date_created

    def get_image_name(self):
        return self.image_name

    def get_description(self):
        return self.description

    def get_date_created(self):
        return self.date_created

    def get_average_color(self):
        # Load the image as a Numpy array
        img = np.array(Image.open(self.image_name))
        # Convert to RGB format (if necessary) and get the pixel values
        pixels = img[:, :, :3].reshape(-1, 3)
        # Get average color
        avg_color = np.mean(pixels, axis=0)
        return avg_color

# Create an instance of the Image class, setting the attributes
my_image = MyImage(image_name = "image_123.jpg", description = "A picture of a sunset", date_created = "02/06/2024")

avg_color = my_image.get_average_color()
print(f"Average color is: {avg_color}")