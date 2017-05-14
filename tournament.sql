-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE player (
	p_id SERIAL PRIMARY KEY,
	p_name VARCHAR(25) NOT NULL,
        total_wins integer DEFAULT 0	
	);

CREATE TABLE matches (
	m_id SERIAL PRIMARY KEY,
	winner INTEGER REFERENCES player (p_id),
	loser INTEGER REFERENCES player (p_id)
	);

CREATE OR REPLACE VIEW rankings AS
	SELECT p.p_id , p.p_name, p.total_wins AS total_wins, count(m.m_id) AS p_rank
	FROM player AS p LEFT JOIN matches AS m
	ON p.p_id = m.winner OR p.p_id = m.loser
GROUP BY p.p_id;
