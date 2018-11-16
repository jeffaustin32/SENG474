const config = require('./config');
const pgp = require('pg-promise')({noLocking:true});
pgp.pg.defaults.ssl = true;
const db = pgp(config.DATABASE_URL);

module.exports = db;