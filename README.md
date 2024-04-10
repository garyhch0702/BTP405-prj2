# Cloud-Based Restaurant Reservation System

## Introduction

This project is a cloud-based restaurant reservation system developed by Chenghao Hu for the BTP 405 course. The system allows users to make, manage, and cancel reservations online. It also provides an interface for restaurant staff to manage booking availability, customer information, and receive notifications about reservations. The application is designed with a microservices architecture to ensure scalability, flexibility, and easy maintenance.

## Features

- **User Account Management**: Users can create accounts, log in, and manage their information.
- **Reservation Management**: Users can make, view, and cancel reservations.
- **Staff Interface**: Allows restaurant staff to manage reservations, view daily booking schedules, and update reservation statuses.
- **Notification System**: Sends notifications to both users and staff about reservation statuses.

## Technologies Used

- **Frontend**: none
- **Backend**: Python, Flask
- **Database**: PostgreSQL
- **Deployment**: The application is deployed on Heroku with the name [restaurant-res-garyhu](https://restaurant-res-garyhu-016561928e29.herokuapp.com/).

## Setup and Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clonehttps://github.com/garyhch0702/BTP405-prj2.git
2.Install the required dependencies:
 ```bash
pip install -r requirements.txt
```
3.Set up the local development database:
 ```bash
# Set up your PostgreSQL database and update the connection string accordingly
```
4.Run the application:
 ```bash
python user_service.py
python reservation_service.py
```
Note: Ensure you have Python and PostgreSQL installed on your development machine.

Using the Application
To use the application, navigate to https://restaurant-res-garyhu-016561928e29.herokuapp.com/. The API can be accessed via endpoints documented in the API.md file (if available).

Contributing
Contributions to the project are welcome. Please follow the standard fork-pull request workflow.

## YouTube Video link
https://www.youtube.com/watch?v=_T63G_Vu3d8
