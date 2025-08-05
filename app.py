from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Page du formulaire
@app.route('/form')
def form():
    return render_template('form.html')

# Traitement des infos
@app.route('/submit', methods=['POST'])
def submit():
    pseudo = request.form.get('pseudo')
    discord = request.form.get('discord')

    webhook_url = 'https://discord.com/api/webhooks/1402364233374630010/5z9fMGOvXiK3BvfgcsMXCsvoR1WoTMefLKeKeOpWxcp6XtzbSg57OigookjpZGW7Q3B3'  # 🔁 Remplace par ton lien Webhook réel

    payload = {
        "content": f"🚨 Nouveau participant !\nPseudo Roblox : {pseudo}\nDiscord : {discord}"
    }

    try:
        requests.post(webhook_url, json=payload)
        return "✅ Informations envoyées avec succès !"
    except Exception as e:
        return f"❌ Erreur lors de l'envoi : {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)