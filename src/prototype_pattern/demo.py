from persib_player import PersibPlayer

print("===== DEMO PROTOTYPE PATTERN PERSIB =====")

# Prototype asli
original_player = PersibPlayer(
    name="Beckham Putra",
    position="Gelandang",
    base_salary=20000000
)

# Clone dari prototype
clone_player = original_player.clone()
clone_player.name = "Marc Klok"

print("\n--- Player Original ---")
original_player.display()

print("\n--- Player Clone ---")
clone_player.display()
