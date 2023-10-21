# Whether Data Integration for Solar Farm

## Description

This project provides an Asset Management System specifically designed for a solar farm. It integrates real-time weather data to assess the operational status of different assets and predicts possible impacts on them based on the weather conditions.

![image](https://github.com/bozkuya/Whether-Data-Integration-for-Solar-Farm/assets/129911627/700a8f18-a72c-4167-a0e6-1d928e4083cd)


## Features

### Asset Management:
- Predefined list of assets with attributes like name and location.
- Dynamic weather effects updates according to the real-time weather data.
- User interface for adding new assets.

### Weather Integration:
- Uses OpenWeatherMap API to fetch real-time weather data.
- Shows the possible effects of the current weather on the equipment.

## Setup and Installation

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/bozkuya/Whether-Data-Integration-for-Solar-Farm.git
    cd Whether-Data-Integration-for-Solar-Farm
    ```


2. **Set Up the OpenWeatherMap API Key:**
    - Go to [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and sign up for a free API key.
    - Replace 'YOUR_API_KEY' in the `main.py` file with the actual API key.

3. **Run the Application:**
    ```sh
    python main.py
    ```

5. **Access the Web Interface:**
    - Open a web browser and navigate to [http://localhost:5000/](http://localhost:5000/).

## Usage

- **Viewing Assets:**
    - The home page displays a list of assets along with their locations and the effects of the current weather on them.

- **Adding New Assets:**
    - Use the form on the home page to add new assets. Enter the name and location, and the new asset will appear in the list with real-time weather effects.
