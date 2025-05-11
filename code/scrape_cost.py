from playwright.sync_api import sync_playwright
import pandas as pd

def scrape_numbeo_cost(city_slug: str = "syracuse") -> pd.DataFrame:
    """
    Scrapes cost of living data from Numbeo for a given city.
    """
    url = f"https://www.numbeo.com/cost-of-living/in/{city_slug}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        # Find the cost of living table
        rows = page.query_selector_all("table.data_wide_table tr")
        items = []
        for row in rows:
            columns = row.query_selector_all("td")
            if len(columns) >= 2:
                item = columns[0].inner_text().strip()
                price = columns[1].inner_text().strip()
                items.append({"item": item, "price": price})

        browser.close()

    return pd.DataFrame(items)

if __name__ == "__main__":
    df = scrape_numbeo_cost("syracuse")
    print(df.head())
    df.to_csv("cache/cleaned/numbeo_cost_data.csv", index=False)
    print("✅ Scraped cost of living data saved to cache/cleaned/numbeo_cost_data.csv")
