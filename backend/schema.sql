-- This script can be used to manually create the necessary table in your MySQL database.
-- Make sure you have created a database first, for example:
-- CREATE DATABASE codequeryportal;
-- USE codequeryportal;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    picture VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
