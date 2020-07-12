# MQTT Quickstart. Set up an MQTT broker and client for your IoT project!
Today we will be discussing how to set up a [MQTT](http://mqtt.org/) broker and client. I will show you a step-by-step guide along with the resources required. Ideally, you should also get a foundational understanding of how a broker and client communicates via MQTT topics, payloads, and publish-subscribe pattern.

![MQTT Communication Flow - By Simon A. Eugster](https://miro.medium.com/max/700/1*PENMRcBBqSNrB3STT_4NTg.jpeg)

# Broker Role
The broker’s main role is to dispatch messages between the clients. Payloads (or messages) will be dispatched to clients which are subscribed to a certain topic, vice versa, clients can publish payloads to specified topics. Take note though that the initiation (CONNECT) comes from the clients whereby the brokers acknowledged the request (CONNACK) to create the session.

# Broker Installation.
For this demo, we will use [RabbitMQ](https://www.rabbitmq.com/) as our broker. It is widely deployed in enterprise because it is open source, lightweight, and intuitive to deploy and manage.
There are various ways to install RabbitMQ, but considering I have done this on a private machine within the network, the straightforward way is to get the .rpm downloaded and installed. If you are on public network and can easily connect to public repositories then you can install by connect to those repo. [Click here for installation options](https://www.rabbitmq.com/download.html)
Note: If you just wanna have a quick play with it without all the hassle. I suggest you install the Windows broker on your local machine. This took me not more than five minutes to install!

# Installing on RPM-based Linux (RedHat Enterprise Linux, CentOS, Fedora, openSUSE)
**Download the .RPM files.** Note: Erlang is a pre-requisite for RabbitMQ. Also consider which CentOS version you have as well as your processor (32-bit or 64-bit)
For Erlang, you can get it from [here](https://www.erlang-solutions.com/resources/download.html). I have used *“esl-erlang_23.0.2–2~centos~7_amd64.rpm”*
For RabbitMQ, you can get the file from [here](https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.5/rabbitmq-server-3.8.5-1.el7.noarch.rpm). I have used *“rabbitmq-server-3.8.5–1.el7.noarch.rpm”*

**Load them into your VM.** You can use any FTP/SFTP client. I personally use [MobaXterm](https://mobaxterm.mobatek.net/), it is free, intuitive and does session management pretty well.

# Install RPM files
    sudo rpm -i esl-erlang_23.0.2-2~centos~7_amd64.rpm
    sudo rpm -i rabbitmq-server-3.8.5-1.el7.noarch.rpm

# ..and verify installation.
    rpm -qa | grep erlang
    rpm -qa | grep rabbit

# Start the service.
    sudo service rabbitmq-server start
# Check the service status.
    sudo service rabbitmq-server status
    
![After running the service status command, we can see that RabbitMQ is active(running)](https://miro.medium.com/max/700/1*GrX-qM8R-TsDXsIAdMZFOQ.jpeg)

**Install the [MQTT plugin](https://www.rabbitmq.com/mqtt.html).** Please note that the default way of communication with RabbitMQ is AQMP (which is another type of message-queueing-dispatch protocol). In this case we have to install MQTT plugin, do not worry though are it is fully supported and in some cases, deemed interoperable.

    rabbitmq-plugins enable rabbitmq_mqtt
    
Afterwards, **check if MQTT ports are open.** From the display below you should see that default MQTT port 1833 is open and listening.

    netstat -tulnp

![Near the bottom, you can see that tcp port 1883 is open.](https://miro.medium.com/max/700/1*1XtIqCLcxRadnMMwsHKIyA.jpeg)

Best practice: **Add user with permissions and strong password** as opposed to using default guest / anonymous. Also, we will use this on our client to connect with the broker later.
    
    sudo rabbitmqctl add_user "{Username}" "{Password}"
    sudo rabbitmqctl set_permissions -p / "{Username}" ".*" ".*" ".*"
    sudo rabbitmqctl set_user_tags "{Username}" development
    
#Test that user is successfully created.

    sudo rabbitmqctl authenticate_user "{Username}" "{Password}"

That’s it! We are now ready to communicate (publish and subscribe) with this broker.

![source](https://miro.medium.com/max/600/1*X44wIqlGd43THtr0DSbEwA.jpeg)

# Client Role
A client runs the MQTT scripts and is configure to connect to the broker. A client can both publish or subscribe to one or more topics for payload distribution. Because of the lightweight nature of MQTT, the client can be a full-fledged computer server, or a micro controller such as a Raspsberry PI).

# Client Configuration
We will use the paho-mqtt library for our client’s code. You can download client code snippets for publish and subscribe. Start with publish, subscribe, and then both.

# Conclusion
Congratulations! Upon completing this demo you now have a solid foundation and understanding of MQTT concepts which are required in deploying a broker and clients in a production environment. I have used it personally in building management systems connecting hundreds of sites with tens of thousands of messages.

Additional note: At present, MQTT this is a preferred protocol in the field of Internet of Things and Smart Buildings because of its scalability, lightweight overhead, and resilient connectivity. Because of these benefits, this will be a norm for select IoT use cases.

Disclaimer: That being said, it is now up to you to extend the knowledge, there are advanced topics which need to be considered, connectivity, redundancy, error handling and management, and logging especially in production.
