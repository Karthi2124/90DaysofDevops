const express = require("express");
const { Client } = require("pg");
const redis = require("redis");

const app = express();

const PORT = 5000;

const dbClient = new Client({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  port: 5432,
});

const redisClient = redis.createClient({
  url: `redis://${process.env.REDIS_HOST}:6379`,
});

app.get("/", async (req, res) => {
  try {

    // PostgreSQL Connection
    await dbClient.connect();

    const dbResult = await dbClient.query("SELECT NOW()");

    // Redis Connection
    await redisClient.connect();

    await redisClient.set("message", "Redis is working!");

    const redisMessage = await redisClient.get("message");

    res.send(`
      <h1>Docker Compose Advanced</h1>

      <h2>PostgreSQL Connected</h2>
      <p>${dbResult.rows[0].now}</p>

      <h2>Redis Connected</h2>
      <p>${redisMessage}</p>
    `);

  } catch (error) {

    console.error(error);

    res.status(500).send("Error connecting services");

  } finally {

    await dbClient.end();

    await redisClient.disconnect();

  }
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});