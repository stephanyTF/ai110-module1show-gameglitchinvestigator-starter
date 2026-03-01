import pytest
import sys
from pathlib import Path

# Add parent directory to path to import from app.py
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import check_guess, update_score


# Difficulty attempt limits
EASY_LIMIT = 6
NORMAL_LIMIT = 8
HARD_LIMIT = 5


class TestCheckRange:
    def test_guess_within_range(self):
        # If secret is 50 and guess is 50, it should be a win
        outcome, message = check_guess(50, 50)
        assert outcome == "Win"
        assert "Correct" in message

    def test_guess_above_range(self):
        # If secret is 50 and guess is 150, hint should be "Too High"
        outcome, message = check_guess(150, 50)
        assert outcome == "Too High"
        assert "LOWER" in message or "LOW" in message

    def test_guess_below_range(self):
        # If secret is 50 and guess is -10, hint should be "Too Low"
        outcome, message = check_guess(-10, 50)
        assert outcome == "Too Low"
        assert "HIGHER" in message or "HIGH" in message

class TestCheckGuess:
    def test_winning_guess(self):
        # If the secret is 50 and guess is 50, it should be a win
        outcome, message = check_guess(50, 50)
        assert outcome == "Win"
        assert "Correct" in message

    def test_guess_too_high(self):
        # If secret is 50 and guess is 60, hint should be "Too High"
        outcome, message = check_guess(60, 50)
        assert outcome == "Too High"
        assert "HIGHER" in message or "HIGH" in message

    def test_guess_too_low(self):
        # If secret is 50 and guess is 40, hint should be "Too Low"
        outcome, message = check_guess(40, 50)
        assert outcome == "Too Low"
        assert "LOWER" in message or "LOW" in message


class TestUpdateScore:
    """Tests for the new scoring logic based on efficiency."""
    
    # Test Win scenarios - Efficiency-based scoring
    def test_win_first_attempt_easy(self):
        """Perfect game on Easy difficulty (attempt limit: 6).
        Efficiency: 1/6 ≈ 0.167, Points: 100 - (0.167 * 90) ≈ 85"""
        points = update_score(0, "Win", 1, EASY_LIMIT)
        efficiency = 1 / EASY_LIMIT
        expected = max(10, int(100 - (efficiency * 90)))
        assert points == expected
        assert points == 85
    
    def test_win_halfway_through_normal(self):
        """Win on 4th attempt on Normal difficulty (attempt limit: 8).
        Efficiency: 4/8 = 0.5, Points: 100 - (0.5 * 90) = 55"""
        points = update_score(0, "Win", 4, NORMAL_LIMIT)
        efficiency = 4 / NORMAL_LIMIT
        expected = max(10, int(100 - (efficiency * 90)))
        assert points == expected
        assert points == 55
    
    def test_win_last_attempt_hard(self):
        """Win on last attempt on Hard difficulty (attempt limit: 5).
        Efficiency: 5/5 = 1.0, Points: 100 - (1.0 * 90) = 10"""
        points = update_score(0, "Win", 5, HARD_LIMIT)
        efficiency = 5 / HARD_LIMIT
        expected = max(10, int(100 - (efficiency * 90)))
        assert points == expected
        assert points == 10
    
    def test_win_excellent_easy(self):
        """Win on 2nd attempt on Easy difficulty (attempt limit: 6).
        Efficiency: 2/6 ≈ 0.333, Points: 100 - (0.333 * 90) ≈ 70"""
        points = update_score(0, "Win", 2, EASY_LIMIT)
        efficiency = 2 / EASY_LIMIT
        expected = max(10, int(100 - (efficiency * 90)))
        assert points == expected
        assert points == 70
    
    def test_win_good_normal(self):
        """Win on 2nd attempt on Normal difficulty (attempt limit: 8).
        Efficiency: 2/8 = 0.25, Points: 100 - (0.25 * 90) = 77.5 → 77"""
        points = update_score(0, "Win", 2, NORMAL_LIMIT)
        efficiency = 2 / NORMAL_LIMIT
        expected = max(10, int(100 - (efficiency * 90)))
        assert points == expected
        assert points == 77
    
    def test_win_minimum_points_threshold(self):
        """Win with maximum attempts should result in minimum points (10).
        Efficiency = 1.0, Points: must be at least 10"""
        points = update_score(0, "Win", 8, NORMAL_LIMIT)
        efficiency = 8 / NORMAL_LIMIT
        expected = max(10, int(100 - (efficiency * 90)))
        assert points == expected
        assert points >= 10

    # Test Loss scenarios - Should return 0
    def test_loss_returns_zero(self):
        """Player loses, should return 0 points regardless of attempts."""
        points = update_score(100, "Loss", 8, NORMAL_LIMIT)
        assert points == 0
    
    def test_loss_with_few_attempts(self):
        """Even if player was doing well before losing, returns 0."""
        points = update_score(50, "Loss", 2, EASY_LIMIT)
        assert points == 0
    
    def test_loss_with_all_attempts_used(self):
        """Loss after using all attempts returns 0."""
        points = update_score(0, "Loss", 8, NORMAL_LIMIT)
        assert points == 0

    # Test other outcomes - Should return 0
    def test_too_high_returns_zero(self):
        """Ongoing game (Too High) should not update score."""
        points = update_score(50, "Too High", 3, NORMAL_LIMIT)
        assert points == 0
    
    def test_too_low_returns_zero(self):
        """Ongoing game (Too Low) should not update score."""
        points = update_score(50, "Too Low", 3, NORMAL_LIMIT)
        assert points == 0

    # Test edge cases
    def test_win_first_attempt_different_difficulties(self):
        """First attempt wins give scores based on attempt limit.
        The formula: points = 100 - (attempts/limit * 90)
        So with 1 attempt, higher limit = lower efficiency = higher score"""
        points_easy = update_score(0, "Win", 1, EASY_LIMIT)      # 1/6
        points_normal = update_score(0, "Win", 1, NORMAL_LIMIT)  # 1/8
        points_hard = update_score(0, "Win", 1, HARD_LIMIT)      # 1/5
        
        # Higher attempt limit (easier difficulty) = lower efficiency = higher score
        assert points_normal > points_easy > points_hard
        assert points_easy == 85   # 1/6 = 0.167, 100 - 15 = 85
        assert points_normal == 88  # 1/8 = 0.125, 100 - 11.25 = 88
        assert points_hard == 82   # 1/5 = 0.2, 100 - 18 = 82

    def test_current_score_parameter_ignored(self):
        """Current score parameter should not affect the new score calculation."""
        points_with_0 = update_score(0, "Win", 3, NORMAL_LIMIT)
        points_with_100 = update_score(100, "Win", 3, NORMAL_LIMIT)
        points_with_50 = update_score(50, "Win", 3, NORMAL_LIMIT)
        
        # All should return the same score
        assert points_with_0 == points_with_100 == points_with_50
    
    def test_score_calculation_precision(self):
        """Verify the scoring formula uses int() conversion correctly."""
        # Test case where int() matters: 3/8 = 0.375, 0.375 * 90 = 33.75
        # 100 - 33.75 = 66.25, int(66.25) = 66
        points = update_score(0, "Win", 3, NORMAL_LIMIT)
        efficiency = 3 / NORMAL_LIMIT
        expected = max(10, int(100 - (efficiency * 90)))
        assert points == expected
        assert points == 66

    # Test scoring fairness across difficulties
    @pytest.mark.parametrize("attempts,limit,expected_points", [
        (1, 6, 85),      # Easy: 1/6 = 0.167, 100 - 15 = 85
        (3, 6, 55),      # Easy: 3/6 = 0.5, 100 - 45 = 55
        (6, 6, 10),      # Easy: 6/6 = 1.0, 100 - 90 = 10
        (1, 8, 88),      # Normal: 1/8 = 0.125, 100 - 11.25 = 88.75 → 88
        (4, 8, 55),      # Normal: 4/8 = 0.5, 100 - 45 = 55
        (8, 8, 10),      # Normal: 8/8 = 1.0, 100 - 90 = 10
        (1, 5, 82),      # Hard: 1/5 = 0.2, 100 - 18 = 82
        (3, 5, 46),      # Hard: 3/5 = 0.6, 100 - 54 = 46
        (5, 5, 10),      # Hard: 5/5 = 1.0, 100 - 90 = 10
    ])
    def test_win_various_difficulties(self, attempts, limit, expected_points):
        """Test scoring across different difficulties and attempt counts."""
        points = update_score(0, "Win", attempts, limit)
        efficiency = attempts / limit
        expected = max(10, int(100 - (efficiency * 90)))
        assert points == expected_points
        assert points == expected

    def test_score_always_at_least_10(self):
        """Minimum score should always be 10 for wins."""
        # Even with very poor efficiency
        points_worst = update_score(0, "Win", 6, 6)  # 100% attempts
        points_poor = update_score(0, "Win", 8, 8)   # 100% attempts on Normal
        
        assert points_worst >= 10
        assert points_poor >= 10

    def test_score_never_exceeds_100(self):
        """Perfect game should not exceed 100 points.
        Even 1st attempt should be max 100 - (1/limit * 90)"""
        points_best = update_score(0, "Win", 1, 8)  # Best case Normal
        assert points_best <= 100

    # Test default parameter
    def test_default_attempt_limit(self):
        """Test that the function works with default attempt_limit of 8."""
        # This should use the default NORMAL_LIMIT (8)
        points_with_default = update_score(0, "Win", 4)
        points_with_explicit = update_score(0, "Win", 4, 8)
        assert points_with_default == points_with_explicit
