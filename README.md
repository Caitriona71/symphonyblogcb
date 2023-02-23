<!-- Heading -->

# Symphony ![View the live site here](https://)

## Introduction

Symphony is a fully responsive classical music blog website. Users have the ability to like and comment on posts.

![Am I Responsive](./assets/documentation/responsive-view.png)

## Design

An agile project management method was used, together with the **MoSCoW** prioritization method, to help me plan and track my work effectively. I set up a project in Github and created a template for user stories. The user stories are categorized and labelled as essential - **Must Have**, desirable - **Should Have** and nice to have but not essential - **Could Have**. **Milestones** were created and the user stories are attached to the milestones they pertain to. The user stories were then added to a kanban board which has three columns, **ToDo**, **In Progress** and **Done**. All user stories are initially placed in the **ToDo** column and when work commences on the project some user stories are transferred to the **In Progress** column. When work is completed on each user story they are then moved across to the **Done** column.

## User Experience

### User Stories

### Project Creator

- As **project creator** I need to create the base setup of the application so that other features can be added.

### Admin/Site Staff

- As **site admin/staff** I can create draft posts so that I can work on them and complete the content.
- As **site admin/staff** I can create, read, update and delete particular posts, so that I can manage the content of the blog.
- As **site admin/staff** I can approve comments, so that I can decide if a comment is suitable or unsuitable for viewing.

### Site User

- As a **site user** I can view a list of blog posts so that I can choose which one I want to read.
- As a **site user** I can select a post to view its full content.
- As a **site user** I can view the comments on a particular post so that I can see the discussion about that post.
- As a **site user** I can set up and account so that I can comment on and like posts.

### Logged in User

- As a **logged in user** I can log into my account so that I can use my role specific features.
- As a **logged in user** I can log out of my account so that I can keep my information secure and prevent unauthorized access.
- As a **logged in user** I can add comments on a post so that I can join in the conversation.
- As a **logged in user** I can like or unlike a post so that I can give feedback on the content.

### Color Scheme

The main colours used throughout the blog were black, white, and grey. This creates a clean and easy-to-navigate look for the blog. 

### Typography

The main font used is 'Roboto Slab'. The font used for the blog name is 'Mea Culpa'.

### Database

The database is a PostgreSQL database, hosted on [ElephantSQL](https:www.elephantsql.com/).

### Models

[Post Database Model](./readme-docs/database-models/posts-model.png)<br>
[Comments Database Model](./readme-docs/database-models/comments-model.png)<br>
[Contributors Database Model](./readme-docs/database-models/contributors-model.png)


## Technologies

### Workspace

#### Gitpod
[GitPod](https://gitpod.io) was the IDE workspace used to build the site.

### Version Control

#### Git
[Git](https://git-scm.com/) was used for version control, committing and pushing to GitHub.

### GitHub
[GitHub](https://github.com/) was used to store the repository, files and images pushed from Gitpod.

## Website Design

#### Google Fonts
[Google Fonts](https://fonts.google.com/) was used for the fonts on the site.

#### Bootstrap

[Bootstrap](https://getbootstrap.com/) was imported for responsiveness and styling of the site.

### Development

#### Django
[Django](https://www.djangoproject.com/) was the web framework used to build the project.

#### Django Crispy Forms
[Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest) was used to give forms improved styling.

#### Summernote
[Summernote](https://summernote.org/) for the forms to create the blog posts.

#### Allauth
[Allauth](https://django-allauth.readthedocs.io/en/latest/) to enable users to create accounts and log in. Allauth is a third-party Django application.

## Hosting

### Heroku
[Heroku](https://www.heroku.com/) is used to host the application.

### Gunicorn
[Gunicorn](https://gunicorn.org/) for deploying the project to Heroku

### Cloudinary
[Cloudinary](https://cloudinary.com/) was used for images and static files.

### ElephantSQL
[ElephantSQL](https://elephantsql.com/) to host the database. ElephantSQL is a cloud-based PostgreSQL database hosting service.

## Frameworks, Libraries and Tools Used

[Lucidchart](https://www.lucidchart.com/) for the UML Use Case Diagram.

[AmIResponsive](https://www.amiresponsive.co.uk) was used for the responsiveness of the site.

## Testing

The W3C Markup Validator, W3C CSS Validator Services, JS Hint and PEP8 were used to validate the code to ensure there were no syntax errors in the project.

### HTML
[W3CMarkupValidationService](https://validator.w3.org/)

### CSS
[W3CCSSValidationService](https://jigsaw.w3.org/css-validator/)

#### Javascript
[JSHint](https://jshint.com/)

## Manual Testing

### Home Page
|Test                               |Test Performed                 |Expected Result                |Result|
|-----------------------------------|-------------------------------|-------------------------------|------
| Navbar Register                   | Click Link                    | Redirects the user to the Sign Up page|Pass   
| Navbar Login                      | Click Link                    | Takes the user to the Sign In page|Pass   
| Navbar small/medium screens       | Click hamburger icon          | Login, Sign Up, Logout and About Us can be clicked and work the same as on large screens|Pass
| Navbar About Us                   | Click Link                    | Takes the user to the About Us page|Pass

### Sign Up Page/Form
|Test                                  |Test Performed                 |Expected Result                |Result|
|--------------------------------------|-------------------------------|-------------------------------|------
| Log In Link                          | Click Link                    | Redirects the user to the Sign In page|Pass
| Sign Up Form Works                   | Enter Username and Password   | The Django registration form is validating automatically if the username is valid and if the passwords match and are valid. Otherwise an error message is shown. The user is then redirected to the home page and a green alert message "Successfully signed in as <i>(username entered on previous page)</i>" is displayed. |Pass
| Navbar Logout                        | Click Link                   | Redirects the user to the Sign Out page|Pass
### Sign Out Page
|Test                               |Test Performed                 |Expected Result                |Result|
|-----------------------------------|-------------------------------|-------------------------------|------
| Sign Out Button                   | Click Button                  | Redirects the user to the Home page and displays green "You have signed out" alert message|Pass

### Sign In Page
|Test                               |Test Performed                 |Expected Result                |Result|
|-----------------------------------|-------------------------------|-------------------------------|------
| Sign Up Link                      | Click Link                    | Redirects the user to the Sign Up page|Pass
| Sign In Form Works                | Enter Username and Password   | The Django registration form is validating automatically if the username is valid and if the passwords match and are valid. The user is redirected to the home page. Otherwise an error message is shown.|Pass
| Log In Link                       | Click Link                    | Redirects the user to the Home page with green "Successfully signed in as <i>(username entered on previous screen)</i>" alert message|Pass|
| Navbar Logout                     | Click Link                    | Redirects the user to the Sign Out page|Pass















To log in:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked



------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
