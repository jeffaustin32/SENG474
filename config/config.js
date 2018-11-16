const config = {
    ENV: process.env.NODE_ENV,
    PORT: process.env.PORT || 3200,
    DATABASE_URL: process.env.DATABASE_URL || 'postgres://'
}

module.exports = config;