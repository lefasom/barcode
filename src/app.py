import os
import cv2
from playsound import playsound
from flask import Flask, render_template, Response

app = Flask(__name__)
barcode_value = "None" 
def barcode():
    global barcode_value
    bd = cv2.barcode.BarcodeDetector()
    cap = cv2.VideoCapture(0)
    
    deteccion = {}
    
    while True:
        ret, frame = cap.read()
        if ret:
            (
                ret_bc,
                decode,
                _,
                puntos
            ) = bd.detectAndDecode(frame)
            if ret_bc:
                barcode_value = decode
       
                


@app.route("/") #decorador
def Home():
    return render_template('index.html', barcode_value=barcode_value)  # Pasar el valor del código de barras a la plantilla HTML


@app.route('/video_feed')
def video_feed():
    return Response(barcode(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)

