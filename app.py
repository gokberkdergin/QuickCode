from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr/')
def generate_qr():
    data = request.args.get('data') 
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        img_filename = 'qrcode.png'
        img_path = os.path.join('static', 'qrcodes', img_filename)
        qr_img.save(img_path)
        return render_template('qr.html', img_path=img_path)
    else:
        return "Missing 'data' parameter."

if __name__ == '__main__':
    app.run(debug=True)
