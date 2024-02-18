# treehacks





# THE PLAN


- Parse a list of actions that replicate the twitter interface



Checklist:
- Project Setup
- Page Definitions
- Basic UI Setup
- States setup for user auth
- Create context for documentation and actions


# top level interface

- Defines all the pages
- README that defines the pages, purposes, etc
- High level breakdown
- calls functions and renders objects on components further down


# second level components
- Functions: implements the functions called by the top level, as well as necessary fetching of data
- defines components being used
- Comes with ReadME defining all the functions available and its uses
- Defines each page's states???





# process:

Requires:

python3 -m venv .venv
source .venv/bin/activate
pip install reflex
reflex init


then run and deploy






Notes:

rx.config.py file defines the app name and ports. can be replaced by .env file


Generation:
Starts with UI components
Adds dependencies to a stack (abstractions that need to be implemented in the second pass)
Implements abstractions





Checklist:

1. GPT To write the schema from a config description of the schema
2. To get GPT to define the pages from the config layout through reflex syntax
3. Get GPT to define the necessary UI components it needs for each page based off of an existing list of pre-built UI components passed through as context

Goes page by page from the configuration file



4. Actions, data, user auth, events, conditions