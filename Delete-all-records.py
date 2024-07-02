import requests

def list_domains(api_key, email):
    url = "https://api.cloudflare.com/client/v4/zones"
    headers = {
        "X-Auth-Key": api_key,
        "X-Auth-Email": email,
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data["success"]:
            domains = [{"id": zone["id"], "name": zone["name"]} for zone in data["result"]]
            return domains
        else:
            print("Failed to list domains.")
            print(data)
            return None
    else:
        print("Failed to fetch domains.")
        print(response.json())
        return None

def delete_dns_records(zone_id, api_key, email):
    print("Attempting Authentication with Provided Global API Key...")

    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "X-Auth-Key": api_key,
        "X-Auth-Email": email,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        do_delete = input("Authenticated! Are you sure you want to delete ALL dns records? This action cannot be reversed! [y/n]: ")
        if do_delete.lower() != "y":
            print("Aborting!")
            return

        data = response.json()
        delCount = 0
        for record in data["result"]:
            record_id = record["id"]
            delete_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
            delete_response = requests.delete(delete_url, headers=headers)
            if delete_response.status_code == 200:
                print(f"Record {record['name']} deleted successfully.")
                delCount += 1
            else:
                print(f"Failed to delete record {record['name']}.")
                print(delete_response.json())

        print(f"Done! Deleted a total of {delCount} DNS records!")
    else:
        print("Failed to fetch DNS records.")
        print(response.json())

def main(api_key, email):
    domains = list_domains(api_key, email)
    if not domains:
        return

    print("Available Domains:")
    for idx, domain in enumerate(domains):
        print(f"{idx + 1}. {domain['name']}")

    choice = int(input("Enter the number of the domain you want to manage: ")) - 1
    if 0 <= choice < len(domains):
        domain = domains[choice]
        delete_dns_records(domain["id"], api_key, email)
    else:
        print("Invalid choice.")

# Set the required parameters
api_key = "Global API Key"
email = "example@example.com"

main(api_key, email)
