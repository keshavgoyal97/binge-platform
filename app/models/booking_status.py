from enum import Enum


class BookingStatus(Enum):
    CREATED = 1
    IN_PROGRESS = 2
    PAYMENT_DONE = 3
    COMPLETED = 4
    CANCELLED = 5
    UPDATED = 6



