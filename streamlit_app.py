import streamlit as st

# --- KONFIGURATION ---
st.set_page_config(page_title="Wahl-O-Mat BW 2026", page_icon="🗳️")

# --- PARTEI-DATEN (Mapping: ++=2, +=1, o=0, -= -1, --= -2) ---
PARTIES = ["GRÜNE", "CDU", "SPD", "FDP", "AfD", "BSW"]
PARTY_DATA = {
    "GRÜNE": [0, -2, 2, 0, -1, 1, -1, 2, -2, 2, 0, 1, -2, 1, -1, 2, 1, 2, -2, 0, 1, 2, 2, -1, 1],
    "CDU":   [1, 2, 2, 2, 1, 1, 2, -1, 2, 1, 2, -2, 2, -1, 2, 0, 1, -1, 1, -1, 1, -1, 0, 2, -1],
    "SPD":   [2, 1, 0, 1, 1, 1, 1, -1, 0, -1, 1, -1, 1, 1, 1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1],
    "FDP":   [1, 2, -1, 1, 2, 1, 0, 0, -1, 2, 1, -2, -1, 1, -1, -1, 1, 0, 2, -1, 1, 1, -1, 1, -1],
    "AfD":   [1, 2, -2, 2, 2, 0, 2, -2, 2, -1, 2, -2, 2, -2, 2, -2, 1, -2, 2, 1, 1, -2, -2, 2, 0],
    "BSW":   [1, 1, -1, 1, 0, 1, 0, -1, 0, 0, 1, 2, 1, 1, 1, 0, 1, -1, 1, 1, -1, 0, -1, 1, 2]
}

# --- THESEN ---
THESEN = [
    {"t": "G9-Rückkehr sofort", "info": "Die Rückkehr zum neunjährigen Gymnasium (G9) soll für fast alle Klassenstufen sofort umgesetzt werden."},
    {"t": "Verbrenner-Aus auf EU-Ebene", "info": "Baden-Württemberg soll aktiv auf einen Stopp des EU-Verbrenner-Verbots ab 2035 hinwirken."},
    {"t": "Windkraft im Staatswald", "info": "Für den Ausbau der Windenergie sollen vermehrt Flächen im Staatswald (z. B. Schwarzwald) genutzt werden."},
    {"t": "Bezahlkarte für Geflüchtete", "info": "Geflüchtete sollen ihre Leistungen flächendeckend über eine Bezahlkarte statt als Bargeld erhalten."},
    {"t": "Grunderwerbsteuer beim Eigenheim", "info": "Die Steuer beim Kauf der ersten selbstgenutzten Immobilie soll deutlich gesenkt werden."},
    {"t": "A13-Besoldung für Grundschullehrkräfte", "info": "Grundschullehrkräfte sollen genauso wie Gymnasiallehrer nach der Besoldungsgruppe A13 bezahlt werden."},
    {"t": "Intelligente Videoüberwachung", "info": "An Kriminalitätsschwerpunkten soll verstärkt KI-gestützte Videoüberwachung eingesetzt werden."},
    {"t": "Netto-Null-Flächenverbrauch", "info": "Das Ziel, ab 2030 gar keine neuen Flächen mehr zu versiegeln, soll gesetzlich festgeschrieben werden."},
    {"t": "Kernkraft-Reserve", "info": "Stillgelegte Kernkraftwerke wie Neckarwestheim sollen als Energiereserve gesichert werden."},
    {"t": "Wahlalter 16", "info": "Das aktive Wahlrecht ab 16 Jahren bei Landtagswahlen soll dauerhaft beibehalten werden."},
    {"t": "Wolfsabschuss", "info": "Die rechtlichen Hürden für den Abschuss von Wölfen bei Bedrohung von Nutztieren sollen gesenkt werden."},
    {"t": "Mietendeckel", "info": "Das Land soll gesetzliche Höchstgrenzen für Mietpreise in Städten mit angespanntem Wohnungsmarkt einführen."},
    {"t": "Gender-Verbot", "info": "Die Verwendung von Gendersprache in Schulen und Behörden soll verboten werden."},
    {"t": "Industriestrompreis", "info": "Das Land soll die Stromkosten für energieintensive Betriebe (Zulieferer) subventionieren."},
    {"t": "Notenpflicht Grundschule", "info": "An Grundschulen sollen ab der 3. Klasse wieder verpflichtend Ziffernnoten vergeben werden."},
    {"t": "Nationalpark Schwarzwald", "info": "Die geschützten Kernzonen des Nationalparks Schwarzwald sollen weiter vergrößert werden."},
    {"t": "Pflicht-Vorschuljahr", "info": "Ein verpflichtendes zusätzliches Schuljahr für Kinder mit deutlichen Sprachdefiziten soll eingeführt werden."},
    {"t": "Radweg-Priorität", "info": "Der Ausbau von Radwegen soll finanziell Vorrang vor der Sanierung von Landesstraßen haben."},
    {"t": "Grundsteuer-Modell", "info": "Das baden-württembergische Bodenwertmodell soll durch das Bundesmodell ersetzt werden."},
    {"t": "Erhalt kleiner Kliniken", "info": "Das Land soll den Erhalt kleiner Krankenhäuser in ländlichen Regionen finanziell garantieren."},
    {"t": "Ländle-KI", "info": "Das Land soll massiv in die Entwicklung einer eigenen KI für die heimische Wirtschaft investieren."},
    {"t": "Studiengebühren für Nicht-EU-Ausländer", "info": "Die Studiengebühren für Studierende aus Staaten außerhalb der EU sollen abgeschafft werden."},
    {"t": "Solarpflicht im Bestand", "info": "Eigentümer sollen bei einer Dachsanierung auch im Bestand zur Solaranlage verpflichtet werden."},
    {"t": "Waffenverbotszonen", "info": "Kommunen sollen einfacher Zonen mit generellem Waffenverbot in Innenstädten einrichten dürfen."},
    {"t": "Gratis Mittagessen", "info": "Das Land soll die Kosten für das Mittagessen in allen Kitas und Grundschulen komplett übernehmen."}
]

# --- SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.choices = []

def handle_click(direction, weight):
    st.session_state.choices.append({"dir": direction, "weight": weight})
    st.session_state.step += 1

# --- UI ---
st.title("🗳️ Wahl-O-Mat BW 2026")

if st.session_state.step < len(THESEN):
    curr = THESEN[st.session_state.step]
    st.write(f"**These {st.session_state.step + 1} von 25**")
    st.progress(st.session_state.step / 25)
    
    st.subheader(curr["t"])
    with st.expander("ℹ️ Erläuterung"):
        st.info(curr["info"])
    
    # Buttons mit deiner Logik
    c1, c2, c3, c4, c5 = st.columns(5)
    if c1.button("✅✅", help="Stimme voll und ganz zu (Gewichtung x2)"): handle_click(1, 2)
    if c2.button("✅", help="Stimme zu"): handle_click(1, 1)
    if c3.button("⚪", help="Ist mir egal"): handle_click(0, 1)
    if c4.button("❌", help="Stimme nicht zu"): handle_click(-1, 1)
    if c5.button("❌❌", help="Stimme gar nicht zu (Gewichtung x2)"): handle_click(-1, 2)
    
    st.caption("Doppelte Symbole gewichten das Thema zweifach.")

else:
    st.header("Dein Ergebnis")
    results = {}
    
    for party in PARTIES:
        score = 0
        max_score = 0
        for i, choice in enumerate(st.session_state.choices):
            u_dir = choice["dir"]
            u_weight = choice["weight"]
            
            # Parteirichtung bestimmen
            p_val = PARTY_DATA[party][i]
            p_dir = 1 if p_val > 0 else (-1 if p_val < 0 else 0)
            
            # Distanz-Punkte (2=gleich, 1=neutral dabei, 0=Gegensatz)
            dist_pts = 2 - abs(u_dir - p_dir)
            score += dist_pts * u_weight
            max_score += 2 * u_weight
            
        results[party] = round((score / max_score) * 100, 1)
    
    # Sortierte Anzeige
    sorted_res = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
    for p, v in sorted_res.items():
        col_name, col_bar = st.columns([1, 4])
        col_name.write(f"**{p}**")
        col_bar.progress(v/100)
        st.write(f"Übereinstimmung: {v}%")

    if st.button("Neustart"):
        st.session_state.step = 0
        st.session_state.choices = []
        st.rerun()
