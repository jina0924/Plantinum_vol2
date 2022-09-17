const mysql = require("mysql2/promise");

const pool = mysql.createPool({
    host: "db_server",
    port : "port_num",
    user: "user",
    password: "pw",
    database: "db_name",
    waitForConnections:true,
    connectionLimit:10,
    queueLimit:0,
});

module.exports = { pool };