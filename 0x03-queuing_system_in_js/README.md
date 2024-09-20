## 0x03. Queuing System in JS

## Requirements
- Redis 7.2.4 Stable

| File Name | Description     |
| ------------ | ------------    |
| `0-redis_client.js` | Connects to Redis server and logs connection status |
| `1-redis_op.js` | Performs Redis operations using callbacks |
| `2-redis_op_async.js` | Performs Redis operations using async/await |
| `4-redis_advanced_op.js` | Stores hash values in Redis |
| `5-subscriber.js` | Redis subscriber that listens for messages |
| `5-publisher.js` | Redis publisher that sends messages |
| `6-job_creator.js` | Creates jobs for a queue |
| `6-job_processor.js` | Processes jobs from a queue |
| `7-job_creator.js` | Creates jobs with additional data |
| `7-job_processor.js` | Processes jobs with progress tracking |
| `8-job.js` | Job creation function with custom options |
| `8-job-main.js` | Tests the job creation function |
| `9-stock.js` | Express app with Redis for product stock management |
| ------------ | ----------------- |
| `100-seats.js` | Express app with Redis for managing cinema seats |
