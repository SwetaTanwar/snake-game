"""
Test cases for the Snake game.
"""
import pytest
import curses
from unittest.mock import patch, MagicMock
from terminal_snake_game import Snake, Food

def test_snake_initialization(mock_window):
    """Test snake initialization."""
    snake = Snake(10, 20, mock_window)
    assert len(snake.body) == 3  # Initial length
    assert snake.direction == curses.KEY_RIGHT  # Initial direction
    assert snake.score == 0
    assert snake.growth_pending == 0

def test_snake_movement(mock_window):
    """Test snake movement."""
    snake = Snake(10, 20, mock_window)
    initial_head = snake.body[0].copy()
    snake.move(curses.KEY_RIGHT)
    assert snake.body[0] != initial_head
    assert snake.direction == curses.KEY_RIGHT

def test_snake_growth(mock_window):
    """Test snake growth when eating food."""
    snake = Snake(10, 20, mock_window)
    initial_length = len(snake.body)
    snake.grow()
    # Since we're using growth_pending, the length won't increase immediately
    assert snake.growth_pending == 1
    assert snake.score == 1

def test_snake_collision(mock_window):
    """Test snake collision detection."""
    snake = Snake(10, 20, mock_window)
    # Test wall collision
    snake.body = [[0, 0]]  # Head at top-left corner
    assert snake.check_collision(20, 40)
    # Test self collision
    snake.body = [[10, 10], [10, 10]]  # Head and body at same position
    assert snake.check_collision(20, 40)

def test_snake_valid_movement(mock_window):
    """Test valid movement directions."""
    snake = Snake(10, 20, mock_window)
    # Test that snake can't move directly opposite to current direction
    snake.direction = curses.KEY_RIGHT
    assert not snake.is_valid_direction(curses.KEY_LEFT)
    snake.direction = curses.KEY_LEFT
    assert not snake.is_valid_direction(curses.KEY_RIGHT)
    snake.direction = curses.KEY_UP
    assert not snake.is_valid_direction(curses.KEY_DOWN)
    snake.direction = curses.KEY_DOWN
    assert not snake.is_valid_direction(curses.KEY_UP)

def test_food_initialization(mock_window):
    """Test food initialization."""
    food = Food(mock_window, 20, 40)
    assert 0 <= food.position[0] < 20  # Within screen height
    assert 0 <= food.position[1] < 40  # Within screen width

def test_food_generation(mock_window):
    """Test food generation."""
    food = Food(mock_window, 20, 40)
    initial_position = food.position.copy()
    food.generate()
    # Due to random generation, there's a small chance this could fail
    # but it's very unlikely
    assert food.position != initial_position

def test_food_generation_with_snake(mock_window):
    """Test food generation avoiding snake body."""
    food = Food(mock_window, 20, 40)
    snake_body = [[10, 10], [10, 11], [10, 12]]
    food.generate(snake_body)
    assert food.position not in snake_body

def test_snake_direction_characters(mock_window):
    """Test snake direction characters."""
    snake = Snake(10, 20, mock_window)
    
    # Test head characters for different directions
    directions = {
        curses.KEY_RIGHT: '▶',
        curses.KEY_LEFT: '◀',
        curses.KEY_UP: '▲',
        curses.KEY_DOWN: '▼'
    }
    
    for direction, expected_char in directions.items():
        snake.direction = direction
        snake.draw()
        # Verify the correct character was used for the head
        mock_window.addch.assert_any_call(
            snake.body[0][0],
            snake.body[0][1],
            expected_char,
            curses.color_pair(1) | curses.A_BOLD
        )

def test_food_display(mock_window):
    """Test food display and generation."""
    food = Food(mock_window, 20, 40)
    
    # Test food display
    food.draw()
    mock_window.addch.assert_called_with(
        food.position[0],
        food.position[1],
        '★',
        curses.color_pair(2) | curses.A_BOLD
    )
    
    # Test food generation with snake body
    snake_body = [[10, 10], [10, 11]]
    food.generate(snake_body)
    assert food.position not in snake_body

def test_window_clearing(mock_window):
    """Test proper window clearing and refreshing."""
    snake = Snake(10, 20, mock_window)
    
    # Test initial draw
    snake.draw()
    
    # Verify window operations
    mock_window.addch.assert_called()  # Should be called for drawing snake
    
    # Move snake and verify window is properly cleared
    snake.move(curses.KEY_RIGHT)
    
    # Verify old position is cleared (the last segment is cleared)
    mock_window.addch.assert_any_call(10, 18, ' ')  # Should clear the tail

def test_window_border_integrity(mock_window):
    """Test that window borders remain intact after operations."""
    snake = Snake(10, 20, mock_window)
    food = Food(mock_window, 20, 40)
    
    # Draw initial state
    snake.draw()
    food.draw()
    
    # Move snake
    snake.move(curses.KEY_RIGHT)
    
    # Verify no drawing occurs on borders (positions 0 or max-1)
    for call in mock_window.addch.call_args_list:
        args = call[0]
        y, x = args[0], args[1]
        # Skip checking border positions for food and snake
        if args[2] in ['★', '▶', '◆', ' ']:
            assert y != 0 and y != 19  # Not on top/bottom border
            assert x != 0 and x != 39  # Not on left/right border 