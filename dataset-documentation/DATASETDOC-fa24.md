**Project Information**  

- What is the project name?

  - Season Watch

<!-- -->

- **What is the link to your project\'s GitHub repository? Please
  provide the link below.**

  - https://github.com/BU-Spark/ds-seasonwatch-trees

<!-- -->

- **What is the link to your project's Google Drive folder? \*\*This
  should be a Spark! Owned Google Drive folder - please contact your PM
  if you do not have access\*\***

  - https://drive.google.com/drive/folders/1uetBj6p5mk_EkASibqyaJgvsCDm7-J7r

<!-- -->

- **In your own words, what is this project about? What is the goal of
  this project?**

  - Season Watch uses a reference database to flag errors in
    citizen-submitted data on tree phenology (leafing, flowering, and
    fruiting times). However, due to rapid climate changes, trees are
    experiencing seasonal phases earlier or later than expected, meaning
    citizen inputs may not necessarily be inaccurate. To address this,
    Season Watch seeks to assess and understand shifts in seasonal
    behavior by comparing citizen-submitted observations with the
    historical reference database. The aim is to identify discrepancies,
    infer actual shifts over a decade, and update the reference database
    to enhance its accuracy and reliability.

<!-- -->

- Who is the client for the project?

  - Season Watch

<!-- -->

- Who are the client contacts for the project?

  - Geetha Ramaswami, Program Manager -
    [[LinkedIn](https://www.linkedin.com/in/geetha-ramaswami/)]{.underline}

<!-- -->

- **What class was this project part of?**

  - DS549  
      
    **Dataset Information**  

<!-- -->

- What data sets did you use in your project? Please provide a link to
  the data sets, this could be a link to a folder in your GitHub Repo,
  Spark! owned Google Drive Folder for this project, or a path on the
  SCC, etc.

  - https://github.com/BU-Spark/ds-seasonwatch-trees/tree/data-analysis/data/Fall%202024%20data

<!-- -->

- **What keywords or tags would you attach to the data set?**

  - Domain(s) of Application:** **Data Validation and Correction,
    Time-Series Analysis, Machine Learning for Pattern Recognition,
    Power BI for Visualization and Insights

  - Phenology Analysis, Climate-Induced Shifts, Citizen Science Data,
    Reference Database Updates, Tree Seasonal Patterns  
      
    **Motivation**

<!-- -->

- For what purpose was the dataset created? Was there a specific task in
  mind? Was there a specific gap that needed to be filled? Please
  provide a description.

  - The dataset was provided to us by the client and was cleaned in
    order to ensure that all the datapoints were within India, aswell as
    ensure that any unfilled values that could've been filled with API
    can be corrected.  
      
    **Composition**  

<!-- -->

- **What do the instances that comprise the dataset represent (e.g.,
  documents, photos, people, countries)? Are there multiple types of
  instances (e.g., movies, users, and ratings; people and interactions
  between them; nodes and edges)? What is the format of the instances
  (e.g., image data, text data, tabular data, audio data, video data,
  time series, graph data, geospatial data, multimodal (please specify),
  etc.)? Please provide a description.**

  - The instances (rows) represent citizen-submitted observations of
    tree phenology (e.g., leafing, flowering, and fruiting stages) for
    different tree species.

  - nstance Type: There is only one type of instance---phenology
    observations for trees.

  - Instance Format: Tabular data with fields like date, species name,
    geographic location (latitude, longitude), and phenological metrics.

<!-- -->

- **How many instances are there in total (of each type, if
  appropriate)?**

  - The dataset contains 571,834 instances (rows)

<!-- -->

- **Does the dataset contain all possible instances or is it a sample
  (not necessarily random) of instances from a larger set?**

  - Contains everything

<!-- -->

- What data does each instance represent?

  - Species Information: Species name and ID.

  - Phenological Stages: Metrics for leaves, flowers, and fruits at
    different stages.

  - Geographical Data: Latitude, longitude, and state name.

  - Temporal Information: Date, year, and week of observation.

<!-- -->

- **Are there recommended data splits (e.g., training,
  development/validation, testing)?**

  - There is no splits

<!-- -->

- **Are there any errors, sources of noise, or redundancies in the
  dataset?**

  - Errors should be corrected

<!-- -->

- Is the dataset self-contained, or does it link to or otherwise rely on
  external resources?

  - The dataset is self-contained.

<!-- -->

- **Are there any restrictions (e.g., licenses, fees) associated with
  any of the external resources that might apply to a dataset consumer?
  Please provide descriptions of all external resources and any
  restrictions associated with them, as well as links or other access
  points as appropriate.**

  - No restrictions

<!-- -->

- Does the dataset contain data that might be considered confidential
  (e.g., data that is protected by legal privilege or by doctor-patient
  confidentiality, data that includes the content of individuals'
  non-public communications)? If so, please provide a description

  - No it is publically available

<!-- -->

- **Does the dataset contain data that, if viewed directly, might be
  offensive, insulting, threatening, or might otherwise cause anxiety?
  If so, please describe why.**

  - No

<!-- -->

- Is it possible to identify individuals (i.e., one or more natural
  persons), either directly or indirectly (i.e., in combination with
  other data) from the dataset? If so, please describe how.

  - No  
      
    **Collection Process**  

<!-- -->

- What mechanisms or procedures were used to collect the data (e.g.,
  API, artificially generated, crowdsourced - paid, crowdsourced -
  volunteer, scraped or crawled, survey, forms, or polls, taken from
  other existing datasets, provided by the client, etc)? How were these
  mechanisms or procedures validated?

  - Dataset was given to us by our client, Google API was used in order
    to correct the values, aswell as Python code to remove/correct some
    values.

<!-- -->

- **If the dataset is a sample from a larger set, what was the sampling
  strategy (e.g., deterministic, probabilistic with specific sampling
  probabilities)?**

  - It is not

<!-- -->

- **Over what timeframe was the data collected? Does this timeframe
  match the creation timeframe of the data associated with the instances
  (e.g., recent crawl of old news articles)? If not, please describe the
  timeframe in which the data associated with the instances was
  created.**

  - 2015 to 2023  
      
    Preprocessing/cleaning/labeling  

<!-- -->

- Was any preprocessing/cleaning/labeling of the data done (e.g.,
  discretization or bucketing, tokenization, part-of-speech tagging,
  SIFT feature extraction, removal of instances, processing of missing
  values)? If so, please provide a description. If not, you may skip the
  remaining questions in this section.

  - Correction of states from Coordinates

  - Removal of coordinates outside India

  - Outlier detection using isolation forest

<!-- -->

- **Were any transformations applied to the data (e.g., cleaning
  mismatched values, cleaning missing values, converting data types,
  data aggregation, dimensionality reduction, joining input sources,
  redaction or anonymization, etc.)? If so, please provide a
  description.**

  - No  
      

<!-- -->

- Was the "raw" data saved in addition to the
  preprocessed/cleaned/labeled data (e.g., to support unanticipated
  future uses)? If so, please provide a link or other access point to
  the "raw" data, this could be a link to a folder in your GitHub Repo,
  Spark! owned Google Drive Folder for this project, or a path on the
  SCC, etc.

  - Both documents are sitting within the data folder in Github

<!-- -->

- **Is the code that was used to preprocess/clean the data available? If
  so, please provide a link to it (e.g., EDA notebook/EDA script in the
  GitHub repository).**

  - https://github.com/BU-Spark/ds-seasonwatch-trees/tree/data-analysis/code/Fall%202024%20Code  
    **Uses**  

<!-- -->

- What tasks has the dataset been used for so far? Please provide a
  description.

  - Answering the base questions for the client as well as creating a
    interactive PowerBI for further analysis

<!-- -->

- **Is there anything about the composition of the dataset or the way it
  was collected and preprocessed/cleaned/labeled that might impact
  future uses**?

  - No

<!-- -->

- Are there tasks for which the dataset should not be used? If so,
  please provide a description.

  - No  
      
    **Distribution**  

<!-- -->

- Based on discussions with the client, what access type should this
  dataset be given (eg., Internal (Restricted), External Open Access,
  Other)?

  - Open Access  
      
    **Maintenance:**

<!-- -->

- If others want to extend/augment/build on/contribute to the dataset,
  is there a mechanism for them to do so? If so, please provide a
  description or a link to the code.

  - Extend from our data cleaning and analysis
    https://github.com/BU-Spark/ds-seasonwatch-trees/tree/data-analysis/code/Fall%202024%20Code  
    **Other**

<!-- -->

- Is there any other additional information that you would like to
  provide that has not already been covered in other sections?

  - None
