import cv2
import zbarlight
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
        
        # Convertir la imagen de la cámara a escala de grises para zbarlight
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Escanear códigos de barras en la imagen en escala de grises
        codes = zbarlight.scan_codes('qrcode', gray)
        
        if codes is not None:
            barcode_value = codes[0].decode("utf-8")
            
        cv2.imshow("Barcode Scanner", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()


@app.route("/")
def Home():
    return render_template('index.html', barcode_value=barcode_value)


@app.route('/video_feed')
def video_feed():
    return Response(barcode(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
