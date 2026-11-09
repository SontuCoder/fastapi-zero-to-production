from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from typing import Optional

#

class Book(SQLModel, table=True):
    pass