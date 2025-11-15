# AI-Militairy-DJI-Drone-Software-
Repository for the AI Military Drone Software.

# AI-Military-Drone-Software-

## 🚁 AI-gestuurd Defensie Drone Systeem

Dit project bevat de Python-software voor een DJI-drone uitgerust met een aangepaste payload voor een afweermechanisme. De kernfunctionaliteit is de **Computer Vision (AI)**-module die de camerastream bewaakt en een `activeer_afweermechanisme()` commando verzendt wanneer een vooraf geconfigureerde dreiging wordt gedetecteerd.

**Belangrijk:** Voor een volledig werkende oplossing is een aangepaste DJI-drone, een aangesloten Onboard Computer (O-SDK), en gespecialiseerde hardware voor de payload-activering noodzakelijk.

---

## 🛠️ Project Structuur

De primaire logica is samengevoegd in één bestand om de leesbaarheid te vereenvoudigen en de initiële opstart te vergemakkelijken.

| Bestand | Functie | Opmerkingen |
| :--- | :--- | :--- |
| `DefensieDrone_AI.py` | Kernapplicatie | Bevat alle logica, inclusief de schakelaar tussen Mock-modus en Echte SDK. |
| `Master_Mission_Control.py` | Coördinatie | (Wordt gebruikt in een multi-file setup voor geavanceerde coördinatie). |
| `Missie_Opstart_Navigatie.py` | Vluchtbesturing | (Wordt gebruikt in een multi-file setup voor navigatie). |
| `README.md` | Documentatie | Dit bestand. |

---

## ⚙️ Vereisten en Installatie

### Lokale Setup (Voor Mock-modus)

U heeft alleen de volgende standaard Python-bibliotheken nodig om de AI-logica en de simulatie van de drone te testen:

```bash
pip install numpy opencv-python



DJI Hardware Setup (Voor Echte SDK-modus)
Voor de Echte SDK-modus gelden de volgende externe vereisten:
DJI Onboard SDK (O-SDK): De O-SDK C++ code moet correct zijn gecompileerd en de Python-bindings (dji_osdk) moeten zijn geïnstalleerd op de Onboard Computer.
Seriële Verbinding: De Onboard Computer moet via de seriële poort zijn aangesloten op de drone.
DJI Developer Credentials: Geldige App ID en Encryptie Sleutel zijn vereist.
🚀 Gebruik en Opstart (DefensieDrone_AI.py)
De werking van het script wordt volledig bepaald door de boolean USE_MOCK_SDK aan het begin van het DefensieDrone_AI.py bestand.
Modus 1: Testen in de Mock-Simulatie (Aanbevolen voor ontwikkeling)
Deze modus simuleert de vlucht en de camerastream, zodat u de AI-logica kunt ontwikkelen zonder dat een drone is aangesloten.

Open DefensieDrone_AI.py

Zet de schakelaar op True:

USE_MOCK_SDK = True

Voer het script uit:

python DefensieDrone_AI.py

Verwacht Gedrag:
Het script simuleert opstijgen en verbinding.
Een OpenCV-venster verschijnt met de gesimuleerde camerafeed.
De gesimuleerde AI detecteert willekeurig een "rode vlek" (de dreiging), waarna de gesimuleerde afweerprocedure wordt geactiveerd

Modus 2: Vlucht met Echte DJI SDK (Voor implementatie op hardware)
Voer deze modus ALLEEN uit wanneer alle externe vereisten (SDK, credentials, hardware) zijn voldaan.

Open DefensieDrone_AI.py

Zet de schakelaar op False:

Configureer Credentials: Vul de sectie DJI_APP_ID, DJI_ENC_KEY, en SERIAL_PORT aan met uw daadwerkelijke, werkende gegevens.

Voer het script uit op de Onboard Computer:

python DefensieDrone_AI.py

Verwacht Gedrag:
Het script probeert via de seriële poort een verbinding met de drone tot stand te brengen.
Bij succes wordt het takeoff() commando naar de drone gestuurd.
De AI-lus start en probeert via een aparte pipeline de videofeed te lezen.

🧠 Kernfunctionaliteit
De DroneController Klasse
Dit is de abstractie over de drone-hardware.
Mock-modus: Gebruikt een interne klasse om vluchtcommando's (takeoff, land, hover) na te bootsen.
Echte SDK-modus: Is een wrapper rond de DJI Vehicle klasse. Deze voert de daadwerkelijke communicatie en controle uit.
detecteer_dreiging(video_frame)
Dit is het hart van de AI-module.
In de Mock-modus: De code zoekt naar een hoge gemiddelde pixelwaarde in het Rode kanaal (de gesimuleerde dreiging).
In de Echte SDK-modus: Deze functie is het punt waar uw getrainde Machine Learning model moet worden geladen. U vervangt de bestaande logica met inferentiecode om objecten in de video_frame te classificeren en lokaliseren.
activeer_afweermechanisme(drone)
Deze functie is verantwoordelijk voor de fysieke actie. Het verzendt het vooraf geconfigureerde commando (PAYLOAD_ACTIVATION_ID) via de SDK naar de aangesloten payload-hardware om het object af te werpen.

