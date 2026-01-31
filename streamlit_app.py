import streamlit as st

# --- KONFIGURATION ---
st.set_page_config(page_title="Wahl-O-Mat BW 2026", page_icon="🗳️", layout="centered")

# --- PARTEI-DATEN & FARBEN ---
PARTIES = ["GRÜNE", "CDU", "SPD", "FDP", "AfD", "BSW"]
PARTY_COLORS = {
    "GRÜNE": "#64A12D", "CDU": "#323232", "SPD": "#E3000F",
    "FDP": "#FFED00", "AfD": "#009EE0", "BSW": "#7E1C44"
}

# Werte aus deiner Tabelle: ++=2, +=1, o=0, -= -1, --= -2
PARTY_DATA = {
    "GRÜNE": [0, -2, 2, 0, -1, 1, -1, 2, -2, 2, 0, 1, -2, 1, -1, 2, 1, 2, -2, 0, 1, 2, 2, -1, 1],
    "CDU":   [1, 2, 2, 2, 1, 1, 2, -1, 2, 1, 2, -2, 2, -1, 2, 0, 1, -1, 1, -1, 1, -1, 0, 2, -1],
    "SPD":   [2, 1, 0, 1, 1, 1, 1, -1, 0, -1, 1, -1, 1, 1, 1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1],
    "FDP":   [1, 2, -1, 1, 2, 1, 0, 0, -1, 2, 1, -2, -1, 1, -1, -1, 1, 0, 2, -1, 1, 1, -1, 1, -1],
    "AfD":   [1, 2, -2, 2, 2, 0, 2, -2, 2, -1, 2, -2, 2, -2, 2, -2, 1, -2, 2, 1, 1, -2, -2, 2, 0],
    "BSW":   [1, 1, -1, 1, 0, 1, 0, -1, 0, 0, 1, 2, 1, 1, 1, 0, 1, -1, 1, 1, -1, 0, -1, 1, 2]
}

# --- DATEN-KOMBINATION ---
# Struktur: [Überschrift, These, tl;dr-Beschreibung, Lange Erläuterung]
DATA = [
    ["G9-Rückkehr", "Die Umstellung auf das neunjährige Gymnasium soll sofort für alle Klassenstufen erfolgen.", "Bei diesem Thema geht es darum, ob die Rückkehr zum neunjährigen Gymnasium (G9) für fast alle Klassenstufen sofort umgesetzt werden soll.", "Baden-Württemberg stellt das Gymnasium aktuell wieder auf neun Jahre um. Da die Umstellung im Schuljahr 2025/26 primär für neue Jahrgänge startete, wird diskutiert, ob auch Schüler in höheren Klassenstufen sofort das Recht auf das zusätzliche Jahr erhalten sollten."],
    ["Verbrenner-Aus", "Baden-Württemberg soll sich dafür einsetzen, das EU-Verbot für Neuwagen mit Verbrennermotor ab 2035 zu stoppen.", "Bei diesem Thema geht es darum, ob das Land Baden-Württemberg aktiv auf einen Stopp des EU-Verbrenner-Verbots hinwirken soll.", "Die EU plant ein Verbot für neue Pkw mit Verbrennungsmotor ab 2035. Da Baden-Württemberg ein Zentrum der Automobilindustrie ist, steht die Frage im Raum, ob das Land auf eine Aufhebung oder Lockerung dieses Verbots hinwirken sollte."],
    ["Windkraft im Wald", "Für den Ausbau der Windenergie sollen vermehrt Flächen im Staatswald (z. B. Schwarzwald) freigegeben werden.", "Bei diesem Thema geht es darum, ob für den Ausbau der Windenergie verstärkt Flächen im Staatswald (z. B. Schwarzwald) genutzt werden sollen.", "Zur Erreichung der Klimaziele werden auch Waldflächen des Landes als Standorte für Windräder geprüft. Dies führt zu Konflikten zwischen dem Ausbau erneuerbarer Energien und dem Schutz von Waldökosystemen und Erholungsräumen."],
    ["Bezahlkarte", "Geflüchtete sollen ihre Leistungen flächendeckend nur noch per Bezahlkarte statt als Bargeld erhalten.", "Bei diesem Thema geht es darum, ob Geflüchtete ihre Leistungen flächendeckend über eine Bezahlkarte statt als Bargeld erhalten sollen.", "Asylsuchende erhalten finanzielle Unterstützung. Eine Bezahlkarte soll sicherstellen, dass diese Mittel vorrangig für den lokalen Bedarf genutzt und nicht in die Herkunftsländer überwiesen werden."],
    ["Grunderwerbsteuer", "Die Steuer beim Kauf der ersten selbstgenutzten Immobilie soll deutlich gesenkt werden.", "Bei diesem Thema geht es darum, ob die Steuer beim Kauf der ersten selbstgenutzten Immobilie deutlich gesenkt werden soll.", "Beim Kauf einer Immobilie fällt eine Steuer an, die in BW recht hoch ist. Zur Förderung von Wohneigentum wird diskutiert, Käufer beim ersten Erwerb einer selbstgenutzten Immobilie steuerlich zu entlasten."],
    ["A13 für alle", "Grundschullehrer sollen genau wie Gymnasiallehrer nach der Besoldungsgruppe A13 bezahlt werden.", "Bei diesem Thema geht es darum, ob Grundschullehrkräfte genauso wie Gymnasiallehrer nach der höheren Besoldungsgruppe A13 bezahlt werden sollen.", "Grundschullehrer verdienen in BW bisher weniger als Gymnasiallehrer. Eine Angleichung der Gehälter soll den Beruf attraktiver machen, belastet aber den Landeshaushalt erheblich."],
    ["Videoüberwachung", "An Kriminalitätsschwerpunkten soll verstärkt intelligente (KI-gestützte) Videoüberwachung eingesetzt werden.", "Bei diesem Thema geht es darum, ob an Kriminalitätsschwerpunkten verstärkt intelligente, KI-gestützte Videoüberwachung eingesetzt werden soll.", "Zur Kriminalitätsbekämpfung könnten öffentliche Plätze vermehrt mit Kameras überwacht werden, die mithilfe von Software auffälliges Verhalten oder Gesichter automatisch erkennen können."],
    ["Flächenverbrauch", "Das Land soll ein striktes „Netto-Null“-Ziel für die Neuversiegelung von Flächen bis 2030 gesetzlich festschreiben.", "Bei diesem Thema geht es darum, ob das Ziel, ab 2030 gar keine neuen Flächen mehr zu versiegeln, gesetzlich festgeschrieben werden soll.", "Jeden Tag werden neue Flächen für Bauprojekte versiegelt. Das Ziel „Netto-Null“ bedeutet, dass ab einem bestimmten Zeitpunkt gar keine neuen Flächen mehr verbaut werden dürfen, ohne einen Ausgleich an anderer Stelle."],
    ["Kernkraft", "Der Standort Neckarwestheim soll für eine mögliche Reaktivierung als Energiereserve gesichert werden.", "Bei diesem Thema geht es darum, ob stillgelegte Kernkraftwerke wie Neckarwestheim als Energiereserve gesichert werden sollen.", "Nach dem Atomausstieg stehen Anlagen wie Neckarwestheim still. Es wird debattiert, ob diese Standorte als einsatzbereite Energiereserve erhalten bleiben sollten, um die Stromversorgung im Krisenfall zu sichern."],
    ["Wahlalter 16", "Das Wahlrecht ab 16 Jahren bei Landtagswahlen soll beibehalten werden.", "Bei diesem Thema geht es darum, ob das aktive Wahlrecht ab 16 Jahren bei Landtagswahlen dauerhaft beibehalten werden soll.", "Seit kurzem dürfen 16-Jährige in BW bei Landtagswahlen wählen. Es wird diskutiert, ob dieses Recht beibehalten werden soll oder ob die Wahlberechtigung wieder erst ab der Volljährigkeit gelten sollte."],
    ["Wolfsabschuss", "Die Hürden für den Abschuss von Wölfen bei Bedrohung von Nutztieren sollen gesenkt werden.", "Bei diesem Thema geht es darum, ob die rechtlichen Hürden für den Abschuss von Wölfen bei Bedrohung von Nutztieren gesenkt werden sollen.", "Die Rückkehr des Wolfes führt zu Rissen bei Schafen und Ziegen. Diskutiert wird, ob die rechtlichen Hürden gesenkt werden sollten, um Tiere, die wiederholt Herden angreifen, schneller abschießen zu dürfen."],
    ["Mietendeckel", "In Städten mit besonders angespanntem Wohnungsmarkt soll ein staatlicher Mietendeckel eingeführt werden.", "Bei diesem Thema geht es darum, ob das Land gesetzliche Höchstgrenzen für Mietpreise in Städten mit angespanntem Wohnungsmarkt einführen soll.", "In vielen Städten steigen die Mieten rasant an. Ein gesetzlicher Deckel würde die Mietpreise für einen bestimmten Zeitraum staatlich einfrieren oder auf einen Maximalwert begrenzen."],
    ["Gender-Verbot", "An Schulen und in der Verwaltung soll die Verwendung von Gendersprache (z. B. Sternchen) untersagt werden.", "Bei diesem Thema geht es darum, ob die Verwendung von Gendersprache in Schulen und Behörden verboten werden soll.", "In der öffentlichen Verwaltung und an Schulen wird teilweise geschlechtergerechte Sprache (z. B. Gendersternchen) genutzt. Ein Verbot würde die Verwendung solcher Sonderzeichen in offiziellen Dokumenten untersagen."],
    ["Industriestrompreis", "Das Land soll einen eigenen Fonds zur Subventionierung der Stromkosten für Zulieferbetriebe auflegen.", "Bei diesem Thema geht es darum, ob das Land die Stromkosten für energieintensive Betriebe subventionieren soll.", "Hohe Energiekosten belasten die Industrie im Land. Eine staatliche Subventionierung des Strompreises für energieintensive Unternehmen soll deren Abwanderung verhindern, ist aber wettbewerbsrechtlich umstritten."],
    ["Notenpflicht", "An allen Grundschulen sollen ab der 3. Klasse wieder verpflichtend Noten vergeben werden.", "Bei diesem Thema geht es darum, ob an Grundschulen ab der 3. Klasse wieder verpflichtend Ziffernnoten vergeben werden sollen.", "Oft werden Noten in der Grundschule durch schriftliche Lernberichte ersetzt. Es wird diskutiert, ob klassische Ziffernnoten ab der dritten Klasse wieder zur Pflicht werden sollen, um Leistungen vergleichbarer zu machen."],
    ["Nationalpark Schwarzwald", "Der Anteil der forstwirtschaftlich ungenutzten Waldflächen im Nationalpark soll über die bisherigen Pläne hinaus erweitert werden.", "Bei diesem Thema geht es darum, ob die geschützten Kernzonen des Nationalparks Schwarzwald weiter vergrößert werden sollen.", "Der Nationalpark schützt Flächen, die nicht wirtschaftlich genutzt werden. Diskutiert wird, ob diese „Kernzonen“ über die aktuellen Pläne hinaus weiter ausgedehnt werden sollen."],
    ["Sprach-Vorschule", "Kinder mit Sprachdefiziten sollen zu einem verpflichtenden Vorschuljahr verpflichtet werden.", "Bei diesem Thema geht es darum, ob ein verpflichtendes zusätzliches Schuljahr für Kinder mit deutlichen Sprachdefiziten eingeführt werden soll.", "Immer mehr Kinder beherrschen bei der Einschulung Deutsch nicht ausreichend. Ein verpflichtendes Vorschuljahr soll sicherstellen, dass betroffene Kinder durch gezielte Förderung auf den Unterricht vorbereitet werden."],
    ["Radweg-Priorität", "Der Ausbau von Radwegen soll finanziell Vorrang vor der Sanierung von Landesstraßen haben.", "Bei diesem Thema geht es darum, ob der Ausbau von Radwegen finanziell Vorrang vor der Sanierung von Landesstraßen haben soll.", "Bei der Budgetverteilung im Verkehrsbereich steht die Frage im Raum, ob der Ausbau von Radwegen Vorrang vor der Instandhaltung und Sanierung von Straßen für Autos haben sollte."],
    ["Grundsteuer", "Das baden-württembergische Bodenwertmodell soll abgeschafft und durch das Bundesmodell ersetzt werden.", "Bei diesem Thema geht es darum, ob das baden-württembergische Bodenwertmodell durch das Bundesmodell ersetzt werden soll.", "Baden-Württemberg nutzt ein Modell, das sich allein am Bodenwert orientiert. Kritiker fordern die Rückkehr zum Bundesmodell, bei dem auch das Gebäude auf dem Grundstück mitbewertet wird."],
    ["Krankenhäuser", "Kleine Kliniken im ländlichen Raum sollen durch Landesmittel vor der Schließung bewahrt werden.", "Bei diesem Thema geht es darum, ob das Land den Erhalt kleiner Krankenhäuser in ländlichen Regionen finanziell garantieren soll.", "Viele kleine Krankenhäuser auf dem Land sind unrentabel. Gefragt ist, ob das Land diese Standorte finanziell stützen sollte, um die medizinische Versorgung in der Fläche zu garantieren."],
    ["Ländle-KI", "Baden-Württemberg soll Milliarden in regionale KI-Modelle für die heimische Wirtschaft investieren.", "Bei diesem Thema geht es darum, ob das Land massiv in die Entwicklung einer eigenen Künstlichen Intelligenz für die Industrie investieren soll.", "Um technologisch unabhängig zu bleiben, wird diskutiert, ob das Land Milliarden in die Entwicklung einer eigenen KI-Infrastruktur investieren sollte, die speziell auf die Bedürfnisse der heimischen Industrie zugeschnitten ist."],
    ["Studiengebühren", "Die Gebühren für Studierende aus Nicht-EU-Ländern sollen wieder abgeschafft werden.", "Bei diesem Thema geht es darum, ob die Studiengebühren für Studierende aus Staaten außerhalb der EU abgeschafft werden sollen.", "Derzeit zahlen Studierende von außerhalb der EU in BW 1.500 Euro Gebühren pro Semester. Es wird diskutiert, ob diese Gebühren abgeschafft werden sollten, um international attraktiver für Fachkräfte zu werden."],
    ["Solarpflicht", "Die Photovoltaik-Pflicht soll auch auf die Sanierung bestehender Wohnhäuser ausgeweitet werden.", "Bei diesem Thema geht es darum, ob Eigentümer bei einer Dachsanierung auch im Gebäudebestand zur Installation einer Solaranlage verpflichtet werden sollen.", "Während Photovoltaik bei Neubauten Pflicht ist, wird nun darüber gestritten, ob Hausbesitzer auch bei der Sanierung alter Dächer verpflichtet werden sollen, Solarpanels zu installieren."],
    ["Waffenverbotszonen", "Kommunen sollen leichter Messer- und Waffenverbotszonen in Innenstädten einrichten dürfen.", "Bei diesem Thema geht es darum, ob Kommunen einfacher Zonen mit generellem Waffenverbot in Innenstädten einrichten dürfen.", "Um Gewaltkriminalität vorzubeugen, könnten Kommunen Zonen einrichten, in denen das Mitführen von Messern und Waffen generell verboten ist. Es geht um die Frage, ob die Hürden für solche Zonen gesenkt werden sollen."],
    ["Gratis Mittagessen", "Das Land soll die Kosten für das Mittagessen in allen Kitas und Grundschulen komplett übernehmen.", "Bei diesem Thema geht es darum, ob das Land die Kosten für das Mittagessen in allen Kitas und Grundschulen komplett übernehmen soll.", "Die Mittagsverpflegung in Kitas und Schulen ist oft kostenpflichtig. Es steht zur Debatte, ob das Land die Kosten für eine warme Mahlzeit für alle Kinder komplett übernehmen sollte."]
]

# --- SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step, st.session_state.choices = 0, []

def handle(direction, weight):
    st.session_state.choices.append({"dir": direction, "weight": weight})
    st.session_state.step += 1

def render_bar(name, pct, color):
    st.markdown(f"""<div style="margin-bottom:12px;"><div style="display:flex;justify-content:space-between;margin-bottom:2px;">
    <span style="font-weight:bold;color:{color};">{name}</span><span>{pct}%</span></div>
    <div style="background:#f0f0f0;border-radius:5px;height:14px;"><div style="background:{color};width:{pct}%;height:14px;border-radius:5px;"></div></div></div>""", unsafe_allow_html=True)

# --- GUI ---
st.title("🗳️ Wahl-O-Mat BW 2026")

if st.session_state.step < len(DATA):
    h, t, d, i = DATA[st.session_state.step]
    st.write(f"**These {st.session_state.step + 1} von 25**")
    st.progress(st.session_state.step / 25)
    st.markdown(f"## {h}")
    st.markdown(f"#### {t}")
    st.info(d)
    with st.expander("ℹ️ Erläuterung"): st.write(i)
    
    st.write("---")
    cols = st.columns(5)
    opts = [("✅✅", 1, 2), ("✅", 1, 1), ("⚪", 0, 1), ("❌", -1, 1), ("❌❌", -1, 2)]
    for idx, (icon, dr, wt) in enumerate(opts):
        if cols[idx].button(icon, use_container_width=True): handle(dr, wt)
    
    st.caption("Doppelt = Gewichtung x2 | Einfach = Gewichtung x1")
    if st.session_state.step > 0:
        if st.button("⬅️ Zurück"):
            st.session_state.step -= 1
            st.session_state.choices.pop()
            st.rerun()
else:
    st.header("Dein Ergebnis")
    results = {}
    for party in PARTIES:
        s, m = 0, 0
        for idx, c in enumerate(st.session_state.choices):
            p_dir = 1 if PARTY_DATA[party][idx] > 0 else (-1 if PARTY_DATA[party][idx] < 0 else 0)
            s += (2 - abs(c["dir"] - p_dir)) * c["weight"]
            m += 2 * c["weight"]
        results[party] = round((s / m) * 100, 1)
    
    for p, v in dict(sorted(results.items(), key=lambda x: x[1], reverse=True)).items():
        render_bar(p, v, PARTY_COLORS[p])
    
    if st.button("🔄 Neustart"):
        st.session_state.step = 0
        st.session_state.choices = []
        st.rerun()
