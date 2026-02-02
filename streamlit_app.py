import streamlit as st
import random
from fpdf import FPDF

# --- SETUP ---
st.set_page_config(page_title="Wahl-O-Mat BW 2026", page_icon="🗳️", layout="centered")

# --- PARTEIEN & FARBEN ---
PARTIES = ["GRÜNE", "CDU", "SPD", "FDP", "AfD", "BSW", "DIE LINKE"]
PARTY_COLORS = {
    "GRÜNE": "#64A12D", "CDU": "#323232", "SPD": "#E3000F",
    "FDP": "#FFED00", "AfD": "#009EE0", "BSW": "#7E1C44", "DIE LINKE": "#BE3075"
}

# --- PARTEI-DATEN ---
PARTY_DATA = {
    "GRÜNE":    [0, -2, 2, 0, -1, 1, -1, 2, -2, 2, 0, 1, -2, 1, -1, 2, 1, 2, -2, 0, 1, -2, 2, -1, 2],
    "CDU":      [1, 2, 1, 2, 2, 1, 2, -2, 2, -1, 2, -2, 2, -1, 2, 0, 1, -2, -2, -1, 1, -1, 0, 2, -1],
    "SPD":      [2, 0, 1, 1, 0, 2, 1, -1, 0, 2, 1, 2, -2, 2, 2, 1, 2, -1, 1, 2, 1, 2, 1, 1, 2],
    "FDP":      [1, 2, -1, 2, 2, 1, 1, -1, 2, 2, 1, -2, 2, -2, 2, -1, 2, -1, 2, -1, 1, 2, -2, 1, -2],
    "AfD":      [1, 2, -2, 2, 2, 0, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 1, -2, 2, 2, 0, -2, -2, 2, 0],
    "BSW":      [1, 1, -1, 1, 0, 1, 0, -1, 0, 0, 1, 2, 1, 1, 1, 0, 1, -1, 1, 1, -1, 0, -1, 1, 2],
    "DIE LINKE": [2, -2, 2, -2, -1, 2, -2, 2, -2, 2, -1, 2, -2, 1, -2, 2, 1, 2, -1, 2, 1, 2, 2, -1, 2]
}

# --- THESEN DATEN (ORIGINALTEXTE UNGEKÜRZT) ---
DATA = [
    ["G9-Rückkehr", "Die Umstellung auf das neunjährige Gymnasium soll sofort für alle Klassenstufen erfolgen.", "Baden-Württemberg stellt das Gymnasium aktuell wieder auf neun Jahre um. Da die Umstellung im Schuljahr 2025/26 primär für neue Jahrgänge startete, wird diskutiert, ob auch Schüler in höheren Klassenstufen sofort das Recht auf das zusätzliche Jahr erhalten sollten."],
    ["Verbrenner-Aus", "Baden-Württemberg soll sich dafür einsetzen, das EU-Verbot für Neuwagen mit Verbrennermotor ab 2035 zu stoppen.", "Die EU plant ein Verbot für neue Pkw mit Verbrennungsmotor ab 2035. Da Baden-Württemberg ein Zentrum der Automobilindustrie ist, steht die Frage im Raum, ob das Land auf eine Aufhebung oder Lockerung dieses Verbots hinwirken sollte."],
    ["Windkraft im Wald", "Für den Ausbau der Windenergie sollen vermehrt Flächen im Staatswald (z. B. Schwarzwald) freigegeben werden.", "Zur Erreichung der Klimaziele werden auch Waldflächen des Landes als Standorte für Windräder geprüft. Dies führt zu Konflikten zwischen dem Ausbau erneuerbarer Energien und dem Schutz von Waldökosystemen und Erholungsräumen."],
    ["Bezahlkarte", "Geflüchtete sollen ihre Leistungen flächendeckend nur noch per Bezahlkarte statt als Bargeld erhalten.", "Asylsuchende erhalten finanzielle Unterstützung. Eine Bezahlkarte soll sicherstellen, dass diese Mittel vorrangig für den lokalen Bedarf genutzt und nicht in die Herkunftsländer überwiesen werden."],
    ["Grunderwerbsteuer", "Die Steuer beim Kauf der ersten selbstgenutzten Immobilie soll deutlich gesenkt werden.", "Beim Kauf einer Immobilie fällt eine Steuer an, die in BW recht hoch ist. Zur Förderung von Wohneigentum wird diskutiert, Käufer beim ersten Erwerb einer selbstgenutzten Immobilie steuerlich zu entlasten."],
    ["A13 für alle", "Grundschullehrer sollen genau wie Gymnasiallehrer nach der Besoldungsgruppe A13 bezahlt werden.", "Grundschullehrer verdienen in BW bisher weniger als Gymnasiallehrer. Eine Angleichung der Gehälter soll den Beruf attraktiver machen, belastet aber den Landeshaushalt erheblich."],
    ["Videoüberwachung", "An Kriminalitätsschwerpunkten soll verstärkt intelligente (KI-gestützte) Videoüberwachung eingesetzt werden.", "Zur Kriminalitätsbekämpfung könnten öffentliche Plätze vermehrt mit Kameras überwacht werden, die mithilfe von Software auffälliges Verhalten oder Gesichter automatisch erkennen können."],
    ["Flächenverbrauch", "Das Land soll ein striktes „Netto-Null“-Ziel für die Neuversiegelung von Flächen bis 2030 gesetzlich festschreiben.", "Jeden Tag werden neue Flächen für Bauprojekte versiegelt. Das Ziel „Netto-Null“ bedeutet, dass ab einem bestimmten Zeitpunkt gar keine neuen Flächen mehr verbaut werden dürfen, ohne einen Ausgleich an anderer Stelle."],
    ["Kernkraft", "Der Standort Neckarwestheim soll für eine mögliche Reaktivierung als Energiereserve gesichert werden.", "Nach dem Atomausstieg stehen Anlagen wie Neckarwestheim still. Es wird debattiert, ob diese Standorte als einsatzbereite Energiereserve erhalten bleiben sollten, um die Stromversorgung im Krisenfall zu sichern."],
    ["Wahlalter 16", "Das Wahlrecht ab 16 Jahren bei Landtagswahlen soll beibehalten werden.", "Seit kurzem dürfen 16-Jährige in BW bei Landtagswahlen wählen. Es wird diskutiert, ob dieses Recht beibehalten werden soll oder ob die Wahlberechtigung wieder erst ab der Volljährigkeit gelten sollte."],
    ["Wolfsabschuss", "Die Hürden für den Abschuss von Wölfen bei Bedrohung von Nutztieren sollen gesenkt werden.", "Die Rückkehr des Wolfes führt zu Rissen bei Schafen und Ziegen. Diskutiert wird, ob die rechtlichen Hürden gesenkt werden sollten, um Tiere, die wiederholt Herden angreifen, schneller abschießen zu dürfen."],
    ["Mietendeckel", "In Städten mit besonders angespanntem Wohnungsmarkt soll ein staatlicher Mietendeckel eingeführt werden.", "In vielen Städten steigen die Mieten rasant an. Ein gesetzlicher Deckel würde die Mietpreise für einen bestimmten Zeitraum staatlich einfrieren oder auf einen Maximalwert begrenzen."],
    ["Gender-Verbot", "An Schulen und in der Verwaltung soll die Verwendung von Gendersprache (z. B. Sternchen) untersagt werden.", "In der öffentlichen Verwaltung und an Schulen wird teilweise geschlechtergerechte Sprache (z. B. Gendersternchen) genutzt. Ein Verbot würde die Verwendung solcher Sonderzeichen in offiziellen Dokumenten untersagen."],
    ["Industriestrompreis", "Das Land soll einen eigenen Fonds zur Subventionierung der Stromkosten für Zulieferbetriebe auflegen.", "Hohe Energiekosten belasten die Industrie im Land. Eine staatliche Subventionierung des Strompreises für energieintensive Unternehmen soll deren Abwanderung verhindern, ist aber wettbewerbsrechtlich umstritten."],
    ["Notenpflicht", "An allen Grundschulen sollen ab der 3. Klasse wieder verpflichtend Noten vergeben werden.", "Oft werden Noten in der Grundschule durch schriftliche Lernberichte ersetzt. Es wird diskutiert, ob klassische Ziffernnoten ab der dritten Klasse wieder zur Pflicht werden sollen, um Leistungen vergleichbarer zu machen."],
    ["Nationalpark Schwarzwald", "Der Anteil der forstwirtschaftlich ungenutzten Waldflächen im Nationalpark soll über die bisherigen Pläne hinaus erweitert werden.", "Der Nationalpark schützt Flächen, die nicht wirtschaftlich genutzt werden. Diskutiert wird, ob diese „Kernzonen“ über die aktuellen Pläne hinaus weiter ausgedehnt werden sollen."],
    ["Sprach-Vorschule", "Kinder mit Sprachdefiziten sollen zu einem verpflichtenden Vorschuljahr verpflichtet werden.", "Immer mehr Kinder beherrschen bei der Einschulung Deutsch nicht ausreichend. Ein verpflichtendes Vorschuljahr soll sicherstellen, dass betroffene Kinder durch gezielte Förderung auf den Unterricht vorbereitet werden."],
    ["Radweg-Priorität", "Der Ausbau von Radwegen soll finanziell Vorrang vor der Sanierung von Landesstraßen haben.", "Bei der Budgetverteilung im Verkehrsbereich steht die Frage im Raum, ob der Ausbau von Radwegen Vorrang vor der Instandhaltung und Sanierung von Straßen für Autos haben sollte."],
    ["Grundsteuer", "Das baden-württembergische Bodenwertmodell soll abgeschafft und durch das Bundesmodell ersetzt werden.", "Baden-Württemberg nutzt ein Modell, das sich allein am Bodenwert orientiert. Kritiker fordern die Rückkehr zum Bundesmodell, bei dem auch das Gebäude auf dem Grundstück mitbewertet wird."],
    ["Krankenhäuser", "Kleine Kliniken im ländlichen Raum sollen durch Landesmittel vor der Schließung bewahrt werden.", "Viele kleine Krankenhäuser auf dem Land sind unrentabel. Gefragt ist, ob das Land diese Standorte finanziell stützen sollte, um die medizinische Versorgung in der Fläche zu garantieren."],
    ["Ländle-KI", "Baden-Württemberg soll Milliarden in regionale KI-Modelle für die heimische Wirtschaft investieren.", "Um technologisch unabhängig zu bleiben, wird diskutiert, ob das Land Milliarden in die Entwicklung einer eigenen KI-Infrastruktur investieren sollte, die speziell auf die Bedürfnisse der heimischen Industrie zugeschnitten ist."],
    ["Studiengebühren", "Die Gebühren für Studierende aus Nicht-EU-Ländern sollen wieder abgeschafft werden.", "Derzeit zahlen Studierende von außerhalb der EU in BW 1.500 Euro Gebühren pro Semester. Es wird diskutiert, ob diese Gebühren abgeschafft werden sollten, um international attraktiver für Fachkräfte zu werden."],
    ["Solarpflicht", "Die Photovoltaik-Pflicht soll auch auf die Sanierung bestehender Wohnhäuser ausgeweitet werden.", "Während Photovoltaik bei Neubauten Pflicht ist, wird nun darüber gestritten, ob Hausbesitzer auch bei der Sanierung alter Dächer verpflichtet werden sollen, Solarpanels zu installieren."],
    ["Waffenverbotszonen", "Kommunen sollen leichter Messer- und Waffenverbotszonen in Innenstädten einrichten dürfen.", "Um Gewaltkriminalität vorzubeugen, könnten Kommunen Zonen einrichten, in denen das Mitführen von Messern und Waffen generell verboten ist. Es geht um die Frage, ob die Hürden für solche Zonen gesenkt werden sollen."],
    ["Gratis Mittagessen", "Das Land soll die Kosten für das Mittagessen in allen Kitas und Grundschulen komplett übernehmen.", "Die Mittagsverpflegung in Kitas und Schulen ist oft kostenpflichtig. Es steht zur Debatte, ob das Land die Kosten für eine warme Mahlzeit für alle Kinder komplett übernehmen sollte."]
]

# --- SESSION STATE ---
if 'order' not in st.session_state:
    st.session_state.order = list(range(len(DATA)))
    random.shuffle(st.session_state.order)
    st.session_state.step, st.session_state.choices = 0, []

def handle(q_idx, val):
    st.session_state.choices.append({"index": q_idx, "val": val})
    st.session_state.step += 1

# Neuer Bewertungsfunktion
def calculate_pts(u, p):
    if u == 0: return 0  # Neutraler Nutzer = keine Punkte-Basis
    
    # Wir berechnen den Abstand auf einer Skala von 0 bis 4
    # (z.B. von ++ [2] bis -- [-2] ist der Abstand 4)
    distance = abs(u - p)
    
    # Starke Meinung des Nutzers (++ oder --)
    if abs(u) == 2:
        mapping = {0: 6, 1: 4, 2: 2, 3: 1, 4: 0}
        return mapping.get(distance, 0)
    
    # Normale Meinung des Nutzers (+ oder -)
    if abs(u) == 1:
        mapping = {0: 3, 1: 4, 2: 2, 3: 0, 4: 0} 
        # Hinweis: Bei Abstand 1 (u=+1, p=+2) gibt es 4 Pkt, 
        # weil die Partei "überzeugt" ist, was der Nutzer nur "gut" findet.
        return mapping.get(distance, 0)
    
    return 0

# Alte Funktion anhand folgender Matrix

# --- BERECHNUNGSLOGIK ---
# Nutzer | P:+2 | P:+1 | P:0 | P:-1 | P:-2
# ++(+2) |  2   |  1   |  0  |  -1  |  -2
# + (+1) |  1   |  1   |  1  |   0  |   0
# o  (0) |  0   |  0   |  0  |   0  |   0
# - (-1) |  0   |  0   |  1  |   1  |   1
# --(-2) | -2   | -1   |  0  |   1  |   2

def calculate_pts_old(u, p):
    if u == 2: # Nutzer ++
        if p == 2: return 2
        if p == 1: return 1
        if p == 0: return 0
        if p == -1: return -1
        if p == -2: return -2
    if u == 1: # Nutzer +
        if p >= 0: return 1
        return 0
    if u == 0: # Nutzer o
        return 0
    if u == -1: # Nutzer -
        if p <= 0: return 1
        return 0
    if u == -2: # Nutzer --
        if p == -2: return 2
        if p == -1: return 1
        if p == 0: return 0
        if p == 1: return -1
        if p == 2: return -2
    return 0

def get_icon(val):
    mapping = {2: "✅✅", 1: "✅", 0: "⚪", -1: "❌", -2: "❌❌"}
    return mapping.get(val, "?")

def render_bar(name, points, color):
    # Skalierung auf 150 Punkte (25 Thesen * max 6 Punkte)
    display_width = min(100, max(0, (points / 150) * 100))
    st.markdown(f"""
    <div style="margin-top: 10px;">
        <div style="display:flex; justify-content:space-between; margin-bottom: 2px;">
            <span style="font-weight:bold; color:{color};">{name}</span>
            <span style="font-weight:bold;">{points} / 150 Pkt</span>
        </div>
        <div style="background:#e0e0e0; border-radius:10px; height:18px; width:100%;">
            <div style="background:{color}; width:{display_width}%; height:18px; border-radius:10px; transition: width 0.8s ease-in-out;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- GUI ---
st.title("🗳️ Wahl-O-Mat BW 2026")

if st.session_state.step < len(DATA):
    idx = st.session_state.order[st.session_state.step]
    h, t, i = DATA[idx][0], DATA[idx][1], DATA[idx][2]
    
    st.write(f"**These {st.session_state.step + 1} von 25**")
    st.progress(st.session_state.step / 25)
    st.markdown(f"## {h}\n#### {t}")
    with st.expander("ℹ️ Erläuterung"): st.write(i)
    
    st.write("---")
    cols = st.columns(5)
    opts = [("✅✅", 2), ("✅", 1), ("⚪", 0), ("❌", -1), ("❌❌", -2)]
    for b_idx, (icon, val) in enumerate(opts):
        if cols[b_idx].button(icon, use_container_width=True, key=f"b{st.session_state.step}{b_idx}"):
            handle(idx, val)
            st.rerun()
    
    if st.session_state.step > 0:
        if st.button("⬅️ Zurück"):
            st.session_state.step -= 1
            st.session_state.choices.pop()
            st.rerun()
else:
    st.balloons()
    st.header("🎉 Dein Ergebnis")
    
    final_results = []
    for party in PARTIES:
        total_pts = 0
        details, conflicts = [], []
        for c in st.session_state.choices:
            p_val = PARTY_DATA[party][c["index"]]
            pts = calculate_pts(c["val"], p_val)
            total_pts += pts
            
            row = {"These": DATA[c["index"]][0], "Du": get_icon(c["val"]), "Partei": get_icon(p_val), "Punkte": pts}
            details.append(row)
            if pts == 0 and abs(c["val"]) == 2:
                conflicts.append(row)
        
        perc = (total_pts / 150) * 100
        final_results.append({
            "name": party, "pts": total_pts, "perc": round(perc, 1),
            "color": PARTY_COLORS[party], "details": details, "conflicts": conflicts
        })
    
    sorted_results = sorted(final_results, key=lambda x: x["pts"], reverse=True)

    # Top 3 Podium
    st.subheader("🏆 Deine Top-Matches")
    pod_cols = st.columns(3)
    for i, entry in enumerate(sorted_results[:3]):
        with pod_cols[i]:
            st.markdown(f"""
            <div style="background:{entry['color']}; padding:20px; border-radius:15px; text-align:center; color:white;">
                <h1 style="margin:0;">#{i+1}</h1>
                <h2 style="margin:0;">{entry['name']}</h2>
                <h3 style="margin:0;">{entry['perc']}%</h3>
            </div>
            """, unsafe_allow_html=True)
    
    st.write("---")

    # Ergebnisliste
    st.subheader("📊 Alle Parteien im Detail")
    for entry in sorted_results:
        render_bar(f"{entry['name']} ({entry['perc']}%)", entry['pts'], entry['color'])
        with st.expander(f"Vergleich einblenden"):
            if entry["conflicts"]:
                st.warning("⚡ Harte Gegensätze bei deinen Kern-Themen")
                st.table(entry["conflicts"])
            st.table(entry["details"])

    if st.button("🔄 Test neu starten"):
        st.session_state.step, st.session_state.choices = 0, []
        st.rerun()
