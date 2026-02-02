# 🚂 Railway Deployment Guide - Stap voor Stap

## Voorbereiding

✅ Je hebt nodig:
- Je Dropbox Access Token (die je eerder hebt gegenereerd)
- Alle project bestanden

## Stap 1: Railway Account Aanmaken

1. Ga naar: https://railway.app
2. Klik op "Login" rechtsboven
3. Kies "Login with GitHub" (makkelijkst)
4. Als je geen GitHub hebt, gebruik "Login with Email"
5. Bevestig je email adres

✅ **Klaar!** Je hebt nu een Railway account.

---

## Stap 2: Nieuw Project Maken

1. Klik op het paarse "New Project" knopje
2. Je ziet nu verschillende opties:

### Optie A: Deploy from GitHub (Als je GitHub hebt)
- Kies "Deploy from GitHub repo"
- Connecteer je GitHub account
- Upload eerst alle bestanden naar een GitHub repository
- Selecteer de repository

### Optie B: Empty Project (Zonder GitHub) - **AANBEVOLEN**
- Kies "Empty Project"
- Klik op "Create"

---

## Stap 3: Service Toevoegen

1. In je lege project, klik op "+ New"
2. Kies "Empty Service"
3. Geef een naam: bijv. "fillout-dropbox-webhook"

---

## Stap 4: Code Uploaden

### Met CLI (Aanbevolen):

1. Installeer Railway CLI:
   ```bash
   npm install -g @railway/cli
   ```

2. Login:
   ```bash
   railway login
   ```

3. Link project:
   ```bash
   cd fillout-to-dropbox
   railway link
   ```

4. Deploy:
   ```bash
   railway up
   ```

### Zonder CLI (Via GitHub):

1. Maak een GitHub repository aan
2. Upload alle bestanden
3. In Railway: "Deploy from GitHub repo"
4. Selecteer je repository

---

## Stap 5: Environment Variabelen Toevoegen

**DIT IS CRUCIAAL!**

1. In Railway, ga naar je service
2. Klik op het "Variables" tabblad
3. Klik op "+ New Variable"
4. Voeg toe:
   - **Variable**: `DROPBOX_TOKEN`
   - **Value**: `[plak hier je Dropbox token]`

5. Klik "Add"

**Let op:** Zonder deze variabele werkt het systeem NIET!

---

## Stap 6: Publieke URL Genereren

1. Ga naar "Settings" tab
2. Scroll naar "Networking" sectie
3. Klik "Generate Domain"
4. Je krijgt een URL zoals: `https://fillout-dropbox-webhook-production.up.railway.app`

✅ **Bewaar deze URL!** Dit is je webhook URL.

---

## Stap 7: Webhook Toevoegen in Fillout

1. Ga naar https://fillout.com
2. Open je INTAKEDOCUMENT formulier
3. Ga naar "Settings" (tandwiel icoon)
4. Klik op "Integrations"
5. Scroll naar "Webhooks"
6. Klik "+ Add Webhook"
7. Vul in:
   - **URL**: `https://jouw-railway-url.up.railway.app/webhook`
   - **Events**: Selecteer "Form Submitted"
8. Klik "Save"

---

## Stap 8: Testen!

### Test 1: Health Check
1. Open in browser: `https://jouw-railway-url.up.railway.app/health`
2. Je zou moeten zien: `{"status": "ok"}`

### Test 2: Volledig Formulier
1. Vul je Fillout formulier in met testdata
2. Vul minimaal in:
   - Voornaam
   - Achternaam
   - Groep (als je wilt)

### Test 3: Check Dropbox
1. Ga naar je Dropbox
2. Navigeer naar: `/City Solid 2025 - Kernteam/D. City Solid uitvoering 2/`
3. Je zou een nieuwe map moeten zien: `Groep [X]/Intake/`
4. Daarin staat het Word document!

---

## Logs Bekijken (Bij Problemen)

1. In Railway, ga naar je service
2. Klik op "Deployments"
3. Klik op de laatste deployment
4. Klik "View Logs"
5. Zie real-time wat er gebeurt

**Wat je zou moeten zien bij een succesvolle submission:**
```
INFO: Webhook ontvangen van Fillout
INFO: Template vullen voor [Voornaam] [Achternaam]
INFO: Folder bestaat al: /City Solid 2025 - Kernteam/...
INFO: Uploaden naar Dropbox: /City Solid 2025.../Intakedocument_X_Y.docx
INFO: Bestand geüpload naar Dropbox
```

---

## ⚠️ Veel Voorkomende Problemen

### "DROPBOX_TOKEN niet ingesteld"
**Oplossing:**
- Ga naar Variables tab
- Check of DROPBOX_TOKEN er staat
- Als niet: voeg toe
- Herstart service: Settings → Service → Restart

### "Upload naar Dropbox mislukt"
**Oplossing:**
- Check of je Dropbox token geldig is
- Test handmatig met Dropbox API
- Genereer nieuwe token als nodig

### "404 Not Found"
**Oplossing:**
- Check of je URL eindigt met `/webhook`
- Juiste URL is: `https://jouw-app.up.railway.app/webhook`
- NIET: `https://jouw-app.up.railway.app`

### Webhook doet niets
**Oplossing:**
- Check Fillout webhook configuratie
- Test `/health` endpoint eerst
- Check Railway logs voor errors
- Hertest formulier submission

---

## 💰 Kosten

Railway free tier geeft je:
- **$5 gratis credits** per maand
- **500GB bandwidth**
- Ongeveer **500+ formulier submissions per maand GRATIS**

Na free tier:
- ~$5-10 per maand bij normaal gebruik
- Je krijgt email als credits opraken

---

## 🎉 Klaar!

Je webhook systeem draait nu 24/7 in de cloud!

Elke keer dat iemand het Fillout formulier invult:
1. ✅ Webhook wordt getriggerd
2. ✅ Word document wordt gegenereerd
3. ✅ Upload naar Dropbox in juiste map
4. ✅ Mappen worden automatisch aangemaakt

---

## 📱 Extra Tips

### Railway App
Download de Railway mobile app om:
- Logs te checken onderweg
- Deployment status te zien
- Credits te monitoren

### Monitoring
Railway stuurt je email als:
- Deployment faalt
- Service crasht
- Credits bijna op zijn

### Updates
Om je code te updaten:
1. Verander de code lokaal
2. Run weer `railway up`
3. Railway deploy automatisch
4. Check logs of alles werkt

---

## 🆘 Hulp Nodig?

Als iets niet werkt:
1. ✅ Check Railway logs
2. ✅ Test `/health` endpoint
3. ✅ Controleer environment variabelen
4. ✅ Check Fillout webhook configuratie
5. ✅ Test Dropbox token handmatig

Railway community: https://discord.gg/railway
