
from sqlalchemy.types import TypeDecorator, DateTime
from datetime import datetime
from dateutil import parser
class DateTimeString(TypeDecorator):
    impl = DateTime

    def process_bind_param(self, value, dialect):
        if value is not None:
            # Si el valor es una cadena, conviértelo a un objeto datetime
            if isinstance(value, str):
                return datetime.fromisoformat(value)
            # Si ya es un objeto datetime, déjalo como está
            elif isinstance(value, datetime):
                return value
        # Si el valor es None, déjalo como está
        return value

    
