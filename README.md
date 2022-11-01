# Optimal office placement

## Objective

This project has the goal of solving the following problem:

You recently created a new company in the `GAMING industry`. The company will have the following scheme:

- 20 Designers
- 5 UI/UX Engineers
- 10 Frontend Developers
- 15 Data Engineers
- 5 Backend Developers
- 20 Account Managers
- 1 Maintenance guy that loves basketball
- 10 Executives
- 1 CEO/President.


As a data engineer you have asked all the employees to show their preferences on where to place the new office. Your goal is to place the **new company offices** in the best place for the company to grow. You have to find a place that more or less covers all the following requirements (note that **it's impossible to cover all requirements**, so you have to prioritize at your glance):

- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- 30% of the company staff have at least 1 child.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Executives like Starbucks A LOT. Ensure there's a starbucks not too far.
- Account managers need to travel a lot.
- Everyone in the company is between 25 and 40, give them some place to go party.
- The CEO is vegan.
- If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.
- The office dog—"Dobby" needs a hairdresser every month. Ensure there's one not too far away.

## Choosing the candidate cities

For choosing the 

[Selecting city notebook](https://github.com/marccalvente/GeoSpatial-Data-Project/tree/main/src/selecting_city.ipynb)

## Process for selecting the best placement in the city

[Selecting optimal location notebook](https://github.com/marccalvente/GeoSpatial-Data-Project/tree/main/src/getting_api_locations.ipynb)

## Visualization

## Conclusion

-----------------------
#### Project structure

The project follows the structure:

- ./data
    - Contains the DataFrames with information extracted from MongoDB for San Francisco and New York.

- ./images
    - empty for now

- ./src
    - utilities.py: containing all the functions defined for the project
    - selecting_city.ipynb: notebook with the process of extracting data from mongoDB, manipulating it and exporting dataframes with the info for the selected cities.
    - getting_api_locations.ipynb: 