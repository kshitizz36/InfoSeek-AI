from asyncio import run
import os
import sys
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
from app.services.google_sheets import GoogleSheetsService

ASYNCIO_PREFIX = ''

# Add the project root to Python path
root_dir = Path(__file__).parent
sys.path.append(str(root_dir))

# Load environment variables
load_dotenv()

# Import after environment variables are loaded
from app.services.google_sheets import GoogleSheetsService

class GoogleSheetsServiceTest:
    async def test_sheet_sharing(self):
        try:
            print('\\nChecking environment setup...')
            # Verify credentials path
            if 'GOOGLE_CREDENTIALS_FILE' not in os.environ:
                print('❌ GOOGLE_CREDENTIALS_FILE not found in environment variables')
                return

            creds_path = os.environ['GOOGLE_CREDENTIALS_FILE']
            abs_creds_path = Path(creds_path)
            print(f'Looking for credentials at: {abs_creds_path}')

            if not abs_creds_path.exists():
                print(f'❌ Credentials file not found at: {abs_creds_path}')
                return

            # Create test data
            print('\nCreating test data...')
            test_data = {
                'Column1': ['Test1', 'Test2', 'Test3'],
                'Column2': [100, 200, 300],
                'Column3': ['A', 'B', 'C']
            }
            df = pd.DataFrame(test_data)

            # Initialize service
            print('\nInitializing Google Sheets service...')
            GoogleSheetsService()

            # Create and share spreadsheet
            print('\nCreating and sharing spreadsheet...')
            sheet_id = await GoogleSheetsService().export_to_sheets(
                df=df,
                sheet_title='Public Test Sheet',
                make_public=True,
                share_with_email='kshitizyadav69@gmail.com'
            )

            print(f'\\n\\u2705 Success!')
            print(f'Sheet ID: {sheet_id}')
            print(f'Public URL: https://docs.google.com/spreadsheets/d/{sheet_id}/view')
            print(f'Sheet has been shared with kshitizyadav69@gmail.com')

        except Exception as e:
            print(f'\\n\\u26E9 Error: {str(e)}')
            import traceback
            print('\\nFull error trace:')
            print(traceback.format_exc())


if __name__ == '__main__':
    print('Starting Google Sheets sharing test...')
    root_dir = Path(__file__).parent

    # Verify .env file exists
    if not (root_dir / '.env').exists():
        print(f'\\n\\u26E9 .env file not found at: {root_dir}')
        sys.exit(1)

    # Run the test
    run(GoogleSheetsServiceTest().test_sheet_sharing())