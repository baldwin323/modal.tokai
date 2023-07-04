```python
import tensorflow as tf

def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

    return model

def train_model(model, train_data, train_labels):
    model.fit(train_data, train_labels, epochs=5)

def evaluate_model(model, test_data, test_labels):
    model.evaluate(test_data, test_labels, verbose=2)

def predict(model, input_data):
    probability_model = tf.keras.Sequential([
        model,
        tf.keras.layers.Softmax()
    ])

    predictions = probability_model.predict(input_data)

    return predictions
```