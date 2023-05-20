#chatgpt: generate a script which imports sales leads from an airtable relational database (untested)
import airtable

# Airtable API credentials
base_key = 'YOUR_BASE_KEY'
table_name = 'YOUR_TABLE_NAME'
api_key = 'YOUR_API_KEY'

# Initialize Airtable client
base = airtable.Airtable(base_key, table_name, api_key)

# Function to fetch lead data
def fetch_lead_data():
    try:
        # Fetch all records from Airtable
        records = base.get_all()
        
        # Process lead data
        leads = []
        for record in records:
            lead = {}
            lead['id'] = record['id']
            lead['name'] = record['fields'].get('Name', '')
            lead['email'] = record['fields'].get('Email', '')
            lead['phone'] = record['fields'].get('Phone', '')
            # Add more fields as needed
            
            leads.append(lead)
        
        return leads
    
    except Exception as e:
        print('Error fetching lead data:', str(e))
        return []

# Fetch lead data
leads = fetch_lead_data()

# Print lead data
for lead in leads:
    print('Lead ID:', lead['id'])
    print('Name:', lead['name'])
    print('Email:', lead['email'])
    print('Phone:', lead['phone'])
    print('---')
