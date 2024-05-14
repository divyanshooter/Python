

# Flask User Registration and NER Application

This Flask application provides a simple user registration system along with a Named Entity Recognition (NER) tool. Users can register, log in, perform NER on text inputs, and log out. The application uses a SQLite database for user data storage.

## Features

- **User Registration**: Allows users to register with a unique email address.
- **User Login**: Authenticates users based on email and password.
- **Profile Page**: Displays user profile information after successful login.
- **Named Entity Recognition (NER)**: Parses text input for named entities.
- **Session Management**: Uses Flask session to maintain user login state.
- **Error Handling**: Provides error messages for invalid inputs and actions.
- **Logging Out**: Allows users to log out and end their session.

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

- **Python (version 3.x)**: The core programming language used for development.
- **Flask**: A lightweight WSGI web application framework for Python.
- **SQLite3**: A self-contained, serverless, zero-configuration, transactional SQL database engine.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
   ```

2. **Install Dependencies**:

   ```bash
   pip install flask
   ```

3. **Run the Application**:

   ```bash
   python app.py
   ```

   The application will start running at `http://localhost:5000`.

## Usage

1. **Registration**: Visit the `/register` route to create a new account. Provide a unique name, email, and password. Upon successful registration, you will be redirected to the login page.

2. **Login**: Access the `/` route to log in with your registered email and password. After successful authentication, you will be redirected to your profile page.

3. **Profile**: Once logged in, you can access your profile at `/profile`. Here, you can view your profile information.

4. **Named Entity Recognition (NER)**: Navigate to the `/ner` route to utilize the NER tool. Enter text input and submit to extract named entities from the text.

5. **Logout**: To end your session, click on the "Logout" button or visit the `/logout` route.

## Additional Notes

- This application is intended for educational purposes and may require additional security enhancements for production use.
- Ensure proper error handling and input validation to enhance the robustness of the application.
- Customize the application as needed to meet specific requirements or integrate additional features.
- For advanced usage or deployment in a production environment, consider using a more secure database solution such as PostgreSQL or MySQL.
- Explore Flask extensions for additional functionality such as user authentication, form validation, and RESTful APIs.

## Contributing

Contributions are welcome! If you have suggestions for improvements, feature requests, or bug reports, please open an issue on GitHub or submit a pull request.
