A .vly file contains the following:

```
[DESCRIPTION] (requires description of the company and the purpose of the site)

Company information: (insert)
Website Description: (insert)

[FEATURES] (requires breakdown of each feature on the site specifically)
The website features the following user flow: (insert)

[DATA STRUCTURES] (requires database schema that covers the features and purpose)
(example:)
blog: title (str), content (str), image (img), views (int), author (user)
user: email (str), password (str), name, list of blogs


[PAGES] (requires page breakdown and description that covers the features, purpose, and data structure)

(example:)
Home (root): Main landing page where the user can view the company information, details, vision, marketing, and more. The user can also read most recent blog articles and most viewed articles written by other users. When logged in, the user can view their drafted blogs as well as published blogs, and click on them to edit them.

Auth: The authentication page, where the user can log in or sign up. Logging in requires just an email and password, while signing up requires an email and password confirmation.

Write (blog id): The page where the user can write and edit their blog articles. The blog articles save to the database after the user clicks off and if the value of the text is different. The blog articles can then be published, deleted, or viewed for the reading page. The blog id is the database id of the blog article. The user must be verified to be the author in order to edit, save, publish, etc.

Read (blog id): The page where the user can read blog articles. If the user is the author, they can also press a edit button that appears. At the bottom, recommended articles include most recent as well as top viewed articles.


[SHARED UI COMPONENTS] (requires breakdown of re-usable ui components shared across pages)
Nav Bar: When logged out, it contains a discord link to the discord server, and when logged in, it contains the discord link,
log out link, and share link.


[PAGE: home]
States:
Events:

UI:
Template { (example of what goes inside a component)
    Conditionals: 
    Text Parameters: 
    Actions: 
}
Nav Bar
Hero {
    Hidden when the user is logged in
    Title displays "Create a full stack web app in 1 click" and the subtitle displays "Ship 100x faster and cheaper"
    Call to action adds their email to a waitlist and the button says "Join"
}


[PAGE: auth]


[PAGE: write/[id]]


[PAGE: read/[id]]

etc


```