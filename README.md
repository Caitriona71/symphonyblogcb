
<!-- Heading -->

# Symphony ![View the live site here](https://)

## **Introduction**

Symphony is a fully responsive classical music blog website. Users have the ability to like and comment on posts.

![Am I Responsive](./assets/documentation/responsive-view.png)

## **Design**

An agile project management method was used, together with the **MoSCoW** prioritization method, to help me plan and track my work effectively. I set up a project in Github and created a template for user stories. The user stories are categorized and labelled as essential - **Must Have**, desirable - **Should Have** and nice to have but not essential - **Could Have**. **Milestones** were created and the user stories are attached to the milestones they pertain to. The user stories were then added to a kanban board which has three columns, **ToDo**, **In Progress** and **Done**. All user stories are initially placed in the **ToDo** column and when work commences on the project some user stories are transferred to the **In Progress** column. When work is completed on each user story they are then moved across to the **Done** column.<br><br>

## **User Experience**<br>

### **User Stories**<br><br>

### **Project Creator**

- As **project creator** I need to create the base setup of the application so that other features can be added.

### **Admin**

- As **site admin** I can create draft posts so that I can work on them and complete the content.
- As **site admin** I can create, read, update and delete particular posts, so that I can manage the content of the blog.
- As **site admin** I can approve comments, so that I can decide if a comment is suitable or unsuitable for viewing.
- As a **site admin** I can configure the Administration page so that the view of this area of the blog is customized.
- As a **site admin** I can create, read, update and delete posts from the front end of the blog site, so that I can do this quickly without having to access the administration page.

### **Site User**

- As a **site user** I can view a list of blog posts so that I can choose which one I want to read.
- As a **site user** I can select a post to view its full content.
- As a **site user** I can view the comments on a particular post so that I can see the discussion about that post.
- As a **site user** I can set up an account so that I can comment on and like posts.

### **Registered in User**

- As a **registered user** I can log into my account so that I can use my role specific features.
- As a **registered user** I can log out of my account so that I can keep my information secure and prevent unauthorized access.
- As a **registered user** I can add comments on a post so that I can join in the conversation.
- As a **registered user** I can like or unlike a post so that I can give feedback on the content.
- As a **registered user** I can add posts to favourites so that I can save them and read them later.<br><br>

### **Color Scheme**

The main colours used throughout the blog were black, white, and grey. This creates a clean and easy-to-navigate look for the blog.<br><br>

### **Typography**

The main font used is 'Roboto Slab'. The font used for the blog name is 'Mea Culpa'.<br><br>

## **Features**

Registered users can view the list of posts on the home page. They can click on a post to view its full content. They can comment on a post by filling in the comment form and clicking "submit" and they can like or unlike a post by clicking on the heart icon under the text of the post. <br>
Admin users have access to full CRUD functionality. They can **Create**, **Read**, **Update** and **Delete** blogs on the admin page and on the front end.<br><br>

### **Home Page**

- The Home page has a navigation bar with the blog name logo which will bring the user back to the home page when it is clicked.  The navigation menu also has a Register link, a Log In link and an About Us link. When any of those are clicked the user is redirected to the relevant page. At the right hand side of the navigation bar there is a "Welcome to the world of classical music" banner displayed.<br>
- A user can view the site but if they are not a registered user they can't leave a comment or like or unlike a post. Registered and logged in users have access to that functionality. When a user is logged in the home page navigation bar changes and now the menu consists of the blogsite logo, a Home link, a Logout Link and the About Us link.<br>
- When an admin user is logged in the navigation bar consists of the blogsite logo. A Create Post link, a Logout Link and the About Us link all redirect the user to the relevant page when clicked.<br>

### **Admin Page**

- When admin is added to the end of the web address in the browser, the user is brought to the Django administration login page. When they enter their username and password they are then redirected to the admin page which gives them access to all the functionality of the blog site. Here they can create a post, update a post, delete a post, approve user comments, delete comments and add or delete a contributor to the About Us page.<br><br>

## **Database**

The database is a PostgreSQL database, hosted on [ElephantSQL](https:www.elephantsql.com/).

### **Models**

- [Post Database Model](./readme-docs/database-models/posts-model.png)<br>
- [Comments Database Model](./readme-docs/database-models/comments-model.png)<br>
- [Contributors Database Model](./readme-docs/database-models/contributors-model.png)<br>

### **Diagrams**

- [User Stories UML Diagram](./readme-docs/diagram/user-stories-uml-diagram.png)<br>

### **Languages Used**
- HTML5
- CSS3
- Javascript
- Python<br><br>

## **Technologies**<br>

### **Workspace**

- Gitpod was the IDE used to build the site.<br><br>

### **Version Control**

- Git was used for version control, committing and pushing to GitHub.

- Github was used to store the repository, files and images pushed from Gitpod.<br><br>

## **Website Design**

- [Google Fonts](https://fonts.google.com/) was used for the fonts on the site.

- [Bootstrap](https://getbootstrap.com/) was imported for responsiveness and styling of the site.<br><br>

## **Development**

- [Django](https://www.djangoproject.com/) was the web framework used to build the project.

- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest) was used to give forms improved styling.

- [Summernote](https://summernote.org/) for the forms to create the blog posts.

- [Allauth](https://django-allauth.readthedocs.io/en/latest/) to enable users to create accounts and log in. Allauth is a third-party Django application.<br><br>

## **Hosting**

- [Heroku](https://www.heroku.com/) is used to host the application.

- [Gunicorn](https://gunicorn.org/) for deploying the project to Heroku

- [Cloudinary](https://cloudinary.com/) was used for images and static files.

- [ElephantSQL](https://elephantsql.com/) to host the database. ElephantSQL is a cloud-based PostgreSQL database hosting service.<br><br>

## **Frameworks, Libraries and Tools Used**

- [Lucidchart](https://www.lucidchart.com/) for the UML Use Case Diagram.

- [AmIResponsive](https://www.amiresponsive.co.uk) was used for the responsiveness of the site.<br><br>

## **Testing**

The W3C Markup Validator, W3C CSS Validator Services, JS Hint and PEP8 were used to validate the code to ensure there were no syntax errors in the project.

### **HTML**
All HTML pages were checked using [W3CMarkupValidationService](https://validator.w3.org/)
- No errors were found.

### **CSS**
The CSS file was checked using [W3CCSSValidationService](https://jigsaw.w3.org/css-validator/)
- No errors were found.

### **Python**
The following python files were checked using [pep8CI](https://pep8ci.herokuapp.com/). No errors found apart from some lines too long in settings.py, env.py and blog urls.py files.:<br>
- admin.py<br>
- apps.py<br>
- asgi.py<br>
- env.py<br>
- forms.py<br>
- models.py<br>
- settings.py<br>
- tests.py<br>
- urls.py<br>
- views.py<br>
- wsgi.py<br>

### **Javascript**
The Javascript file was checked using [JSHint](https://jshint.com/)
- No errors were found.<br><br>

## **Code Formatting**
HTML formatted using [HTML Formatter](https://webformatter.com)<br><br>

## **Manual Testing**

### **Testing Tables**
- [Home Page](./readme-docs/manual-testing/home-page-testing.png)<br>
- [Post Detail Page](./readme-docs/manual-testing/blog-post-detail-page-testing.png)<br>
- [Post Detail Page Admin Access](./readme-docs/manual-testing/blog-post-detail-page-admin-contrib.png)<br>
- [Admin Page Approve/Delete Comments](./readme-docs/manual-testing/approve-and-delete-comments-test.png)<br>
- [Sign Up Page](./readme-docs/manual-testing/sign-up-page-form.png)<br>
- [Sign In Page](./readme-docs/manual-testing/sign-in-page-form.png)<br>
- [Sign Out Page](./readme-docs/manual-testing/sign-out-page.png)<br>
- [Blog Post Detail Page Admin Staff](./readme-docs/manual-testing/blog-post-detail-page-admin-contrib.png)<br>
- [Admin Page Delete Contributor](./readme-docs/manual-testing/admin-page-select-contrib-to-delete.png)
### **Post Detail Admin Page**
- [Post Detail Page Admin Change Post](./readme-docs/manual-testing/change-post-screen.png)<br>
### **Delete Post**
- [Post Detail Admin Delete Post](./readme-docs/manual-testing/admin-page-delete-selected-post.png)<br>
- [Post Detail Admin Delete Post 2](./readme-docs/manual-testing/are-you-sure-you-want-to-delete.png)<br>
- [Post Detail Admin Delete Post 3](./readme-docs/manual-testing/successfully-deleted-1-post.png)<br>
### **Delete Comment**
- [Admin Page Change Comment](./readme-docs/manual-testing/select-comment-to-change.png)<br>
- [Admin Page Delete Comment1](./readme-docs/manual-testing/delete-selected-comments.png)<br>
- [Admin Page Delete Comment2](./readme-docs/manual-testing/delete-comment-admin-screen.png)<br>
- [Admin Page Delete Comment3](./readme-docs/manual-testing/successfully-deleted-1-comment.png)<br>
### **Delete Contributor**
- [Admin Page Change Contributor](./readme-docs/manual-testing/select-contributor-to-change.png)<br>
- [Admin Page Delete Contributor 1](./readme-docs/manual-testing/delete-contrib-are-you-sure.png)<br>
- [Admin Page Delete Contributor 2](./readme-docs/manual-testing/successfully-delete-1-contributor.png)<br><br>

## **Manual Testing on Smaller Screen Sizes**

- As well as desktop, the blog site was tested on tablet and mobile screens also. Links and buttons were tested and are all functioning as expected.<br><br>

## **User Stories Testing**

To ensure the application is working and the functions are operating as expected, manual testing was also performed on user stories to verify that acceptance criteria was met.


**1.** As **project creator** I need to create the base setup of the application so that other features can be added.

_Acceptance Criteria_
- The project creator must be able to install django and it frameworks and libraries to set up the app
- THe project creator should be able to create an external database with ElephantSQL
- The project creator should be able to deploy the project to Heroku

_Test Performed_
- Followed steps in Code Institute Django Instruction Sheet
- When all steps completed correctly the screen "The Install Worked Successfully! Congratulations!" displayed<br><br>

**2.** As **site admin** I can create draft posts so that I can work on them and complete the content.

_Acceptance Criteria_
- Site admin can log in to the /admin URL with a superuser account
- Site admin can create draft posts and save them for publishing later in the admin panel

_Test Performed_
- Logged in to the /admin URL with the superuser account
- Can create draft posts and save them so that they can be published later<br><br>


**3.** As **site admin** I can create, read, update and delete particular posts, so that I can manage the content of the blog.

_Acceptance Criteria_
- Site admin can log in to the /admin URL with a superuser account
- Site admin can manage all posts logged in with a superuser account
- Site admin can manage all comments logged in with a superuser account

_Test Performed_
- Logged in to the /admin URL with the superuser account
- Can create, update and delete posts and comments with the superuser account<br><br>


**4.** As **site admin** I can approve comments, so that I can decide if a comment is suitable or unsuitable for viewing.

_Acceptance Criteria_
- Site admin can log in to the /admin URL with a superuser account
- Site admin can approve comments so they can be published under the blog posts
- Site admin can delete a comment if it is deemed unsuitable for publishing

_Test Performed_
- Logged in to the /admin URL with the superuser account
- Can click on comments and select ones that are awaiting approval and approve them
- Can delete unsuitable comments using the superuser account<br><br>

**5.** As a **site admin** I can configure the Administration page so that the view of this area of the blog is customized.

_This user story was a **"Could Have"** and time constraints didn't allow for it to be developed_<br><br>

**6.** As a **site admin** I can create, read, update and delete posts from the front end of the blog site, so that I can do this quickly without having to access the administration page.

_Acceptance Criteria_
- Site admin can log in on the blog site like other registered users
- Site admin can click on the "create post" link and create a new post and save it
- Site admin can click on "update post" to edit the post directly on the blog site
- Site admin can click on "delete post" to delete a post on the blog site without accessing the administration page

_Test Performed_
- Logged in to the blog site the same as other registered users
- Can click on "Create Post" link and create a new post and save it
- Can click on "Update Post" and "Delete Post" buttons to edit or delete the post<br><br>

**7.** As a **site user** I can view a list of blog posts so that I can choose which one I want to read.

_Acceptance Criteria_
- All posts are listed on the blog page
- Posts are sorted by date created
- Author, image, title and date created is displayed under each post
- Paginated view of 6 posts per page

_Test Performed_
- All posts are listed on the blog page and if the number of total posts exceeds six, a paginated view is displayed to the user with a "next" button.
- When clicked the "next" button brings the user to the next page where the other posts can be viewed together with a "previous" button which can be clicked to return to the first page of posts.
- The correct information is presented to the user for each blog post.
- Posts are sorted by date created and that any new blog posts are automatically added to the blog list.<br><br>

**8.** As a **site user** I can select a post to view its full content.

_Acceptance Criteria_
- Author, image, title, date created and blog content is displayed on screen
- Likes and comments can be viewed

_Test Performed_
- All posts on the blog and home page can be clicked and opened for full detail view
- The correct information is displayed to the user for each blog post<br><br>

**9.** As a **site user** I can view the comments on a particular post so that I can see the discussion about that post.

_Acceptance Criteria_
- All comments should be displayed when viewing a post
- Comments should be sorted by date created

_Test Performed_
- All users can view the comments section on the Post Detail page and all comments are displayed correctly
- Comments are sorted by date created<br><br>

**10.** As a **site user** I can set up an account so that I can comment on and like posts.

_Acceptance Criteria_
- To register, a user must enter a username and password (email is optional)
- User should not be able to register the same username more than once

_Test Performed_
- Username and password is required and that email is optional
- Registering with a username that has already been created returns a message "A user with that username already exists"<br><br>

**11.** As a **registered user** I can log into my account so that I can use my role specific features.

_Acceptance Criteria_
- Registered users can log in and enter username, email address (optional) and password
- Registered and logged in users can click on posts
- Registered and logged in users can leave comments
- Registered and logged in users can like posts
 
 _Test Performed_
- Can click on log in link and enter username, email address (optional) and password on sign in form
- Redirected to the blog site and can click on posts to read
- Can leave comments
- Can like posts<br><br>

**12.** As a **registered user** I can log out of my account so that I can keep my information secure and prevent unauthorized access.

_Acceptance Criteria_
- A user must be registered and logged in to be able to log out
- The logout link should redirect the user to the sign out page
- The user should be able to click the "Sign Out" button
- The user should be redirected to the home page
- A green alert message should display "You have signed out"

_Test Performed_
- After logging in, clicked on logout link on navigation bar
- Redirected to sign out page
- Clicked on sign out button
- Redirected to home page with green alert message "You have signed out"<br><br>

**13.** As a **registered user** I can add comments on a post so that I can join in the conversation.

_Acceptance Criteria_
- Registered and logged in users can leave comments on a post
- The name and date should be displayed with the comment

_Test Performed_
- Logged in users are presented with the comment form on the Post Detail page
- The comment form and submit button functions as expected, and when adding a new comment, it creates a green alert "Your comment is awaiting approval" message
- The comment functionality is only available to signed in users<br><br>

**14.** As a **registered user** I can like or unlike a post so that I can give feedback on the content.

_Acceptance Criteria_

- The user must be registered and logged in to like a post
- The like icon should include a matching icon for the toggle feature

 _Test Performed_
 - Signed in users can like posts on the Post Detail page and the like functionality is only available to logged in users
 - The like this post heart icon works as expected and the number of likes increases or decreases when adding or removing a like
 - The user cannot like a post more than once<br><br>

**15.** As a **registered user** I can add posts to favourites so that I can save them and read them later.

_This user story was also a **"Could Have"** and time constraints didn't allow for it to be developed_<br><br>

## **Bugs**

### **Pep8CI syntax errors**
- Line too line<br><br>

## **Deployment**

The project was developed in Gitpod. All the code was committed and pushed to Github where the repository was stored. The Code Institute template was used for the main structure of the repository. The project was deployed to Heroku. The process is outlined below:

### **Step 1:**
**1.** Install Django, supporting libraries and Cloudinary libraries using the following commands in the terminal:
````
pip3 install 'django<4' gunicorn
pip3 install dj_database_url psycopg2
pip3 install dj3-cloudinary-storage
````

**2.** Create the requirements file using the command below in the terminal:
`````
pip3 freeze --local > requirements.txt
`````

**3.** Create the project using the following command in the terminal:
`````
django-admin startproject YOUR_PROJECT_NAME .
`````

**4.** Create the app using this command in the terminal:
````
python3 manage.py startapp YOUR_APP_NAME
````

**5.** Add the installed apps to settings.py file
`````
INSTALLED_APPS = [
    …
    'YOUR_APP_NAME',
]
`````

**6.** Migrate the changes using this command in the terminal:
````
python3 manage.py migrate
````

**7.** Run the server to test using the following command in the terminal:
````
python3 manage.py runserver
````

### **Step 2:**
_Create a new external database_

**1.** Sign Up/Log In on [ElephantSQL](https://www.elephantsql.com/)

**2.** Click "Create New Instance"

**3.** Set up your plan
- Give your plan a name
- Select the Tiny Turtle (Free) plan
- Tags field can be left blank

**4.** Click "Select Region"
- Select a data center near you

**5.** Click "Review"
- Check that your details are correct. Then click "Create instance"

**6.** Go to ElephantSQL dashboard and click on your database project

**7.** Copy your ElephantSQL database URL

### **Step 3:**
_Create a Heroku app_

**1.** Sign Up/Log In on [Heroku](https://www.heroku.com/)

**2.** From the dashboard click on "New" and create a new Heroku App

**3.** Enter your app name and your location

**4.** Go to the settings tab

**5.** Click on "Reveal Config Vars"

**6.** Add a Config Var called DATABASE_URL
- The value should be the ElephantSQL database URL

### **Step 4:**
_Attach the database_

**1.** In GitPod create a new file called env.py on the top level directory

**2.** In the env.py file add these lines of code:
- Import os library
````
import os
````
- Set environment variables
````
os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"
````
- Add secret key
````
os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"
````

**3.** Go back to [Heroku](heroku.com)
- Add your secret key to Config Vars - SECRET_KEY, “randomSecretKey”

### **Step 5:**
_Prepare your environment and settings.py file_

**1.** In settings.py - reference env.py with this line of code:
````
from pathlib import Path
import os
import dj_database_url

if os.path.isfile("env.py"):
   import env
````

**2.** Remove the insecure secret key and replace - links to the SECRET_KEY variable on Heroku
````
SECRET_KEY = os.environ.get('SECRET_KEY')
````

**3.** Comment out the old ````DATABASES```` section.

**4.** Add a new ````DATABASES```` section _(links to the DATATBASE_URL variable on Heroku)_:
````
DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
````

**5.** Save all the files and make migrations in the terminal using this command:
````
python3 manage.py migrate
````

### **Step 6:**
_Get your static and media files stored on [Cloudinary](https://cloudinary.com/):_

**1.** Sign Up/Log In on [Cloudinary](https://cloudinary.com/) and copy your CLOUDINARY_URL from the Cloudinary dashboard.

**2.** Add Cloudinary URL to env.py:
````
os.environ["CLOUDINARY_URL"] = "cloudinary://************************"
````

**3.** Go back to [Heroku](heroku.com) and add Cloudinary URL to Heroku Config Vars
- CLOUDINARY_URL, cloudinary://************************

**4.** Add DISABLE_COLLECTSTATIC to Heroku Config Vars:
- DISABLE_COLLECTSTATIC, 1

**5.** In the settings.py, add Cloudinary libraries to INSTALLED_APPS in this order:
````
INSTALLED_APPS = [
    …,
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    …,
]
````

**6.** Make Django use Cloudinary to store media and static files:
````
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
````

**7.** Link file to the templates directory in Heroku
Place this under the BASE_DIR line:
````
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
````

**8.** Change the templates directory to TEMPLATES_DIR
````
TEMPLATES = [
    {
        …,
        'DIRS': [TEMPLATES_DIR],
       …,
            ],
        },
    },
]
````

**9.** Add Heroku Hostname to ALLOWED_HOSTS:
````
ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]
````

### **Step 7:**

**1.** In GitPod create 3 new folders on top level directory called:
- media
- static
- templates

**2.** Create a file called ````Procfile```` on the top level directory

**3.** In the Procfile add this code:
````
web: gunicorn PROJ_NAME.wsgi
````

**4.** In the Terminal Add, commit and push your files:
````
git add .
git commit -m “Deployment Commit”
git push
````

**5.** In Heroku go to the deploy tab.

**6.** Choose GitHub as deployment method and select your repository.

**7.** At the bottom of the page select Deploy branch (from the main branch).<br><br>

## **Production**

**1.** In your settings.py file, set DEBUG to False
````
DEBUG = False
````

**2.** Make sure that X_FRAME_OPTIONS and ALLOWED_HOSTS are added to your settings.py file.
````
X_FRAME_OPTIONS = 'SAMEORIGIN'

ALLOWED_HOSTS = ['your_app_name.herokuapp.com', 'localhost']
````

**3.** Go to Heroku, in Settings - Reveal Config Vars

**4.** Remove DISABLE_COLLECTSTATIC

**5.** On Heroku, go to Deploy tab and scroll to the bottom of the page and select Deploy(Main branch)

**6.** Click "View App" when the build is done.<br><br>

## **Content**
### **Blog Posts**
- Report: Music in the Metaverse - ludwig-van.com
- Chopin - classicfm.com
- McDonald's restaurant in Wales to play Beethoven to tackle late night anti-social behaviour - classicfm.com
- Report: Could Music Therapy Help in tte Fight Against the Effects of Covid19 - ludwig-van.com
- 2023 Oscar Nominees announced for Original Score - classical-music.com
- New Study: Playing the Piano Boosts Brain Processing Power - pianostreet.com
### **Images**
- Default Orchestra image - Pixabay
- Oscars Image - rd.com
- Orchestra Image - ludwig-van.com
- Beethoven McDonald's Image - classicfm.com
- Girl playing the piano - commons.wikimedia.org
- Woman wearing VR Headset - Pixabay<br><br>

## **Credits**
- My mentor for his continued guidance, help, feedback and support
- The friendly and helpful tutor support team at Code Institute
- My Course Facilitator for continued motivational support and guidance

------
