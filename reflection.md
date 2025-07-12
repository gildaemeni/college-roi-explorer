# Project Reflection: College ROI Explorer

## What I learned
One thing I really learned from this project is how a full data pipeline works from start to finish and not just cleaning a CSV but extracting, transforming, loading (ETL), and building something interactive with it. Before, I had only worked with simple scripts, but this project made me structure things into modules, write test cases which was harder than expected, cache files, and manage folders like a data engineer. That helped me understand the difference between exploratory work and production-level structure.

## Where I Struggled
I struggled the most with merging the datasets specifically aligning `UNITID` from the field-of-study CSV with `STABBR` from the institution CSV to get state-level info. The data didn’t always match cleanly, and I kept getting KeyErrors because I didn’t fully understand how Pandas handles duplicate column names after a merge (like `_x` and `_y`). But fixing that taught me how to be more careful with join keys and column names after merges.

I also had trouble with the choropleth map. I didn’t realize at first that the state abbreviations in my salary dataset wouldn’t match the full state names in the GeoJSON file used by Folium. Debugging that made me revisit how mapping works in geopandas and how important it is to clean string-based data, not just numeric values

## Moving Forward
Overall, this project helped me better understand modular coding, data visualization libraries like Plotly and Folium, caching cleaned data, and how APIs work (both the CENT API and scraping with Playwright). I still need more practice using real APIs in a pipeline and creating interactive components in Streamlit, but this was a huge step. I feel more confident building data-driven tools now and not just writing code for class.

