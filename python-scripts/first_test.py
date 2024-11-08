# Test our Python environment and installed packages
print("Testing Python environment...")

# Test NumPy
import numpy as np
array = np.array([1, 2, 3, 4, 5])
print("\nNumPy test:")
print(f"Created array: {array}")
print(f"Array mean: {array.mean()}")

# Test Pandas
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Paris', 'London', 'New York']
}
df = pd.DataFrame(data)
print("\nPandas test:")
print(df)

print("\nAll tests completed successfully!")