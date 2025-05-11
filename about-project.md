# About My Project

Student Name:  Gilda Emeni
Student Email:  gemeni@syr.edu

### What it does
My project is a tech salary explorer that lets you view average post-graduation earnings for tech majors across different U.S. schools. It combines government datasets (field of study + institution info) and includes a Streamlit dashboard with filters by major, a bar chart of top schools, and a map that shows salary averages by state. I also included a basic scraper for cost of living data from Numbeo.

### How you run my project
1. Install everything from `requirements.txt`
2. Run `code/extract.py` to clean and generate the salary data
3. (Optional) Run `code/scrape_cost.py` to get sample cost of living data
4. Launch the Streamlit dashboard

### Other things you need to know
- The map only works because I merged two different datasets using UNITID to add state info
- The data is filtered to only include tech-related majors like computer science, information systems, and data fields
- All cleaned data is saved in the `cache/cleaned` folder
- I added tests in the `tests` folder to confirm that my extraction function works