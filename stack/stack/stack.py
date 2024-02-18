"""Entry Point"""

from rxconfig import config


import reflex as rx
from stack.ui import navbar, hero, gallery, features, signup, login




def register() -> rx.Component:
    return rx.chakra.box(
        navbar('Home', '/', 'Login', 'signin', 'Register', 'register'),
        signup()
    )


def signin() -> rx.Component:
    return rx.chakra.box(
        navbar('Home', '/', 'Login', 'signin', 'Register', 'register'),
        login()
    )

def index() -> rx.Component:
    return rx.chakra.box(
        navbar('Home', '/', 'Login', 'signin', 'Register', 'register'),
        hero('Generate A Full-Stack SaaS App in 1 Click','Let AI write code for you. 100x faster and 100x cheaper than you average developer.','See it in action', rx.redirect("/register")),
        rx.chakra.container(rx.chakra.divider(border_color="#F4F3F6")),
        features(
            'Production-Ready SaaS Software','We take care of writing code, deploying, and hosting','Stop Coding',
            'Built In SaaS Made Reliably','Automatically integrates stripe, email, user auth, databases, and more!',
            'Create an app in under an hour','Stop spending weeks. Stop spending thousands of dollars.',
            'Constantly Expanding Capabilities','Each day, we add more components that expand what is possible',
            'No Programming Skills Needed','Our AI will do all the work for you so you can focus on what matters most: your customers.'),
        gallery('Build with vly.ai',100,'Integrations Coming Soon',1000000,'Apps Waiting to be Built',400000000,'Expected industry savings in software costs'),

        height="100vh",
    )


app = rx.App()  
app.add_page(index)
app.add_page(register)
app.add_page(signin)
