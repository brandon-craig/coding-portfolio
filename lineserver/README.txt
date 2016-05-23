Question:
How does your system work?

Answer: 
This webservice runs on NodeJS (ver. 4.2.6) + Express (ver. 4.13.4). The service listens on port 3000 and implements the /lines API call. All other endpoints will return a 404 status code. Upon startup the service will begin asynchronously reading into memory the specified file that is defined in its "path" variable. By reading the file into memory on startup the service can avoid excessive Disk I/O operations that take up CPU and allows for faster serve times as in-memory data is more quickly accessed than data on Disk. Internally the service is using an array to store the data from the file. Arrays have constant time lookup which made them attractive to store this data and the line numbers of the file are directly mapped to the index in the array which made implementation simple. 

The service implments the GET /lines API endpoint. 3 status codes are possible in the response. Status code 200 if the request is sent to GET /lines and the requested line number exists. Status code 413 if the request is sent to /lines but the line number is either less than one or out of bounds of the file. Status code 404 if the request is sent to GET /lines with no line number provided or if the the request is sent to an endpoint other than GET /lines.

Question:
How will your system perform with a 1GB file? a 10 GB file? a 100 GB file?

Answer:
Environment assumptions:
100 MiB text file
Ubuntu 16.04 VM w/ 1 CPU 4 Cores and 4 GiB Memory
200 Requests per second per client
100 Users

1 GiB file: Median Latency: ~70 ms
10 GiB file: Median Latency: ~70 ms
100 GiB file: Median Latency: ~100 ms


Question:
How will your system perform with 100 users? 10000 users? 1000000 users?

Answer:
Environment assumptions:
100 MiB text file
Ubuntu 16.04 VM w/ 1 CPU 4 Cores and 4 GiB Memory
200 Requests per second per client

100 Users: Median Latency: ~70 ms
10000 Users: Median Latency: ~130 ms
1000000 Users: Median Latency: ~135 ms

Question:
What documentation, websites, papers, etc did you consult in doing this assignment?

Answer:
https://artillery.io/
https://nodejs.org/en/
http://expressjs.com/

Question:
What third-party libraries or other tools does the system use? How did you choose each library or framework you used?

Answer:
NodeJS/NPM: I chose NodeJS for its simplicity, ease-of-use, and ability to handle thousands of concurrent users at once. It is easy to get a webservice up and running quickly and since the amount of code required is small the number of potential bugs is reduced.

Express: The main reason for express was its ability to simplify the handling of routes. NodeJS on its own takes more work to get proper routing to work. Express makes routing easy with a very idiomatic approach to routes.

Artillery: Artillery is a load testing framework that allows you to do custom test scripts. I decided to use that since it required low amounts of configuration and is easily installable through npm.

Question:
How long did you spend on this exercise? If you had unlimited more time to spend on this, how would you spend it and how would you prioritize each item?

Answer:
On coding and testing I spent approximately 3-4 hours. Outside of the coding and testing, I spent approximately 2 hours researching the capabilities, syntaxes, and frameworks of other languages for implementing a webservice that could handle concurrency well. I looked at Ruby, Python, and Scala outside of NodeJS. I found NodeJS to be the best solution given the scale of the exercise.

If I had unlimited time:

1. I would add an admin page that would allow an admin to upload a file to the server and hot swap in the new file. 

Depending on how pretty I wanted to make it I would estimate one day. The admin page does not need to be fancy and implementing the hot swap functionality on its own would not be a huge lift. 

2. I would containerize the application using Docker Engine and deploy the application to AWS on CoreOS and run Kubernetes to do my container cluster orchestration so I would have high availability. 

I would spend a few days on this so I could test that the application is actually highly available and that the replication is working correctly. 

Question:
If you were to critique your code, what would you have to say about it?

Answer:
Could be broken up into a microservice architecture. Currently its a monolith that handles everything from one service where if I wanted to I could break this up into a smaller piece that specifically only handles the lines API. Makes the code more modular.