CREATE DATABASE news;

CREATE TABLE news_articles (
    id SERIAL PRIMARY KEY,
    source VARCHAR(255),
    author VARCHAR(255),
    title TEXT,
    description TEXT,
    content TEXT,
    url VARCHAR(255),
    published_at TIMESTAMP
);
