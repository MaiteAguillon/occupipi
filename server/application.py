
from flask import Flask, render_template
app= Flask (__name__)

from models.pipi import Pipi
import time

# pour éteindre et allumer les LEDS ( pour éviter que ça reste allumé )
"""while True:
    redLed.off()
    blueLed.off()
    time.sleep(1)"""


pipi = Pipi()
pipi.startDetection()

@app.route('/')
def index():
    return render_template('index.html', status=pipi.status)