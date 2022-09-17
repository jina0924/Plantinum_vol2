const mysql = require("mysql2/promise");

const pool = mysql.createPool({
    host: "hostname",
    port : "port",
    user:"user_name",
    password:"pw",
    database:"db_name",
    waitForConnections:true,
    connectionLimit:10,
    queueLimit:0,
});

module.exports = { pool };