# EasyAccess Remote MVP

EasyAccess Remote MVP is an initial version of a remote computer management solution designed to provide essential functionalities for users to securely connect to and control their remote devices. It prioritizes core features that deliver immediate value and functionality, allowing developers to test user roles effectively. The MVP is structured to accommodate user needs while ensuring realistic implementation within the project's timeframe.

## Getting started with web application setup

### Prerequisites

- Docker
- Docker Compose

That's all you need :)

### Runnning the app cluster

In the project root directory type:

```docker compose up --build -d```

After that, the application should be running (it takes some time to initialize all of the containers in the cluster, so we ask you to be patient). You can navigate to http://localhost:4200 to access the web view.

### Running the client app

Have 3.0 or later version of Python installed.

The client application executable can be run on windows 10 and up.

## User manual

### 1. Device registration

To obtain login credentials for the web application interface, firstly, you should register your device via the instance of client application. Follow these steps to achieve such result:

- Open the client application via the executable, this generates a unique ID on the first launch.
- Click Register Device. Here you can see your unique ID (this should be saved, but it can also be found in the Persistence folder in a file named UID.txt).
- Enter the desired password in the registration field. Make sure to remember this password!
- Click "register" and if the server connection is good a confirmation of success will appear. Press "Ok".
- Your device is registered!

### 2. Using web interface to manage scripts

Once you have logged in with the provided credentials, the script managing dashboard can be accessed. As for now you are able to:

- Create new scripts with the default contents using **"Add script button"** on the top of the page.
- Editing existing scripts' contents using the respective **"Edit script"** buttons.
- Launching scripts on the respective remote device, which you have used for registration using **"Launch script"**.

### 3. Remote script execution guide

For the **"Launch script"** button to actually execute the script on a remote device, the following steps need to be performed using the client application on the said device in advance:

- Open the client application via the executable.
- If you haven't registered your device already, follow the steps in point 1!
- Press the "connect" button, and enter the same password you did during registration.
- If connection with the server is stable, you'll receive a confirmation of success. Press "Ok".
- The client will connect to the server via the cmd that opens up. Don't manually close this cmd, use the "Disconnect" button to close the connection!
- Your client is ready to reveive and run scripts!
