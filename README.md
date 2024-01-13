
## IITK-connect
 Your go-to QnA hub for seamless knowledge sharing within the IITK community. Ask questions, post answers, and engage in discussions effortlessly. Save time, connect, and collaborate!

## Code Structure-

This repository contains an implementation folder that contains all the code for our web app.

The project is divided into several small apps-

- Answers - represents the class of answer
- Questions - represents the class of questions
- Comments- represents the class of comments
- Users - represents the class of users
- Home - represents the home page, and contains the content class
- Notifications - implements functionalities of notifications
- Media - Contains all the images
- Tags - implements functionalities for adding tags to questions
- IITK-connect - app to integrate all the above apps.

Some important files/folders in each of the apps mentioned above -
- models.py - describe each object's class.
- admin.py - registers and customises the admin view for the models
- apps.py - registers apps with Django
- forms.py - contains the form to either create a new object of the given - model/class or edit the already existing object.
- urls.py - contains URL patterns that match a URL with a view for a page
- views.py - contains functions that take web requests and return web - responses
- templates - has the HTML files for the pages

Two more folders are present-
- Templates - it has the HTML files for the pages
- Static - it stores static files such as CSS and javascript files.
