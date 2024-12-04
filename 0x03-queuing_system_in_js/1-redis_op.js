import {createClient} from 'redis';

//  create a redis client

const client = createClient();
// Log success or error messages based on the connection status.

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

// open the connection
client.connect();