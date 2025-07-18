import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, roc_auc_score, precision_recall_curve, classification_report
from sklearn.preprocessing import TargetEncoder, StandardScaler
from keras import layers, losses
from keras.datasets import fashion_mnist
from keras.models import Model
from scipy.sparse import csr_matrix

transformed_training_data = pd.read_csv('../Dataset/Transformed/Normalised/labelled_transformed_training_data.csv')
transformed_testing_data = pd.read_csv('../Dataset/Transformed/Normalised/labelled_transformed_testing_data.csv')
transformed_validation_data = pd.read_csv('../Dataset/Transformed/Normalised/labelled_transformed_validation_data.csv')

# Get the labels by selecting the 9th column (index 8)
training_labels = transformed_training_data.iloc[:, 6]
testing_labels = transformed_testing_data.iloc[:, 6]
validation_labels = transformed_validation_data.iloc[:, 6]

# Remove the columns 8 and 9 (labels) from the features
training_data = transformed_training_data.drop(columns=[transformed_training_data.columns[6], transformed_training_data.columns[7]])
testing_data = transformed_testing_data.drop(columns=[transformed_testing_data.columns[6], transformed_testing_data.columns[7]])
validation_data = transformed_validation_data.drop(columns=[transformed_validation_data.columns[6], transformed_validation_data.columns[7]])


# Convert the data type to float32 and Tensor
training_data = np.array(training_data, dtype=np.float32)
testing_data = np.array(testing_data, dtype=np.float32)
validation_data = np.array(validation_data, dtype=np.float32)

training_data = tf.constant(training_data)
testing_data = tf.constant(testing_data)
validation_data = tf.constant(validation_data)

# Float32
training_data = tf.cast(training_data, tf.float32)
testing_data = tf.cast(testing_data, tf.float32)
validation_data = tf.cast(validation_data, tf.float32)

# Ensure training_labels, testing_labels, and validation_labels are tensors (if not already)
training_labels = tf.convert_to_tensor(training_labels.astype(bool), dtype=tf.bool)
testing_labels = tf.convert_to_tensor(testing_labels.astype(bool), dtype=tf.bool)
validation_labels = tf.convert_to_tensor(validation_labels.astype(bool), dtype=tf.bool)

# Use tf.boolean_mask to select normal/anomalous data
normal_training_data = tf.boolean_mask(training_data, ~training_labels)
anomalous_training_data = tf.boolean_mask(training_data, training_labels)

normal_testing_data = tf.boolean_mask(testing_data, ~testing_labels)
anomalous_testing_data = tf.boolean_mask(testing_data, testing_labels)

normal_validation_data = tf.boolean_mask(validation_data, ~validation_labels)
anomalous_validation_data = tf.boolean_mask(validation_data, validation_labels)

@tf.keras.utils.register_keras_serializable()
class AnomalyDetector(tf.keras.Model):
    def __init__(self, **kwargs):
        super(AnomalyDetector, self).__init__(**kwargs)
        self.encoder = tf.keras.Sequential([
          # layers.Dense(16, activation="relu"),
          # # Model was overfitting so add dropout layers
          # layers.Dropout(0.2),
          # layers.Dense(8, activation="relu"),
          # layers.Dropout(0.2),
          # layers.Dense(4, activation="relu")

            layers.Dense(32, activation=None),
            layers.BatchNormalization(),
            layers.LeakyReLU(),
            layers.Dropout(0.1),
            layers.Dense(16, activation=None),
            layers.BatchNormalization(),
            layers.LeakyReLU(),
            layers.Dense(8, activation=None),
            layers.BatchNormalization(),
            layers.LeakyReLU()
        ])
    
        self.decoder = tf.keras.Sequential([

            layers.Dense(16, activation=None),
            layers.BatchNormalization(),
            layers.LeakyReLU(),
            layers.Dropout(0.1),
            layers.Dense(32, activation=None),
            layers.BatchNormalization(),
            layers.LeakyReLU(),
            layers.Dense(24)
            
          # layers.Dense(8, activation="relu"),
          # layers.Dropout(0.2),
          # layers.Dense(16, activation="relu"),
          # layers.Dropout(0.1),
          # layers.Dense(24)
        ])
      
    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

    def get_config(self):
        # Return config dictionary; empty because no constructor args
        base_config = super(AnomalyDetector, self).get_config()
        return base_config

    @classmethod
    def from_config(cls, config):
        return cls(**config)


autoencoder = AnomalyDetector()

autoencoder.compile(optimizer='adam', loss='mae')

# Callbacks
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)

reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=5,
    min_lr=1e-6
)

history = autoencoder.fit(normal_training_data, normal_training_data,
          epochs=20,
          batch_size=64, #Number of training samples model processes before updating its weights during training
          validation_data=(validation_data, validation_data),
          callbacks=[early_stopping, reduce_lr],
          shuffle=True)

# Save Model
autoencoder.save('Models/8f_cae_model.keras')

plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.legend()
