<h1>COVID-19 India Dashboard</h1>

This dashboard provides comprehensive visualizations and statistics regarding COVID-19 cases in India. It is a web-based application built using Python's Dash framework and Plotly for interactive data visualization.

<h3>Features</h3>

1. Overview Section:
Total Cases: Displays the total number of COVID-19 cases reported in India.
Active Cases: Shows the current active cases requiring hospitalization.
Recovered: Indicates the total number of patients who have recovered from COVID-19.
Deaths: Displays the total number of deaths due to COVID-19.

2. Day-by-Day Analysis:
Line Chart: Visualizes the trend of confirmed cases over time, providing insights into the spread of the virus.

3. Age-wise Analysis:
Pie Chart: Presents the distribution of COVID-19 cases across different age groups, allowing users to understand the demographics affected by the virus.

4. State-wise Analysis:
Bar Chart: Illustrates the distribution of COVID-19 cases by state, enabling users to identify regions with the highest number of cases.
Dynamic Filtering: Users can filter the state-wise analysis based on the status of cases, including hospitalized, recovered, and deceased.

<h3>Data Sources</h3>

The dashboard utilizes the following data sources:

Individual Patient Data: sourced from the IndividualDetails.csv file, providing detailed information about each COVID-19 patient.
Daily COVID-19 Statistics: obtained from the covid_19_india.csv file, offering daily updates on confirmed cases.
Age Group Data: sourced from the AgeGroupDetails.csv file, providing insights into the distribution of cases across different age groups.

<h3>Dependencies</h3>

The following dependencies are required to run the dashboard:

Python 3.x
numpy
pandas
plotly
dash
dash-html-components
dash-core-components

<h3>Installation</h3>

To set up the dashboard locally, follow these steps:

1.Clone this repository:
git clone https://github.com/your_username/COVID19-India-Dashboard.git

2.Navigate to the project directory:
cd COVID19-India-Dashboard

3.Install dependencies:
pip install -r requirements.txt

<h3>Usage</h3>

1.Run the Dash application:
python app.py

2.Open a web browser and go to http://127.0.0.1:8050/ to access the dashboard.

3.Interact with the dashboard to explore COVID-19 statistics and visualizations.

This project is licensed under the MIT License. See the LICENSE file for details.

<h3>Acknowledgements </h3>
Special thanks to the contributors of the COVID-19 data sources used in this dashboard.
I appreciate the efforts of the Dash and Plotly development teams for providing powerful tools for data visualization.
