import pytest
from unittest.mock import MagicMock, patch
from app import insert_price_to_db

# Mock the database connection
@pytest.fixture
def mock_db_connection():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    return mock_conn, mock_cursor

@patch('app.get_db_connection')
def test_db_connection_failure(mock_get_db_connection):
    # Arrange
    mock_get_db_connection.return_value = None

    # Act
    with app.test_client() as client:
        response = client.get('/db_test')

    # Assert
    assert response.status_code == 500
    assert response.json == {"error": "Database connection failed"}

@patch('app.get_db_connection')  # Mock the get_db_connection function
def test_insert_price_success(mock_get_db_connection, mock_db_connection):
    # Arrange
    mock_conn, mock_cursor = mock_db_connection
    mock_get_db_connection.return_value = mock_conn

    # Act
    result, status_code = insert_price_to_db(5000.0)

    # Assert
    assert result == {"status": "success"}
    assert status_code == 200
    mock_cursor.execute.assert_called_once_with(
        """
        INSERT INTO btc_prices (timestamp, price_usd)
        VALUES (CURRENT_TIMESTAMP, %s);
        """,
        (5000.0,)
    )
    mock_conn.commit.assert_called_once()

@patch('app.get_db_connection')  # Mock the get_db_connection function
def test_insert_price_db_connection_failure(mock_get_db_connection):
    # Arrange
    mock_get_db_connection.return_value = None

    # Act
    result, status_code = insert_price_to_db(5000.0)

    # Assert
    assert result == {"error": "Database connection failed"}
    assert status_code == 500

@patch('app.get_db_connection')  # Mock the get_db_connection function
def test_insert_price_query_failure(mock_get_db_connection, mock_db_connection):
    # Arrange
    mock_conn, mock_cursor = mock_db_connection
    mock_get_db_connection.return_value = mock_conn
    mock_cursor.execute.side_effect = Exception("Query failed")

    # Act
    result, status_code = insert_price_to_db(5000.0)

    # Assert
    assert result == {"error": "Query failed"}
    assert status_code == 500
    mock_conn.rollback.assert_called_once()