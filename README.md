


## MySuperDataCompany
## Overview

MySuperDataCompany is a Django-based web application for uploading and querying data files in JSON and CSV formats. This project is containerised using Docker, making it easy to set up and run on any system with Docker installed.

## Prerequisites
1) Docker
2) Docker Compose

## Setup and Running the Project

1) Step 1: Clone the Repository
Clone the repository to your local machine:
git clone https://github.com/YourUsername/MySuperDataCompany.git
cd MySuperDataCompany


2) Step 2: Build and Run the Docker Containers
   Ensure you are in the root directory of the project where the docker-compose.yml file is located, then run:

    docker-compose up --build

    This command will build the Docker images and start the containers for both the Django application and the PostgreSQL database.

3) Step 3: Access the Application
   Once the containers are up and running, you can access the application in your web browser at:

    http://localhost:8000

4) Step 4: Upload Data Files
    Navigate to the upload page to upload JSON or CSV files. This page is accessible at:


    http://localhost:8000/data/upload/

5) Step 5: Query Data

   To view the data in a table format, navigate to:


    http://localhost:8000/data/query/

   You can filter data by type using the query parameter type. For example:

   http://localhost:8000/data/query/?type=invoice

6) step 6: createsuper user
   In docker, enter the web 1 running container and type the command:

   Python manage.py createsuperuser

   Input the username, email and passowrd. After that you can log into the django admin site to view and manage the tables created using the url below: 

   http://localhost:8000/admin

## Directory Structure

1) Dockerfile: Defines the Docker image for the Django application.
2) docker-compose.yml: Defines the Docker services for the application and database.
3) entrypoint.sh: Script to run database migrations and start the Django development server.
4) dataapp/: Django app containing models, views, and templates.
5) models.py: Defines the data models.
6) views.py: Contains the view logic for uploading and querying data.
7) templates/: HTML templates for the application.
8) upload.html: Template for the file upload page.
9) data_table.html: Template for displaying queried data in a table format.
10) requirements.txt: Lists the Python dependencies for the project.


## Troubleshooting
## common Issues
1) Database Connection Error: Ensure that the db service is running and the database credentials in settings.py match those defined in docker-compose.yml.

2) File Upload Issues: Ensure that the uploaded files are in the correct JSON or CSV format.
3) If you run your docker and you get an error saying "could not access entrypoint.sh file" then change the CRLF on your vscode to LF and try running your docker again.
 



 docker-compose down -v
 docker-compose build
 docker-compose up


4) If you run your docker and get this error: 

"could not open directory "pg_notify": No such file or directory" 

 This indicates that there is a problem with the PostgreSQL data directory.

 Just simply run the following commands:


 docker-compose down -v
 Remove-Item -Recurse -Force .\postgres_data


 Then rerun your docker:


 docker-compose build
 docker-compose up



## Useful Commands
1) Stop Docker Containers: docker-compose down
2) Remove Docker Volumes: docker-compose down -v (useful for resetting the database)
3) Rebuild Docker Images: docker-compose up --build

## Inputs for CSV file

type,amount,date
invoice,100,2024-06-19
receipt,50,2024-06-18

## inputs for json file
[
    {
        "type": "invoice",
        "amount": 100,
        "date": "2024-06-19"
    },
    {
        "type": "receipt",
        "amount": 50,
        "date": "2024-06-18"
    }
]


