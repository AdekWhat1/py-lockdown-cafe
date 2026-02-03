from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)

import datetime
# expiration_date = datetime.date(2020, 1, 1)
today = datetime.date.today()


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You are not vaccinated")
        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < today:
            raise OutdatedVaccineError("You're vaccine outdated")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You are not wearing mask")
        return f"Welcome to {self.name}"
