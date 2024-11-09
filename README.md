# Netflix Content Analysis Dashboard

This Streamlit application provides an interactive dashboard for analyzing Netflix movies and TV shows data. With this app, users can filter content by type and year added, and explore content data associated with "India" across years.

## Features

- **Content Type Filter**: Multi-select dropdown to choose between "Movie", "TV Show", or both.
- **Year Filter**: Multi-select dropdown to choose specific years to analyze content addition trends.
- **Content Count by Year and Type**: Visualize the total count of movies and TV shows added to Netflix per selected year(s) with a grouped bar chart.
- **India Content Analysis**:
  - Filter and display the count of content associated with "India" across the chosen years and content types.
  - Visualize the distribution of content with "India" in the country field versus content without it using a pie chart.
  - Display a detailed table showing titles, type, year added, and countries for "India" related content.

## Screenshots

### Main View
- **Content Count by Year and Type**
- **Content with India Analysis**
- **Pie Chart of Content with and without 'India'**

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/netflix-content-analysis
    cd netflix-content-analysis
    ```

2. **Install dependencies**:
    Make sure you have Python installed. You can install the required libraries using:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download Data**:
    Ensure that you have the Netflix dataset (`netflix_movies (1).csv`) in the same directory as the app. The data should contain the following columns:
    - `type` (e.g., Movie, TV Show)
    - `year_added` (the year the content was added to Netflix)
    - `country` (countries associated with the content)

4. **Run the Streamlit app**:
    ```bash
    streamlit run streamlit_app.py
    ```

## File Structure

- `streamlit_app.py`: Main application file for the Streamlit dashboard.
- `data_cleaning.py`: Contains the `clean_df` function to preprocess the Netflix data.
- `netflix_movies (1).csv`: Sample dataset containing Netflix movie and TV show information.

## Usage

1. **Select Content Type**:
   - Choose the type(s) of content (Movies and/or TV Shows) you want to analyze.
  
2. **Select Year(s)**:
   - Choose one or more years to display the content added to Netflix.

3. **Analyze Content with "India"**:
   - View the count and details of content associated with "India".
   - The pie chart displays the distribution of content with and without "India" in the country field.

## Example Dataset

The application assumes the following sample structure for the `netflix_movies (1).csv` file:

| title       | type   | year_added | country                       |
|-------------|--------|------------|-------------------------------|
| Example 1   | Movie  | 2022       | India                         |
| Example 2   | TV Show| 2021       | United States, India          |
| Example 3   | Movie  | 2023       | United Kingdom                |
| Example 4   | TV Show| 2020       | India, United States, Canada  |

## Requirements

- Python 3.x
- Streamlit
- Pandas
- Plotly

Install the above packages using:
pip install streamlit pandas plotly
