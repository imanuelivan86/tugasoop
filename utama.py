from player import Player
from building import Building
from terrain import Terrain  # Import kelas anak yang baru ditambahkan

# Membuat instance pemain
player1 = Player("Player 1")

# Membuat instance bangunan
building1 = Building("Barracks", 500, 0, 60)

# Membuat instance terrain
terrain1 = Terrain("Forest", 2)

# Menampilkan informasi pemain, bangunan, dan terrain
player1.display_resources()
building1.display_info()
terrain1.display_info()
