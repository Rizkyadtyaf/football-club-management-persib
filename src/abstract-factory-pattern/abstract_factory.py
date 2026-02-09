"""
abstract_factory.py
Berisi Abstract Factory dan Concrete Factory
"""

from abc import ABC, abstractmethod
from products import (
    Coach, TrainingProgram, MedicalTeam,
    PersibSeniorCoach, PersibSeniorTraining, PersibSeniorMedical,
    PersibAcademyCoach, PersibAcademyTraining, PersibAcademyMedical
)


class ClubManagementFactory(ABC):
    """
    ABSTRACT FACTORY
    Mendefinisikan method untuk membuat keluarga produk
    """

    @abstractmethod
    def create_coach(self) -> Coach:
        pass

    @abstractmethod
    def create_training_program(self) -> TrainingProgram:
        pass

    @abstractmethod
    def create_medical_team(self) -> MedicalTeam:
        pass


class PersibSeniorFactory(ClubManagementFactory):
    """Concrete Factory untuk Persib Senior"""

    def create_coach(self) -> Coach:
        return PersibSeniorCoach()

    def create_training_program(self) -> TrainingProgram:
        return PersibSeniorTraining()

    def create_medical_team(self) -> MedicalTeam:
        return PersibSeniorMedical()


class PersibAcademyFactory(ClubManagementFactory):
    """Concrete Factory untuk Persib Academy"""

    def create_coach(self) -> Coach:
        return PersibAcademyCoach()

    def create_training_program(self) -> TrainingProgram:
        return PersibAcademyTraining()

    def create_medical_team(self) -> MedicalTeam:
        return PersibAcademyMedical()
