# check_service_health/management/commands/test_storage.py

from django.core.management.base import BaseCommand
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import uuid


class Command(BaseCommand):
    help = 'Test if the storage backend (S3/MinIO/FileSystem) is working properly'

    def add_arguments(self, parser):
        parser.add_argument(
            '--detailed',
            action='store_true',
            help='Show detailed output'
        )

    def handle(self, *args, **options):
        verbose = options.get('detailed', False)
        
        # Generate unique filename to avoid collisions
        test_filename = f'health_check_test_{uuid.uuid4()}.txt'
        test_content = 'This is a storage health check test file.'
        
        try:
            # Check if USE_S3 is enabled
            use_s3 = getattr(settings, 'USE_S3', False)
            storage_backend = default_storage.__class__.__name__
            
            if verbose:
                self.stdout.write(f'Storage backend: {storage_backend}')
                self.stdout.write(f'USE_S3: {use_s3}')
                if use_s3:
                    bucket_name = getattr(settings, 'AWS_STORAGE_BUCKET_NAME', 'Not configured')
                    self.stdout.write(f'S3 Bucket: {bucket_name}')
            
            # Test 1: Write file
            if verbose:
                self.stdout.write(f'Testing file upload: {test_filename}')
            
            saved_path = default_storage.save(test_filename, ContentFile(test_content.encode()))
            
            if verbose:
                self.stdout.write(self.style.SUCCESS(f'✓ File saved successfully: {saved_path}'))
            
            # Test 2: Check if file exists
            if not default_storage.exists(saved_path):
                self.stdout.write(self.style.ERROR('❌ File was saved but does not exist'))
                return
            
            if verbose:
                self.stdout.write(self.style.SUCCESS(f'✓ File exists: {saved_path}'))
            
            # Test 3: Read file
            with default_storage.open(saved_path, 'r') as file:
                retrieved_content = file.read()
            
            if retrieved_content != test_content:
                self.stdout.write(self.style.ERROR(f'❌ File content mismatch'))
                self.stdout.write(f'   Expected: {test_content}')
                self.stdout.write(f'   Got: {retrieved_content}')
                return
            
            if verbose:
                self.stdout.write(self.style.SUCCESS(f'✓ File read successfully'))
                self.stdout.write(f'   Content: {retrieved_content}')
            
            # Test 4: Get file size
            file_size = default_storage.size(saved_path)
            if verbose:
                self.stdout.write(self.style.SUCCESS(f'✓ File size: {file_size} bytes'))
            
            # Test 5: Get file URL (may not work for all backends)
            try:
                file_url = default_storage.url(saved_path)
                if verbose:
                    self.stdout.write(self.style.SUCCESS(f'✓ File URL: {file_url}'))
            except NotImplementedError:
                if verbose:
                    self.stdout.write(self.style.WARNING('⚠️  URL generation not supported by this backend'))
            
            # Test 6: Delete file
            default_storage.delete(saved_path)
            
            if default_storage.exists(saved_path):
                self.stdout.write(self.style.ERROR('❌ File deletion failed'))
                return
            
            if verbose:
                self.stdout.write(self.style.SUCCESS(f'✓ File deleted successfully'))
            
            # Success message
            self.stdout.write(self.style.SUCCESS(
                f'✅ Storage health check passed ({storage_backend})'
            ))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Storage health check failed: {str(e)}'))
            if verbose:
                import traceback
                self.stdout.write(self.style.ERROR(traceback.format_exc()))
            raise
