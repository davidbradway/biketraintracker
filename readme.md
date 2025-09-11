# BikeTrain Tracker

This is a DIY project to track attendance at the weekly Bike Bus ride to school.

I am going to use cheap NFC RFID tags to load a specific URL for each tag, and log the user's participation for that week. We will add loyalty rewards and other benefits to incentivise participation.

```bash
# Set up
cd biketraintracker
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt

# Run
flask run --host=0.0.0.0

# URLs:
http://127.0.0.1:5000/
http://127.0.0.1:5000/i/1
http://127.0.0.1:5000/json
http://127.0.0.1:5000/checkins
http://192.168.1.175:5000
```
