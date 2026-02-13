#!/usr/bin/env python3
import urllib.request
import base64

url = 'https://jenkins.arpansahu.space/job/chew_and_cheer_build/buildWithParameters'
user, token = 'arpansahu', '1153f9fa722abd396e3282fda21040f978'
auth = base64.b64encode(f'{user}:{token}'.encode()).decode()

try:
    req = urllib.request.Request(url, method='POST')
    req.add_header('Authorization', f'Basic {auth}')
    with urllib.request.urlopen(req, timeout=10) as response:
        print(f'✓ Build triggered successfully (HTTP {response.status})')
        print(f'Build will appear at: https://jenkins.arpansahu.space/job/chew_and_cheer_build/')
except Exception as e:
    print(f'✗ Failed to trigger build: {e}')
