# Bestandsnaam: Missie_Opstart_Navigatie.py

import dji_sdk_lib as dji
import time
import math

# --- Configuratie ---
OPSTIJG_HOOGTE_M = 10.0
CRUISE_SNELHEID_MS = 5.0

# Voorbeeld waypoint coördinaten (Relatief ten opzichte van opstijglocatie)
WAYPOINTS = [
    {"x": 50, "y": 0, "z": OPSTIJG_HOOGTE_M},    # Punt A: 50m Oosten
    {"x": 50, "y": 50, "z": OPSTIJG_HOOGTE_M},   # Punt B: 50m N, 50m O
    {"x": 0, "y": 50, "z": OPSTIJG_HOOGTE_M},    # Punt C: 50m Noorden
]

# --- Functies ---

def initialiseer_drone_en_opstijgen(drone):
    """
    Verbindt met de drone, neemt controle over en stijgt op naar de veilige hoogte.
    """
    print("🚁 Initialiseren en verbinden met drone...")
    drone.connect()
    
    # 1. Neem controle over (Mochten de stick controls actief zijn)
    drone.obtain_control()
    
    # 2. Stijg op
    print(f"⬆️ Opstijgen naar {OPSTIJG_HOOGTE_M} meter...")
    drone.takeoff()
    
    # Wacht tot de drone de gewenste hoogte heeft bereikt
    while drone.get_height() < OPSTIJG_HOOGTE_M * 0.95:
        time.sleep(1)
        
    print("✅ Opstijgen voltooid.")

def vlieg_waypoints_missie(drone, waypoints):
    """
    Vliegt een simpele, vooraf gedefinieerde missie met waypoints.
    """
    print("\n🗺️ Start Waypoint Navigatie...")
    
    for i, wp in enumerate(waypoints):
        print(f"➡️ Navigeren naar Waypoint {i+1}: ({wp['x']}, {wp['y']})")
        
        # Stuur het bewegingscommando (x, y, z zijn relatief)
        drone.move_to_position(
            x=wp["x"], 
            y=wp["y"], 
            z=wp["z"], 
            speed=CRUISE_SNELHEID_MS
        )
        
        # Wacht tot de drone dichtbij het waypoint is (vereist complexe positie-check in realiteit)
        time.sleep(10) # Placeholder wachttijd
        print(f"📍 Aangekomen bij Waypoint {i+1}.")
        
    print("✅ Navigatie voltooid.")


# --- Hoofdlus ---
def run_opstart_missie():
    try:
        drone = dji.DroneController()
        initialiseer_drone_en_opstijgen(drone)
        vlieg_waypoints_missie(drone, WAYPOINTS)
        
    except Exception as e:
        print(f"❌ Fout tijdens de missie: {e}")

    finally:
        print("\n⬇️ Missie beëindigen. Landen...")
        # drone.land() # Uncomment in de echte code
        # drone.release_control()
        # drone.disconnect()

# if __name__ == "__main__":
#     run_opstart_missie()
