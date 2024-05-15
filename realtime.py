import pandas as pd

# Tạo DataFrame mẫu
data = {
    'Column1': ['A', 'B', 'A', 'C', 'B'],
    'Column2': ['X', 'Y', 'X', 'X', 'Z'],
    'Column3': [1, 2, 1, 3, 1]
}

df = pd.read_csv("data.csv")

import pandas as pd

# Tính Gini Index cho một tập dữ liệu
def calculate_gini_index(data):
    total_samples = len(data)
    if total_samples == 0:
        return 0

    class_counts = data.value_counts()
    probabilities = class_counts / total_samples
    gini = 1 - sum(probabilities ** 2)

    return gini

# Tính Gini Index Gain cho một cột dựa trên một cột đích (target column)
def calculate_gini_index_gain(data, feature_column, target_column):
    gini_full_dataset = calculate_gini_index(data[target_column])

    unique_values = data[feature_column].unique()
    gini_gain = 0
    for value in unique_values:
        subset = data[data[feature_column] == value]
        subset_weight = len(subset) / len(data)
        subset_gini = calculate_gini_index(subset[target_column])
        gini_gain += subset_weight * subset_gini

    gini_index_gain = gini_full_dataset - gini_gain
    return gini_index_gain

# Tạo DataFrame mẫu


# Tính Gini Index Gain cho từng cột
for column in df.columns:
    if column != 'Buys computer':
        gini_index_gain = calculate_gini_index_gain(df, column, 'Buys computer')
        print(f"Gini Index Gain for column '{column}': {gini_index_gain}")
