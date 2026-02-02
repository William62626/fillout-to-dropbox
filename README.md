# Fillout naar Dropbox Automatisering

Dit systeem ontvangt automatisch Fillout formulier submissions, vult een Word template en upload het naar Dropbox.

## ✨ Wat doet het?

1. ✅ Ontvangt webhook van Fillout formulier
2. ✅ Vult Word template met alle formulier data
3. ✅ Maakt automatisch de juiste Dropbox mappen aan
4. ✅ Upload document naar: `/City Solid 2025 - Kernteam/D. City Solid uitvoering 2/Groep [X]/Intake/`
5. ✅ Bestandsnaam: `Intakedocument_[Voornaam]_[Achternaam].docx`

## 📋 Vereisten

- Dropbox Access Token
- Python 3.11 (voor lokaal testen)
- Railway of Render account (voor cloud deployment)

## 🚀 Deployment naar Railway (Aanbevolen)

### Stap 1: Railway Account
1. Ga naar https://railway.app
2. Maak een gratis account aan (met GitHub)

### Stap 2: Nieuw Project
1. Klik op "New Project"
2. Kies "Deploy from GitHub repo"
3. **OF** kies "Empty Project" en upload bestanden handmatig

### Stap 3: Bestanden Uploaden (als je geen GitHub gebruikt)
Als je geen GitHub hebt, kun je de bestanden handmatig uploaden:

1. Download alle bestanden uit deze map
2. Maak een ZIP van de map
3. In Railway: klik op "Deploy" → upload de ZIP

**Belangrijke bestanden die mee moeten:**
- `app.py` - Het hoofdscript
- `requirements.txt` - Python dependencies
- `Procfile` - Server configuratie
- `runtime.txt` - Python versie
- `template.docx` - Word template

### Stap 4: Environment Variabelen Instellen
1. Ga naar je Railway project
2. Klik op "Variables"
3. Voeg toe:
   ```
   DROPBOX_TOKEN = [jouw_dropbox_token]
   ```
4. Save changes

### Stap 5: Deploy
1. Railway deploy automatisch
2. Wacht tot deployment compleet is (groen vinkje)
3. Klik op "Settings" → "Networking" → "Generate Domain"
4. Kopieer de URL (bijv. `https://jouw-app.up.railway.app`)

### Stap 6: Webhook URL in Fillout
1. Ga naar je Fillout formulier
2. Settings → Integrations → Webhooks
3. Voeg toe: `https://jouw-app.up.railway.app/webhook`
4. Save

## 🧪 Testen

### Test de webhook:
1. Vul het Fillout formulier in
2. Check Railway logs: Dashboard → "View Logs"
3. Check je Dropbox voor het nieuwe document

### Health Check:
Open in browser: `https://jouw-app.up.railway.app/health`
Zou moeten tonen: `{"status": "ok"}`

## 🔧 Lokaal Testen (Optioneel)

Als je het eerst lokaal wilt testen:

### 1. Installeer Dependencies
```bash
pip install -r requirements.txt
```

### 2. Maak .env bestand
```bash
cp .env.example .env
```

Vul in `.env`:
```
DROPBOX_TOKEN=jouw_dropbox_token
PORT=5000
```

### 3. Run de server
```bash
python app.py
```

Server draait nu op `http://localhost:5000`

### 4. Test met ngrok (voor webhook)
```bash
ngrok http 5000
```

Gebruik de ngrok URL in Fillout webhook

## 📁 Dropbox Mapstructuur

Het systeem maakt automatisch deze structuur aan:
```
/City Solid 2025 - Kernteam/
  └── D. City Solid uitvoering 2/
      └── Groep [groepsnaam]/
          └── Intake/
              └── Intakedocument_[Voornaam]_[Achternaam].docx
```

## 🐛 Troubleshooting

### "DROPBOX_TOKEN niet ingesteld"
- Check of je de environment variabele hebt toegevoegd in Railway
- Herstart de service na toevoegen van variabelen

### "Upload naar Dropbox mislukt"
- Check of je Dropbox token nog geldig is
- Controleer of de token "Full Dropbox" toegang heeft

### Webhook ontvangt geen data
- Check of de webhook URL correct is in Fillout
- Check Railway logs voor errors
- Test de `/health` endpoint eerst

### Document wordt niet goed gevuld
- Check Railway logs om te zien welke data binnenkomt
- Mogelijk zijn veldnamen in Fillout veranderd

## 📊 Logs Bekijken

In Railway:
1. Ga naar je project
2. Klik op "View Logs"
3. Zie real-time wat er gebeurt

## 🔒 Beveiliging

- Bewaar je Dropbox token NOOIT in de code
- Gebruik altijd environment variabelen
- Deel je Railway project niet publiekelijk

## 💰 Kosten

Railway free tier:
- $5 gratis credits per maand
- Genoeg voor 500+ formulier submissions
- Na free tier: ~$5-10/maand

## 🆘 Support

Als je problemen hebt:
1. Check Railway logs
2. Test de `/health` endpoint
3. Controleer Dropbox token
4. Check Fillout webhook configuratie

## 📝 Licentie

Voor intern gebruik City Solid 2025.
