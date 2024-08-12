import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Assuming the test set is organized similarly to the training set
test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
    'test_data',
    target_size=(64, 64),
    batch_size=32,
    class_mode='sparse'
)

# Load the trained model
model = tf.keras.models.load_model('exercise_model.h5')

# Evaluate the model
loss, accuracy = model.evaluate(test_generator)
print(f'Test accuracy: {accuracy}, Test loss: {loss}')
