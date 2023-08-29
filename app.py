from flask import Flask, render_template, request
import qrcode
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        d = request.form.get('d')
        fill_color = request.form.get('fill_color')
        back_color = request.form.get('back_color')

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(d)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color=fill_color, back_color=back_color)

        qr_image.save("static/qr_code.png")

        return render_template('index.html', qr_created=True)
    
    return render_template('index.html', qr_created=False)

if __name__ == '__main__':
    app.run(debug=True)
