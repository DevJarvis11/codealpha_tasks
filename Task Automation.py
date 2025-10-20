"""
TASK 3: TASK AUTOMATION WITH PYTHON SCRIPTS
File: task_automation.py
Description: Automate repetitive tasks - file management, email extraction, web scraping
"""

import os
import shutil
import re
from datetime import datetime

# Check if requests module is available
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("⚠️ 'requests' module not installed. Web scraping feature will be limited.")
    print("Install it using: pip install requests\n")


# ===============================================
# AUTOMATION 1: Move Image Files
# ===============================================
def move_jpg_files():
    """Move all .jpg files from source to destination folder"""
    
    print("\n" + "=" * 60)
    print("📁 IMAGE FILE ORGANIZER")
    print("=" * 60)
    
    source = input("Enter source folder path (press Enter for current folder): ").strip()
    if not source:
        source = '.'
    
    if not os.path.exists(source):
        print(f"❌ Source folder '{source}' does not exist!")
        return
    
    destination = input("Enter destination folder name (default: 'images_backup'): ").strip()
    if not destination:
        destination = 'images_backup'
    
    # Create destination folder if it doesn't exist
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)
            print(f"✅ Created folder: {destination}")
    except Exception as e:
        print(f"❌ Error creating destination folder: {e}")
        return
    
    # Move .jpg files
    moved_count = 0
    error_count = 0
    
    try:
        for filename in os.listdir(source):
            if filename.lower().endswith(('.jpg', '.jpeg')):
                source_path = os.path.join(source, filename)
                
                # Skip if it's a directory
                if os.path.isdir(source_path):
                    continue
                
                dest_path = os.path.join(destination, filename)
                
                # Handle duplicate filenames
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(dest_path):
                        new_filename = f"{base}_{counter}{ext}"
                        dest_path = os.path.join(destination, new_filename)
                        counter += 1
                    print(f"  ➡️  Moved: {filename} → {os.path.basename(dest_path)} (renamed)")
                else:
                    print(f"  ➡️  Moved: {filename}")
                
                try:
                    shutil.move(source_path, dest_path)
                    moved_count += 1
                except Exception as e:
                    print(f"  ❌ Error moving {filename}: {e}")
                    error_count += 1
        
        print("\n" + "=" * 60)
        if moved_count > 0:
            print(f"✅ Successfully moved {moved_count} image file(s)")
            print(f"📂 Destination: {os.path.abspath(destination)}")
        else:
            print("⚠️ No .jpg or .jpeg files found in the source folder")
        
        if error_count > 0:
            print(f"⚠️ {error_count} file(s) could not be moved")
        print("=" * 60)
        
    except PermissionError:
        print("❌ Permission denied. Please check folder permissions.")
    except Exception as e:
        print(f"❌ Error: {e}")


# ===============================================
# AUTOMATION 2: Extract Email Addresses
# ===============================================
def extract_email_addresses():
    """Extract all email addresses from a text file"""
    
    print("\n" + "=" * 60)
    print("📧 EMAIL EXTRACTOR")
    print("=" * 60)
    
    input_file = input("Enter input text file name: ").strip()
    
    if not input_file:
        print("❌ Filename cannot be empty!")
        return
    
    if not os.path.exists(input_file):
        print(f"❌ File '{input_file}' not found!")
        print(f"Current directory: {os.getcwd()}")
        return
    
    output_file = input("Enter output file name (default: 'extracted_emails.txt'): ").strip()
    if not output_file:
        output_file = 'extracted_emails.txt'
    
    # Email regex pattern - more comprehensive
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    try:
        # Read input file
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        print(f"\n📄 File size: {len(content)} characters")
        
        # Find all emails
        emails = re.findall(email_pattern, content)
        
        # Remove duplicates while preserving order
        unique_emails = []
        seen = set()
        for email in emails:
            email_lower = email.lower()
            if email_lower not in seen:
                unique_emails.append(email)
                seen.add(email_lower)
        
        if unique_emails:
            # Save to output file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write("=" * 60 + "\n")
                file.write("EMAIL EXTRACTION REPORT\n")
                file.write("=" * 60 + "\n")
                file.write(f"Source File: {input_file}\n")
                file.write(f"Extraction Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"Total Emails Found: {len(unique_emails)}\n")
                file.write("=" * 60 + "\n\n")
                
                for i, email in enumerate(unique_emails, 1):
                    file.write(f"{i}. {email}\n")
                
                file.write("\n" + "=" * 60 + "\n")
            
            print(f"\n✅ Found {len(unique_emails)} unique email address(es):")
            print("-" * 60)
            for i, email in enumerate(unique_emails, 1):
                print(f"   {i}. {email}")
            print("-" * 60)
            print(f"\n✅ Emails saved to: {output_file}")
        else:
            print("\n⚠️ No email addresses found in the file.")
            print("Make sure the file contains valid email addresses.")
    
    except UnicodeDecodeError:
        print("❌ Error reading file. The file might be in a different encoding.")
    except Exception as e:
        print(f"❌ Error: {e}")


# ===============================================
# AUTOMATION 3: Scrape Webpage Title
# ===============================================
def scrape_webpage_title():
    """Scrape the title of a webpage and save it to a file"""
    
    print("\n" + "=" * 60)
    print("🌐 WEBPAGE TITLE SCRAPER")
    print("=" * 60)
    
    if not REQUESTS_AVAILABLE:
        print("❌ This feature requires the 'requests' module.")
        print("Install it using: pip install requests")
        return
    
    url = input("Enter webpage URL (e.g., example.com): ").strip()
    
    if not url:
        print("❌ URL cannot be empty!")
        return
    
    # Add https:// if not present
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    output_file = input("Enter output file name (default: 'webpage_title.txt'): ").strip()
    if not output_file:
        output_file = 'webpage_title.txt'
    
    try:
        print(f"\n🔄 Fetching webpage: {url}")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        print(f"✅ Status Code: {response.status_code}")
        
        # Extract title using regex
        title_match = re.search(r'<title[^>]*>(.*?)</title>', response.text, re.IGNORECASE | re.DOTALL)
        
        if title_match:
            title = title_match.group(1).strip()
            # Clean up whitespace and newlines
            title = re.sub(r'\s+', ' ', title)
            
            # Save to file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write("=" * 60 + "\n")
                file.write("WEBPAGE INFORMATION\n")
                file.write("=" * 60 + "\n")
                file.write(f"URL: {url}\n")
                file.write(f"Title: {title}\n")
                file.write(f"Status Code: {response.status_code}\n")
                file.write(f"Content Type: {response.headers.get('Content-Type', 'N/A')}\n")
                file.write(f"Content Length: {len(response.content)} bytes\n")
                file.write(f"Scraped Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("=" * 60 + "\n")
            
            print(f"\n📄 Page Title: {title}")
            print(f"✅ Information saved to: {output_file}")
        else:
            print("\n⚠️ No title tag found on the webpage.")
            print("The page might not have a proper HTML structure.")
    
    except requests.exceptions.Timeout:
        print("❌ Request timed out. The server took too long to respond.")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check:")
        print("   - Your internet connection")
        print("   - The URL is correct")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        print("The webpage might not be accessible.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")


# ===============================================
# MAIN MENU
# ===============================================
def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 60)
    print("🤖 TASK AUTOMATION TOOLKIT")
    print("=" * 60)
    print("\nSelect an automation task:")
    print("  1️⃣  Move all .jpg files to a new folder")
    print("  2️⃣  Extract email addresses from a text file")
    print("  3️⃣  Scrape webpage title and save it")
    print("  4️⃣  Exit")
    print("=" * 60)


def main():
    """Main function to run the automation toolkit"""
    
    print("\n" + "🎯" * 30)
    print("Welcome to Task Automation Toolkit!")
    print("🎯" * 30)
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            move_jpg_files()
        elif choice == '2':
            extract_email_addresses()
        elif choice == '3':
            scrape_webpage_title()
        elif choice == '4':
            print("\n" + "=" * 60)
            print("👋 Thank you for using Task Automation Toolkit!")
            print("=" * 60)
            break
        else:
            print("\n❌ Invalid choice! Please select 1-4.")
            continue
        
        if choice in ['1', '2', '3']:
            print("\n" + "-" * 60)
            continue_choice = input("🔄 Perform another task? (yes/no): ").lower().strip()
            if not continue_choice.startswith('y'):
                print("\n" + "=" * 60)
                print("👋 Thank you for using Task Automation Toolkit!")
                print("=" * 60)
                break


if __name__ == "__main__":
    main()