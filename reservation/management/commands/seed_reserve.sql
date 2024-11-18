-- Inserting 5 customers    ORDER: Run this first
-- INSERT INTO reservation_customer (user_id, username, first_name, last_name, email, phone_number, address, created_at, updated_at)
-- VALUES
-- (1, 'johndoe12', 'John', 'Doe', 'john.doe@example.com', '1234567890', '123 Elm St, Springfield, IL', NOW(), NOW()),
-- (2, 'jane_smith', 'Jane', 'Smith', 'jane.smith@example.com', '2345678901', '456 Oak St, Springfield, IL', NOW(), NOW()),
-- (3, 'michael_lee', 'Michael', 'Lee', 'michael.lee@example.com', '3456789012', '789 Pine St, Springfield, IL', NOW(), NOW()),
-- (4, 'emily_jones', 'Emily', 'Jones', 'emily.jones@example.com', '4567890123', '321 Birch St, Springfield, IL', NOW(), NOW())


-- -- Inserting 5 bookings    ORDER: Run this second
INSERT INTO reservation_booking (customer_id, room_id, check_in_date, check_out_date, number_of_guests, created_at, updated_at)
VALUES
(6, 122, '2024-11-20', '2024-11-25', 1, NOW(), NOW()),
(7, 122, '2024-11-22', '2024-11-24', 2, NOW(), NOW()),
(7, 123, '2024-11-23', '2024-11-30', 3, NOW(), NOW()),
(8, 124, '2024-11-25', '2024-11-27', 1, NOW(), NOW()),
(9, 125, '2024-11-26', '2024-11-28', 2, NOW(), NOW());
