"""
client.py
Client tidak tahu concrete class
Client hanya berinteraksi dengan abstract factory
"""

from abstract_factory import ClubManagementFactory


def manage_club(factory: ClubManagementFactory):
    coach = factory.create_coach()
    training = factory.create_training_program()
    medical = factory.create_medical_team()

    print(coach.role())
    print(training.plan())
    print(medical.protocol())
