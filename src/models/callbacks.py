import datetime

import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import ReduceLROnPlateau

from config import MODEL_TENSORBOARD_DIR, MODEL_CHECKPOINTER_DIR

# Initialize tensorboard
log_dir = MODEL_TENSORBOARD_DIR + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Initialize model checkpointer
checkpoint = ModelCheckpoint(MODEL_CHECKPOINTER_DIR, monitor='val_loss', verbose=1, save_best_only=True)

# reduce on plateu
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=20, verbose=1, mode='auto', min_lr=0.0000001)
