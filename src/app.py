import os
import cv2
from pyzbar import pyzbar
from flask import Flask, render_template, Response

app = Flask(__name__)
barcode_value = "None" 
def barcode():
    global barcode_value
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        barcodes = pyzbar.decode(frame)
        
        for barcode in barcodes:
            (x,y,w,h) = barcode.rect
            cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0),2)
            barcode_value = barcode.data.decode("utf-8")
            cv2.putText(frame, barcode_value,(x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.0,(0,255,0),2)
            
        cv2.imshow("barcode Scanner", frame)
        if cv2.waitkey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


@app.route("/") #decorador
def Home():
    return render_template('index.html', barcode_value=barcode_value)  # Pasar el valor del código de barras a la plantilla HTML


@app.route('/video_feed')
def video_feed():
    return Response(barcode(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)

