# 🚀 Quick Start - Fillout naar Dropbox

## ✅ Wat je hebt gekregen

- **Compleet webhook systeem** dat Fillout formulieren automatisch verwerkt
- **Word template** die automatisch wordt gevuld
- **Dropbox upload** met automatische mapstructuur
- **Cloud-ready** voor Railway deployment

---

## 📦 Bestanden

```
fillout-to-dropbox/
├── app.py              ← Hoofdscript (webhook server)
├── template.docx       ← Word template
├── requirements.txt    ← Python dependencies
├── Procfile           ← Railway configuratie
├── runtime.txt        ← Python versie
├── test.py            ← Test script
├── README.md          ← Volledige documentatie
└── DEPLOYMENT.md      ← Stap-voor-stap deployment guide
```

---

## ⚡ Snelstart (3 opties)

### Optie 1: Direct naar Cloud (Aanbevolen)
**Voor wie:** Je wilt het meteen live hebben

1. **Download het ZIP bestand**
2. **Pak uit** op je computer
3. **Volg DEPLOYMENT.md** - complete Railway setup
4. **Tijd:** 15 minuten

### Optie 2: Eerst Lokaal Testen
**Voor wie:** Je wilt het eerst testen voor je naar cloud gaat

1. **Download & pak uit**
2. **Installeer Python** (3.11+)
3. **Run:**
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
4. **Test met ngrok** voor webhook
5. **Deploy daarna naar Railway**

### Optie 3: GitHub + Railway
**Voor wie:** Je wilt versiecontrole

1. **Maak GitHub repository**
2. **Upload alle bestanden**
3. **Railway:** "Deploy from GitHub"
4. **Voeg DROPBOX_TOKEN toe**
5. **Done!**

---

## 🎯 Wat gebeurt er?

```
📝 Fillout formulier invullen
    ↓
🔗 Webhook trigger
    ↓
📄 Word template vullen
    ↓
📁 Dropbox map maken
    ↓
⬆️  Document uploaden
    ↓
✅ Klaar!
```

**Locatie in Dropbox:**
```
/City Solid 2025 - Kernteam/
  └── D. City Solid uitvoering 2/
      └── Groep [X]/
          └── Intake/
              └── Intakedocument_[Voornaam]_[Achternaam].docx
```

---

## 🔑 Wat je nodig hebt

1. ✅ **Dropbox Token** (heb je al!)
2. ✅ **Railway account** (gratis - railway.app)
3. ✅ **Fillout formulier** (heb je al!)

---

## 📖 Volledige Guides

- **DEPLOYMENT.md** → Stap-voor-stap Railway deployment
- **README.md** → Complete documentatie + troubleshooting
- **test.py** → Test script voor lokaal testen

---

## 🆘 Hulp Nodig?

### Stap 1: Check de docs
- Lees DEPLOYMENT.md voor Railway setup
- Lees README.md voor troubleshooting

### Stap 2: Test lokaal
```bash
python app.py
python test.py
```

### Stap 3: Check logs
- Railway: View Logs
- Lokaal: Terminal output

---

## 💰 Kosten

**Railway Free Tier:**
- $5 gratis credits/maand
- 500+ formulieren/maand GRATIS
- Perfectie voor dit gebruik

---

## 🎉 Eerste Keer Gebruiken

1. **Deploy naar Railway** (volg DEPLOYMENT.md)
2. **Kopieer je Railway URL**
3. **Voeg webhook toe in Fillout:**
   - URL: `https://jouw-app.up.railway.app/webhook`
4. **Test het formulier!**
5. **Check Dropbox voor je document**

---

## ✨ Features

- ✅ Automatische map creatie
- ✅ 24/7 webhook server
- ✅ Real-time document generatie
- ✅ Alle Fillout velden ondersteund
- ✅ Datum formatting
- ✅ Multi-select velden
- ✅ Adres formatting
- ✅ Error handling
- ✅ Logging
- ✅ Health checks

---

## 🚀 Start Nu

1. Open **DEPLOYMENT.md**
2. Volg de stappen
3. 15 minuten later: LIVE!

**Succes!** 🎊
