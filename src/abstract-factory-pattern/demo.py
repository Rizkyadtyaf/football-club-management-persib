from factory import PersibFactory

print("===== DEMO ABSTRACT FACTORY PERSIB =====")

factory = PersibFactory()

player = factory.create_player()
coach = factory.create_coach()

print("Role:", player.get_role())
print("Role:", coach.get_role())
