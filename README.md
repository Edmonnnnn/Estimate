Estimate Application for Calculating Model & Color Costs with PDF Generation
Description

An interactive web application for calculating the cost of products based on selected models and colors, featuring:

Uploading price lists (models and colors)

Entering client information

Selecting a category, model, up to 5 colors, and area

Adding multiple items (extendable)

Generating a clean and professional estimate (table + PDF)

Easy customization: order history, logo, advanced filtering, etc.

Demo

demo1 demo2
(place your demo links/screenshots here)

Installation & Setup
1. Clone or download the repository
git clone <your_repo_url>
cd estimate_app

2. Create and activate a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Install wkhtmltopdf

Download the installer for your OS and install it.

After installation, update the path_wkhtmltopdf variable inside app.py with the correct path to wkhtmltopdf.exe.

5. Add your price lists

models.csv

category;model name;price per m²
square;Model A;25
hexagon;Model B;30
frieze;Model C;40


colors.csv

color name;price
White;5
Red;7
Blue;6

6. Run the application
python app.py

7. Open in your browser
http://127.0.0.1:5000/

Project Structure
estimate_app/
│
├── app.py               # Main Flask application logic
├── models.csv           # Model price list
├── colors.csv           # Color price list
├── requirements.txt     # Dependency list
│
├── static/              # (Optional) Logos, images, static assets
│
├── templates/
│   ├── client_form.html     # Stylish client input form
│   ├── select_model.html    # Form for selecting model/colors/area
│   └── invoice.html         # Invoice template (for PDF and browser)
│
└── venv/               # Virtual environment (do NOT commit to git)

Example Workflow

Enter client information

Select an item: category, model, up to 5 colors, area

View the complete estimate with totals

Download the formatted PDF document

Dependencies

See requirements.txt.
The project uses:

Flask — web server

pandas — working with price lists

pdfkit — generate PDF from HTML

wkhtmltopdf — external binary required by pdfkit

Possible Enhancements

Shopping cart: support multiple items in one estimate

Order/client history

Custom logo & branding

Emailing PDF to the client

Advanced filtering and sorting for models/colors

Internationalization (multi-language support)


---------------------------------------------------------------------------
---------------------------------------------------------------------------
---------------------------------------------------------------------------


# Сметное приложение для расчёта стоимости моделей и цветов с PDF-генерацией

## Описание

Интерактивное веб-приложение для расчёта стоимости изделий по моделям и цветам с возможностью:
- Загрузки прайс-листов (модели и цвета)
- Ввода данных клиента
- Выбора категории, модели, до 5 цветов, площади
- Добавления нескольких позиций (расширяемо)
- Получения красивой сметы (таблица + PDF)
- Лёгкой доработки: история заказов, логотип, расширенная фильтрация и др.

---

## Демонстрация

![demo1](demo/demo1.png)
![demo2](demo/demo2.png)

---

## Установка и запуск

1. **Склонируйте/скачайте репозиторий:**
    ```sh
    git clone <your_repo_url>
    cd estimate_app
    ```

2. **Создайте и активируйте виртуальное окружение:**
    ```sh
    python -m venv venv
    # Для Windows:
    venv\Scripts\activate
    # Для Mac/Linux:
    source venv/bin/activate
    ```

3. **Установите зависимости:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Установите [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html):**
    - Скачайте инсталлятор для вашей ОС, установите.
    - После установки пропишите путь до `wkhtmltopdf.exe` в переменной `path_wkhtmltopdf` внутри файла `app.py`.

5. **Добавьте свои прайс-листы:**
    - `models.csv`:
        ```
        категория;название модели;цена за м²
        квадратная;Model A;25
        шестиугольная;Model B;30
        фриз;Model C;40
        ```
    - `colors.csv`:
        ```
        название цвета;цена
        Белый;5
        Красный;7
        Синий;6
        ```

6. **Запустите приложение:**
    ```sh
    python app.py
    ```

7. **Откройте браузер и перейдите на:**
    ```
    http://127.0.0.1:5000/
    ```

---

## Структура проекта

estimate_app/
│
├── app.py # Основная логика Flask-приложения
├── models.csv # Прайс-лист моделей
├── colors.csv # Прайс-лист цветов
├── requirements.txt # Список зависимостей pip
├── static/ # (Необязательно) Логотипы, картинки и т.д.
├── templates/
│ ├── client_form.html # Стильная форма ввода клиента
│ ├── select_model.html # Стильная форма выбора модели/цвета/площади
│ └── invoice.html # Красивый шаблон сметы (и для PDF, и для браузера)
└── venv/ # Виртуальное окружение (не добавлять в git)

yaml
Копировать

---

## Пример работы

1. Ввод данных клиента
2. Выбор позиции: категория, модель, до 5 цветов, площадь
3. Просмотр красивой сметы с итогом
4. Скачивание PDF с оформленной таблицей

---

## Зависимости

См. `requirements.txt`.  
В проекте используется:
- Flask (web-сервер)
- pandas (работа с прайс-листами)
- pdfkit (генерация PDF из HTML)
- wkhtmltopdf (внешняя программа для pdfkit)

---

## Возможности доработки

- **Корзина позиций**: добавить поддержку нескольких изделий в одной смете
- **История заказов/клиентов**
- **Загрузка логотипа и фирменный стиль**
- **Отправка PDF на e-mail**
- **Расширенный фильтр и сортировка моделей/цветов**
- **Интернационализация (мультиязычность)**

---

## Лицензия

MIT или любая другая по вашему выбору

---

## Автор

- Edmon (edmooooon@mail.ru)
- Telegram: @Edmon
