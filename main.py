import pandas as pd
import io
import cv2
import numpy as np
import gen_df
import type_caster


# get df from df generator
df = gen_df.get_df()
# Convert DataFrame to CSV string
csv_data = df.to_csv(index=False)

# Convert CSV string to binary data
binary_data = csv_data.encode()

# Convert DataFrame to binary representation
buffer = io.BytesIO()
df.to_pickle(buffer)
buffer.seek(0)
binary_data = buffer.getvalue()

# Desired chunk size in bytes (approximately 25 megabytes)
chunk_size_bits = 24 * 1280 * 720
px_chunk_size_bits = 24

# Initialize variables
current_chunk_size = 0
current_chunk = []
chunks = []

# Dimensions for video frames
frame_height = type_caster.frame_height
frame_width = type_caster.frame_width

# Split the binary data into chunks
chunks = [binary_data[i:i+chunk_size_bits] for i in range(0, len(binary_data), chunk_size_bits)]

video_out = type_caster.video_out

# Process or store each chunk as needed
for i, chunk in enumerate(chunks):
    frame = np.zeros((frame_height,frame_width, 3), dtype = np.uint8)
    pixel_index = 0
    for y in range(frame_height):
        for x in range(frame_width):
            if pixel_index < len(chunk) - 2:
                # Store Pixel as Blue, Green, Red
                B = chunk[pixel_index]
                G = chunk[pixel_index+1]
                R = chunk[pixel_index+2]
                frame[y, x] = [B, G, R]
                pixel_index += 3
    video_out.write(frame)
    print(f"Frame {i  + 1} writen to video")

video_out.release()
print("Created Video successfully")
# Do something with each chunk (e.g., process it, save it to a file)
print(f"Chunk {i + 1}: {len(chunk)} bits")

# Decode video back into the Dataframe

# Read video
video_path = 'color_animation.avi'
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print('Could not open video file')
    exit()

# Collect binary data
binary_data = bytearray()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Convert each frame to binary data
    for row in frame:
        for pixel in row:
            B, G, R = pixel
            binary_data.append(B)
            binary_data.append(G)
            binary_data.append(R)
cap.release()

# Convert binary data to a NumPy array
array_data = np.frombuffer(binary_data, dtype=np.uint8)

# Reshape the array to match the original DataFrame shape
num_rows = len(binary_data) // (3 * len(df.columns))
array_data = array_data.reshape(num_rows, 3 * len(df.columns))

# Create a DataFrame from the reshaped array
df_restored = pd.DataFrame(array_data)

print(df_restored.head())













