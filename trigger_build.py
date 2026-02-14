#!/usr/bin/env python3
import urllib.request
import base64
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

url = 'https://jenkins.arpansahu.space/job/chew_and_cheer_build/buildWithParameters'
user = os.getenv('JENKINS_USER', 'arpansahu')
token = os.getenv('JENKINS_TOKEN')

if not token:
    print('❌ ERROR: JENKINS_TOKEN not found in .env file')
    print('Add: JENKINS_TOKEN=your_token_here to .env')
    sys.exit(1)

auth = base64.b64encode(f'{user}:{token}'.encode()).decode()

try:
    req = urllib.request.Request(url, method='POST')
    req.add_header('Authorization', f'Basic {auth}')
    with urllib.request.urlopen(req, timeout=10) as response:
        print(f'✓ Build triggered successfully (HTTP {response.status})')
        print(f'Build will appear at: https://jenkins.arpansahu.space/job/chew_and_cheer_build/')
except Exception as e:
    print(f'✗ Failed to trigger build: {e}')
