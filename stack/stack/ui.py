import os
from datetime import datetime
from typing import Any, Optional, Set

import requests

import reflex as rx

from stack import styles

from reflex.vars import Var

from stack.state import State


class Spline(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[str] = "https://prod.spline.design/Br2ec3WwuRGxEuij/scene.splinecode"
    is_default = True

    lib_dependencies: list[str] = ["@splinetool/runtime"]


spline = Spline.create


def spline_component():
    return rx.chakra.center(
        rx.center(
            spline(),
            overflow="hidden",
            width="42em",
            height="42em",
        ),
        width="100%",
        display=["none", "none", "flex", "flex", "flex", "flex"],
    )


def navbar(name1, link1, name2, link2, name3, link3) -> rx.Component:
    """Create the navbar component.
    """


    # Create the navbar component.
    return rx.vstack(
        rx.box(
            rx.hstack(
                rx.image(src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600", width="2em", margin='0 2em 0 2em'),
                rx.hstack(
                    rx.link(
                        name1,
                        href=link1,
                        style=styles.NAV_TEXT_STYLE,
                        display=["none", "none", "none", "flex", "flex", "flex"],
                        margin='0 1em 0 0'
                    ),
                    rx.link(
                        name2,
                        href=link2,
                        style=styles.NAV_TEXT_STYLE,
                        display=["none", "none", "none", "flex", "flex", "flex"],
                        margin='0 1em 0 0'
                    ),
                    rx.link(
                        name3,
                        href=link3,
                        style=styles.NAV_TEXT_STYLE,
                        display=["none", "none", "none", "none", "flex", "flex"],
                        margin='0 1em 0 0'
                    ),
                ),
                justify="start",
                padding_x=styles.PADDING_X,
            ),
            bg="rgba(255,255,255, 0.8)",
            backdrop_filter="blur(10px)",
            padding_y=["0.8em", "0.8em", "0.5em"],
            border_bottom="1px solid #F4F3F6",
            width="100%",
        ),
        position="sticky",
        z_index="999",
        top="0",
        width="100%",
        spacing="0",
    )



def hero(title, subtitle, cta, action):
    """
    Landing page that takes in a title text and subtitle text
    """
    return rx.container(
        rx.chakra.hstack(
            rx.center(
                rx.chakra.vstack(
                    rx.chakra.text(
                        rx.chakra.span("[", color="#DACEEE"),
                        rx.chakra.span("Frontend", color="#696287"),
                        rx.chakra.span("]", color="#DACEEE"),
                        rx.chakra.span("[", color="#DACEEE"),
                        rx.chakra.span("Backend", color="#696287"),
                        rx.chakra.span("]", color="#DACEEE"),
                        rx.chakra.span("[", color="#DACEEE"),
                        rx.chakra.span("Hosting", color="#696287"),
                        rx.chakra.span("]", color="#DACEEE"),
                        font_family=styles.MONO,
                        mb=2,
                    ),
                    rx.chakra.text(
                        title,
                        font_family=styles.MONO,
                        font_style="normal",
                        font_weight="600",
                        font_size="5xl",
                        line_height="1.2",
                        letter_spacing="-0.02em",
                    ),
                    rx.chakra.text(
                        subtitle,
                        color="#342E5C",
                        font_size="1.1em",
                        font_family=styles.MONO,
                        padding_top="1em",
                    ),
                    rx.cond(
                        True,
                        rx.chakra.wrap(
                            rx.chakra.input_group(
                                rx.chakra.input(
                                    placeholder="Your email address...",
                                    #on_blur=IndexState.set_email,
                                    style=styles.INPUT_STYLE,
                                    type="email",
                                ),
                                style=styles.INPUT_STYLE,
                            ),
                            rx.chakra.button(
                                cta,
                                on_click=action,
                                style=styles.ACCENT_BUTTON,
                            ),
                            justify="left",
                            should_wrap_children=True,
                            spacing="1em",
                            padding_x=".25em",
                            padding_y="1em",
                        )
                    ),
                    align_items="left",
                    padding="1em",
                ),
                width="100%",
            ),
            spline_component(),
        ),
        padding_top="6em",
        padding_bottom="6em",
        width="100%",
    )



def stat(number, icon, metric):
    """A statistic."""
    return rx.chakra.vstack(
        rx.heading(number, color="#DACEEE"),
        rx.chakra.hstack(
            rx.image(
                src=f"/landing_icons/stats_icons/{icon}.svg",
                height="1em",
            ),
            rx.chakra.text(
                metric,
                color="#82799E",
                text_align="center",
            ),
        ),
        padding_x="2em",
    )


def format_with_commas(number):
    return "{:,}+".format(number)

def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.chakra.container(
        *children,
        **kwargs,
    )

def gallery(main_text, stat_1, stat_1_label, stat_2, stat_2_label, stat_3, stat_3_label):
    return rx.center(
        container(
            rx.chakra.vstack(
                rx.center(
                    rx.chakra.text(
                        main_text,
                        font_family=styles.MONO,
                        font_size=styles.H2_FONT_SIZE,
                        font_weight=styles.BOLD_WEIGHT,
                        text_align="center",
                        color="white",
                    ),
                    width="55%",
                    padding_bottom="2em",
                    padding_top="6em",
                ),
                rx.desktop_only(
                    rx.flex(
                        rx.chakra.spacer(),
                        stat(
                            format_with_commas(stat_1),
                            "project",
                            stat_1_label,
                        ),
                        stat(
                            format_with_commas(stat_2),
                            "github",
                            stat_2_label,
                        ),
                        stat(
                            format_with_commas(stat_3),
                            "discord",
                            stat_3_label,
                        ),
                        rx.chakra.spacer(),
                        height="100%",
                        min_height="10em",
                        width="100%",
                        margin_x="2em",
                    ),
                ),
                rx.mobile_and_tablet(
                    rx.chakra.vstack(
                        rx.chakra.vstack(
                            rx.heading(
                                format_with_commas(stat_1),
                                color="#DACEEE",
                            ),
                            rx.image(
                                src="/landing_icons/stats_icons/project.svg",
                                height="1em",
                            ),
                            rx.chakra.text(
                                stat_1_label,
                                color="#82799E",
                                text_align="center",
                            ),
                        ),
                        rx.chakra.vstack(
                            rx.heading(
                                format_with_commas(stat_2),
                                color="#DACEEE",
                            ),
                            rx.image(
                                src="/landing_icons/stats_icons/github.svg",
                                height="1em",
                            ),
                            rx.chakra.text(
                                stat_2_label, color="#82799E", text_align="center"
                            ),
                        ),
                        rx.chakra.vstack(
                            rx.heading(
                                format_with_commas(stat_3), color="#DACEEE"
                            ),
                            rx.image(
                                src="/landing_icons/stats_icons/discord.svg",
                                height="1em",
                            ),
                            rx.chakra.text(
                                stat_3_label,
                                color="#82799E",
                                text_align="center",
                            ),
                        ),
                        height="100%",
                        min_height="10em",
                        width="100%",
                    ),
                ),
                padding="2em",
            ),
            width="100%",
        ),
        bg="#110F1F",
        width="100%",
    )




boxstyles = {}


stylebox = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/icon2.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Completely customizable",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "All Reflex components are fully customizable. Change the colors, fonts, and styles to match your project.",
            color="#342E5C",
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)

reactbox = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/icon3.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Custom Components",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "Create your own components in a few lines of code. Simply wrap the React component of your choice.",
            color="#342E5C",
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)

powerful = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/icon4.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Now everyone can work across the full-stack",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "With Reflex every engineer can work across the whole stack allowing for a more efficient and productive workflow.",
            color="#342E5C",
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)


def features(title, subtitle, feature, t1,d1,t2,d2,t3,d3,t4,d4):
    return rx.chakra.box(
        container(
            height="8em",
            width="100%",
            background="radial-gradient(55.39% 67.5% at 50% 100%, rgba(188, 136, 255, 0.16) 0%, rgba(255, 255, 255, 0) 100%);",
            opacity="0.4;",
            transform="matrix(1, 0, 0, -1, 0, 0);",
        ),
        container(
            rx.chakra.vstack(
                rx.chakra.box(
                    rx.chakra.text(
                        "[",
                        rx.chakra.span(feature, bg="#F5EFFE", color="#5646ED"),
                        "]",
                        color="#5646ED",
                        font_family=styles.MONO,
                    )
                ),
                rx.heading(
                    title,
                    font_size=styles.H3_FONT_SIZE,
                    font_family=styles.MONO,
                ),
                rx.chakra.text(
                    subtitle,
                    color="#342E5C",
                    max_width="50%",
                ),
                rx.chakra.hstack(
                        rx.chakra.vstack(
                            rx.chakra.hstack(
                                rx.chakra.hstack(
                                    rx.image(
                                        src="/landing_icons/icon1.svg",
                                        height="4em",
                                        width="4em",
                                    ),
                                    rx.chakra.vstack(
                                        rx.chakra.text(
                                            t1,
                                            font_size=styles.TEXT_FONT_SIZE,
                                            font_weight=styles.BOLD_WEIGHT,
                                        ),
                                        rx.chakra.text(
                                            d1,
                                            color="#342E5C",
                                        ),
                                        align_items="left",
                                        width="100%",
                                    ),
                                    style=boxstyles,
                                    align_items="left",
                                    spacing="1em",
                                    width="100%",
                                ),
                                rx.chakra.hstack(
                                    rx.image(
                                        src="/landing_icons/icon2.svg",
                                        height="4em",
                                        width="4em",
                                    ),
                                    rx.chakra.vstack(
                                        rx.chakra.text(
                                            t2,
                                            font_size=styles.TEXT_FONT_SIZE,
                                            font_weight=styles.BOLD_WEIGHT,
                                        ),
                                        rx.chakra.text(
                                            d2,
                                            color="#342E5C",
                                        ),
                                        align_items="left",
                                        width="100%",
                                    ),
                                    style=boxstyles,
                                    align_items="left",
                                    spacing="1em",
                                    width="100%",
                                ),
                                spacing="2em",
                                height="100%",
                            ),
                            rx.chakra.hstack(
                                rx.chakra.hstack(
                                    rx.image(
                                        src="/landing_icons/icon3.svg",
                                        height="4em",
                                        width="4em",
                                    ),
                                    rx.chakra.vstack(
                                        rx.chakra.text(
                                            t3,
                                            font_size=styles.TEXT_FONT_SIZE,
                                            font_weight=styles.BOLD_WEIGHT,
                                        ),
                                        rx.chakra.text(
                                            d3,
                                            color="#342E5C",
                                        ),
                                        align_items="left",
                                        width="100%",
                                    ),
                                    style=boxstyles,
                                    align_items="left",
                                    spacing="1em",
                                    width="100%",
                                ),
                                rx.chakra.hstack(
                                    rx.image(
                                        src="/landing_icons/icon4.svg",
                                        height="4em",
                                        width="4em",
                                    ),
                                    rx.chakra.vstack(
                                        rx.chakra.text(
                                            t4,
                                            font_size=styles.TEXT_FONT_SIZE,
                                            font_weight=styles.BOLD_WEIGHT,
                                        ),
                                        rx.chakra.text(
                                            d4,
                                            color="#342E5C",
                                        ),
                                        align_items="left",
                                        width="100%",
                                    ),
                                    style=boxstyles,
                                    align_items="left",
                                    spacing="1em",
                                    width="100%",
                                ),
                                height="100%",
                                spacing="2em",
                            ),
                            padding_bottom="2em",
                            width="100%",
                            spacing="2em",
                        ),
                    padding_y="2em",
                ),
                padding_bottom="2em",
                align_items="left",
            )
        ),
        bg="rgba(247, 247, 250, 0.6);",
    )


battery_icon = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/battery-icon.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Batteries included",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "Skip the boilerplate and get started faster. Reflex integrates the frontend and backend so there is no need to write API endpoints.",
            color="#342E5C",
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)

orm_icon = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/orm-icon.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Built in database ORM",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "Integrate with existing databases with a single line of code. Or use our built in SQLite database.",
            color="#342E5C",
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)

python_icon = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/python-icon.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Seamlessly integrate with any Python library",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "Never get locked into a framework that doesn't support your existing tech stack.",
            color="#342E5C",
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)





def auth_layout(*args):
    """The shared layout for the login and sign up pages."""
    return rx.box(
        container(
            rx.vstack(
                rx.heading("Welcome!", size="8"),
                rx.heading("Sign in or sign up to get started.", size="8"),
                align="center",
            ),
            *args,
            border_top_radius="10px",
            box_shadow="0 4px 60px 0 rgba(0, 0, 0, 0.08), 0 4px 16px 0 rgba(0, 0, 0, 0.08)",
            display="flex",
            flex_direction="column",
            align_items="center",
            padding_top="50px",
            padding_bottom="24px",
            spacing="4",
        ),
        height="100vh",
        padding_top="40px",
        background="url(bg.svg)",
        background_repeat="no-repeat",
        background_size="cover",
    )


def signup():
    """The sign up page."""
    return auth_layout(
        rx.box(
            rx.vstack(
                rx.input(
                    placeholder="Username",
                    on_blur=State.set_username,
                    size="3",
                ),
                rx.input(
                    type="password",
                    placeholder="Password",
                    on_blur=State.set_password,
                    size="3",
                ),
                rx.input(
                    type="password",
                    placeholder="Confirm password",
                    on_blur=State.set_confirm_password,
                    size="3",
                ),
                rx.button(
                    "Sign up",
                    on_click=State.signup,
                    size="3",
                    width="6em",
                ),
                spacing="4",
            ),
            align_items="left",
            background="white",
            border="1px solid #eaeaea",
            padding="16px",
            width="400px",
            border_radius="8px",
        ),
        rx.text(
            "Already have an account? ",
            rx.link("Sign in here.", href="/"),
            color="gray",
        ),
    )


def login():
    """The login page."""
    return auth_layout(
        rx.box(
            rx.vstack(
                rx.input(
                    placeholder="Username",
                    on_blur=State.set_username,
                    size="3",
                ),
                rx.input(
                    type="password",
                    placeholder="Password",
                    on_blur=State.set_password,
                    size="3",
                ),
                rx.button("Log in", on_click=State.login, size="3", width="5em"),
                spacing="4",
            ),
            align_items="left",
            background="white",
            border="1px solid #eaeaea",
            padding="16px",
            width="400px",
            border_radius="8px",
        ),
        rx.text(
            "Don't have an account yet? ",
            rx.link("Sign up here.", href="/register"),
            color="gray",
        ),
    )



def avatar(name: str):
    return rx.avatar(fallback=name[:2], size="4")


def tab_button(name, href):
    """A tab switcher button."""
    return rx.link(
        rx.flex(rx.icon(tag="star"), margin_right="1rem"),
        name,
        display="inline-flex",
        align_items="center",
        padding="0.75rem",
        href=href,
        border="1px solid #eaeaea",
        font_weight="semibold",
        border_radius="2rem",
    )


def tabs():
    """The tab switcher displayed on the left."""
    return rx.box(
        rx.vstack(
            rx.heading("PySocial", size="5"),
            tab_button("Home", "/"),
            rx.box(
                rx.heading("Followers", size="3"),
                rx.foreach(
                    State.followers,
                    lambda follow: rx.vstack(
                        rx.hstack(
                            avatar(follow.follower_username),
                            rx.text(follow.follower_username),
                        ),
                        padding="1em",
                    ),
                ),
                padding="2rem",
                border_radius="0.5rem",
                border="1px solid #eaeaea",
            ),
            rx.button("Sign out", on_click=State.logout, size="3"),
            align_items="left",
            spacing="4",
        ),
        padding_top="2rem",
        padding_bottom="2rem",
    )


def sidebar(HomeState):
    """The sidebar displayed on the right."""
    return rx.vstack(
        rx.input(
            on_change=HomeState.set_friend,
            placeholder="Search users",
            width="100%",
        ),
        rx.foreach(
            HomeState.search_users,
            lambda user: rx.vstack(
                rx.hstack(
                    avatar(user.username),
                    rx.text(user.username),
                    rx.spacer(),
                    rx.button(
                        rx.icon(tag="plus"),
                        on_click=lambda: HomeState.follow_user(user.username),
                    ),
                    width="100%",
                ),
                padding_top="1rem",
                padding_bottom="1rem",
                width="100%",
            ),
        ),
        rx.box(
            rx.heading("Following", size="3"),
            rx.foreach(
                HomeState.following,
                lambda follow: rx.vstack(
                    rx.hstack(
                        avatar(follow.followed_username),
                        rx.text(follow.followed_username),
                    ),
                    padding="1em",
                ),
            ),
            padding="2rem",
            border_radius="0.5rem",
            border="1px solid #eaeaea",
            width="100%",
        ),
        align_items="start",
        spacing="4",
        height="100%",
        padding_top="2rem",
        padding_bottom="2rem",
    )


def feed_header(HomeState):
    """The header of the feed."""
    return rx.hstack(
        rx.heading("Home", size="5"),
        rx.input(on_change=HomeState.set_search, placeholder="Search tweets"),
        justify="between",
        padding="1.5rem",
        border_bottom="1px solid #ededed",
    )


def composer(HomeState):
    """The composer for new tweets."""
    return rx.grid(
        rx.vstack(
            avatar(State.user.username),
            padding="1.5rem",
        ),
        rx.box(
            rx.flex(
                rx.text_area(
                    width="100%",
                    placeholder="What's happening?",
                    resize="none",
                    _focus={"border": 0, "outline": 0, "boxShadow": "none"},
                    on_blur=HomeState.set_tweet,
                ),
                padding_y="1.5rem",
                padding_right="1.5rem",
            ),
            rx.hstack(
                rx.button(
                    "Tweet",
                    on_click=HomeState.post_tweet,
                    radius="full",
                    size="3",
                ),
                justify_content="flex-end",
                border_top="1px solid #ededed",
                padding_inline_start="1.5em",
                padding_inline_end="1.5em",
                padding_top="0.75rem",
                padding_bottom="0.75rem",
            ),
        ),
        grid_template_columns="1fr 5fr",
        border_bottom="1px solid #ededed",
    )


def tweet(tweet):
    """Display for an individual tweet in the feed."""
    return rx.grid(
        rx.vstack(
            avatar(tweet.author),
        ),
        rx.box(
            rx.vstack(
                rx.text("@" + tweet.author, font_weight="bold"),
                rx.text(tweet.content, width="100%"),
                align_items="left",
            ),
        ),
        grid_template_columns="1fr 5fr",
        padding="1.5rem",
        spacing="1",
        border_bottom="1px solid #ededed",
    )


def feed(HomeState):
    """The feed."""
    return rx.box(
        feed_header(HomeState),
        composer(HomeState),
        rx.cond(
            HomeState.tweets,
            rx.foreach(
                HomeState.tweets,
                tweet,
            ),
            rx.vstack(
                rx.button(
                    rx.icon(
                        tag="rotate-cw",
                    ),
                    rx.text("Click to load tweets"),
                    on_click=HomeState.get_tweets,
                ),
                padding="1.5rem",
            ),
        ),
        border_left="1px solid #ededed",
        border_right="1px solid #ededed",
        height="100%",
    )


def home():
    """The home page."""
    return container(
        rx.grid(
            tabs(),
            feed(State),
            sidebar(State),
            grid_template_columns="1fr 2fr 1fr",
            height="100vh",
            spacing="4",
        ),
        max_width="1300px",
    )
