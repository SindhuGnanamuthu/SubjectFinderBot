from flask import Flask, request, render_template_string

app = Flask(__name__)

DEPT_CODE = "1052"
DEPT_NAME = "Computer Engineering"

# ===== SUBJECT MAPPINGS =====
schemes = {
    # ---- OLD SCHEME (Z/M) ----
    "Old Scheme": {
        "1": {
            "1": {"SNAME": "COMMUNICATIVE ENGLISH - I", "NSNAME": "COMMUNICATIVE ENGLISH - I", "NSCODE": "EN231350", "TYPE": "Practical"},
            "2": {"SNAME": "ENGINEERING MATHEMATICS - I", "NSNAME": "BASIC MATHEMATICS", "NSCODE": "MA231120", "TYPE": "Theory"},
            "3": {"SNAME": "ENGINEERING PHYSICS - I", "NSNAME": "BASIC PHYSICS", "NSCODE": "PH231330", "TYPE": "Theory"},
            "4": {"SNAME": "ENGINEERING CHEMISTRY - I", "NSNAME": "BASIC CHEMISTRY", "NSCODE": "CH231340", "TYPE": "Theory"},
            "5": {"SNAME": "ENGINEERING GRAPHICS - I", "NSNAME": "DRAFTING PRACTICES", "NSCODE": "DP232270", "TYPE": "Practical"}
        },
        "2": {
            "1": {"SNAME": "COMMUNICATIVE ENGLISH - II", "NSNAME": "COMMUNICATIVE ENGLISH II", "NSCODE": "EN232480", "TYPE": "Practical"},
            "2": {"SNAME": "ENGINEERING MATHEMATICS - II", "NSNAME": "APPLIED MATHEMATICS II (CIRCUIT)", "NSCODE": "MA232432", "TYPE": "Practical"},
            "3": {"SNAME": "ENGINEERING PHYSICS - II", "NSNAME": "APPLIED PHYSICS II (CIRCUIT)", "NSCODE": "PH232442", "TYPE": "Practical"},
            "4": {"SNAME": "ENGINEERING CHEMISTRY - II", "NSNAME": "APPLIED CHEMISTRY II (CIRCUIT)", "NSCODE": "CH232452", "TYPE": "Practical"},
            "5": {"SNAME": "ENGINEERING GRAPHICS - II", "NSNAME": "DRAFTING PRACTICES", "NSCODE": "DP232270", "TYPE": "Practical"}
        },
        "3": {
            "1": {"SNAME": "BASICS OF ELECTRICAL AND ELECTRONICS ENGINEERING", "NSNAME": "DIGITAL LOGIC DESIGN", "NSCODE": "1052233110", "TYPE": "Theory"},
            "2": {"SNAME": "OPERATING SYSTEMS", "NSNAME": "OPERATING SYSTEMS", "NSCODE": "1052233640", "TYPE": "Practicum"},
            "3": {"SNAME": "C PROGRAMMING AND DATA STRUCTURE", "NSNAME": "C PROGRAMMING", "NSCODE": "1052233440", "TYPE": "Practicum"}
        },
        "4": {
            "1": {"SNAME": "COMPUTER ARCHITECTURE", "NSNAME": "COMPUTER ARCHITECTURE", "NSCODE": "4052410", "TYPE": "Theory"},
            "2": {"SNAME": "WEB DESIGN AND PROGRAMMING", "NSNAME": "WEB DESIGNING", "NSCODE": "1052233540", "TYPE": "Practicum"},
            "3": {"SNAME": "OBJECT ORIENTED PROGRAMMING WITH JAVA", "NSNAME": "JAVA PROGRAMMING", "NSCODE": "1052233940", "TYPE": "Practicum"},
            "4": {"SNAME": "RDBMS", "NSNAME": "RDBMS", "NSCODE": "1052233230", "TYPE": "Practicum"}
        },
        "5": {
            "1": {"SNAME": "PYTHON PROGRAMMING", "NSNAME": "Python Programming", "NSCODE": "1052234440", "TYPE": "Practicum"},
            "2": {"SNAME": "CLOUD COMPUTING AND INTERNET OF THINGS", "NSNAME": "Cloud Computing", "NSCODE": "1052235130", "TYPE": "Practicum"},
            "3": {"SNAME": "COMPONENT BASED TECHNOLOGY", "NSNAME": "Component Based Technologies", "NSCODE": "1052235543", "TYPE": "Practical"},
            "4": {"SNAME": "ARTIFICIAL INTELLIGENCE AND DATA ANALYTICS", "NSNAME": "Artificial Intelligence", "NSCODE": "1052235215", "TYPE": "Theory"},
            "5": {"SNAME": "MOBILE COMPUTING", "NSNAME": "Mobile Computing", "NSCODE": "1052235542", "TYPE": "Practical"}
        },
        "6": {
            "1": {"SNAME": "COMPUTER HARDWARE AND SERVICING", "NSNAME": "COMPUTER HARDWARE AND SERVICING", "NSCODE": "4052610", "TYPE": "Theory"},
            "2": {"SNAME": "COMPUTER NETWORKS AND SECURITY", "NSNAME": "COMPUTER NETWORKS AND SECURITY", "NSCODE": "4052620", "TYPE": "Theory"},
            "3": {"SNAME": "SOFTWARE ENGINEERING", "NSNAME": "SOFTWARE ENGINEERING", "NSCODE": "4052631", "TYPE": "Theory"},
            "4": {"SNAME": "MULTIMEDIA SYSTEMS", "NSNAME": "MULTIMEDIA SYSTEMS", "NSCODE": "4052632", "TYPE": "Theory"},
            "5": {"SNAME": "DATA SCIENCE AND BIG DATA", "NSNAME": "DATA SCIENCE AND BIG DATA", "NSCODE": "4052633", "TYPE": "Theory"}
        }
    },

    # ---- R2023 SCHEME ----
    "R2023": {
        "1": {
            "1": {"SNAME": "TAMIL MARABU", "NSNAME": "TAMIL MARABU", "NSCODE": "TA231110", "TYPE": "Theory"},
            "2": {"SNAME": "BASIC MATHEMATICS", "NSNAME": "BASIC MATHEMATICS", "NSCODE": "MA231120", "TYPE": "Theory"},
            "3": {"SNAME": "BASIC PHYSICS", "NSNAME": "BASIC PHYSICS", "NSCODE": "PH231330", "TYPE": "Theory"},
            "4": {"SNAME": "BASIC CHEMISTRY", "NSNAME": "BASIC CHEMISTRY", "NSCODE": "CH231340", "TYPE": "Theory"}
        },
        "2": {
            "1": {"SNAME": "TAMILS AND TECHNOLOGY", "NSNAME": "TAMILS AND TECHNOLOGY", "NSCODE": "TA232110", "TYPE": "Theory"},
            "2": {"SNAME": "BASICS OF COMPUTER ENGINEERING", "NSNAME": "BASICS OF COMPUTER ENGINEERING", "NSCODE": "CS232120", "TYPE": "Theory"}
        },
        "3": {
            "1": {"SNAME": "DIGITAL LOGIC DESIGN", "NSNAME": "DIGITAL LOGIC DESIGN", "NSCODE": "1052233110", "TYPE": "Theory"},
            "2": {"SNAME": "RDBMS", "NSNAME": "RDBMS", "NSCODE": "1052233230", "TYPE": "Practicum"}
        },
        "4": {
            "1": {"SNAME": "COMPUTER NETWORKS AND SECURITY", "NSNAME": "COMPUTER NETWORKS AND SECURITY", "NSCODE": "1052234110", "TYPE": "Theory"},
            "2": {"SNAME": "DATA STRUCTURES USING PYTHON", "NSNAME": "DATA STRUCTURES USING PYTHON", "NSCODE": "1052234230", "TYPE": "Practicum"}
        },
        "5": {
            "1": {"SNAME": "Cloud Computing", "NSNAME": "Cloud Computing", "NSCODE": "1052235130", "TYPE": "Practicum"},
            "2": {"SNAME": "Machine Learning", "NSNAME": "Machine Learning", "NSCODE": "1052235211", "TYPE": "Theory"},
            "3": {"SNAME": "Data Warehousing and Data Mining", "NSNAME": "Data Warehousing and Data Mining", "NSCODE": "1052235212", "TYPE": "Theory"},
            "4": {"SNAME": "Ethical Hacking", "NSNAME": "Ethical Hacking", "NSCODE": "1052235213", "TYPE": "Theory"},
            "5": {"SNAME": "Agile Product Development", "NSNAME": "Agile Product Development", "NSCODE": "1052235214", "TYPE": "Theory"},
            "6": {"SNAME": "Artificial Intelligence", "NSNAME": "Artificial Intelligence", "NSCODE": "1052235215", "TYPE": "Theory"}
        }
    }
}

# ===== HTML TEMPLATE =====
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Subject Finder Bot</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f7fb; margin: 0; padding: 20px; }
        h1 { text-align: center; color: #333; }
        form { background: white; padding: 20px; border-radius: 10px; width: 400px; margin: 0 auto;
               box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        input, select, button { width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; }
        button { background: #007BFF; color: white; border: none; font-size: 16px; cursor: pointer; }
        button:hover { background: #0056b3; }
        .result { width: 400px; margin: 20px auto; padding: 15px; border-radius: 8px; }
        .Theory { background-color: #d0e7ff; border-left: 6px solid #007BFF; }
        .Practical { background-color: #d8f8d8; border-left: 6px solid #28a745; }
        .Practicum { background-color: #fff7d1; border-left: 6px solid #ffc107; }
        .EndExam { background-color: #ffe6e6; border-left: 6px solid #dc3545; }
    </style>
</head>
<body>
    <h1>Subject Finder Bot</h1>
    <form method="POST" action="/get">
        <label><b>Department Code:</b></label>
        <input type="text" name="dept" value="1052" readonly>
        <label><b>Scheme:</b></label>
        <select name="scheme" required>
            <option value="">-- Select Scheme --</option>
            <option value="Old Scheme">Old Scheme (Z/M)</option>
            <option value="R2023">R2023</option>
        </select>
        <label><b>Semester:</b></label>
        <input type="number" name="sem" required min="1" max="6" placeholder="e.g. 5">
        <label><b>Column:</b></label>
        <input type="number" name="col" required min="1" max="6" placeholder="e.g. 2">
        <button type="submit">Find Subject</button>
    </form>

    {% if result %}
    <div class="result {{ type_class }}">
        {{ result|safe }}
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/get", methods=["POST"])
def get_subject():
    dept = request.form.get("dept")
    scheme = request.form.get("scheme")
    sem = request.form.get("sem")
    col = request.form.get("col")

    if dept != DEPT_CODE:
        return render_template_string(HTML_TEMPLATE, result="❌ Invalid Department Code.", type_class="EndExam")

    if scheme not in schemes:
        return render_template_string(HTML_TEMPLATE, result="⚠️ Please select a valid scheme.", type_class="EndExam")

    data = schemes[scheme].get(sem, {}).get(col)
    if not data:
        return render_template_string(HTML_TEMPLATE, result=f"⚠️ No subject found for {scheme} — Semester {sem}, Column {col}.", type_class="EndExam")

    subj = data
    type_class = subj['TYPE'].replace(" ", "")
    result = (f"<b>Department:</b> {DEPT_NAME} ({DEPT_CODE})<br>"
              f"<b>Scheme:</b> {scheme}<br>"
              f"<b>Semester:</b> {sem}<br>"
              f"<b>Column:</b> {col}<br><br>"
              f"<b>Subject:</b> {subj['SNAME']}<br>"
              f"<b>Equivalent Subject:</b> {subj['NSNAME']}<br>"
              f"<b>NSCODE:</b> {subj['NSCODE']}<br>"
              f"<b>Exam Type:</b> {subj['TYPE']}")

    return render_template_string(HTML_TEMPLATE, result=result, type_class=type_class)

if __name__ == "__main__":
    app.run(debug=True)
