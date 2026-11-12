"""
SQLAlchemy Lab 04
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine, init_db
from models import Owner, Vet, Pet, Appointment


def update_appt(session):
    """
    This function assumes the user makes
    no mistakes and that there are no duplicates
    """
    name = input("What is your pet's name?\n")
    date = input("\nWhen is the appointment you would like to change? (YYYY-MM-DD)\n")

    pet = session.scalars(select(Pet).where(Pet.name == name)).first()
    # TODO: Can you get the appointment from the pet?
    appt = None

    print("\nGreat! I have the following appointment:")
    print(appt)

    response = input("\nWould you like to reschedule or cancel this appointment?\n")

    if response == "cancel":
        appt.pet = None
        session.commit()
        print("Your appointment has been cancelled. Thank you!")
    else:
        print(f"\nHere are the available appointments for {appt.vet}")

        # TODO: Complete this section to reschedule the appointment

        new_appt = None

        print("\nGreat! You now have the following appointment:")
        print(new_appt)

        verify = input("Is that correct? (Y/N)\n")
        if verify == "N":
            session.rollback()
            print("Oh well. Better luck next time.")
            print(f"Your appointment is still {appt}")
        else:
            session.commit()
            print("Your appointment has been updated")


# Create and fill vet.db if it doesn't exist yet
init_db()

with Session(engine) as session:
    update_appt(session)
