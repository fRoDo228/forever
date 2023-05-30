from flask import Flask, render_template

# Создание экземпляра Flask
app = Flask(__name__)

# Определение маршрута для главной страницы
@app.route('/')
def index():
    return render_template('index.html')

# Определение маршрута для страницы "О нас"
@app.route('/about')
def about():
    return render_template('about.html')

# Запуск приложения Flask
if __name__ == '__main__':
    app.run(debug=True)
