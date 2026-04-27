BEGIN;

CREATE TABLE job_clusters (
    id smallint GENERATED ALWAYS AS IDENTITY,
    job_title TEXT NOT NULL,
    cluster TEXT NOT NULL
);

INSERT INTO job_clusters (job_title, cluster) VALUES
    -- Data & AI
    ('AI Engineer', 'Data & AI'),
    ('Machine Learning Engineer', 'Data & AI'),
    ('Data Scientist', 'Data & AI'),
    ('Data Analyst', 'Data & AI'),
    
    -- Software Engineering
    ('Software Engineer', 'Software Engineering'),
    ('Backend Developer', 'Software Engineering'),
    ('Frontend Developer', 'Software Engineering'),
    
    -- Cloud & DevOps
    ('Cloud Engineer', 'Cloud & DevOps'),
    ('DevOps Engineer', 'Cloud & DevOps'),
    
    -- Product & Strategy
    ('Product Manager', 'Product & Strategy'),
    ('Business Analyst', 'Product & Strategy'),
    
    -- Security
    ('Cybersecurity Analyst', 'Security');

COMMIT;