import pandas as pd
import io
import gen_df

# Load or create your DataFrame here
# For demonstration, let's create a sample DataFrame with 10000 rows and 10 columns
# df = pd.DataFrame({'A': range(10000), 'B': range(10000), 'C': range(10000),
#                    'D': range(10000), 'E': range(10000), 'F': range(10000),
#                    'G': range(10000), 'H': range(10000), 'I': range(10000),
#                    'J': range(10000)})

# get df from df generator
df = gen_df.get_df()

# Convert DataFrame to binary representation
buffer = io.BytesIO()
df.to_pickle(buffer)
binary_data = buffer.getvalue()

# Desired chunk size in bytes (approximately 25 megabytes)
chunk_size_bits = 24 * 3840 * 2160
px_chunk_size_bits = 24

# Initialize variables
current_chunk_size = 0
current_chunk = []
chunks = []

# Split the binary data into chunks
chunks = [binary_data[i:i+chunk_size_bits] for i in range(0, len(binary_data), chunk_size_bits)]

# Process or store each chunk as needed
for i, chunk in enumerate(chunks):
    # Do something with each chunk (e.g., process it, save it to a file)
    print(f"Chunk {i + 1}: {len(chunk)} bits")

    px_chunks = [binary_data[i:i + px_chunk_size_bits] for i in range(0, len(binary_data), px_chunk_size_bits)]

    # conv each pixel to video here
    #for px in px_chunks:

