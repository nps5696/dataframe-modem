import numpy as np
import cv2
import random


# Function to generate a random 24-bit sequence
def generate_random_bits(length=24):
    return ''.join(str(random.randint(0, 1)) for _ in range(length))


# Function to convert a 24-bit sequence into RGB color
def bits_to_color(bits):
    # Split the 24-bit sequence into three 8-bit chunks for red, green, and blue channels
    red = bits[0:8]
    green = bits[8:16]
    blue = bits[16:24]

    # Convert each 8-bit chunk to integer value
    red_int = int(red, 2)
    green_int = int(green, 2)
    blue_int = int(blue, 2)

    # Return the RGB color tuple
    return (blue_int, green_int, red_int)  # OpenCV uses BGR instead of RGB


# Function to convert RGB color to 24-bit sequence
def color_to_bits(color):
    # Extract the red, green, and blue components from the color tuple
    red, green, blue = color

    # Convert each color component to 8-bit binary representation
    red_bits = format(red, '08b')
    green_bits = format(green, '08b')
    blue_bits = format(blue, '08b')

    # Concatenate the binary representations to form a 24-bit sequence
    bits = red_bits + green_bits + blue_bits

    return bits


# Generate frames and save them as images
num_frames = 100  # Number of frames for the video
frame_width = 3840  # Width of each frame (4K resolution)
frame_height = 2160  # Height of each frame (4K resolution)
fps = 30  # Frames per second

# Define the output video file
video_filename = 'color_animation.avi'
video_fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video_out = cv2.VideoWriter(video_filename, video_fourcc, fps, (frame_width, frame_height))

# Generate and write frames to the video
for _ in range(num_frames):
    # Create a blank frame with 4K resolution
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

    # Fill the frame with random colors
    for row in range(frame_height):
        for col in range(frame_width):
            color = bits_to_color(generate_random_bits())
            frame[row, col] = color

    # Write the frame to the video
    video_out.write(frame)

# Release the video writer
video_out.release()

print("Video saved successfully.")
