from dataclasses import dataclass


@dataclass
class PersonData:
    firstname: str = None
    lastname: str = None
    comment: str = None
    email: str = None
    incorrect_email: str = None
