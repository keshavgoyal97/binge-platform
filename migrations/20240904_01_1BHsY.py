"""
Create user table
"""

from yoyo import step

steps = [
    step('''CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'''),
    step(
        "Create table admin (id SERIAL PRIMARY KEY, type varchar(20) NOT NULL, user_id varchar(100) NOT NULL, password varchar(100) NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(0))"),
    step(
        "Create table meta_data (id SERIAL PRIMARY KEY, data jsonb NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(0))"),
    step(
        "Create table user_login (id SERIAL PRIMARY KEY, otp varchar(10) NOT NULL,phone_number varchar(10) NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(0))"),
    step(
        "Create table booking (id varchar(15) PRIMARY KEY, admin_name varchar(100), status varchar(15), booking_name varchar(100), booking_date varchar(10), start_time varchar(5), end_time varchar(5), theatre_id varchar(5), branch_id varchar(5), total_price int, advance_paid int, email varchar(100), total_price, number_of_people int, decor_type varchar(100), decor_name_1 varchar(100), decor_name_2 varchar(100), add_on_ids varchar(100), cake_ids varchar(100), duration int, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(0))"),
    step(
        "Create table transaction (id varchar(15) PRIMARY KEY, booking_id varchar(15), amount float, status varchar(20), vendor varchar(30), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(0))")
]
