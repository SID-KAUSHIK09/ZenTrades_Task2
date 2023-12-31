from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

uploaded_json_data = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    global uploaded_json_data 
    if "jsonFile" in request.files:
        json_file = request.files["jsonFile"]
        if json_file.filename != "":
            uploaded_json_data = json.load(json_file)
            columns = list(uploaded_json_data["products"].values())[0].keys()
            return jsonify({"columns": list(columns)})

    return jsonify({"error": "Invalid request"}), 400

@app.route("/display", methods=["POST"])
def display():
    selected_columns = request.form.getlist("selectedColumns[]")
    

    table_rows = [{column: product[column] for column in selected_columns} for product in uploaded_json_data["products"].values()]

    table_rows.sort(key=lambda x: int(x.get("popularity", 0)), reverse=True)

    table = {"columns": selected_columns, "rows": table_rows}
    return jsonify({"table": table})


if __name__ == "__main__":
    app.run(debug=True)
