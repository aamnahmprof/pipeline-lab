def cancellation_fee(hours_before):
  """A clinic's rule: cancelling less than 24 hours before an
  appointment costs $25. Cancelling 24 hours or more ahead is free."""
  if hours_before < 0:
    raise ValueError("hours_before cannot be negative")
  if hours_before > 24:
    return 0
  return 25
