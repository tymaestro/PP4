# The Sweat Life

The Sweat Life is a web application that allows users to post activities and interact with other users by liking or commenting on their posts

## User Stories

As a standard (not logged-in) user, I would like to:
<br>
<br>

1. View the landing page and know that I'm on a social site for exercise enthusiasts
<br>
<br>

2. View posts by users
<br>
<br>

3. Have a unique sign-up option with username and password
<br>
<br>

As a registered (logged-in) user, I would like to:
<br>
<br>

1. Have a login option to log in to my previously registered account
<br>
<br>

2. Create and post my own activities
<br>
<br>

3. Rate how I felt after my activity
<br>
<br>

4. View the uploads of other users
<br>
<br>

5. Like and comment on users' posts
<br>
<br>

6. Choose a date and time for group activities
<br>
<br>

7. View the other users who have chosen these time slots
<br>
<br>

8. Edit my activity
<br>
<br>

9. Delete my activity
<br>
<br>

## Project Goals

## Flowchart

## Wireframes

## Agile Methodology

## Features

### Navbar

The navigation bar gives you access to the activities page as well as an opportunity to either login with a previously created account or create an account via the sign up option.


The navigation bar once you are logged in gives you the opportunity to add your own activities as well as log out of your account.


### Sign Up Page

The sign up page allows you to create an account by providing a username and password for authentication. Creating an account gives you access to extra functionality such as the ability to create, edit, and delete your own activities and comment on the activities of others.

### Login Page

As with the sign up page, the login page allows previously registered users to access the extra functionality that having an account provides.

### Activities Page

This page presents an ordered and paginated list of activities posted by users. Visible is the title and excerpt of the activity. These activities are public but an account must be created to leave a comment or create your own activities.

### Activity Detail Page

The activity detail page presents the selected activtiy in detail including its title, excerpt, content and comments left by users.

### Create Activity Page

The create activity page displays a form where you can enter a title, excerpt and the content of your activity.

### Create Comment Page

The create comment page is shown as a form where you can leave a comment on the selected post.

### Edit Activity Page

The edit activity page displays your activity as a form, pre-populated with the details and content previously provided so that you can edit your post.

### Delete Activity Page

The delete activity page displays a warning (defensive programming) to ensure that you are certain of your choice to delete the chosen activity and are aware of the consequences.

## Features Left To Implement

Add a calendar so that users can organise meet ups to exercise or explore nature in a group setting. This adds to the social aspect of this web application and encourages users to engage with others during their activities.

## Languages Used

Python 3.0

CSS

## Libraries, Frameworks, and Programs Used

Django

## Code Validation

## Testing

## Bug Fixes

## Deployment

### Heroku Deployment

1. Create a new app in the Heroku dashboard. Choose a name and location for your app.

2. Click the resources tab to add the Heroku Postgres database.

3. Click on the settings tab and reveal config vars. Copy the DATABASE_URL and paste it into the env.py file in your project. Mkae sure that the env.py file is in the .gitignore file.

4. Add a SECRET_KEY both to the env.py file and in the config vars on Heroku.

5. In the Gitpod settings.py file, remove the insecure SECRET_KEY and replace it with the environment variable (SECRET_KEY) that was created.

6. Replace existing DATABASES section in settings.py file with the DATABASE_URL environment variable that is located in the env.py file.

7. Ensure that all static and files have been added to the settings.py file in Gitpod.

8. Add the TEMPLATES_DIR to settings.py file in Gitpod and link it in the TEMPLATES section.

9. Make sure that the project name for the Heroku app has been added as an allowed host in Gitpod.

10. Ensure to create a Procfile and add web: gunicorn activities.wsgi to this file

11. Make sure that the DEBUG flag is set to False in settings.py file in Gitpod

12. Add X_FRAME OPTIONS = 'SAMEORIGIN' to the settings.py file to ensure that the Summernote editor works once the project is deployed.

13. Make sure that all dependencies have been added to the requirements.txt file using the command pip3 freeze > requirements.txt

WARNING: Heroku has halted automatic deployments from Github so the steps to build your Heroku app are as follows...

Using the CLI, enter the following commands to deploy to Heroku

1. Login to Heroku using the command heroku login -i

2. Enter your email address and password

3. Find the relevant app using the command heroku apps

4. Set the Heroku remote using the command heroku git:remote -a <app_name>

5. Add, commit and push to Github using the command git add . && git commit -m "Deploy to Heroku via CLI"

6. Push to both Github and Heroku using the command git push origin main (for Github) and the command git push heroku main (for Heroku)

## Credits

Images etc.

## Acknowledgements

Daisy/Slack/Stack Overflow etc.