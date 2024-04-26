import pandas as pd
import numpy as np

def get_df():
    # Define the number of rows and columns to generate
    num_rows = 10  # 1 million rows
    num_cols = 10    # 100 columns

    # Create a DataFrame with random data
    data = np.random.rand(num_rows, num_cols)
    df = pd.DataFrame(data, columns=[f'Column_{i}' for i in range(num_cols)])

    # Calculate the size of the DataFrame in megabytes
    size_mb = df.memory_usage(deep=True).sum() / (1024 * 1024)

    print(f"Size of the DataFrame: {size_mb:.2f} megabytes")

    return df