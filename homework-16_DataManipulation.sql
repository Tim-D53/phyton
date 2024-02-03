DELETE FROM "RESERVATIONS";
DELETE FROM "ROOMS";
DELETE FROM "GUESTS";
DELETE FROM "HOSTS";
DELETE FROM "USERS";

INSERT INTO "USERS" (id, name) VALUES (1, '1 Host and Guest');
INSERT INTO "USERS" (id, name) VALUES (2, '2 Guest');
INSERT INTO "USERS" (id, name) VALUES (3, '3 Host');

INSERT INTO "HOSTS" (id) VALUES (1);
INSERT INTO "HOSTS" (id) VALUES (3);

INSERT INTO "GUESTS" (id) VALUES (1);
INSERT INTO "GUESTS" (id) VALUES (2);

-- '1 Host and Guest' rent out 'Room 1' with 1 resident for 300$ with aircondition and refrigerator
INSERT INTO "ROOMS" (id, host_id, name, residents, price, aircondition, refrigerator) VALUES (1, 1, 'Room 1', 1, 300, true, true);
INSERT INTO "ROOMS" (id, host_id, name, residents, price, aircondition, refrigerator) VALUES (2, 1, 'Room 2', 1, 100, false, false);
INSERT INTO "ROOMS" (id, host_id, name, residents, price, aircondition, refrigerator) VALUES (3, 3, 'Room 3', 1, 200, false, true);

-- '1 Host and Guest' reserves 'Room 3'
INSERT INTO "RESERVATIONS" (guest_id, room_id) VALUES (1, 3);
INSERT INTO "RESERVATIONS" (guest_id, room_id) VALUES (2, 1);
INSERT INTO "RESERVATIONS" (guest_id, room_id) VALUES (2, 2);

SELECT u.id AS user_id, u.name AS user_name
FROM "USERS" u
JOIN "RESERVATIONS" rs ON u.id = rs.guest_id
JOIN "ROOMS" rm ON rm.id =  rs.room_id
WHERE rm.host_id != rs.guest_id
GROUP BY u.id, u.name
ORDER BY COUNT(*) DESC
LIMIT 1;
