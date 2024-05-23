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

<h1>TODO!!</h1>

## User manual

### 1. Device registration

To obtain login credentials for the web application interface, firstly, you should register your device via the instance of client application. Follow these steps to achieve such result:

<h1>TODO!!</h1>

### 2. Using web interface to manage scripts

Once you have logged in with the provided credentials, the script managing dashboard can be accessed. As for now you are able to:

- Create new scripts with the default contents using **"Add script button"** on the top of the page.
- Editing existing scripts' contents using the respective **"Edit script"** buttons.
- Launching scripts on the respective remote device, which you have used for registration using **"Launch script"**.

### 3. Remote script execution guide

For the **"Launch script"** button to actually execute the script on a remote device, the following steps need to be performed using the client application on the said device in advance:

<h1>TODO!!</h1>
