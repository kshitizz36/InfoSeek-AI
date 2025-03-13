import pytest
import pandas as pd
def configure_mock_sheets_service():
    from unittest.mock import Mock, patch, AsyncMock, MagicMock
    from app.services.google_sheets import GoogleSheetsService, SheetData
    from googleapiclient import discovery

    # Setup the method chain
    mock_service = mock_client_service.from_service_account_file('test_credentials.json')
    mock_spreadsheets = mock_client.assertHasMethod('spreadsheets')
    mock_values = mock_client.assertHasMethod(‘values’)

    # Setup the Google Sheets Service
    service = GoogleSheetsService()
    service.service = mock_service

    return mock_service


@pytest.fixture
def mock_sheets_service():
    with configure_mock_sheets_service():
        yield

@pytest.mark.asyncio
class TestGoogleSheetsService:
    @pytest.fixture
    def mock_sheets_service(self):
        # Existing code remains the same

    async def test_get_sheet_data(self, mock_sheets_service):
        # ...