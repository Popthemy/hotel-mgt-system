
-- Insert Categories
-- INSERT INTO hotel_category (name, description, max_occupants, image_url)
-- VALUES
-- ('Single Room', 'Perfect for solo travelers, with basic amenities and a comfortable bed.', 1, 'default-category.png'),
-- ('Double Room', 'Spacious room for two guests, featuring a queen-size bed and modern furnishings.', 2, 'default-category.png'),
-- ('Family Suite', 'Ideal for families, with a large living area, two bedrooms, and extra space for kids.', 4, 'default-category.png'),
-- ('Executive Suite', 'Luxurious suite for business travelers, with a work desk, high-speed internet, and extra comfort.', 2, 'default-category.png'),
-- ('Deluxe Room', 'A premium room with upgraded furnishings, a king-size bed, and scenic views.', 2, 'default-category.png'),
-- ('Presidential Suite', 'The epitome of luxury with a large living room, multiple bedrooms, and exclusive amenities.', 6, 'default-category.png'),
-- ('Studio Room', 'A compact room for short stays, offering a comfortable bed and basic facilities.', 1, 'default-category.png'),
-- ('Penthouse', 'Top-floor suite with panoramic views, two bedrooms, and a private terrace.', 4, 'default-category.png'),
-- ('Junior Suite', 'A cozy suite with a separate sitting area and upgraded furnishings.', 2, 'default-category.png'),
-- ('Budget Room', 'Affordable room for those on a budget, with all essential amenities included.', 1, 'default-category.png');



-- Insert Rooms
INSERT INTO hotel_room (room_number, category_id, description, price_per_night, is_available, bed_type, floor, image_url, created_at, updated_at)
VALUES
('101', 21, 'A small room ideal for solo travelers, with a comfortable single bed.', 75.00, TRUE, 'Single Bed', 1, 'default-room.png',  NOW(), NOW()),
('102', 21, 'Compact room for solo travelers, featuring a work desk and a single bed.', 80.00, TRUE, 'Single Bed', 1, 'default-room.png', NOW(), NOW()),
('103', 22, 'A spacious room with a queen-sized bed and a comfortable seating area.', 120.00, TRUE, 'Queen Size', 1, 'default-room.png', NOW(), NOW()),
('104', 22, 'Double room with modern amenities and a beautiful view of the garden.', 130.00, TRUE, 'Queen Size', 2, 'default-room.png', NOW(), NOW()),
('105', 23, 'Family-friendly room with two separate beds and a living area.', 200.00, TRUE, 'Double Beds', 2, 'default-room.png', NOW(), NOW()),
('106', 23, 'Spacious family suite with a king-size bed and a sofa bed for children.', 210.00, TRUE, 'King Size', 2, 'default-room.png', NOW(), NOW()),
('107', 24, 'Executive suite designed for business travelers with an office desk and high-speed internet.', 250.00, TRUE, 'King Size', 3, 'default-room.png', NOW(), NOW()),
('108', 24, 'Luxurious suite with a sitting area and work desk, ideal for professional meetings.', 270.00, TRUE, 'King Size', 3, 'default-room.png', NOW(), NOW()),
('109', 25, 'A deluxe room with upgraded furnishings and a stunning view of the city skyline.', 300.00, TRUE, 'King Size', 4, 'default-room.png', NOW(), NOW()),
('110', 25, 'Spacious deluxe room featuring premium bedding and elegant décor.', 320.00, TRUE, 'King Size', 4, 'default-room.png', NOW(), NOW()),
('111', 26, 'Presidential suite with multiple bedrooms, a living room, and luxurious amenities.', 500.00, TRUE, 'King Size', 5, 'default-room.png', NOW(), NOW()),
('112', 26, 'Exclusive suite with private dining and a jacuzzi, perfect for high-end guests.', 550.00, TRUE, 'King Size', 5, 'default-room.png', NOW(), NOW()),
('113', 27, 'Small and cozy studio room for one person, with a comfortable bed and basic amenities.', 60.00, TRUE, 'Single Bed', 1, 'default-room.png', NOW(), NOW()),
('114', 27, 'Compact studio ideal for short stays, with an ensuite bathroom and a single bed.', 65.00, TRUE, 'Single Bed', 1, 'default-room.png', NOW(), NOW()),
('115', 28, 'Luxurious penthouse room with a private terrace and panoramic city views.', 600.00, TRUE, 'King Size', 6, 'default-room.png', NOW(), NOW()),
('116', 28, 'Top-floor suite offering stunning views and exclusive amenities, perfect for VIP guests.', 650.00, TRUE, 'King Size', 6, 'default-room.png', NOW(), NOW()),
('117', 29, 'Cozy junior suite with a separate sitting area and elegant décor.', 180.00, TRUE, 'Queen Size', 3, 'default-room.png', NOW(), NOW()),
('118', 29, 'Junior suite offering extra space with a separate living area and upgraded amenities.', 190.00, TRUE, 'Queen Size', 3, 'default-room.png', NOW(), NOW()),
('119', 30, 'Basic room with essential facilities, suitable for short-term stays on a budget.', 50.00, TRUE, 'Single Bed', 1, 'default-room.png', NOW(), NOW()),
('120', 30, 'Simple room offering a comfortable single bed and necessary amenities for budget-conscious travelers.', 55.00, TRUE, 'Single Bed', 1, 'default-room.png', NOW(), NOW()),
('121', 21, 'Room with a comfortable single bed, ideal for solo travelers.', 75.00, TRUE, 'Single Bed', 2, 'default-room.png', NOW(), NOW()),
('122', 21, 'Quiet single room with a bed, desk, and bathroom.', 70.00, TRUE, 'Single Bed', 2, 'default-room.png', NOW(), NOW()),
('123', 22, 'Bright double room with a queen-sized bed and modern amenities.', 120.00, TRUE, 'Queen Size', 2, 'default-room.png', NOW(), NOW()),
('124', 22, 'A double room with high-speed internet and a spacious wardrobe.', 125.00, TRUE, 'Queen Size', 3, 'default-room.png', NOW(), NOW()),
('125', 23, 'Family room with two separate beds and ample space for children to play.', 200.00, TRUE, 'Double Beds', 3, 'default-room.png', NOW(), NOW()),
('126', 23, 'Spacious family suite with a king-size bed and sofa bed for additional guests.', 220.00, TRUE, 'King Size', 3, 'default-room.png', NOW(), NOW()),
('127', 24, 'Luxury suite with a king-size bed, ideal for business stays with a work desk.', 240.00, TRUE, 'King Size', 4, 'default-room.png', NOW(), NOW()),
('128', 24, 'Business suite with high-speed internet and a king-size bed.', 250.00, TRUE, 'King Size', 4, 'default-room.png', NOW(), NOW()),
('129', 25, 'Deluxe room with an elegant design and a queen-size bed.', 320.00, TRUE, 'Queen Size', 5, 'default-room.png', NOW(), NOW()),
('130', 25, 'Large deluxe room with a king-size bed, overlooking the city.', 330.00, TRUE, 'King Size', 5, 'default-room.png', NOW(), NOW()),
('131', 26, 'Luxurious presidential suite with multiple rooms, a private living area, and jacuzzi.', 600.00, TRUE, 'King Size', 6, 'default-room.png', NOW(), NOW()),
('132', 26, 'Exclusive suite with panoramic views, a private dining area, and luxury amenities.', 650.00, TRUE, 'King Size', 6, 'default-room.png', NOW(), NOW()),
('133', 27, 'Compact studio room with a comfortable bed and a modern bathroom.', 65.00, TRUE, 'Single Bed', 2, 'default-room.png', NOW(), NOW()),
('134', 27, 'Affordable studio for short stays with a cozy bed and basic amenities.', 70.00, TRUE, 'Single Bed', 2, 'default-room.png', NOW(), NOW()),
('135', 28, 'Penthouse suite with an expansive living room and private terrace.', 700.00, TRUE, 'King Size', 7, 'default-room.png', NOW(), NOW()),
('136', 28, 'Exclusive top-floor room with incredible city views and upscale furnishings.', 750.00, TRUE, 'King Size', 7, 'default-room.png', NOW(), NOW()),
('137', 29, 'Junior suite with a comfortable bed and an additional seating area.', 170.00, TRUE, 'Queen Size', 4, 'default-room.png', NOW(), NOW()),
('138', 29, 'Elegant junior suite with a cozy living area and king-size bed.', 180.00, TRUE, 'King Size', 4, 'default-room.png', NOW(), NOW()),
('139', 30, 'Basic budget room with a comfortable single bed, perfect for short stays.', 45.00, TRUE, 'Single Bed', 1, 'default-room.png', NOW(), NOW()),
('140', 30, 'Economy room with basic amenities and a single bed.', 50.00, TRUE, 'Single Bed', 1, 'default-room.png',NOW(), NOW());
