[![Build Status](https://travis-ci.org/samuelbwambale/book-a-meal.svg?branch=master)](https://travis-ci.org/samuelbwambale/book-a-meal)




# Book-A-Meal

This repository contains the description and a guide on how to clone and run the app.

### Project Description:
Book-A-Meal is an application that allows customers to make food orders and helps the food vendor know what the customers want to eat. 

### Required Features
  1.	Users can create an account and log in
  2.  Admin (Caterer) should be able to manage (i.e: add, modify and delete) meal options in the application
  3.  Admin (Caterer) should be able to setup menu for a specific day by selecting from the meal options available on the system
  4.  Authenticated users (customers) should be able to see the menu for a specific day and select an option out of the menu
  5.  Authenticated users (customers) should be able to change their meal choice
  6.  Admin (Caterer) should be able to see the orders made by the user
  7.  Admin should be able to see amount of money made by end of day

  
| EndPoint                                              | Functionality                                    |
| ----------------------------------------------------- | ------------------------------------------------ |
| [POST /auth/signup](#)                                | Register a user                                  |
| [POST /auth/login](#)                                 | Logs in a user                                   |
| [GET /meals/](#)                                      | Get all meal options                             |
| [POST /meals/ ](#)                                    | Add a meal                                       |
| [PUT /meals/<mealId>](#)                              | Update the information of a meal option          |
| [DELETE /meals/<mealId>](#)                           | Remove a meal option                             |
| [POST  /menu/](#)                                     | Set up the menu of the day                       |
| [GET /menu/](#)                                       | Get the menu of the day                          |
| [POST  /orders](#)                                    | Select a meal option from the menu               |
| [PUT /orders/orderId](#)                              | Modify an order                                  |
| [GET  /orders](#)                                     | Get all orders                                   |


### Prerequisites
  1.	HTML/CSS
  2.	Javascript/ES6
  3.	Python/Flask
  4.  GIT and Version Control  

## Technologies

* Python 2.7 and above
* Flask Restful

## Requirements

* Install [Python](https://www.python.org/downloads/)
* Run `pip install virtualenv` on command prompt
* Run `pip install virtualenvwrapper-win` on command prompt
* Run `set WORKON_HOME=%USERPROFILES%\Envs` on command prompt

## Setup

* Run `git clone` this repository and `cd` into the project root.
* Run `mkvirtualenv venv` on command prompt
* Run `workon venv` on command prompt
* Run `pip freeze > requirements.txt` on command prompt
* Run `export FLASK_APP=app.py` on command prompt
* Run `flask run` on command prompt
* View the app on `http://127.0.0.1:5000/`
  
## GitHub pages

View the userinterface at (https://samuelbwambale.github.io/book-a-meal/UI/src/home.html)
