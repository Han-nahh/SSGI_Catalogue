# SSGI Catalogue classification system

Welcome to SSGI Catalogue classification system! This is a web application built using the Django framework that aims to provide satellite imagery classification and querying services


## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [API Documentation](#api-documentation)
- [Contribution](#contribution)
- [Contact](#contact)

## Installation

Follow the instructions below to set up the project locally:

1. Clone the repository:
   ```shell
   git clone https://github.com/melaku468/ssgi_catalog.git
   cd ssgi_catalog
2. Create and activate a virtual environment:
   ```shell
   python -m venv ./venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows

3. Install the dependencies:
   ```shell
   pip install django
   pip install psycopg2
   pip install load_dotenv
   pip install validate_email
   pip install six
   pip install pillow
   
   
4. Perform database migrations:
   ```shell
   python manage.py migrate

5. Start the development server:
   ```shell
   python manage.py runserver
##### The web application should now be accessible at http://localhost:8000. 



## Features
- Sign up and sign in: provides user registration and login functionality.
- Search and Browse: provides an advanced search platform for users to easily search and locate satellite image.
- Mapping and Drawing: incorporates google mapping and direction features in the web to help users to drag and draw polygon of specific area to search an image.
- Security and Privacy: implements security and privacy measures to ensure the integrity and confidentiality of user action.


## API Documentation

1. Leaflet is an open-source JavaScript library for interactive maps. It provides a lightweight and versatile solution for displaying maps on web pages.
2. The Google Maps API is a powerful set of tools and services provided by Google that allows developers to integrate maps, location data, and other related features into their applications.


## Contribution


1. By default the branch is on main, so first make sure you are on dev-middle branch
- This command shows which branch you are on
   ```shell
   git branch
      
- This command shows all the available branches 
   ```shell
   git branch -a
 - Use the following command to switch to your own branch. Make sure you replace `<your branch name>` with your own branch name (eg- dev-abc)
   ```shell
   git checkout <your branch name>
 - Before trying to push any code to the middle branch, first make sure you pulled any changes made on the middle branch by other contributors.
    ```shell
   git pull origin dev-middle
 - After syncing the change, You are now ready to push your code. Make sure to replace `source-branch` with your branch's name
   ```shell
   git add .
   git commit -m "Commit message"
   git push origin source-branch:dev-middle




## Contact
If you have any questions, suggestions, or feedback, please feel free to reach out to us.



