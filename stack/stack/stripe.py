"""The payment page."""
import reflex as rx
import stripe

from state import State

stripe.api_key = "sk_test_your_stripe_key"

load_stripe = """
const stripePromise = loadStripe('pk_test_your_stripe_key');
"""


class StripeElements(rx.Component):
    """Stripe elements."""

    library = "@stripe/react-stripe-js"
    tag = "Elements"

    options: dict = {}

    def _get_custom_code(self) -> str | None:
        return super()._get_custom_code() or "" + load_stripe

    def _get_imports(self):
        return rx.utils.imports.merge_imports(  # type: ignore
            super()._get_imports()
            | {
                "@stripe/stripe-js": {rx.vars.ImportVar(tag="loadStripe")},
            }
        )

    def _render(self):
        return (
            super()
            ._render()
            .add_props(
                stripe=rx.vars.BaseVar(_var_name="stripePromise"),  # type: ignore
            )
        )


class PaymentElement(rx.Component):
    """Stripe payment element component."""

    library = "@stripe/react-stripe-js"
    tag = "PaymentElement"


stripe_elements = StripeElements.create
payment_element = PaymentElement.create


class PaymentState(State):
    """The payment page state."""

    @rx.var
    def client_secret(self) -> str:
        """The client secret for the payment intent."""
        session = stripe.PaymentIntent.create(
            amount=200000,
            currency="usd",
            payment_method_types=["card"],
            payment_method="pm_card_visa",
            confirm=True,
            return_url="http://localhost:8000/payment?session_id={CHECKOUT_SESSION_ID}",
        )
        return session.client_secret or ""


def payment() -> rx.Component:
    """The payment page."""
    return rx.fragment(
        rx.vstack(
            rx.text("Hosting premium plan", font_size="1em", font_weight="600"),
            stripe_elements(
                rx.form(payment_element(), rx.button("Submit")),
                options=dict(
                    clientSecret=PaymentState.client_secret,
                    appearance={"theme": "stripe"},
                ),
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        )
    )