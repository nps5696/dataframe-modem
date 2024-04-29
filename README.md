# dataframe-modem
Modulate Data Frames from Panda to Video Frames 

### 1. Code Outline

- `gen_df.py`: Generates a random DataFrame with a specified number of rows and columns.
-  `main.py`: Converts the DataFrame to binary data, splits it into chunks, processes each chunk to create video frames, and then decodes the video back into a DataFrame.
- `rest_df.py`: Demonstrates converting a DataFrame to an RGB image and restoring the DataFrame from the image.
- `type_caster.py`: Contains utility functions for generating random 24-bit sequences, converting bits to RGB color, and vice versa. It also generates a video with random color frames.

### 2. Grammar Used

The code is written in Python and utilizes several libraries and frameworks:

- `pandas`: Used for data manipulation and DataFrame operations.
- `NumPy`: Used for numerical computations and array operations.
- `OpenCV` (cv2): Used for video processing and frame manipulation.
- `Pillow (PIL)`: Used for image processing in `rest_df.py`.

The code follows standard Python syntax and utilizes common programming constructs such as loops, conditionals, and function definitions.

### 3. Evaluation and Interpretation: 

The purpose of this project was to create a Proof of Concept (POC) which successfully demonstrated its intended functionality. The final product is capable of converting a Pandas DataFrame into an image and vice versa. The conversion process involves translating each 24-bit chunk of data into a pixel, sequentially. Given that video generation depends on the size of the data and the available computing power, this process can be time-consuming. 

One potential improvement is to parallelize this process by dividing the source DataFrame not only into pixel chunks but also into frame chunks. This would allow frame generation to occur in parallel across multiple processes, utilizing every physical CPU core available. Such an approach could potentially speed up the process by 8-16 times, depending on the core count of modern CPUs.
Another enhancement could involve encoding and decoding to and from compressed video formats. Instead of using a single pixel—which, if altered, will corrupt the source data—we could replicate the original 24-bit chunk into a square of 10x10 or 100x100 pixels containing the same data. In such case, we could use a simple majority voting system within the square to determine the color, based on the most common value. This assumes that the compression algorithm would alter fewer than half of the pixels, which is typical for video compression. 
The strength of this project lies in its approach to encoding the Pandas DataFrame by using data chunks, which allows us to heavily parallelize the process and enable it to utilize multiple CPU cores.`

### 4. Results and Use Cases: 

The main use case of this code is to demonstrate the feasibility of encoding a DataFrame into a video format and then decoding it back into a DataFrame. This approach could be useful in scenarios where data needs to be stored or transmitted in a visual format, such as for data visualization or communication purposes.
The code also provides an example of converting a DataFrame to an RGB image, which could be useful for visualizing small datasets or for data compression and storage.

Overall, the code serves as a proof of concept for alternative data representation and storage methods, showcasing the flexibility and versatility of Python and its libraries for data manipulation and processing.
