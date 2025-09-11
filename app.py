from datetime import datetime
from tinydb import TinyDB, Query
from flask import Flask, render_template, jsonify

app = Flask(__name__)
db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))

@app.route("/checkins")
def root():
    all_items = db.all()
    return render_template("table.html", items=all_items)


@app.route("/i/<int:item_id>")
def create(item_id):
    data = {"item_id": "i" + str(item_id), "datetime": str(datetime.now().isoformat())}
    db.insert(data)

    items = Query()
    all_items = db.search(items.item_id == "i" + str(item_id))

    unique_weeks = []
    for item in all_items:
        # convert back to datetime
        dt = datetime.fromisoformat(item["datetime"])
        week_number = dt.isocalendar().week

        # find the number of unique weeks
        if week_number not in unique_weeks:
            unique_weeks.append(week_number)

    week_count = len(unique_weeks)
    return render_template("results.html", d={"week_count": week_count, "datetime": data["datetime"]})


@app.route("/json")
def json_route():
    all_items = db.all()
    return jsonify(all_items)


@app.route("/")
def leaderboard_route():

    counts = {}
    for item in db.all():

        # convert back to datetime
        dt = datetime.fromisoformat(item["datetime"])
        week_number = dt.isocalendar().week
        #year_number = dt.isocalendar().year

        unique_weeks = counts.get(item["item_id"], [])

        # find the number of unique weeks
        if week_number not in unique_weeks:
            unique_weeks.append(week_number)
            counts[item["item_id"]] = unique_weeks

    data = {}
    for key, value in counts.items():
        data[key] = len(value)

    my_leaderboard = []
    for key, value in sorted(data.items(), key=lambda kv: kv[1], reverse=True):  # sort by value
        my_leaderboard.append({'item_id': key, 'weeks': value})

    return render_template("table2.html", items=my_leaderboard)
