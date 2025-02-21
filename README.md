# Weather App (Flask)

This is a simple weather application built with Flask. It is my first completed pet project, where I learned how to interact with open APIs, handle GET and POST requests, and display retrieved information in a template.

## Features

- Fetches weather data using the OpenWeather API
- Handles user input for city, state, and country
- Displays weather conditions including temperature, description, and an icon
- Implements error handling for invalid city names

## Installation and Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/kateutkate23/weather_app.git
   cd weather_app
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   # On Linux
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Get an API key from OpenWeather:**

   - Go to [OpenWeather API](https://openweathermap.org/)
   - Sign up and generate an API key

5. **Create a `.os` file in the project root and add your API key:**

   ```
   API_KEY=generated_api
   ```

6. **Run the application:**

   ```sh
   flask run
   ```

7. **Open in your browser:**

   - Visit `http://127.0.0.1:5000/` to use the weather app.

## Technologies Used

- Python
- Flask
- Bootstrap (for basic styling)
- OpenWeather API

---

### License

This project is for learning purposes and is open for modification and improvement.

