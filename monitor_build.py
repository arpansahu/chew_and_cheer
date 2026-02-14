#!/usr/bin/env python3
import time, json, urllib.request, base64, sys, os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

url_base = 'https://jenkins.arpansahu.space/job/chew_and_cheer_build'
user = os.getenv('JENKINS_USER', 'arpansahu')
token = os.getenv('JENKINS_TOKEN')

if not token:
    print('❌ ERROR: JENKINS_TOKEN not found in .env file')
    print('Add: JENKINS_TOKEN=your_token_here to .env')
    sys.exit(1)

auth = base64.b64encode(f'{user}:{token}'.encode()).decode()
build_num = int(sys.argv[1]) if len(sys.argv) > 1 else 19

print(f'🔄 Monitoring Jenkins Build #{build_num}')
print(f'📍 {url_base}/{build_num}/')
print('='*70)

for i in range(1, 51):
    try:
        req = urllib.request.Request(f'{url_base}/{build_num}/api/json')
        req.add_header('Authorization', f'Basic {auth}')
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        
        building = data.get('building', False)
        result = data.get('result')
        duration = int(data.get('duration', 0) / 1000)
        
        status = '🔄' if building else '✅' if result == 'SUCCESS' else '❌'
        print(f'{status} Check {i:2d}: Building={str(building):5s} | Result={str(result):7s} | Duration={duration:4d}s')
        
        if not building:
            print('='*70)
            print(f'Build #{build_num} COMPLETED: {result}')
            print(f'Duration: {duration}s ({duration/60:.1f} minutes)')
            print('='*70)
            if result == 'SUCCESS':
                print('✅ BUILD SUCCEEDED!')
                sys.exit(0)
            else:
                print(f'❌ BUILD FAILED: {result}')
                print(f'Console: {url_base}/{build_num}/console')
                sys.exit(1)
        
        if i < 50:
            time.sleep(30)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f'⏳ Check{i:2d}: Build not started yet...')
            time.sleep(15)
        else:
            print(f'❌ HTTP Error: {e}')
            time.sleep(15)
    except Exception as e:
        print(f'⚠️  Check {i:2d}: Error - {e}')
        time.sleep(15)

print('⏰ Monitoring timeout after 25 minutes')
sys.exit(2)
