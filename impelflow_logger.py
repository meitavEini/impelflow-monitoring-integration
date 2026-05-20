import requests
import json
from datetime import datetime

ELASTIC_URL = "https://my-observability-project-ff7d26.kb.us-central1.gcp.elastic.cloud"
HEADERS = {
    "Authorization": "ckhPT1JKNEJUTF9ZcmRUX2J4cUU6emlRM2MzR3UtNktrZERwU3ZXbF9rZw==",
    "Content-Type": "application/json"
}

def send_scandulous_log(status, service, message, duration=None):
    """פונקציה שמארגנת את הלוג כ-JSON ושולחת אותו ב-API"""
    
    payload = {
        "@timestamp": datetime.utcnow().isoformat() + "Z",
        "service_name": service,
        "status": status,
        "message": message,
        "duration_ms": duration
    }
    
    print(f"🤫 Gossip Girl is whispering to Elastic about {service}...")
    
    # שליחת בקשת HTTP POST ל-Endpoint
    response = requests.post(ELASTIC_ENDPOINT, headers=HEADERS, data=json.dumps(payload))
    
    if response.status_code in [200, 201]:
        print(f"✅ Spotted! Log successfully ingested into Kibana. (Status: {response.status_code})")
    else:
        print(f"❌ XOXO, we have a problem. Code: {response.status_code}, Response: {response.text}")

# --- כאן מריצים בדיקות סימולציה של תקלות והצלחות ב-Impelflow ---

# 1. סימולציה של הצלחה
send_scandulous_log("SUCCESS", "HeyGen-Avatar-Bridge", "Avatar video generated perfectly for client VIP setup.")

# 2. סימולציה של תקלה (Error) שעובדת על אינטגרציה
send_scandulous_log("ERROR", "n8n-Workflow-Engine", "Webhook timeout from client database connection.", duration=5000)
