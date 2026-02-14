#!/usr/bin/env python3
"""Monitor Jenkins deploy pipeline until completion."""
import urllib.request
import json
import time
import sys
import os
import base64
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

JENKINS_USER = os.getenv('JENKINS_USER', 'arpansahu')
JENKINS_TOKEN = os.getenv('JENKINS_TOKEN')

if not JENKINS_TOKEN:
    print('❌ ERROR: JENKINS_TOKEN not found in .env file')
    print('Add: JENKINS_TOKEN=your_token_here to .env')
    sys.exit(1)

def check_build_status(build_number):
    """Check Jenkins deploy build status."""
    url = f"https://jenkins.arpansahu.space/job/chew_and_cheer_deploy/{build_number}/api/json"
    req = urllib.request.Request(url)
    
    # Add authentication
    credentials = base64.b64encode(f"{JENKINS_USER}:{JENKINS_TOKEN}".encode()).decode('ascii')
    req.add_header('Authorization', f'Basic {credentials}')
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            return data.get('result'), data.get('building', False)
    except Exception as e:
        return None, None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 monitor_deploy.py <build_number>")
        sys.exit(1)
    
    build_num = sys.argv[1]
    print(f"\n🚀 Monitoring deploy build #{build_num}...")
    print("=" * 60)
    
    start_time = time.time()
    iteration = 0
    max_iterations = 50  # 25 minutes max (50 * 30 seconds)
    
    while iteration < max_iterations:
        result, building = check_build_status(build_num)
        elapsed = int(time.time() - start_time)
        elapsed_min = elapsed / 60
        
        if result is None:
            print(f"⏳ [{iteration+1}/50] {elapsed}s ({elapsed_min:.1f}min) - Waiting for build to start...")
        elif building:
            print(f"⚙️  [{iteration+1}/50] {elapsed}s ({elapsed_min:.1f}min) - Deploying...")
        elif result == "SUCCESS":
            print(f"\n✅ DEPLOY BUILD #{build_num} SUCCEEDED!")
            print(f"⏱️  Total time: {elapsed}s ({elapsed_min:.1f} minutes)")
            print("=" * 60)
            sys.exit(0)
        elif result == "FAILURE":
            print(f"\n❌ DEPLOY BUILD #{build_num} FAILED!")
            print(f"Check logs: https://jenkins.arpansahu.space/job/chew_and_cheer_deploy/{build_num}/console")
            sys.exit(1)
        elif result == "ABORTED":
            print(f"\n⚠️  DEPLOY BUILD #{build_num} ABORTED")
            sys.exit(2)
        
        time.sleep(30)
        iteration += 1
    
    print(f"\n⏱️  TIMEOUT: Deploy monitoring exceeded {max_iterations * 30 / 60} minutes")
    print(f"Check manually: https://jenkins.arpansahu.space/job/chew_and_cheer_deploy/{build_num}/")
    sys.exit(2)
