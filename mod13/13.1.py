from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<luku>')


def alkuluku(luku):
    luku = int(luku)

    on_alkuluku = True
    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            on_alkuluku = False

    if on_alkuluku:
        tulos = {f"luku {luku} on alkuluku:True"}
    else:
        tulos = {f"luku:{luku}, on_alkuluku:false"}
    return str(tulos)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)