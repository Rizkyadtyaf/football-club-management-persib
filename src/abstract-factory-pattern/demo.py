"""
demo.py
Main program untuk menjalankan Abstract Factory Pattern
"""

from abstract_factory import PersibSeniorFactory, PersibAcademyFactory
from client import manage_club


print("=== PERSIB SENIOR MANAGEMENT ===")
senior_factory = PersibSeniorFactory()
manage_club(senior_factory)

print("\n=== PERSIB ACADEMY MANAGEMENT ===")
academy_factory = PersibAcademyFactory()
manage_club(academy_factory)
