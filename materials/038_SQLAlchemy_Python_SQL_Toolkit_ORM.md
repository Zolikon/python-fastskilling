# SQLAlchemy: Python SQL Toolkit and ORM

SQLAlchemy is a powerful and flexible toolkit for working with databases in Python. It supports both SQL (core) and Object Relational Mapping (ORM) approaches, making it suitable for a wide range of applications.

## Installation
```cmd
pip install sqlalchemy
pip install sqlalchemy[asyncio]  # For async support
pip install aiosqlite  # For async SQLite
```

## Connecting to a Database (Core)
```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///example.db')
connection = engine.connect()
result = connection.execute("SELECT 1")
print(result.scalar())
connection.close()
```

## Defining Tables (Core)
```python
from sqlalchemy import Table, Column, Integer, String, MetaData
metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
)
metadata.create_all(engine)
```

## Inserting and Querying Data (Core)
```python
with engine.begin() as conn:
    conn.execute(users.insert().values(name="Alice"))
    result = conn.execute(users.select())
    for row in result:
        print(row)
```

## Using the ORM: Defining Models
```python
from sqlalchemy.orm import declarative_base, Session
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

Base.metadata.create_all(engine)
```

## Adding and Querying ORM Objects
```python
with Session(engine) as session:
    user = User(name="Bob")
    session.add(user)
    session.commit()
    users = session.query(User).all()
    for user in users:
        print(user.id, user.name)
```

## Filtering, Updating, and Deleting
```python
with Session(engine) as session:
    # Filtering
    user = session.query(User).filter_by(name="Bob").first()
    # Updating
    user.name = "Robert"
    session.commit()
    # Deleting
    session.delete(user)
    session.commit()
```

## Relationships (One-to-Many)
```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='posts')

User.posts = relationship('Post', back_populates='user')
Base.metadata.create_all(engine)
```

## Async ORM Example (SQLAlchemy 2.x)
```python
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

async def async_main():
    engine = create_async_engine('sqlite+aiosqlite:///example.db')
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        result = await session.execute(users.select())
        for row in result:
            print(row)

asyncio.run(async_main())
```

## Common Pitfalls
- Forgetting to commit transactions
- Not closing sessions/connections
- Using synchronous code in async contexts

SQLAlchemy is the de facto standard for database access in Python, supporting everything from quick scripts to large-scale applications.
