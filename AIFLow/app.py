from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    idea = request.json.get("idea")

    # Smart demo responses
    research = f"{idea.capitalize()} is a rapidly growing industry with strong demand in the market. Many startups are entering this space."

    project = f"Problem: Users face difficulty in {idea}. Solution: Develop a smart platform that improves {idea} using automation."

    learning = "HTML, CSS, JavaScript, Python, Problem Solving, UI Design"

    content = f"🚀 Excited to build an innovative {idea} project using modern technology!"

    return jsonify({
        "research": research,
        "project": project,
        "learning": learning,
        "content": content
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")