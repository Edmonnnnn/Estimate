import os
import pandas as pd
import json
from flask import Flask, render_template, request, session, redirect, url_for, make_response
import pdfkit
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def client_form():
    if request.method == 'POST':
        name = request.form.get('name')
        patronymic = request.form.get('patronymic')
        address = request.form.get('address')
        phone = request.form.get('phone')
        email = request.form.get('email')
        client = {
            'name': name,
            'patronymic': patronymic,
            'address': address,
            'phone': phone,
            'email': email
        }
        session['client'] = client
        return redirect(url_for('select_model'))
    return render_template('client_form.html')

@app.route('/select_model', methods=['GET', 'POST'])
def select_model():
    models_df = pd.read_csv('models.csv', delimiter=';')
    colors_df = pd.read_csv('colors.csv', delimiter=';')
    categories = models_df['категория'].unique().tolist()
    models_dict = {}
    for cat in categories:
        filtered = models_df[models_df['категория'] == cat]
        models_dict[cat] = [
            {'name': row['название модели'], 'price': row['цена за м²']}
            for _, row in filtered.iterrows()
        ]
    colors = colors_df['название цвета'].tolist()
    if request.method == 'POST':
        position = {
            'category': request.form['category'],
            'model': request.form['model'],
            'colors': request.form.getlist('colors'),
            'area': float(request.form['area'])
        }
        session['position'] = position
        return redirect(url_for('result'))
    return render_template(
        'select_model.html',
        categories=categories,
        colors=colors,
        models_json=json.dumps(models_dict, ensure_ascii=False)
    )

@app.route('/result')
def result():
    client = session.get('client')
    position = session.get('position')
    if not client or not position:
        return redirect(url_for('client_form'))
    models_df = pd.read_csv('models.csv', delimiter=';')
    colors_df = pd.read_csv('colors.csv', delimiter=';')
    model_row = models_df[(models_df['категория'] == position['category']) &
                          (models_df['название модели'] == position['model'])]
    model_price = float(model_row.iloc[0]['цена за м²']) if not model_row.empty else 0
    selected_colors = position['colors']
    colors_price = sum(
        float(colors_df[colors_df['название цвета'] == c].iloc[0]['цена'])
        for c in selected_colors if not colors_df[colors_df['название цвета'] == c].empty
    )
    area = float(position['area'])
    total = f"{(model_price + colors_price) * area:.2f}"
    colors_str = ', '.join(selected_colors)
    date = datetime.now().strftime("%d.%m.%Y")
    html = render_template(
        'invoice.html',
        client=client,
        position=position,
        colors_str=colors_str,
        area=area,
        model_price=model_price,
        colors_price=colors_price,
        total=total,
        date=date
    )
    # Красивая кнопка и ссылка под сметой (уже вне контейнера!)
    html += """
    <form method="get" action="/download_pdf" style="text-align:center; margin-top:20px;">
        <button type="submit" style="padding: 10px 24px; background: #1976d2; color: #fff; border:none; border-radius:7px; font-size:1em; cursor:pointer;">Скачать PDF</button>
    </form>
    <div style="text-align:center; margin-top:12px;">
        <a href="/" style="color:#2196f3; text-decoration:none;">Начать заново</a>
    </div>
    """
    return html

@app.route('/download_pdf')
def download_pdf():
    client = session.get('client')
    position = session.get('position')
    if not client or not position:
        return redirect(url_for('client_form'))
    models_df = pd.read_csv('models.csv', delimiter=';')
    colors_df = pd.read_csv('colors.csv', delimiter=';')
    model_row = models_df[(models_df['категория'] == position['category']) &
                          (models_df['название модели'] == position['model'])]
    model_price = float(model_row.iloc[0]['цена за м²']) if not model_row.empty else 0
    selected_colors = position['colors']
    colors_price = sum(
        float(colors_df[colors_df['название цвета'] == c].iloc[0]['цена'])
        for c in selected_colors if not colors_df[colors_df['название цвета'] == c].empty
    )
    area = float(position['area'])
    total = f"{(model_price + colors_price) * area:.2f}"
    colors_str = ', '.join(selected_colors)
    date = datetime.now().strftime("%d.%m.%Y")
    rendered = render_template(
        'invoice.html',
        client=client,
        position=position,
        colors_str=colors_str,
        area=area,
        model_price=model_price,
        colors_price=colors_price,
        total=total,
        date=date
    )
    # Указываем путь к wkhtmltopdf.exe
    path_wkhtmltopdf = r'C:\Users\User\Desktop\wkhtmltopdf\bin\wkhtmltopdf.exe'

    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(rendered, False, configuration=config)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=invoice.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)
