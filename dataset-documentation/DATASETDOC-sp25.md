
# Project Information

**What is the project name?**  
Season Watch

**What is the link to your project’s GitHub repository?**  
https://github.com/BU-Spark/ds-seasonwatch-trees

**What is the link to your project’s Google Drive folder?**  
https://drive.google.com/drive/folders/1uetBj6p5mk_EkASibqyaJgvsCDm7-J7r

**In your own words, what is this project about? What is the goal of this project?**  
Season Watch collects citizen-submitted data on the seasonal behavior (leafing, flowering, fruiting) of trees in India. Rapid climate change has caused shifts in these behaviors, making the historical reference database less reliable. This project aims to analyze these shifts using environmental factors (temperature, precipitation, soil moisture, urbanization) and update validation frameworks for future citizen science contributions.

**Who is the client for the project?**  
Season Watch

**Who are the client contacts for the project?**  
Geetha Ramaswami ([LinkedIn](https://www.linkedin.com/in/geetha-ramaswami/))

**What class was this project part of?**  
DS539

# Dataset Information

**What data sets did you use in your project?**  
- Citizen-submitted observations (2015–2023)
- Nighttime lights data (NASA Black Marble)
- UN Population Density Data (2020)
- Precipitation datasets (weekly resolution)
- Soil moisture datasets

**Links to datasets:**  
- GitHub: https://github.com/BU-Spark/ds-seasonwatch-trees/tree/data-analysis/data/Fall%202024%20data
- Drive: https://drive.google.com/drive/folders/1uetBj6p5mk_EkASibqyaJgvsCDm7-J7r

**Data Dictionary:**  
Provided inside the Drive folder (Fall 2024 Final Deliverables).

**Keywords/Tags:**  
- Domains: Time-Series Analysis, Climate Impact Studies, Geospatial Analysis
- Application Areas: Sustainability, Environmental Science, Civic Tech

---

# Dataset Details

**Motivation**  
To monitor and correct shifts in tree phenology over time due to climate change and urbanization impacts.

**Composition**  
- Tabular data
- Each row: one observation of a tree's leafing, flowering, or fruiting state
- Fields include: Date, Species, Latitude/Longitude, Phenology metrics
- 571,834 total observations

**Instance Sampling**  
No sampling — complete citizen-contributed database.

**Data Characteristics**  
- Includes both raw and cleaned versions.
- Some errors originally existed but were cleaned.

**Recommended Splits**  
No official splits (future users can create based on year, species, or region).

**Errors or Noise**  
- Minimal post-cleaning
- Remaining minor observational inconsistencies are expected in citizen science projects.

**External Dependencies**  
- None.

**Confidentiality**  
- No sensitive information.
- Publicly available.

**Identification Risks**  
- No PII (Personally Identifiable Information).

**Dataset Snapshot**  

| Attribute | Value |
|:---|:---|
| Size of dataset | ~571,834 instances |
| Number of fields | ~15-20 per dataset |
| Labeled classes | Leafing, Flowering, Fruiting states (0–2) |
| Number of labels | 3 main phenophases × 3 stages each |

---

# Collection Process

**Mechanisms**  
- Citizen-science reporting via Season Watch platform.
- Additional environmental datasets from NASA and UN sources.

**Timeframe**  
- 2015–2023 for citizen observations
- 2020+ for environmental layers

**Sampling Strategy**  
- No sampling, full dataset.

---

# Preprocessing / Cleaning / Labeling

**Preprocessing Steps**  
- State name corrections based on geocoordinates.
- Outlier detection (Isolation Forest).
- Handling missing coordinates and dates.

**Transformations**  
- None major beyond cleaning and normalization.

**Raw Data Availability**  
- Raw and cleaned datasets available on GitHub and Google Drive.

**Code for Cleaning**  
- https://github.com/BU-Spark/ds-seasonwatch-trees/tree/data-analysis/code/Fall%202024%20Code

---

# Uses

**Tasks Done**  
- Time-series modeling of tree phenology shifts
- Visualization of seasonal onset shifts
- Clustering analysis based on urbanization
- Survival analysis for transition times

**Possible Future Tasks**  
- Deep learning predictive modeling
- Expansion to more species and regions
- Phenophase prediction under future climate scenarios

**Limitations**  
- Geographical bias toward Kerala (may not fully represent pan-India behavior)

**Tasks Not Recommended**  
- Individual tree-specific modeling (data is too coarse-grained).

---

# Distribution

**Access Type**  
- Open Access

---

# Maintenance

**Extension Mechanisms**  
- Users can extend existing Jupyter notebooks and scripts from the GitHub repository.

---

# Other Notes

None beyond information provided above.
