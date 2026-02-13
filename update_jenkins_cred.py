#!/usr/bin/env python3
"""Update Jenkins credential with .env file content."""
import urllib.request
import urllib.parse

# Read .env file
with open('.env', 'r') as f:
    env_content = f.read()

# Create XML payload
xml_content = f'''<org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl plugin="plain-credentials">
  <scope>GLOBAL</scope>
  <id>chew_and_cheer_env_file</id>
  <description>.env file for chew_and_cheer project</description>
  <secret><![CDATA[{env_content}]]></secret>
</org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl>'''

# Prepare request
url = "https://jenkins.arpansahu.space/credentials/store/system/domain/_/credential/chew_and_cheer_env_file/config.xml"
req = urllib.request.Request(url, data=xml_content.encode('utf-8'), method='POST')

# Add authentication
import base64
credentials = base64.b64encode(b"arpansahu:1153f9fa722abd396e3282fda21040f978").decode('ascii')
req.add_header('Authorization', f'Basic {credentials}')
req.add_header('Content-Type', 'application/xml')

try:
    with urllib.request.urlopen(req) as response:
        status = response.status
        print(f"✅ Credential updated successfully (HTTP {status})")
except urllib.error.HTTPError as e:
    print(f"❌ Failed to update credential (HTTP {e.code})")
    print(e.read().decode())
except Exception as e:
    print(f"❌ Error: {e}")
