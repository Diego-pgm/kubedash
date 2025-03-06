# kubedash

A Python web application that displays Kubernetes pods and their status in a table.

### Prerequisites

- Certificates to authenticate with the Kubernetes API in a `certs` directory on the same path as the program.
- - The certificates need to be named:
    - user.key - User key
    - user.crt - User certificate
    - ca.crt - Verification certificate (taken from the cluster)
- A Kubernetes Role object created on the cluster with authorization to at least watch pods.
- The Kubernetes API URL as an environment variable `KUBEHOST`

### Docker

This application has a Dockerfile to create a Docker container.

- It needs to have the user certificates mounted in the /app/certs volume.
- The port running the app by default is the 5000.

Steps:

1. Build the image.

```
docker build -t kubedash:<tag> .
```

2. Run a container

```
docker run -dti -p 5000:5000 -e "KUBEHOST=https://<kubernetes-api-url>:<port>/api/v1/namespace/default/pods" -v ./certs/:/app/certs kubedash:<tag>
```

If done correctly and the user has the authorization to watch pods in the default namespace it should show the dashboard containing a table with the pods name and their status.