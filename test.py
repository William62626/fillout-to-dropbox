import requests
import json

# Test webhook lokaal of op Railway
BASE_URL = "http://localhost:5000"  # Verander naar je Railway URL voor cloud test

def test_health():
    """Test health endpoint"""
    print("🔍 Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_webhook():
    """Test webhook met voorbeeld data"""
    print("🔍 Testing webhook endpoint...")
    
    # Voorbeeld Fillout data
    test_data = {
        "formId": "6y8fzv3Tr7us",
        "formName": "INTAKEDOCUMENT CERTI & SKILLS",
        "submission": {
            "submissionId": "test123",
            "submissionTime": "2026-02-02T13:58:20.123Z",
            "lastUpdatedAt": "2026-02-02T13:58:20.123Z",
            "questions": [
                {"id": "heip", "name": "Intakedatum", "type": "DatePicker", "value": "2026-02-02"},
                {"id": "i4yT", "name": "Intake gedaan door:", "type": "ShortAnswer", "value": "Jan Jansen"},
                {"id": "vBpL", "name": "Voornaam:", "type": "ShortAnswer", "value": "Test"},
                {"id": "3bMB", "name": "Achternaam:", "type": "ShortAnswer", "value": "Persoon"},
                {"id": "ocfm", "name": "Geboortedatum", "type": "DatePicker", "value": "1990-01-01"},
                {"id": "tzXP", "name": "Leeftijd", "type": "NumberInput", "value": 34},
                {"id": "hYRK", "name": "Geboorteplaats", "type": "ShortAnswer", "value": "Amsterdam"},
                {"id": "jV8S", "name": "BSN", "type": "NumberInput", "value": 123456789},
                {"id": "pky3", "name": "Nationaliteit:", "type": "ShortAnswer", "value": "Nederlands"},
                {"id": "xniC", "name": "Geslacht", "type": "Dropdown", "value": "man"},
                {"id": "bLdr", "name": "Straat", "type": "ShortAnswer", "value": "Teststraat 123"},
                {"id": "5KrJ", "name": "Postcode", "type": "ShortAnswer", "value": "1234AB"},
                {"id": "vDLe", "name": "Woonplaats", "type": "ShortAnswer", "value": "Rotterdam"},
                {"id": "vUgM", "name": "Mobiele nummer", "type": "PhoneNumber", "value": "0612345678"},
                {"id": "q75r", "name": "E-mail", "type": "EmailInput", "value": "test@example.com"},
                {"id": "k6Yb", "name": "Groep", "type": "MultiSelect", "value": ["A"]},
            ]
        }
    }
    
    response = requests.post(
        f"{BASE_URL}/webhook",
        json=test_data,
        headers={'Content-Type': 'application/json'}
    )
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

if __name__ == "__main__":
    print("=" * 50)
    print("🧪 Testing Fillout to Dropbox Webhook")
    print("=" * 50)
    print()
    
    try:
        test_health()
        
        print("💡 Wil je de webhook testen? (Zorg dat DROPBOX_TOKEN is ingesteld)")
        user_input = input("Test webhook? (y/n): ")
        
        if user_input.lower() == 'y':
            test_webhook()
        
        print("✅ Tests voltooid!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Kan geen verbinding maken met de server.")
        print("💡 Zorg dat de server draait met: python app.py")
    except Exception as e:
        print(f"❌ Error: {e}")
