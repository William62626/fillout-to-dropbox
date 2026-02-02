import os
from flask import Flask, request, jsonify
from docx import Document
import dropbox
from dropbox.exceptions import ApiError
from datetime import datetime
import logging
from flask_cors import CORS

# Configuratie
app = Flask(__name__)
CORS(app)  # Allow CORS for all routes
```

5. Commit changes

6. **Update ook `requirements.txt`** - voeg toe:
```
flask-cors==4.0.0
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variabelen
DROPBOX_TOKEN = os.environ.get('DROPBOX_TOKEN', '')
BASE_FOLDER = '/City Solid 2025 - Kernteam/D. City Solid uitvoering 2'

def get_field_value(questions, field_name):
    """Haal waarde op uit Fillout questions array"""
    for q in questions:
        if q.get('name') == field_name:
            value = q.get('value')
            # Als value een dict is (zoals Address), converteer naar string
            if isinstance(value, dict):
                return format_dict_value(value)
            # Als value een list is (MultiSelect), join met komma's
            elif isinstance(value, list):
                return ', '.join(str(v) for v in value if v)
            return value if value is not None else ''
    return ''

def format_dict_value(dict_value):
    """Formatteer dict waarden (zoals Address) naar leesbare string"""
    if not dict_value:
        return ''
    parts = []
    if dict_value.get('address'):
        parts.append(dict_value['address'])
    if dict_value.get('zipCode'):
        parts.append(dict_value['zipCode'])
    if dict_value.get('city'):
        parts.append(dict_value['city'])
    if dict_value.get('country'):
        parts.append(dict_value['country'])
    return ', '.join(parts)

def format_date(date_str):
    """Formatteer datum naar NL formaat"""
    if not date_str:
        return ''
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime('%d-%m-%Y')
    except:
        return date_str

def fill_word_template(template_path, data):
    """Vul Word template met Fillout data"""
    doc = Document(template_path)
    questions = data.get('submission', {}).get('questions', [])
    
    # Mapping van Fillout velden naar template cellen
    field_mapping = {
        'Intake gedaan door:': 'Intake gedaan door:',
        'Intakedatum': 'Intakedatum',
        'Voornaam:': 'Voornaam:',
        'Achternaam:': 'Achternaam:',
        'Geboortedatum': 'Geboortedatum',
        'Leeftijd': 'Leeftijd',
        'Geboorteplaats': 'Geboorteplaats',
        'BSN': 'BSN',
        'Nationaliteit:': 'Nationaliteit:',
        'Geslacht': 'Geslacht',
        'Straat': 'Straat',
        'Postcode': 'Postcode',
        'Wijk': 'Wijk',
        'Gebied': 'Gebied',
        'Woonplaats': 'Woonplaats',
        'Ingeschreven op adres': 'Ingeschreven op adres',
        'Ingeschreven op adres (BRP)': 'Ingeschreven op adres (BRP)',
        'Reden indien geen BRP/ander adres': 'Reden indien geen BRP/ander adres',
        'WhatsApp:': 'WhatsApp:',
        'Mobiele nummer': 'Mobiele nummer',
        'E-mail': 'E-mail',
        'Zorgverzekering': 'Zorgverzekering',
        'Uitkering?': 'Uitkering?',
        'Type Uitkering': 'Type Uitkering',
        'Goedkeuring door klantmanager?': 'Goedkeuring door klantmanager?',
        'Contactpersoon:': 'Contactpersoon:',
        'Toestemming:': 'Toestemming:',
        'Eigen vervoer:': 'Eigen vervoer:',
        'Rijbewijs:': 'Rijbewijs:',
        'Medische bijzonderheden': 'Medische bijzonderheden',
        'Wat zijn de medische bijzonderheden:': 'Wat zijn de medische bijzonderheden:',
        'Door wie weet je van ons bestaan?': 'Door wie weet je van ons bestaan?',
        'Aanmeldorganisatie': 'Aanmeldorganisatie',
        'Klantmanager Jongerenloket': 'Klantmanager Jongerenloket',
        'Aanmelder': 'Aanmelder',
        'Mailadres aanmelder': 'Mailadres aanmelder',
        'Welke sector wil je werken?': 'Welke sector wil je werken?',
        'Wensberoep': 'Wensberoep',
        'Gewenste certificaten': 'Gewenste certificaten',
        'Wat stimuleert/motiveert jou?': 'Wat stimuleert/motiveert jou?',
        'Wat demotiveert jou? Wat zijn belemmeringen?': 'Wat demotiveert jou? Wat zijn belemmeringen?',
        'Wat is je stip aan de horizon?Lange termijn doel?': 'Wat is je stip aan de horizon?Lange termijn doel?',
        'Wat zijn je goede eigenschappen?': 'Wat zijn je goede eigenschappen?',
        'Waar ben je minder goed in?': 'Waar ben je minder goed in?',
        'Welke talen spreek je?': 'Welke talen spreek je?',
        'Wat zijn je hobby\'s?': 'Wat zijn je hobby\'s?',
        'Woonsituatie': 'Woonsituatie',
        'Kinderen': 'Kinderen',
        'Eenoudergezin?': 'Eenoudergezin?',
        'Eerder al aan trajecten deelgenomen': 'Eerder al aan trajecten deelgenomen',
        'Zo ja, welke trajecten?': 'Zo ja, welke trajecten?',
        'Welke hulpverleners zijn er momenteel betrokken ?': 'Welke hulpverleners zijn er momenteel betrokken ?',
        'Speelt drugs of alcohol een rol in je leven?': 'Speelt drugs of alcohol een rol in je leven?',
        'Heb je schulden?': 'Heb je schulden?',
        'Wat is de reden? (1)': 'Wat is de reden? (1)',
        'Hoe hoog is het bedrag?': 'Hoe hoog is het bedrag?',
        'Afspraken / hulp': 'Afspraken / hulp',
        'Ben je in aanraking geweest met politie en/of justitie?': 'Ben je in aanraking geweest met politie en/of justitie?',
        'Veroordeeld voor een feit of in detentie geweest?': 'Veroordeeld voor een feit of in detentie geweest?',
        'Wat is de reden?': 'Wat is de reden?',
        'Zijn er nog lopende zaken?': 'Zijn er nog lopende zaken?',
        'Middelbare & vervolgonderwijs Diploma behaald?': 'Middelbare & vervolgonderwijs Diploma behaald?',
        'Opleidingsniveau': 'Opleidingsniveau',
        'Reden uitval?': 'Reden uitval?',
        'Cursussen gevolgd?': 'Cursussen gevolgd?',
        'Zo ja, welke cursusen?': 'Zo ja, welke cursusen?',
        'Certificaten behaald?': 'Certificaten behaald?',
        'Zo ja, welke Certificaten?': 'Zo ja, welke Certificaten?',
        'Waar heb je gewerkt?': 'Waar heb je gewerkt?',
        'Waarom lukte het wel/niet?': 'Waarom lukte het wel/niet?',
        'Heb je een cv?': 'Heb je een cv?',
        'Afspraken?': 'Afspraken?',
        'Leefgebieden waar aandacht voor moet zijn?': 'Leefgebieden waar aandacht voor moet zijn?',
        'Groep': 'Groep',
        'Startdatum': 'Startdatum'
    }
    
    # Vul de tabel in het document
    for table in doc.tables:
        for row in table.rows:
            cells = row.cells
            if len(cells) >= 2:
                # Eerste cel bevat de veldnaam
                field_label = cells[0].text.strip().rstrip(':')
                
                # Zoek de waarde in de Fillout data
                for fillout_field, template_field in field_mapping.items():
                    if field_label in template_field or template_field in field_label:
                        value = get_field_value(questions, fillout_field)
                        
                        # Speciale formatting voor datums
                        if 'datum' in fillout_field.lower() or 'Startdatum' in fillout_field:
                            value = format_date(value)
                        
                        # Zet waarde in tweede cel
                        if value:
                            cells[1].text = str(value)
                        break
    
    return doc

def upload_to_dropbox(file_path, dropbox_path):
    """Upload bestand naar Dropbox"""
    try:
        dbx = dropbox.Dropbox(DROPBOX_TOKEN)
        
        with open(file_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode('overwrite'))
        
        logger.info(f"Bestand geüpload naar Dropbox: {dropbox_path}")
        return True
    except ApiError as e:
        logger.error(f"Dropbox API error: {e}")
        return False
    except Exception as e:
        logger.error(f"Upload error: {e}")
        return False

def ensure_folder_exists(dbx, folder_path):
    """Zorg dat folder bestaat in Dropbox, maak aan indien nodig"""
    try:
        dbx.files_get_metadata(folder_path)
        logger.info(f"Folder bestaat al: {folder_path}")
    except ApiError as e:
        if e.error.is_path() and e.error.get_path().is_not_found():
            try:
                dbx.files_create_folder_v2(folder_path)
                logger.info(f"Folder aangemaakt: {folder_path}")
            except ApiError as create_error:
                logger.error(f"Kon folder niet aanmaken: {create_error}")
        else:
            logger.error(f"Fout bij checken folder: {e}")

@app.route('/webhook', methods=['POST'])
def webhook():
    """Fillout webhook endpoint"""
    try:
        data = request.json
        logger.info("Webhook ontvangen van Fillout")
        
        if not DROPBOX_TOKEN:
            return jsonify({'error': 'DROPBOX_TOKEN niet ingesteld'}), 500
        
        questions = data.get('submission', {}).get('questions', [])
        
        # Haal belangrijke velden op
        voornaam = get_field_value(questions, 'Voornaam:')
        achternaam = get_field_value(questions, 'Achternaam:')
        groep = get_field_value(questions, 'Groep')
        
        if not voornaam or not achternaam:
            return jsonify({'error': 'Voornaam en Achternaam zijn verplicht'}), 400
        
        # Als geen groep is opgegeven, gebruik "Algemeen"
        if not groep:
            groep = 'Algemeen'
        
        # Maak bestandsnaam
        filename = f"Intakedocument_{voornaam}_{achternaam}.docx"
        
        # Vul Word template
        logger.info(f"Template vullen voor {voornaam} {achternaam}")
        doc = fill_word_template('template.docx', data)
        
        # Sla tijdelijk op
        temp_path = f'/tmp/{filename}'
        doc.save(temp_path)
        
        # Maak Dropbox pad
        dropbox_folder = f"{BASE_FOLDER}/Groep {groep}/Intake"
        dropbox_path = f"{dropbox_folder}/{filename}"
        
        # Zorg dat folders bestaan
        dbx = dropbox.Dropbox(DROPBOX_TOKEN)
        ensure_folder_exists(dbx, f"{BASE_FOLDER}/Groep {groep}")
        ensure_folder_exists(dbx, dropbox_folder)
        
        # Upload naar Dropbox
        logger.info(f"Uploaden naar Dropbox: {dropbox_path}")
        success = upload_to_dropbox(temp_path, dropbox_path)
        
        # Verwijder tijdelijk bestand
        os.remove(temp_path)
        
        if success:
            return jsonify({
                'status': 'success',
                'message': f'Document succesvol aangemaakt en geüpload',
                'filename': filename,
                'dropbox_path': dropbox_path
            }), 200
        else:
            return jsonify({'error': 'Upload naar Dropbox mislukt'}), 500
            
    except Exception as e:
        logger.error(f"Error in webhook: {e}", exc_info=True)
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'}), 200

@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        'status': 'Fillout to Dropbox webhook server is running',
        'endpoints': {
            'webhook': '/webhook (POST)',
            'health': '/health (GET)'
        }
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
