# In-Depth Analysis of the Airbnb Market

## 1. Project Overview

This project provides a comprehensive analysis of the Airbnb market, leveraging data from Inside Airbnb. The primary goal is to uncover actionable insights for various stakeholders by transforming raw data into a clear, data-driven narrative.

The project is built on a robust ETL (Extract, Transform, Load) pipeline that processes raw data and loads it into a PostgreSQL database. The subsequent analysis, conducted in a Jupyter Notebook (`airbnb-analysis.ipynb`), explores the data to answer 11 key business questions.

## 2. Key Findings & Detailed Analysis

The core of this project is a deep-dive analysis into 11 key business questions, revealing strategies for pricing, marketing, and operations.

Below is a summary of the most critical insights. For the complete, detailed analysis with all visualizations and strategic takeaways, please see the separate report:

### ➡️ **[Click here to view the full In-Depth Analysis & Findings](FINDINGS.md)**

#### Key Insights Summary:
*   **Top Earners:** Newstead - Bowen Hills is the highest-earning neighborhood, and serviced apartments are the most lucrative property type, earning 2x more than standard homes.
*   **Peak Seasonality:** Demand and prices peak in July, while September sees a significant slump, making a dynamic pricing strategy essential.
*   **Success Factors:** High-performing hosts are distinguished by their adoption of Instant Book and high operational ratings, not by charging higher prices.
*   **Optimal Strategy:** The most profitable strategy involves a minimum stay of 2-7 nights, pricing competitively at or just above the market average, and actively managing prices for weekends and based on booking lead time.

## 3. Business Problems Investigated

1.  **Marketing Strategy**: Which neighborhoods and property types generate the highest revenue?
2.  **Seasonal Demand**: How does booking demand fluctuate throughout the year?
3.  **Host Performance**: What are the characteristics of high-performing hosts?
4.  **Impact of Reviews**: How do review scores affect booking rates and revenue?
5.  **Competitive Pricing**: How can hosts price their properties to maximize occupancy and revenue?
6.  **Minimum Night Policies**: What is the optimal minimum-night policy?
7.  **Market Opportunity**: Which neighborhoods are saturated, and where are the opportunities?
8.  **Property Size**: How does property size (accommodation capacity) impact performance?
9.  **Weekday vs. Weekend Trends**: How do booking patterns differ between weekdays and weekends?
10. **Booking Lead Time**: How far in advance do guests book their stays?
11. **Geospatial Distribution**: How are listings, prices, and room types distributed across the city?

## 4. Project Structure

<pre>
.
├── README.md                # Project documentation and summary of findings
├── FINDINGS.md              # Full analysis report with visualizations
├── requirements.txt         # Python dependencies
├── config_template.py       # Template for database configuration (copy and rename to config.py)
├── .gitignore               # Specifies files/folders to ignore in version control
├── run_etl_pipeline.py      # Main script to run the ETL pipeline
├── airbnb-analysis.ipynb    # Jupyter notebook with all analysis and answers to business questions
├── airbnb_listings_map.html # Interactive map visualizing Airbnb listings
├── Power-BI-Dashboard/      # Power BI dashboard files (work in progress)
├── dataset/                 # Folder containing raw and processed data files
└── screenshot/              # Folder containing screenshots and images used in documentation
</pre>

### File Descriptions

| File/Directory              | Purpose                                                                 |
|-----------------------------|-------------------------------------------------------------------------|
| `README.md`                 | Main project documentation, setup guide, and summary of findings        |
| `FINDINGS.md`               | The complete, detailed analytical report with all charts and strategic takeaways |
| `requirements.txt`          | List of Python packages required to run the project                     |
| `config_template.py`        | Database configuration template (copy to `config.py` and fill in)       |
| `run_etl_pipeline.py`       | Complete ETL pipeline for data extraction, cleaning, and loading        |
| `airbnb-analysis.ipynb`     | Main analysis notebook answering all 11 business questions              |
| `airbnb_listings_map.html`  | Interactive Folium map of listing distribution                          |
| `Power-BI-Dashboard/`       | Power BI dashboard files (work in progress, updating soon)              |
| `dataset/`                  | Directory containing all raw and processed data files                   |
| `screenshots/`              | Folder containing screenshots and images used in documentation          |


## 5. Tools and Libraries Used

*   **ETL**: Python, Pandas, SQLAlchemy, psycopg2
*   **Database**: PostgreSQL
*   **Analysis**: Jupyter Notebook, Pandas, SQL
*   **Visualization**: Matplotlib, Seaborn, Folium

## 6. How to Run This Project

1.  **Clone the Repository**: `git clone <repository-url>` and navigate into the directory.
2.  **Install Dependencies**: `pip install -r requirements.txt`
3.  **Set Up PostgreSQL**: Ensure you have a running PostgreSQL instance and create a database for this project.
4.  **Configure Credentials**: Copy `config_template.py` to `config.py` and fill in your database details.
5.  **Download Data**: Place the `listings.csv.gz` and `calendar.csv.gz` files from Inside Airbnb into the `dataset/` directory.
6.  **Run ETL Pipeline**: `python run_etl_pipeline.py`
7.  **Run Analysis**: Open and execute the `airbnb-analysis.ipynb` notebook in a Jupyter environment.

## 7. Future Enhancements

- **Power BI Dashboard**: Create interactive Power BI reports for better business insights.
- **Multi-City Analysis**: Expand the pipeline to include other cities for market comparison.
- **Automated Reports**: Generate weekly/monthly market summary reports.
- **Real-Time Updates**: Implement automated data refresh from Inside Airbnb.