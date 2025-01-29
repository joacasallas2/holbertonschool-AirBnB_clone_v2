USE hbnb_dev_db;
SET FOREIGN_KEY_CHECKS = 0;  -- Desactivar temporalmente la comprobación de claves foráneas
DROP TABLE IF EXISTS 
    amenities, 
    cities, 
    places, 
    reviews, 
    states, 
    users, 
    place_amenity;  -- Aquí puedes agregar todas las tablas que deseas borrar
SET FOREIGN_KEY_CHECKS = 1;  -- Reactivar la comprobación de claves foráneas
