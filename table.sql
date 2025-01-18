CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique ID for the account
    username VARCHAR(255),                      -- Username for the account
    domain VARCHAR(255),                        -- Domain (e.g., example.com)
    ip_address VARCHAR(45),                     -- IPv4 or IPv6 address
    application VARCHAR(255),                   -- Application (e.g., WordPress, Citrix)
    port INT,                                   -- Port number (e.g., 443, 3000)
    url_path VARCHAR(255),                      -- URL path (e.g., /login)
    password_hash VARCHAR(255),                 -- Securely hashed password
    tags JSON DEFAULT NULL,                     -- Tags (e.g., ["resolved", "active"])
    url_title VARCHAR(255) DEFAULT NULL,        -- Retrieved page title
    login_form_detected BOOLEAN DEFAULT FALSE,  -- Whether a login form is present
    captcha_required BOOLEAN DEFAULT FALSE,     -- Whether a CAPTCHA is required
    otp_required BOOLEAN DEFAULT FALSE,         -- Whether OTP is required
    is_parked BOOLEAN DEFAULT NULL,             -- Whether the domain is parked
    is_accessible BOOLEAN DEFAULT NULL,         -- Whether the URL is accessible
    breach_detected BOOLEAN DEFAULT NULL        -- Whether the account is part of a breach
);
