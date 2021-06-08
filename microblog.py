from app import app

if __name__ == '__main__':
    context = ('local.crt', 'local.key')  # certificate and key files
    app.run(host='127.0.0.1', debug=True, ssl_context='adhoc')
