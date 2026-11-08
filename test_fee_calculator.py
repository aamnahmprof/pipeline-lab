import pytest
from fee_calculator import cancellation_fee

def test_early_cancellation_is_free():
  assert cancellation_fee(48) == 0
  
def test_late_cancellation_costs_25():
  assert cancellation_fee(3) == 25
  
def test_boundary_exactly_24_hours_is_free():
  assert cancellation_fee(24) == 0 # the boundary — where bugs hide
  
def test_negative_hours_is_rejected():
  with pytest.raises(ValueError):
    cancellation_fee(-1)
