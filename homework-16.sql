DROP TABLE IF EXISTS "RESERVATIONS";
DROP TABLE IF EXISTS "ROOMS";
DROP TABLE IF EXISTS "HOSTS";
DROP TABLE IF EXISTS "GUESTS";
DROP TABLE IF EXISTS "USERS";

CREATE TABLE IF NOT EXISTS "USERS"
(
    id integer NOT NULL,
    name text NOT NULL,
    CONSTRAINT users_id_pk PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS "HOSTS"
(
    id integer NOT NULL,
    CONSTRAINT hosts_id_pk PRIMARY KEY (id),
    CONSTRAINT id_fk FOREIGN KEY (id) REFERENCES "USERS" (id) 
);

CREATE TABLE IF NOT EXISTS "GUESTS"
(
    id integer NOT NULL,
    CONSTRAINT guests_id_pk PRIMARY KEY (id),
    CONSTRAINT id_fk FOREIGN KEY (id) REFERENCES "USERS" (id)
);


CREATE TABLE IF NOT EXISTS "ROOMS"
(
    id integer NOT NULL,
    host_id integer NOT NULL,
    name text NOT NULL,
    residents smallint NOT NULL,
    price money NOT NULL,
    aircondition boolean NOT NULL,
    refrigerator boolean NOT NULL,
    CONSTRAINT rooms_id_pk PRIMARY KEY (id),
    CONSTRAINT host_id_fk FOREIGN KEY (host_id) REFERENCES "HOSTS" (id)
);

CREATE TABLE IF NOT EXISTS "RESERVATIONS"
(
    guest_id integer NOT NULL,
    room_id integer NOT NULL,
    CONSTRAINT guest_id_room_id_pk PRIMARY KEY (guest_id, room_id),
    CONSTRAINT guest_id_fk FOREIGN KEY (guest_id) REFERENCES "GUESTS" (id),
    CONSTRAINT room_id_fk FOREIGN KEY (room_id)  REFERENCES "ROOMS" (id)
);



DELETE FROM "RESERVATIONS";
DELETE FROM "ROOMS";
DELETE FROM "GUESTS";
DELETE FROM "HOSTS";
DELETE FROM "USERS";

INSERT INTO "USERS" (id, name) VALUES (1, 'Host and Guest 1');
INSERT INTO "USERS" (id, name) VALUES (2, 'Guest 2');
INSERT INTO "USERS" (id, name) VALUES (3, 'Host and Guest 3');

INSERT INTO "HOSTS" (id) VALUES (1);
INSERT INTO "HOSTS" (id) VALUES (3);

INSERT INTO "GUESTS" (id) VALUES (1);
INSERT INTO "GUESTS" (id) VALUES (2);
INSERT INTO "GUESTS" (id) VALUES (3);

INSERT INTO "ROOMS" (id, host_id, name, residents, price, aircondition, refrigerator) VALUES (1, 1, 'Room 1', 1, 300, true, true);
INSERT INTO "ROOMS" (id, host_id, name, residents, price, aircondition, refrigerator) VALUES (2, 1, 'Room 2', 1, 100, false, false);
INSERT INTO "ROOMS" (id, host_id, name, residents, price, aircondition, refrigerator) VALUES (3, 3, 'Room 3', 1, 200, false, true);

INSERT INTO "RESERVATIONS" (guest_id, room_id) VALUES (1, 3);
INSERT INTO "RESERVATIONS" (guest_id, room_id) VALUES (2, 1);
INSERT INTO "RESERVATIONS" (guest_id, room_id) VALUES (2, 2);

SELECT u.id AS user_id, u.name AS user_name
FROM "USERS" u
JOIN "RESERVATIONS" r ON u.id = r.guest_id
GROUP BY u.id, u.name
ORDER BY COUNT(*) DESC
LIMIT 1;
