```markdown
# Cloudflare DNS Records Deletion Script

This script allows you to authenticate with your Cloudflare account using your Global API Key and email, list all domains associated with your account, and delete all DNS records for a selected domain.

## Features

- Authenticate with Cloudflare using Global API Key and email.
- List all domains associated with your Cloudflare account.
- Delete all DNS records for a selected domain.

## Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)

## Usage

1. Clone the repository or download the script.

2. Install the required library:
   ```sh
   pip install requests
   ```

3. Edit the script to include your Cloudflare Global API Key and email:
   ```python
   # Set the required parameters
   api_key = "YOUR_GLOBAL_API_KEY"
   email = "YOUR_EMAIL"
   ```

4. Run the script:
   ```sh
   python3 script.py
   ```

5. The script will list all the domains associated with your Cloudflare account. Enter the number corresponding to the domain you want to manage.

6. Confirm the deletion of all DNS records for the selected domain by typing `y` when prompted.

## Example

1. Run the script:
   ```sh
   python3 script.py
   ```

2. Output:
   ```
   Available Domains:
   1. example.com
   2. anotherdomain.com

   Enter the number of the domain you want to manage: 1
   Attempting Authentication with Provided Global API Key...
   Authenticated! Are you sure you want to delete ALL dns records? This action cannot be reversed! [y/n]: y
   Record www.example.com deleted successfully.
   Record api.example.com deleted successfully.
   Done! Deleted a total of 2 DNS records!
   ```

## Notes

- Ensure that your Global API Key and email are correct and have the necessary permissions.
- Be cautious when deleting DNS records as this action cannot be reversed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Explanation:

- **Features**: Highlights the key features of the script.
- **Requirements**: Lists the prerequisites for running the script.
- **Usage**: Provides step-by-step instructions on how to set up and use the script.
- **Example**: Gives an example of the script's output.
- **Notes**: Important notes and warnings for users.
- **License**: Specifies the license under which the project is released.

This README file is designed to help users understand how to use the script, what to expect from it, and any important considerations they should be aware of.
