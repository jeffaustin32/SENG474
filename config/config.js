const config = {
    ENV: process.env.NODE_ENV,
    PORT: process.env.PORT || 3200,
    DATABASE_URL: process.env.HEROKU_POSTGRESQL_MAUVE_URL || 'postgres://'
}

module.exports = config;