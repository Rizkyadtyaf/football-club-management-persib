"""
products.py
Berisi abstract product dan concrete product
Untuk kasus Football Club Management - Persib
"""

from abc import ABC, abstractmethod


# =========================
# ABSTRACT PRODUCTS
# =========================

class Coach(ABC):
    """Abstract Product: Coach"""

    @abstractmethod
    def role(self) -> str:
        pass


class TrainingProgram(ABC):
    """Abstract Product: Training Program"""

    @abstractmethod
    def plan(self) -> str:
        pass


class MedicalTeam(ABC):
    """Abstract Product: Medical Team"""

    @abstractmethod
    def protocol(self) -> str:
        pass


# =========================
# CONCRETE PRODUCTS
# FAMILY: PERSIB SENIOR
# =========================

class PersibSeniorCoach(Coach):
    def role(self) -> str:
        return (
            "Head Coach PERSIB Bandung (Tim Senior): "
            "menentukan strategi Liga 1, taktik Maung Bandung, dan manajemen starting XI."
        )


class PersibSeniorTraining(TrainingProgram):
    def plan(self) -> str:
        return (
            "Program Latihan PERSIB Senior: "
            "tactical drill, match preparation Liga 1, dan recovery pasca pertandingan."
        )


class PersibSeniorMedical(MedicalTeam):
    def protocol(self) -> str:
        return (
            "Tim Medis PERSIB Senior: "
            "monitoring kebugaran pemain, penanganan cedera, dan return-to-play protocol."
        )
# =========================
# CONCRETE PRODUCTS
# FAMILY: PERSIB ACADEMY
# =========================

class PersibAcademyCoach(Coach):
    def role(self) -> str:
        return (
            "Coach Akademi PERSIB: "
            "fokus pembinaan pemain muda Maung Bandung dan pengembangan karakter."
        )


class PersibAcademyTraining(TrainingProgram):
    def plan(self) -> str:
        return (
            "Program Latihan Akademi PERSIB: "
            "teknik dasar sepak bola, pembinaan fisik, dan evaluasi perkembangan pemain."
        )


class PersibAcademyMedical(MedicalTeam):
    def protocol(self) -> str:
        return (
            "Tim Medis Akademi PERSIB: "
            "pencegahan cedera dini dan monitoring fisik pemain usia muda."
        )
