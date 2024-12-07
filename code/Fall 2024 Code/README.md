# SeasonWatch Project

## Overview
The SeasonWatch Project aims to analyze the phenological changes in tree species in India, with a focus on Kerala, using citizen-science data collected from 2015 to 2023. The project examines the relationship between climate change and tree phenology by identifying trends, seasonal shifts, and geographic variations. Our final deliverables include visualizations, statistical analyses, and code that can be reused for similar ecological studies.

## Objectives
1. **Analyze phenological changes:** Investigate how trees respond to climate change and seasonal transitions.
2. **Identify key patterns:** Focus on the timing of phenological stages (leaves, flowers, fruits) for the top 30 observed tree species.
3. **Visualize shifts:** Create interactive and static visualizations to convey changes in onset weeks, geographic clustering, and seasonal variability.
4. **Provide reusable tools:** Develop and share scripts, cleaned datasets, and workflows for future analysis.

---

## Deliverables
### 1. Data Cleaning and Preparation
- **Input Data:**
  - Citizen-submitted observations from SeasonWatch (2015–2023).
  - ~177 species with detailed phenological stage observations.
- **Cleaned Data:**
  - Filtered dataset with accurate geocoding, standardized state names, and adjusted missing values.
  - Historical (pre-2020) and comparative (post-2020) datasets for reference.

### 2. Visualizations
- **Interactive Visualizations:** Created with Flourish Studio, including:
  - Seasonal shifts in onset weeks.
  - Geographic clustering of phenological stages.
- **Static Visuals:** Heatmaps, time-series plots, and summary tables saved to:
  `/data/VISUALIZATIONS-fall 2024/Kerala Visuals`

### 3. Statistical Analysis
- Summary statistics, regression analysis, and survival modeling to answer base questions:
  - How are trees changing due to climate change?
  - What is the onset timing for flowering and fruiting in tropical species?
  - What is the probability of transitioning between seasonal states?

### 4. Final Report
- Comprehensive document with:
  - Visualizations.
  - Interpretations of patterns and trends.
  - Recommendations for conservation efforts.
  - Delivered in PDF format.

---

## Getting Started
### Prerequisites
1. **Python Environment:**
   - Python 3.9 or higher.
   - Required libraries:
     - `pandas`
     - `numpy`
     - `matplotlib`
     - `geopandas (v0.9.0)`
     - `shapely (v2.0.1)`
     - `googlemaps`
     - `seaborn`
2. **Geospatial Tools:**
   - Shapefiles available in `india_map` folder for geographic visualizations.
   - Google Maps API key for geocoding (optional).
3. **Data Files:**
   - Cleaned datasets stored in the `/data` directory.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/seasonwatch-project.git
   cd seasonwatch-project
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```
3. Download the cleaned datasets and place them in the `/data` directory.

### Running the Code
1. **Data Cleaning:**
   ```bash
   python scripts/data_cleaning.py
   ```
   Cleans raw observation data, standardizes formats, and generates cleaned datasets.

2. **Geocoding:**
   If using Google Maps API, update your API key in `config.py`:
   ```python
   GOOGLE_API_KEY = 'your-api-key'
   ```
   Run geocoding script:
   ```bash
   python scripts/geocoding.py
   ```

3. **Visualization Generation:**
   Generate visuals:
   ```bash
   python scripts/visualizations.py
   ```
   Outputs saved in `/data/VISUALIZATIONS-fall 2024`.

4. **Statistical Analysis:**
   Perform analyses and generate summary tables:
   ```bash
   python scripts/analysis.py
   ```

---

## Directory General Structure
```
seasonwatch-project/
├── data/
│   ├── raw_data.csv
│   ├── cleaned_data.csv
│   ├── VISUALIZATIONS-fall 2024/
│   │   ├── Kerala Visuals/
│   │   └── ...
├── scripts/
│   ├── data_cleaning.py
│   ├── geocoding.py
│   ├── visualizations.py
│   └── analysis.py
├── india_map/
│   ├── shapefiles/
│   └── ...
├── README.md
├── requirements.txt
└── config.py
```

---

## Contributors
- 
- **Team Members:** Cecily Wang-Munoz, Aditya Chopra, An Ngo (Sue), Brenda Kim

---

## Acknowledgments
This project uses data from SeasonWatch and insights from the SeasonWatch tree phenology handbook. Special thanks to BU SPARK for supporting the project.
