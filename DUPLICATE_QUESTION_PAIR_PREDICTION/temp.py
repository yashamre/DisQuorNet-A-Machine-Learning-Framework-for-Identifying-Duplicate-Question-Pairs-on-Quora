import helper
import pickle

# model = pickle.load(open('model.pkl','rb'))

import pickletools

# Open the pickle file
with open("model1.pkl", "rb") as f:
    # Read the pickle file
    data = f.read()

print(data)
# Optimize the pickle file
optimized_data = pickletools.optimize(data)

# Get the format of the pickle file
format = optimized_data.format

# Print the format of the pickle file
print(format)
