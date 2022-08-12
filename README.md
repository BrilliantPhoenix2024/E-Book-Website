What is this project?

# Bookstore repository is a sample of a Back-end and Front-end tutorial course.

challenges that i deal with in this project:

1-How to use custom manager
2-How to use Static files in my Templates
3-How to install diffrent and very usefull third-party Django Packages in my project
4-How to clone a readi-to-use repository in my project
5-How to use Docker


How to use?
If you want to get notified about the future changes Follow my github account.

First clone the project.

If you are on windows click on the Docker Desktop icon and wait for about a minute.
Then in the project directory run this command:

docker-compose up --build

It will create two containers: One for Django and one for PostgreSql as the database for the project. All the required packages will be installed.

Install a new package.

Attention: If you want to install a package for django project you should run this command:
docker-compose exec web pip install <package-name>

Don't forget to add the new package to requirements.txt for further use:

docker-compose exec web pip freeze > requirements.txt
