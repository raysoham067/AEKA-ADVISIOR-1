# Weekend Getaway Ranker

A data-driven Python application that helps you find the best weekend destinations in India based on multiple factors including Google reviews, visit duration, entrance fees, and accessibility.

## Overview

This project ranks Indian tourist destinations to help users find the perfect weekend getaway. It uses a scoring algorithm that considers various factors to recommend the top 5 destinations based on your source city.

## Features

- **Smart Ranking Algorithm**: Uses weighted scoring based on multiple factors
- **Comprehensive Dataset**: Includes popular tourist destinations across India
- **Multiple Criteria**: Considers Google ratings, reviews, time needed, cost, and accessibility
- **Top 5 Recommendations**: Provides the best weekend destinations ranked by score

## Scoring Algorithm

The final score is calculated using the following weighted formula:

- **35%** - Google Review Rating (0-5 scale)
- **35%** - Number of Google Reviews (in lakhs)
- **15%** - Time Score (inverse of time needed - shorter visits score higher)
- **10%** - Cost Score (inverse of entrance fee - lower costs score higher)
- **5%** - Airport Accessibility (1 if airport within 50km, 0 otherwise)

## Dataset

The project uses a CSV file (`Top Indian Places to Visit .csv`) containing information about various tourist destinations including:

- City and location details
- Visit duration (in hours)
- Google review ratings and review counts
- Entrance fees (in INR)
- Airport accessibility
- DSLR camera permissions
- Best time to visit
- And more...

## Requirements

- Python 3.x
- pandas library

## Installation

1. Clone or download this repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install pandas
   ```

## Usage

### Using Jupyter Notebook

1. Open `Weekend_Getaway_Ranker.ipynb` in Jupyter Notebook or Google Colab
2. Update the CSV file path if needed (default: `/content/Top Indian Places to Visit.csv` for Colab)
3. Run all cells
4. Enter your source city when prompted
5. View the top 5 ranked destinations

### Using Python Script

1. Run the Python script:
   ```bash
   python weekend_getaway_ranker.py
   ```
2. Enter your source city when prompted

## Output

The application displays the top 5 weekend destinations with the following information:

- Destination Name
- City
- Time needed to visit (in hours)
- Google review rating
- Entrance fee (in INR)
- Number of Google reviews (in lakhs)
- Airport accessibility (within 50km)
- DSLR camera allowed
- Best time to visit
- Final Score

## Example Outputs

Sample outputs for different source cities are available in the `outputs/` directory:
- `output_mumbai.txt` - Top destinations from Mumbai
- `output_delhi.txt` - Top destinations from Delhi
- `output_bangalore.txt` - Top destinations from Bangalore

## Project Structure

```
Weekend Getaway Ranker/
│
├── Weekend_Getaway_Ranker.ipynb    # Main Jupyter notebook
├── Top Indian Places to Visit .csv # Dataset
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
├── generate_outputs.py             # Script to generate outputs for multiple cities
└── outputs/                         # Sample output files
    ├── output_mumbai.txt
    ├── output_delhi.txt
    └── output_bangalore.txt
```

## How It Works

1. **Data Loading**: Loads the CSV dataset containing tourist destination information
2. **Filtering**: Filters out destinations in the same city as the source
3. **Feature Engineering**: Creates normalized scores for time, cost, and accessibility
4. **Scoring**: Calculates a weighted final score for each destination
5. **Ranking**: Sorts destinations by final score and displays top 5

## Notes

- The algorithm excludes destinations in the same city as your source
- Scores are normalized to ensure fair comparison across different metrics
- The ranking prioritizes popular and highly-rated destinations while considering practical factors like time and cost

## License

This project is open source and available for educational purposes.

## Author

Created as part of a college project for ranking weekend getaway destinations in India.

