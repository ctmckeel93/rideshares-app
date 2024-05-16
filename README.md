# Rideshares Application

This README provides an overview of the Rideshares Application, detailing its functionality, technology stack, and usage.

## Overview

The Rideshares Application is a web application developed using the Flask framework, integrating pymysql for database management. It facilitates ride-sharing by allowing users to request rides, which are then fulfilled by other users acting as drivers. The application ensures data integrity through proper validation of user inputs and offers secure user authentication via Flask-Bcrypt.

## Functionality

- **User Registration and Authentication**: Users can register with their email and password securely. Flask-Bcrypt encrypts passwords to ensure data security and authenticate users.

- **Ride Request and Fulfillment**: Users can request rides, which are displayed on the dashboard. Other users can volunteer to drive for these requests. Once a driver accepts a ride, a details page is created for both parties.

- **Real-Time Communication**: Riders and drivers can communicate with each other through messaging on the details page. This feature helps both parties stay updated on the status of the ride.

- **Request Management**: Riders have the ability to delete their ride requests, while drivers can cancel their acceptance to drive for a particular request. Additionally, riders can update their requests as needed.

## Technology Stack

The Rideshares Application utilizes the following packages:

- **Flask**: A micro web framework for Python, used for building the web application.
- **Flask-Bcrypt**: A Flask extension that provides bcrypt hashing utilities for securing user passwords.
- **Flask-Dotenv**: A Flask extension that loads environment variables from a .env file into Flask application.
- **pymysql**: A Python library for interacting with MySQL databases.
- **Bootstrap-Flask**: A Flask extension that integrates Bootstrap CSS framework with Flask applications for responsive design.

## Usage

To use the Rideshares Application, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone the repository to your local machine.
3. Install the required packages using pipenv with pipenv install.
4. Set up your environment variables in a `.env` file, including database connection details and any sensitive information.
5. Run the Flask application using the `flask run` command.
6. Access the application through your web browser using the provided URL.

Feel free to explore and contribute to the application as needed!

## Contributors

- Corey: ALL

