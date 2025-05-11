# Reflection

Student Name:  Gilda Emeni
Student Email:  gemeni@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
One thing I really learned from this project is how a full data pipeline works from start to finish and not just cleaning a CSV but extracting, transforming, loading (ETL), and building something interactive with it. Before, I had only worked with simple scripts, but this project made me structure things into modules, write test cases (was complicated), cache files, and manage folders like a real data engineer or a professor. That helped me understand the difference between exploratory work and production-level structure.

I struggled the most with merging the datasets specifically aligning `UNITID` from the field-of-study CSV with `STABBR` from the institution CSV to get state-level info. The data didn’t always match cleanly, and I kept getting KeyErrors because I didn’t fully understand how Pandas handles duplicate column names after a merge (like `_x` and `_y`). But fixing that taught me how to be more careful with join keys and column names after merges.

I also had trouble with the choropleth map. I didn’t realize at first that the state abbreviations in my salary dataset wouldn’t match the full state names in the GeoJSON file used by Folium. Debugging that made me revisit how mapping works in geopandas and how important it is to clean string-based data, not just numeric values

Overall, this project helped me better understand modular coding, data visualization libraries like Plotly and Folium, caching cleaned data, and how APIs work (both the CENT API and scraping with Playwright). I still need more practice using real APIs in a pipeline and creating interactive components in Streamlit, but this was a huge step. I feel more confident building data-driven tools now and not just writing code for class.

