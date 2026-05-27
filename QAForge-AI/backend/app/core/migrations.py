from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func

def upgrade():
    # Create users table
    op.create_table(
        'users',
        Column('id', Integer, primary_key=True, index=True),
        Column('email', String, unique=True, index=True),
        Column('hashed_password', String),
        Column('is_active', Boolean, default=True),
        Column('created_at', DateTime, default=func.now()),
        Column('updated_at', DateTime, default=func.now(), onupdate=func.now())
    )

    # Create projects table
    op.create_table(
        'projects',
        Column('id', Integer, primary_key=True, index=True),
        Column('name', String, index=True),
        Column('description', String),
        Column('owner_id', Integer, ForeignKey('users.id')),
        Column('created_at', DateTime, default=func.now()),
        Column('updated_at', DateTime, default=func.now(), onupdate=func.now())
    )

    # Create test_runs table
    op.create_table(
        'test_runs',
        Column('id', Integer, primary_key=True, index=True),
        Column('project_id', Integer, ForeignKey('projects.id')),
        Column('status', String),
        Column('started_at', DateTime, default=func.now()),
        Column('completed_at', DateTime),
        Column('created_at', DateTime, default=func.now()),
        Column('updated_at', DateTime, default=func.now(), onupdate=func.now())
    )

def downgrade():
    # Drop tables in reverse order
    op.drop_table('test_runs')
    op.drop_table('projects')
    op.drop_table('users')