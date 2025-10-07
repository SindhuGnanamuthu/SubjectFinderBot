from flask import Flask, request, render_template_string

app = Flask(__name__)

DEPT_CODE = "1052"
DEPT_NAME = "Computer Engineering"

# ===== SUBJECT MAPPINGS =====
schemes = {
    # ---- OLD SCHEME (Z/M) ----
    "Old Scheme": {
        "1": {
            "1": {"SNAME": "COMMUNICATIVE ENGLISH - I", "NSNAME": "COMMUNICATIVE ENGLISH I", "TYPE": "Theory"},
            "2": {"SNAME": "ENGINEERING MATHEMATICS - I", "NSNAME": "BASIC MATHEMATICS", "TYPE": "Theory"},
            "3": {"SNAME": "ENGINEERING PHYSICS - I", "NSNAME": "BASIC PHYSICS", "TYPE": "Theory"},
            "4": {"SNAME": "ENGINEERING CHEMISTRY - I", "NSNAME": "BASIC CHEMISTRY", "TYPE": "Theory"},
            "5": {"SNAME": "ENGINEERING GRAPHICS - I", "NSNAME": "DRAFTING PRACTICES", "TYPE": "Practical"}
        },
        "4": {
            "1": {"SNAME": "COMPUTER ARCHITECTURE", "NSNAME": "COMPUTER ARCHITECTURE", "TYPE": "Theory"},
            "2": {"SNAME": "WEB DESIGN AND PROGRAMMING", "NSNAME": "WEB DESIGNING", "TYPE": "Practical"},
            "3": {"SNAME": "OBJECT ORIENTED PROGRAMMING WITH JAVA", "NSNAME": "JAVA PROGRAMMING", "TYPE": "Theory"},
            "4": {"SNAME": "RDBMS", "NSNAME": "RDBMS", "TYPE": "Practical"}
        },
        "5": {
            "1": {"SNAME": "PYTHON PROGRAMMING", "NSNAME": "Python Programming", "TYPE": "Theory"},
            "2": {"SNAME": "CLOUD COMPUTING AND INTERNET OF THINGS", "NSNAME": "Cloud Computing", "TYPE": "Theory"},
            "3": {"SNAME": "COMPONENT BASED TECHNOLOGY", "NSNAME": "Component Based Technologies", "TYPE": "Practical"},
            "4": {"SNAME": "ARTIFICIAL INTELLIGENCE AND DATA ANALYTICS", "NSNAME": "Artificial Intelligence", "TYPE": "Theory"},
            "5": {"SNAME": "MOBILE COMPUTING", "NSNAME": "Mobile Computing", "TYPE": "End Exam"}
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
            "2": {"SNAME": "BASICS OF COMPUTER ENGINEERING", "NSNAME": "BASICS OF COMPUTER ENGINEERING", "TYPE": "Theory"}
        },
        "3": {
            "1": {"SNAME": "DIGITAL LOGIC DESIGN", "NSNAME": "DIGITAL LOGIC DESIGN", "TYPE": "Theory"},
            "2": {"SNAME": "RDBMS", "NSNAME": "RDBMS", "TYPE": "Practicum"}
        },
        "4": {
            "1": {"SNAME": "COMPUTER NETWORKS AND SECURITY", "NSNAME": "COMPUTER NETWORKS AND SECURITY", "TYPE": "Theory"},
            "2": {"SNAME": "DATA STRUCTURES USING PYTHON", "NSNAME": "DATA STRUCTURES USING PYTHON", "TYPE": "Practicum"}
        },
        "5": {
            "1": {"SNAME": "CLOUD COMPUTING", "NSNAME": "CLOUD COMPUTING", "TYPE": "Practicum"},
            "2": {"SNAME": "MACHINE LEARNING", "NSNAME": "MACHINE LEARNING", "TYPE": "Theory"},
            "3": {"SNAME": "DATA WAREHOUSING AND DATA MINING", "NSNAME": "DATA WAREHOUSING AND DATA MINING", "TYPE": "Theory"},
            "4": {"SNAME": "ETHICAL HACKING", "NSNAME": "ETHICAL HACKING", "TYPE": "Theory"},
            "5": {"SNAME": "AGILE PRODUCT DEVELOPMENT", "NSNAME": "AGILE PRODUCT DEVELOPMENT", "TYPE": "Theory"},
            "6": {"SNAME": "ARTIFICIAL INTELLIGENCE", "NSNAME": "ARTIFICIAL INTELLIGENCE", "TYPE": "Theory"}
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
        body { font-family: Arial, sans-serif; background-color: #f3f7fb; margin: 0; padding: 20px; }
        h1 { text-align: center; color: #222; }
        form { background: white; padding: 20px; border-radius: 10px; width: 400px; margin: 0 auto; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        input, select { width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; }
        button { width: 100%; padding: 10px; background: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background: #0056b3; }
        .result { background: #eaf6ff; padding: 20px; margin-top: 25px; border-left: 6px solid #007BFF; border-radius: 8px; line-height: 1.6; font-size: 15px; }
        .error { background: #ffe6e6; padding: 15px; border-left: 6px solid #ff4d4d; }
    </style>
</head>
<body>
    <h1>Subject Finder Bot</h1>
    <form method="POST" action="/get">
        <label><b>Department Code:</b></label>
        <input type="text" name="dept" required value="1052" readonly>
        <label><b>Scheme:</b></label>
        <select name="scheme" required>
            <option value="">-- Select Scheme --</option>
            <option value="Old Scheme">Old Scheme (Z/M)</option>
            <option value="R2023">R2023</option>
        </select>
        <label><b>Semester:</b></label>
        <input type="number" name="sem" required placeholder="e.g. 5">
        <label><b>Column:</b></label>
        <input type="number" name="col" required placeholder="e.g. 2">
        <button type="submit">Find Subject</button>
    </form>

    {% if result %}
    <div class="result">{{ result|safe }}</div>
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
        result = f"<div class='error'>❌ Invalid Department Code: {dept}. Please use {DEPT_CODE} for {DEPT_NAME}.</div>"
    elif scheme not in schemes:
        result = f"<div class='error'>⚠️ Please select a valid scheme.</div>"
    elif sem in schemes[scheme] and col in schemes[scheme][sem]:
        subj = schemes[scheme][sem][col]
        result = (f"<b>Department:</b> {DEPT_NAME} ({DEPT_CODE})<br>"
                  f"<b>Scheme:</b> {scheme}<br>"
                  f"<b>Semester:</b> {sem}<br>"
                  f"<b>Column:</b> {col}<br><br>"
                  f"<b>Subject:</b> {subj['SNAME']}<br>"
                  f"<b>Equivalent Subject:</b> {subj['NSNAME']}<br>"
                  f"<b>Exam Type:</b> {subj['TYPE']}")
    else:
        result = f"⚠️ No subject found for {scheme} — Semester {sem}, Column {col}."

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True)
