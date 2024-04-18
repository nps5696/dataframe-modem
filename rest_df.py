# Load the image
import pandas as pd
from PIL import Image
import numpy as np

# Example DataFrame
data = {'A': [0, 255], 'B': [128, 200], 'C': [64, 30]}
print("Original data:", data)
df = pd.DataFrame(data)

# Normalize or scale data (if necessary)
# Here we assume data is already in 0-255 range for simplicity

# Convert DataFrame to RGB values array
rgb_array = df.to_numpy(dtype=np.uint8).reshape((1, len(df), 3))

# Create image
img = Image.fromarray(rgb_array, 'RGB')
img.save('data_image.png')


img_loaded = Image.open('data_image.png')

# Convert image to NumPy array
data_array = np.array(img_loaded)

# Reshape and convert to DataFrame
restored_df = pd.DataFrame(data_array.reshape(-1, 3), columns=['A', 'B', 'C'])

print("Restored data:", restored_df)
