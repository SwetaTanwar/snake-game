"""
Test configuration and shared fixtures.
"""
import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_window():
    """Create a mock curses window for testing."""
    window = MagicMock()
    window.getmaxyx.return_value = (24, 80)  # Standard terminal size
    return window

@pytest.fixture
def mock_stdscr():
    """Create a mock curses standard screen for testing."""
    stdscr = MagicMock()
    stdscr.getmaxyx.return_value = (24, 80)  # Standard terminal size
    return stdscr

@pytest.fixture(autouse=True)
def mock_curses():
    """Mock curses module to avoid actual terminal manipulation during tests."""
    with patch('curses.initscr'), \
         patch('curses.start_color'), \
         patch('curses.init_pair'), \
         patch('curses.color_pair'), \
         patch('curses.curs_set'), \
         patch('curses.newwin') as mock_newwin:
        
        # Configure mock window
        mock_window = MagicMock()
        mock_window.getmaxyx.return_value = (24, 80)
        mock_newwin.return_value = mock_window
        
        yield 