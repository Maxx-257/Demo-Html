"""Practical 12: ResNet flower classification with a safe visual fallback."""
from pathlib import Path
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

BASE = Path(__file__).parent

try:
    if os.environ.get("DIP_FORCE_FALLBACK") == "1":
        raise ImportError("Safe fallback mode")

    import tensorflow as tf
    import tensorflow_datasets as tfds

    train_ds, info = tfds.load("tf_flowers", split="train[:10%]", as_supervised=True, with_info=True)
    class_names = info.features["label"].names

    def prepare(image, label):
        image = tf.image.resize(image, (160, 160))
        image = tf.keras.applications.resnet50.preprocess_input(image)
        return image, label

    train_ds = train_ds.map(prepare).batch(32)
    base = tf.keras.applications.ResNet50(weights="imagenet", include_top=False, input_shape=(160, 160, 3))
    base.trainable = False

    model = tf.keras.Sequential([
        base,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(len(class_names), activation="softmax")
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(train_ds, epochs=1, verbose=1)
    print("ResNet flower classification completed.")

    images = []
    titles = []
    for image, label in tfds.load("tf_flowers", split="train[:3]", as_supervised=True):
        images.append(image.numpy())
        titles.append(class_names[int(label)])

except Exception as e:
    print("ResNet unavailable, using a simple flower demo:", type(e).__name__)
    colors = [(220, 80, 80), (80, 180, 80), (80, 100, 220)]
    titles = ["Flower A", "Flower B", "Flower C"]
    images = []
    for petals, color in zip([5, 7, 9], colors):
        img = np.full((180, 180, 3), 245, dtype=np.uint8)
        center = (90, 90)
        for i in range(petals):
            angle = 2 * np.pi * i / petals
            p = (int(90 + 45 * np.cos(angle)), int(90 + 45 * np.sin(angle)))
            cv2.circle(img, p, 25, color, -1)
        cv2.circle(img, center, 22, (40, 200, 230), -1)
        images.append(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.figure(figsize=(9, 3))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis("off")
plt.tight_layout()
plt.savefig(BASE / "output_resnet_flower.png")
if os.environ.get("DIP_TEST_MODE") != "1":
    plt.show()
plt.close()
