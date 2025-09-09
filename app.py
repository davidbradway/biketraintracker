from datetime import datetime
from tinydb import TinyDB, Query
from flask import Flask, render_template, jsonify

app = Flask(__name__)
db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))


@app.route("/")
def root():
    all_items = db.all()
    return render_template("table.html", items=all_items)


@app.route("/i/<int:item_id>")
def create(item_id):
    data = {"item_id": "i" + str(item_id), "datetime": datetime.now().isoformat()}
    db.insert(data)

    items = Query()
    all_items = db.search(items.item_id == "i" + str(item_id))

    week_count = 0
    unique_weeks = []
    for item in all_items:
        # convert back to datetime
        dt = datetime.fromisoformat(item["datetime"])
        week_number = dt.isocalendar().week
        # find the number of unique weeks
        if week_number not in unique_weeks:
            unique_weeks.append(week_number)
            week_count = week_count + 1
    return render_template("results.html", d={'week_count': week_count, 'datetime': data['datetime']})


@app.route("/json")
def json():
    all_items = db.all()
    return jsonify(all_items)
