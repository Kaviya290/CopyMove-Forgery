# CopyMove-Forgery

## Project Overview
Copy-Move Forgery is a common type of image tampering where a part of an image is copied and pasted elsewhere within the same image to conceal, replicate, or alter content. This project detects such manipulations using deep learning techniques, including CNN and DenseNet architectures.

## Features
- **Forgery Detection:** Identifies copy-move forgery in images, distinguishing between fake and original images.
- **Deep Learning Models:** Implements both a standard CNN (see `model.py`) and a DenseNet-based classifier (see `DenseModel.py`).
- **Data Preparation:** Processes and organizes images for training and testing.
- **GUI Application:** Provides a user-friendly interface for training models and testing images.
- **Visualization:** Plots accuracy and loss during model training for easy monitoring.

## Getting Started
1. **Prepare Dataset:** Place your images in the `Data` folder, sorted into `Fake` and `Orginal` subfolders.
2. **Training:** Run `model.py` or `DenseModel.py` to train a neural network for forgery detection.
3. **Testing:** Use the GUI (`GUI.py`) to test new images and view results.
4. **Visualization:** Training history is plotted automatically.

## Main Files
- `model.py`: Builds and trains a CNN for detecting image forgery.
- `DenseModel.py`: Implements a DenseNet architecture for improved classification.
- `GUI.py`: Launches a graphical user interface for training and testing.
- `forged.py`: Prepares datasets and labels from the CoMoFoD dataset.
- `Main.py`: Alternate GUI for blood cell classification (may be legacy or demo code).

## Requirements
- Python 3.x
- TensorFlow, Keras, OpenCV, NumPy, Matplotlib, Seaborn, Tkinter

## Example Usage
```bash
python model.py         # Train CNN model
python DenseModel.py    # Train DenseNet model
python GUI.py           # Launch GUI for testing images
```

## Results
After training, the model will classify new images as either "Fake" or "Orginal" and display regions of tampering.

## License
MIT License

---

**Note:** For best results, ensure dataset folders are organized as expected. For more details, review the comments in each script.
