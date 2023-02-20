<!-- Heading -->

# Symphony ![View the live site here](https://)

## Introduction

Symphony is a fully responsive classical music blog website. Users have the ability to like and comment on posts.

![Am I Responsive](./assets/documentation/responsive-view.png)

## Design

I used an agile project management method, together with the MoSCoW prioritization method, to help me plan and track my work effectively. I set up a project in Github and created a template for user stories. The user stories are categorized and labelled as essential - "Must Have", desirable - "Should Have" and nice to have but not essential - "Could Have". Milestones were created and the user stories are attached to the milestones they pertain to. The user stories were then added to a kanban board which has three columns, To Do, In Progress and Done. All user stories are initially placed in the To Do column and when work commences on the project some user stories are transferred to the In Progress column. When work is completed on each user story they are then moved across to the Done column.
<br>

## User Experience

### User Stories
<br>

### Project Creator

- As the project creator I need to create the base setup of the application so that other features can be added.
<br>

### Admin/Site Staff

- As site admin/staff I can create draft posts so that I can work on them and complete the content.
- As site admin/staff I can create, read, update and delete particular posts, so that I can manage the content of the blog.
- As site admin/staff I can approve comments, so that I can decide if a comment is suitable or unsuitable for viewing.
<br>

### Site User

- As a site user I can view a list of blog posts so that I can choose which one I want to read.
- As a site user I can select a post to view its full content.
- As a site user I can view the comments on a particular post so that I can see the discussion about that post.
- As a site user I can set up and account so that I can comment on and like posts.
<br>

### Logged in User

- As a logged in user I can log into my account so that I can use my role specific features.
- As a logged in user I can log out of my account so that I can keep my information secure and prevent unauthorized access.
- As a logged in user I can add comments on a post so that I can join in the conversation.
- As a logged in user I can like or unlike a post so that I can give feedback on the content.
<br>

### Color Scheme
The main colours used throughout the blog were black, white, and grey. This creates a clean and easy-to-navigate look for the blog. 
<br>

### Typography

The main font used is called 'Roboto Slab'. The font used for the blog name is 'Mea Culpa'.

### Database

The database is a PostgreSQL database, hosted on [ElephantSQL](https:www.elephantsql.com/).

### Models

- [Database models](#database-models)






To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

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
