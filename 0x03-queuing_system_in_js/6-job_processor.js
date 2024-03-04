// Process job with data logged
const kue = require('kue');
const q = kue.createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

q.process(('push_notification_code'), (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});