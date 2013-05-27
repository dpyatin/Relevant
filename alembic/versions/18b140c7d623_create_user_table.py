"""create User table

Revision ID: 18b140c7d623
Revises: None
Create Date: 2013-05-27 18:00:21.123074

"""

# revision identifiers, used by Alembic.
revision = '18b140c7d623'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
	op.create_table(
        'User',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(100), nullable=False, unique=True),
        sa.Column('lastTweet', sa.String(200)),
    )

def downgrade():
    op.drop_table('User')
