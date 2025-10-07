from flask import Flask, request, render_template_string

app = Flask(__name__)

DEPT_CODE = "1052"
DEPT_NAME = "Computer Engineering"

# ===== SUBJECT MAPPINGS =====
schemes = {

    # ---- OLD SCHEME (Z/M) ----
    "Old Scheme": {
        "1": {
            "1": {"SNAME": "COMMUNICATIVE ENGLISH - I", "NSNAME": "COMMUNICATIVE ENGLISH - I", "TYPE": "Practical"},
            "2": {"SNAME": "ENGINEERING MATHEMATICS - I", "NSNAME": "BASIC MATHEMATICS", "TYPE": "Theory"},
            "3": {"SNAME": "ENGINEERING PHYSICS - I", "NSNAME": "BASIC PHYSICS", "TYPE": "Theory"},
            "4": {"SNAME": "ENGINEERING CHEMISTRY - I", "NSNAME": "BASIC CHEMISTRY", "TYPE": "Theory"},
            "5": {"SNAME": "ENGINEERING GRAPHICS - I", "NSNAME": "DRAFTING PRACTICES", "TYPE": "Practical"}
        },
        "2": {
            "1": {"SNAME": "COMMUNICATIVE ENGLISH - II", "NSNAME": "COMMUNICATIVE ENGLISH II", "TYPE": "Practical"},
            "2": {"SNAME": "ENGINEERING MATHEMATICS - II", "NSNAME": "APPLIED MATHEMATICS II (CIRCUIT)", "TYPE": "Practical"},
            "3": {"SNAME": "ENGINEERING PHYSICS - II", "NSNAME": "APPLIED PHYSICS II (CIRCUIT)", "TYPE": "Practical"},
            "4": {"SNAME": "ENGINEERING CHEMISTRY - II", "NSNAME": "APPLIED CHEMISTRY II (CIRCUIT)", "TYPE": "Practical"},
            "5": {"SNAME": "ENGINEERING GRAPHICS - II", "NSNAME": "DRAFTING PRACTICES", "TYPE": "Practical"}
        },
        "3": {
            "1": {"SNAME": "BASICS OF ELECTRICAL AND ELECTRONICS ENGINEERING", "NSNAME": "DIGITAL LOGIC DESIGN", "TYPE": "Theory"},
            "2": {"SNAME": "OPERATING SYSTEMS", "NSNAME": "OPERATING SYSTEMS", "TYPE": "Practical"},
            "3": {"SNAME": "C PROGRAMMING AND DATA STRUCTURE", "NSNAME": "C PROGRAMMING", "TYPE": "Practical"}
        },
        "4": {
            "1": {"SNAME": "COMPUTER ARCHITECTURE", "NSNAME": "COMPUTER ARCHITECTURE", "TYPE": "Theory"},
            "2": {"SNAME": "WEB DESIGN AND PROGRAMMING", "NSNAME": "WEB DESIGNING", "TYPE": "Practical"},
            "3": {"SNAME": "OBJECT ORIENTED PROGRAMMING WITH JAVA", "NSNAME": "JAVA PROGRAMMING", "TYPE": "Practical"},
            "4": {"SNAME": "RDBMS", "NSNAME": "RDBMS", "TYPE": "Practicum"}
        },
        "5": {
            "1": {"SNAME": "PYTHON PROGRAMMING", "NSNAME": "Python Programming", "TYPE": "Practical"},
            "2": {"SNAME": "CLOUD COMPUTING AND INTERNET OF THINGS", "NSNAME": "Cloud Computing", "TYPE": "Practicum"},
            "3": {"SNAME": "COMPONENT BASED TECHNOLOGY", "NSNAME": "Component Based Technologies", "TYPE": "Practical"},
            "4": {"SNAME": "ARTIFICIAL INTELLIGENCE AND DATA ANALYTICS", "NSNAME": "Artificial Intelligence", "TYPE": "Theory"},
            "5": {"SNAME": "MOBILE COMPUTING", "NSNAME": "Mobile Computing", "TYPE": "Practical"}
        },
        "6": {
            "1": {"SNAME": "COMPUTER HARDWARE AND SERVICING", "NSNAME": "COMPUTER HARDWARE AND SERVICING", "TYPE": "Theory"},
            "2": {"SNAME": "COMPUTER NETWORKS AND SECURITY", "NSNAME": "COMPUTER NETWORKS AND SECURITY", "TYPE": "Theory"},
            "3": {"SNAME": "SOFTWARE ENGINEERING", "NSNAME": "SOFTWARE ENGINEERING", "TYPE": "Theory"},
            "4": {"SNAME": "MULTIMEDIA SYSTEMS", "NSNAME": "MULTIMEDIA SYSTEMS", "TYPE": "Theory"},
            "5": {"SNAME": "DATA SCIENCE AND BIG DATA", "NSNAME": "DATA SCIENCE AND BIG DATA", "TYPE": "Theory"}
        }
    },

    # ---- R2023 SCHEME ----
    "R2023": {
        "1": {
            "1": {"SNAME": "TAMIL MARABU", "NSNAME": "TAMIL MARABU", "TYPE": "Theory"},
            "2": {"SNAME": "BASIC MATHEMATICS", "NSNAME": "BASIC MATHEMATICS", "TYPE": "Theory"},
            "3": {"SNAME": "BASIC PHYSICS", "NSNAME": "BASIC PHYSICS", "TYPE": "Theory"},
            "4": {"SNAME": "BASIC CHEMISTRY", "NSNAME": "BASIC CHEMISTRY", "TYPE": "Theory"}
        },
        "2": {
            "1": {"SNAME": "TAMILS AND TECHNOLOGY", "NSNAME": "TAMILS AND TECHNOLOGY", "TYPE": "Theory"},
            "2": {"SNAME": "BASICS OF COMPUTER ENGINEERING", "NSNAME": "BASICS OF COMPUTER ENGINEERING", "TYPE": "Theory"},
            "3": {"SNAME": "PYTHON PROGRAMMING", "NSNAME": "PYTHON PROGRAMMING", "TYPE": "Practicum"},
            "4": {"SNAME": "ENGINEERING GRAPHICS", "NSNAME": "ENGINEERING GRAPHICS", "TYPE": "Practicum"}
        },
        "3": {
            "1": {"SNAME": "DIGITAL LOGIC DESIGN", "NSNAME": "DIGITAL LOGIC DESIGN", "TYPE": "Theory"},
            "2": {"SNAME": "RDBMS", "NSNAME": "RDBMS", "TYPE": "Practicum"},
            "3": {"SNAME": "OPERATING SYSTEMS", "NSNAME": "OPERATING SYSTEMS", "TYPE": "Theory"},
            "4": {"SNAME": "DATA STRUCTURES USING PYTHON", "NSNAME": "DATA STRUCTURES USING PYTHON", "TYPE": "Practicum"}
        },
        "4": {
            "1": {"SNAME": "COMPUTER NETWORKS AND SECURITY", "NSNAME": "COMPUTER NETWORKS AND SECURITY", "TYPE": "Theory"},
            "2": {"SNAME": "JAVA PROGRAMMING", "NSNAME": "JAVA PROGRAMMING", "TYPE": "Practicum"},
            "3": {"SNAME": "WEB TECHNOLOGIES", "NSNAME": "WEB TECHNOLOGIES", "TYPE": "Practicum"},
            "4": {"SNAME": "DATA VISUALIZATION", "NSNAME": "DATA VISUALIZATION", "TYPE": "Theory"}
        },
        "5": {
            "1": {"SNAME": "CLOUD COMPUTING", "NSNAME": "CLOUD COMPUTING", "TYPE": "Practicum"},
            "2": {"SNAME": "MACHINE LEARNING", "NSNAME": "MACHINE LEARNING", "TYPE": "Theory"},
            "3": {"SNAME": "DATA WAREHOUSING AND DATA MINING", "NSNAME": "DATA WAREHOUSING AND DATA MINING", "TYPE": "Theory"},
            "4": {"SNAME": "ETHICAL HACKING", "NSNAME": "ETHICAL HACKING", "TYPE": "Theory"},
            "5": {"SNAME": "AGILE PRODUCT DEVELOPMENT", "NSNAME": "AGILE PRODUCT DEVELOPMENT", "TYPE": "Theory"},
            "6": {"SNAME": "ARTIFICIAL INTELLIGENCE", "NSNAME": "ARTIFICIAL INTELLIGENCE", "TYPE": "Theory"}
        },
        "6": {
            "1": {"SNAME": "FULL STACK DEVELOPMENT", "NSNAME": "FULL STACK DEVELOPMENT", "TYPE": "Practicum"},
            "2": {"SNAME": "INTERNET OF THINGS", "NSNAME": "INTERNET OF THINGS", "TYPE": "Practicum"},
            "3": {"SNAME": "PROJECT WORK", "NSNAME": "PROJECT WORK", "TYPE": "End Exam"}
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
              f"<b>Exam Type:</b> {subj['TYPE']}")

    return render_template_string(HTML_TEMPLATE, result=result, type_class=type_class)

if __name__ == "__main__":
    app.run(debug=True)
