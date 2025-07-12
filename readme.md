# College ROI Explorer

**[Try the Live Demo →](https://gildaemeni-college-roi-explorer-codestreamlit-app-eef8ca.streamlit.app/)**

A fully interactive dashboard that helps users explore **post-graduation earnings** across 300+ U.S. universities for tech-related majors with **cost of living comparisons**, **state salary maps**, and a **modular ETL pipeline**. This project highlights the **return on investment (ROI)** for tech degrees based on location and field of study.

---

## Features

- Filterable dashboard by major
- Plotly bar charts showing top-paying schools
- Choropleth map of average earnings by U.S. state
- Basic cost-of-living scraper from Numbeo
- Unit tests with `pytest` to validate ETL logic
- Modular ETL pipeline (Extract, Transform, Load)

---

## Tools Used

| Function         | Tools & Libraries |
|------------------|-------------------|
| Programming      | Python 3.11       |
| Dashboard        | Streamlit, Plotly |
| Data Wrangling   | pandas            |
| Mapping          | Folium, GeoPandas |
| Web Scraping     | Playwright        |
| API Integration  | Azure CENT API    |
| Testing          | pytest            |

---

## Project Structure
<pre lang="markdown">
college-roi-explorer/
│
├── code/
│ ├── extract.py # Salary data cleaning
│ ├── scrape_cost.py # Cost of living scraper
│ ├── streamlit_app.py # Interactive dashboard
│ ├── api_calls.py # Azure entity recognition
│
├── cache/
│ ├── raw/ # Original CSVs (DOE)
│ └── cleaned/ # Cleaned datasets
│
├── tests/
│ └── test_extract.py # Pytest validations
├── README.md
├── reflection.md
`` </pre>

## How to Run the Project
```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the ETL pipeline
python code/extract.py
python code/scrape_cost.py  # optional

# Step 3: Launch the dashboard
streamlit run code/streamlit_app.py
```
---

## Reflection
[Read my personal reflection](reflection.md)

## Author
**Gilda Emeni**
gemeni@syr.edu
[linkedin.com/in/gilda-emeni](https://linkedin.com/in/gilda-emeni)