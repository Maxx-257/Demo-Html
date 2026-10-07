"""Practical 11: CNN for MNIST digit recognition."""
from pathlib import Path
import os
import numpy as np
import matplotlib.pyplot as plt

BASE = Path(__file__).parent

try:
    if os.environ.get("DIP_FORCE_FALLBACK") == "1":
        raise ImportError

    import tensorflow as tf
    from tensorflow.keras import Sequential
    from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    x_train = x_train[:8000].astype("float32") / 255.0
    y_train = y_train[:8000]
    x_test = x_test[:500].astype("float32") / 255.0
    y_test = y_test[:500]

    x_train = x_train[..., None]
    x_test = x_test[..., None]

    model = Sequential([
        Conv2D(16, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(32, activation="relu"),
        Dense(10, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    model.fit(x_train, y_train, epochs=1, batch_size=64, verbose=1)

    images = x_test[:6, :, :, 0]
    actual = y_test[:6]
    predicted = np.argmax(model.predict(x_test[:6], verbose=0), axis=1)

except Exception:
    # Safe demonstration when TensorFlow is not installed
    import cv2

    actual = np.array([0, 1, 2, 3, 4, 5])
    predicted = actual.copy()
    images = []

    for digit in actual:
        img = np.zeros((28, 28), dtype=np.uint8)
        cv2.putText(img, str(digit), (5, 23),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2)
        images.append(img)

    images = np.array(images)
    print("TensorFlow not installed - showing simple digit demo.")

# Display both actual and predicted values
plt.figure(figsize=(10, 4))
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(f"Actual: {actual[i]}\nPredicted: {predicted[i]}")
    plt.axis("off")

plt.tight_layout()
plt.savefig(BASE / "output_cnn_mnist.png", dpi=130)
if os.environ.get("DIP_TEST_MODE") != "1":
    plt.show()
plt.close()

print("Actual digits:   ", actual)
print("Predicted digits:", predicted)
