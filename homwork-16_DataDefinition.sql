DROP TABLE IF EXISTS "RESERVATIONS";
DROP TABLE IF EXISTS "ROOMS";
DROP TABLE IF EXISTS "HOSTS";
DROP TABLE IF EXISTS "GUESTS";
DROP TABLE IF EXISTS "USERS";

CREATE TABLE "USERS"
(
    id integer NOT NULL,
    name text NOT NULL,
    CONSTRAINT users_id_pk PRIMARY KEY (id)
);

CREATE TABLE "HOSTS"
(
    id integer NOT NULL,
    CONSTRAINT hosts_id_pk PRIMARY KEY (id),
    CONSTRAINT id_fk FOREIGN KEY (id) REFERENCES "USERS" (id) 
);

CREATE TABLE "GUESTS"
(
    id integer NOT NULL,
    CONSTRAINT guests_id_pk PRIMARY KEY (id),
    CONSTRAINT id_fk FOREIGN KEY (id) REFERENCES "USERS" (id)
);


CREATE TABLE "ROOMS"
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

CREATE TABLE "RESERVATIONS"
(
    guest_id integer NOT NULL,
    room_id integer NOT NULL,
    CONSTRAINT guest_id_room_id_pk PRIMARY KEY (guest_id, room_id),
    CONSTRAINT guest_id_fk FOREIGN KEY (guest_id) REFERENCES "GUESTS" (id),
    CONSTRAINT room_id_fk FOREIGN KEY (room_id)  REFERENCES "ROOMS" (id)
);
