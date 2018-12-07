# Item Catalog Project

This project is a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication. OAuth2 provides authentication for further CRUD functionality on the application. Currently OAuth2 is implemented for Google Accounts.

## Project Content

This project has one main Python module `app.py` which runs the Flask application. A SQL database is created using the `database_setup.py` module and you can populate the database with test data using `filling_items.py`.
The Flask application uses stored HTML templates in the templates folder to build the front-end of the application. CSS/Images are stored in the static directory.

## Technologies/Skills used

1. Python
2. HTML
3. CSS
4. OAuth
5. Flask Framework

### Prerequisites

1. Download [Vagrant](https://www.vagrantup.com/)
2. Download [Virtual Box](https://www.virtualbox.org/)
3. [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)

### Installing

1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Go to Vagrant directory and clone this repository to a directory of your choice
4. Launch the Vagrant VM (`vagrant up`)
5. Log into Vagrant VM (`vagrant ssh`)
6. Navigate to `cd/vagrant` as instructed in terminal
7. Setup application database `python /item-catalog/database_setup.py`
8. Insert fake data `python /item-catalog/filling_items.py`
9. Run application using `python /item-catalog/app.py`
10. Access the application locally using http://localhost:8000

## Using Google Login
To get the Google login working there are a few additional steps:

1. Go to [Google Dev Console](https://console.developers.google.com)
2. Sign up or Login
3. Go to Credentials
4. Select Create Credentials > OAuth Client ID
5. Select Web application
6. Enter name 'Item-Catalog'
7. Authorized JavaScript origins = 'http://localhost:8000'
8. Authorized redirect URIs = 'http://localhost:8000/login' && 'http://localhost:8000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the `data-clientid` in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in item-catalog directory that you cloned from here
14. Run application using `python /item-catalog/app.py`

## Authors

* **Arwa Alshathri** - *Initial work* - [iarwa](https://github.com/iarwa)
