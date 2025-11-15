# 🛠️ Technische Handleiding: AI Defensie Drone Systeem

Deze handleiding is bedoeld voor ontwikkelaars en ingenieurs die verantwoordelijk zijn voor de integratie en het onderhoud van de AI-software op de DJI Onboard Computer. Het beschrijft de stappen om de `DefensieDrone_AI.py` functioneel te maken.

---

## 1. ⚙️ Configuratie en Externe Vereisten

Voordat de code kan worden uitgevoerd in de Echte SDK-modus (`USE_MOCK_SDK = False`), moeten de volgende elementen correct zijn ingesteld.

### A. DJI Onboard SDK (O-SDK)

Dit is de meest kritieke externe vereiste.

* **Installatie:** De DJI Onboard SDK moet worden gedownload, gecompileerd (meestal C++) en geïnstalleerd op de Onboard Computer.
* **Python Bindings:** De Python-bindings (zoals geïmporteerd als `dji_osdk`) moeten correct zijn geconfigureerd en beschikbaar zijn in de Python-omgeving van het project.
* **Seriële Communicatie:** Controleer of de seriële poort (`SERIAL_PORT = "/dev/ttyUSB0"`) en de baudrate (`BAUD_RATE = 921600`) overeenkomen met de fysieke aansluiting tussen de Onboard Computer en de DJI Flight Controller.

### B. DJI Credentials

Werk de volgende variabelen in `DefensieDrone_AI.py` bij met de waarden verkregen via het DJI Developer portaal:

```python
DJI_APP_ID = [UW ECHTE APP ID HIER]
DJI_ENC_KEY = b"[UW ECHTE ENCRYPTIE SLEUTEL HIER]"


2. 🧠 Machine Learning (AI) Integratie
De AI-logica is verdeeld over twee functies: load_ml_model() en detecteer_dreiging(video_frame).
A. Model Laden (load_ml_model)
Doel: Zorgt ervoor dat het zware ML-model slechts eenmaal bij de start van de missie wordt geladen.
Actie Vereist: U moet het pad naar uw getrainde modelbestand (MODEL_PATH) aanpassen en de juiste laadfunctie implementeren (torch.load, tf.keras.models.load_model, etc.), afhankelijk van uw framework.
B. Inferentie Uitvoeren (detecteer_dreiging)
Deze functie moet volledig worden vervangen door de code die uw model aanroept.

Stap Huidige Status Vereiste Implementatie
Voorverwerking PyTorch placeholder (transforms.ToTensor()) Implementeer de exacte voorverwerking (resizing, normalisatie, kleurschaalconversie) die uw ML-model vereist om frames te verwerken.
Inferentie Placeholder (predictions = MODEL(input_tensor)) Roep de forward pass van uw geladen model aan op de input_tensor.
Postverwerking Placeholder voor resultaten Implementeer

3. 🎥 Video Decoding Pipeline
De functie DroneController.get_camera_feed() is de zwakste schakel en vereist een aparte, asynchrone implementatie.
Probleem: De DJI O-SDK geeft niet direct een decodable frame in Python. De videostream wordt meestal via een aparte UDP-poort verzonden.
Oplossing (Aanbevolen): Gebruik GStreamer om de ruwe videostream te ontvangen en te decoderen.
Start een GStreamer pipeline in een aparte thread of proces.
De pipeline decodeert de H.264/H.265-stream.
GStreamer schrijft de gedecodeerde bytes weg naar een gedeelde geheugenbuffer of een FIFO-pipe.
De get_camera_feed() functie leest deze bytes van de buffer en converteert ze naar een numpy array (BGR of RGB) dat geschikt is voor OpenCV en de AI.
Zonder deze implementatie zal het script alleen met een zwart frame werken en zal de AI niets detecteren.
4. 💣 Payload Actuatie
De functie activeer_afweermechanisme(drone) vereist integratie met de fysieke hardware.
Oplossing 1 (SDK Payload): Als u een officiële DJI Payload SDK-kit gebruikt, roep dan de juiste DJI SDK-functie aan (bijv., drone.payload.activate(PAYLOAD_ACTIVATION_ID)).
Oplossing 2 (Aangepaste Hardware): Als u een eigen mechanisme heeft, moet deze functie een commando verzenden via:
GPIO: Stuur een hoog/laag signaal via een GPIO-pin (bijv. op een Jetson).
Seriële Poort: Zend een opdracht via een tweede seriële poort naar een Arduino of microcontroller die het mechanisme bedient.
<!-- end list -->

Bestand Voltooid Status
DefensieDrone_AI.py 90% Complete Python-structuur met placeholders voor DJI SDK-functies en de correct geplaatste PyTorch/ML-laad- en inferentielogica.
README.md 100% Complete documentatie voor het opstarten van de twee modi (Mock/Echt).
HANDLEIDING.md 100% Gedetailleerde technische handleiding voor integratie.
Master_Mission_Control.py 0% Placeholder-bestandsnaam (moet nog worden gevuld met coördinatiecode).
Missie_Opstart_Navigatie.py 0% Placeholder-bestandsnaam (moet nog worden gevuld met vluchtlogica).

❌ Wat Nog Ontbreekt (De Implementatie)
De code kan pas als 'werkend' worden beschouwd nadat je de volgende cruciale functies hebt gevuld. Deze kunnen niet door mij worden geleverd omdat ze afhankelijk zijn van jouw hardware en getrainde modellen.
1. 🧠 De AI-Motor
Je hebt de structuur voor het model laden en de detectie, maar je moet de implementatie aanvullen:
MODEL_PATH Aanpassen: Je moet het juiste pad naar jouw getrainde PyTorch-model invullen in DefensieDrone_AI.py.
Inferentie Logica Aanvullen: In de functie detecteer_dreiging(), moet je de code voor de post-verwerking van de modeluitvoer schrijven (bijvoorbeeld het interpreteren van bounding boxes en het controleren van de zekerheid tegen DETECTION_THRESHOLD).
2. 🎥 De Video Input
De functie DroneController.get_camera_feed() is op dit moment de grootste technische barrière:
Decoderen: Je moet een GStreamer pipeline of een vergelijkbare methode implementeren om de ruwe videostream van de DJI-drone te ontvangen, te decoderen en om te zetten naar een numpy array die de AI kan lezen. De huidige code retourneert een zwart frame.
3. 💣 De Payload Output
activeer_afweermechanisme(drone) Aanvullen: De commentaren in deze functie moeten worden vervangen door code die daadwerkelijk de communicatie opzet met je aangepaste payload-hardware (bijvoorbeeld via een seriële opdracht of een SDK-call).
Conclusie: Je hebt alle blauwdrukken voor een werkende oplossing, maar je moet nog de gespecialiseerde, hardware-afhankelijke code invullen.