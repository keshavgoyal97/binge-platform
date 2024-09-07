"""
Create user table
"""

from yoyo import step

steps = [
    step('''CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'''),
    step(
        "Create table admin (id SERIAL, type varchar(20), user_id varchar(100), password varchar(255), phone_number varchar(10), email varchar(100), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"),
    step(
        "Create table meta_data (id SERIAL, data jsonb, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"),
    step(
        "Create table theater (id SERIAL, city varchar(30), branch varchar(50), slots jsonb, metadata jsonb, add_on jsonb, gallery jsonb, address varchar(200), google_map_link varchar(500), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"),
    step(
        "Create table booking (id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), user_id uuid, slot_id uuid, theater_id uuid, city varchar(30), branch varchar(50), transaction_id uuid, status varchar(20), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"),
    step(
        "Create table transaction (id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), token_id varchar(50), amount float, status varchar(20), vendor varchar(30), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
]
