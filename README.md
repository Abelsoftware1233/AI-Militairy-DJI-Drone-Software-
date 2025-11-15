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

