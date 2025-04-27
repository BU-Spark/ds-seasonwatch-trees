# Season Watch: Spring 2025  
Behavior of Trees under Climate Change

## Project Overview

This project, in collaboration with **Season Watch** (a citizen science initiative in India), analyzes how trees' seasonal behavior — flowering, fruiting, and leafing (phenology) — is changing in response to urbanization, temperature, soil moisture, and precipitation.  

The objective was to detect shifts over time by comparing citizen-submitted tree data against historical references and environmental factors, aiming to update validation protocols and reference databases accordingly.

---

## Repository Structure

```
spring_2025_code/
  ├── urban_data_cleaning.ipynb              # Cleans urbanization datasets (population density, night lights)
  ├── clustering_with_urbanization.ipynb     # DBSCAN clustering analysis with urbanization features
  ├── precipitation_analysis.ipynb           # Analyzes the relationship between precipitation and phenology
  ├── urban_vs_non_urban.ipynb                # Compares tree behaviors between urban and rural areas
  ├── temperature_analysis/
  │    └── temperature_analysis_v2.ipynb     # Examines how temperature affects phenophase presence
  ├── soil_moisture/
  │    ├── soil_moisture_analysis.ipynb       # Evaluates soil moisture impacts (including lagged effects)
  │    └── mango_phenophase_soilmoisture_summary.csv # Pre-computed soil moisture summary for Mango species
  ├── join_euclidean.py                       # Utility script for nearest-neighbor spatial joins
```

---

## How to Set Up and Run the Code

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd spring_2025_code
   ```

2. **Install dependencies**:
   The project mainly uses Python 3.10+ and the following libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn geopandas shapely
   ```

3. **Prepare the data**:
   - Ensure you have access to the cleaned citizen observation and environmental datasets (soil moisture, temperature, precipitation, night lights, population density).
   - Place these datasets into an appropriate `data/` subfolder (create if missing).

4. **Running the code**:
   Open each `.ipynb` notebook in Jupyter Lab or VSCode and run all cells.
   - **Urbanization Analysis**: Start with `urban_data_cleaning.ipynb`, then `clustering_with_urbanization.ipynb`.
   - **Urban vs Rural Comparison**: Run `urban_vs_non_urban.ipynb`.
   - **Temperature Analysis**: Run `temperature_analysis/temperature_analysis_v2.ipynb`.
   - **Soil Moisture Analysis**: Run `soil_moisture/soil_moisture_analysis.ipynb`.
   - **Precipitation Analysis**: Run `precipitation_analysis.ipynb`.
   - **Spatial Joins**: Use `join_euclidean.py` if you need to spatially match trees to environmental grids.

---

## Blockers Faced and Solutions

| Blocker | Solution |
| :--- | :--- |
| Difficulty joining phenology data with environmental grids due to differing resolutions | Created a spatial nearest-neighbor join utility (`join_euclidean.py`) |
| Monthly resolution of soil moisture data mismatched tree event timings | Implemented lagged analyses and shifted phenology event dates |
| Sparse or missing precipitation data for some regions | Focused analysis primarily on Kerala region where data density was high |
| Urban vs rural distinction was ambiguous using population thresholds | Incorporated both population density and nighttime light radiance as proxies |
| Lack of statistical significance in clustering results | Augmented clusters with auxiliary environmental variables for richer analysis |

---

## Future Work for the Next Student Team

### Short-Term Improvements
- **Extend Time Series Modeling**: Integrate urbanization into temporal models instead of static clustering.
- **Expand Species-Specific Models**: Develop phenology models for more sensitive species individually.
- **Enhance Clustering**: Tune DBSCAN hyperparameters further, or test hierarchical clustering (HDBSCAN).

### Longer-Term Goals
- **Nationwide Expansion**: Apply models to all India regions beyond Kerala.
- **Reference Database Update**: Use model outputs to create updated seasonal calendars for citizen science validation.
- **Interactive Visualization Dashboard**: Deploy a Looker Studio, Streamlit, or PowerBI dashboard allowing dynamic filtering by species, location, and year.
- **Multivariate Environmental Modeling**: Analyze how temperature, soil moisture, and precipitation interact together rather than separately.

---

## Contact

- **Client**: Geetha Ramaswami — [geetha@ncf-india.org](mailto:geetha@ncf-india.org)
- **Program Manager**: Makayla Tajalle — [mtajalle@bu.edu](mailto:mtajalle@bu.edu)

---

## Acknowledgments

This project was completed as part of the **Spring 2025 SPARK! DS539** course at Boston University, under the mentorship of Spark! advisors and in collaboration with the National Centre for Biological Sciences (NCBS), India.

---

