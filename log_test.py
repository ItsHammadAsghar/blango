import logging

logger = logging.getLogger(__name__)

username = "example_username"
email = "example_email@mail.com"

logger.log(logging.WARNING, "Created user %s with email %s", username, email)

try:
    answer = 9 / 0
    print(f"The answer is: {answer}")
    raise_exception()
except ZeroDivisionError:
    logger.exception("A divide by zero exception occured")