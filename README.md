### Neighbourhood Web Application

#### Author

Robert Gitonga

#### Description

This is a neighbourhood application where a user must signup first, be able to join a hood owned by the hood admin, and once you join a hood, one can see businesses and posts in only that hood they belong to.

#### Live Link

Click the link to visit site

#### User Story

- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.

#### Setup and Installation

- Cloning the repository:
  - https://github.com/CodeRichBob/Neighborhood
- Navigate into the folder and install requirements
  - cd Neighbourhood
- Install and activate Virtual
  - python3 -m venv virtual - source virtual/bin/activate
- Install Dependencies
  - pip install -r requirements.txt
- Setup Database
  - python manage.py makemigrations
  - python manage.py migrate
- Run the application
  - python manage.py runserver
- Open the application on your browser 127.0.0.1:8000.

#### Technology used

- Python3.9.10
- Django 4.0.4
- Heroku

#### Known Bugs

- There are no known bugs currently but pull requests are allowed incase you spot a bug

#### Contact Information

If you have any question or contributions, please email me at rgitonga07@gmail.com

#### License

- MIT License
- Copyright &copy; 2022 | Robert Gitonga
