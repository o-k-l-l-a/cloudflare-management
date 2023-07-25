import requests

def delete_cloudflare_records(zone_id, api_key):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # دریافت لیست رکوردهای DNS
    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        # حذف هر رکورد DNS به طور جداگانه
        for record in data["result"]:
            record_id = record["id"]
            delete_url = f"{url}/{record_id}"
            delete_response = requests.delete(delete_url, headers=headers)
            
            if delete_response.status_code == 200:
                print(f"Record with ID {record_id} was successfully deleted.")
            else:
                print(f"Error deleting record with ID {record_id}: {delete response.text}")
    else:
        print(f"Error fetching records DNS: {response.text}")

# مقادیر مورد نیاز را جایگزین کنید
zone_id = ""
api_key = ""


delete_cloudflare_records(zone_id, api_key)
