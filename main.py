from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "<h1>Миссия Колонизация Марса </h1>"


@app.route('/index')
def index():
    return "<h1> И на Марсе будут яблони цвести! </h1>"


@app.route('/promotion')
def promotion():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Рекламная кампания</title>
                  </head>
                  <body>
                    <p>Человечество вырастает из детства.</p>
                    <p>Человечеству мала одна планета.</p>
                    <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p>И начнем с Марса!</p>
                    <p>Присоединяйся!</p>
                  </body>
                </html>"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                        <h1>Жди нас, Марс!</h1>
                      <body>
                        <img src="{url_for('static', filename='img/mars.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                        <p>Вот она какая, красная планета</p>
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Колонизация</title>
                      </head>
                        <h1>Жди нас, Марс!</h1>
                      <body>
                        <img src="{url_for('static', filename='img/mars.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                        <h1><div class="alert alert-primary" role="alert">Человечество вырастает из детства.</div></h1>

                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
