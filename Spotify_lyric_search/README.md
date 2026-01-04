# Spotify Lyric Search

A machine learning project that predicts the artist and song based on lyric snippets using deep learning and TF-IDF similarity matching.

## Overview

This project uses a neural network model trained on Spotify song lyrics to:
- **Predict the artist** from a given lyric snippet using a TensorFlow/Keras model
- **Find the matching song** using TF-IDF vectorization and cosine similarity

The model achieves **99.70% accuracy** on artist prediction when tested on 1000 random samples from the dataset.

## Features

- 🎵 Artist prediction from lyrics using a deep learning model
- 🎶 Song matching using TF-IDF and cosine similarity
- 📊 Trained on 50,000 songs from 642 different artists
- 🔍 High accuracy prediction system

## Dataset

The project uses the **Spotify Million Song Dataset** (`Spotify Million Song Dataset_exported.csv`) containing:
- Artist names
- Song titles
- Song lyrics (text)

## Project Structure

```
Spotify_lyric_search/
├── Spotify Million Song Dataset_exported.csv    # Dataset file
├── Spotify_Lyric_Search.ipynb                  # Jupyter notebook with full implementation
├── spotify_lyric_search.py                     # Python script
└── README.md                                   # This file
```

## Requirements

Install the required dependencies:

```bash
pip install pandas tensorflow scikit-learn numpy
```

Or create a `requirements.txt` with:
```
pandas>=1.5.0
tensorflow>=2.10.0
scikit-learn>=1.0.0
numpy>=1.21.0
```

## Model Architecture

The neural network model consists of:
- **Text Vectorization Layer**: Converts lyrics to numerical sequences (max 30,000 tokens, sequence length 200)
- **Embedding Layer**: 64-dimensional embeddings
- **Global Average Pooling**: Reduces sequence to fixed-size vector
- **Dense Layers**: 
  - 128 neurons with ReLU activation
  - Output layer with softmax activation (642 classes for artists)

## Usage

### Using the Jupyter Notebook

1. Open `Spotify_Lyric_Search.ipynb` in Jupyter Notebook or Google Colab
2. Update the CSV file path in the first cell if needed
3. Run all cells to train the model
4. Use the `predict_artist_song()` function to search for songs:

```python
predict_artist_song()
# Enter lyrics snippet when prompted
```

### Example

```
Enter lyrics snippet: Look at her face it's a wonderful face

Predicted Artist: Foreigner
Predicted Song: Face To Face
```

## Model Training

The model is trained with:
- **Training set**: 40,000 samples (80%)
- **Validation set**: 10,000 samples (20%)
- **Epochs**: 5
- **Batch size**: 128
- **Optimizer**: Adam
- **Loss function**: Sparse categorical crossentropy

## Evaluation

The model evaluation function tests accuracy on 1000 random samples:
- **Artist Accuracy**: 99.70%

## How It Works

1. **Data Preprocessing**: 
   - Loads dataset and filters out songs with missing lyrics
   - Samples 50,000 songs for training
   - Encodes artist names to numerical IDs

2. **Model Training**:
   - Vectorizes lyrics using TensorFlow's TextVectorization
   - Trains a neural network to classify artists from lyrics

3. **Prediction**:
   - Uses the trained model to predict the artist from input lyrics
   - Filters the dataset to songs by the predicted artist
   - Uses TF-IDF and cosine similarity to find the best matching song

## Technologies Used

- **Python**: Programming language
- **TensorFlow/Keras**: Deep learning framework
- **scikit-learn**: Machine learning utilities (TF-IDF, cosine similarity)
- **pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing

## Notes

- The dataset path in the notebook is set to `/content/` (Google Colab path). Update it to your local path if running locally.
- The model samples 50,000 songs for faster training. You can adjust this number in the notebook.
- For better accuracy, consider training for more epochs or using a larger dataset.

## License

This project is for educational purposes.

## Author

College project - Spotify Lyric Search

