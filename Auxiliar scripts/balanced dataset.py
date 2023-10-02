import pandas as pd
from imblearn.over_sampling import SMOTE

# Load the dataset
df = pd.read_csv('fer2013.csv')

class_counts = df['emotion'].value_counts()

# Print the class counts
print(class_counts)

# Separate features and target variable
X = df.drop('emotion', axis=1)
y = df['emotion']

# Apply SMOTE to the dataset
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Concatenate the resampled dataframes
df_resampled = pd.concat([X_resampled, y_resampled], axis=1)

# Save the resampled dataset to a new CSV file
df_resampled.to_csv('SMOTE.csv', index=False)



""" import pandas as pd
from sklearn.utils import resample

# Load the dataset
df = pd.read_csv('fer2013.csv')

class_counts = df['emotion'].value_counts()

# Print the class counts
print(class_counts)
# Split the dataset by label
df_0 = df[df['emotion'] == 0] # Angry
df_1 = df[df['emotion'] == 1] # Disgust
df_2 = df[df['emotion'] == 2] # Fear
df_3 = df[df['emotion'] == 3] # Happy
df_4 = df[df['emotion'] == 4] # Sad
df_5 = df[df['emotion'] == 5] # Surprise
df_6 = df[df['emotion'] == 6] # Neutral

# Oversample each label using random over-sampling
df_0_oversampled = resample(df_0, replace=True, n_samples=len(df_3), random_state=42)
df_1_oversampled = resample(df_1, replace=True, n_samples=len(df_3), random_state=42)
df_2_oversampled = resample(df_2, replace=True, n_samples=len(df_3), random_state=42)
df_4_oversampled = resample(df_4, replace=True, n_samples=len(df_3), random_state=42)
df_5_oversampled = resample(df_5, replace=True, n_samples=len(df_3), random_state=42)
df_6_oversampled = resample(df_6, replace=True, n_samples=len(df_3), random_state=42)

# Concatenate all oversampled dataframes
df_oversampled = pd.concat([df_0_oversampled, df_1_oversampled, df_2_oversampled, df_3, df_4_oversampled, df_5_oversampled, df_6_oversampled])

# Save the oversampled dataset to a new CSV file
df_oversampled.to_csv('fer2013_oversampled.csv', index=False) """