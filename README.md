# carina-jupyterhub

[Jupyterhub](https://github.com/jupyter/jupyterhub) backed by [carina](https://getcarina.com)!


# Wut?

This allows you to host a jupyterhub instance where the users bring
their own computing power. You host the frontend to jupyterhub, your
users bring the computing power. Amazing!


# Wat?

Head over to [getcarina.com](https://getcarina.com), register for an
account, and fire up a cluster. Click "Get access" to download a
zipfile containing all the information on how to connect to your
cluster. This is your *auth file*.


# Do it yourself

To setup your own jupyterhub frontend running on carina:

 * create a new cluster on [getcarina.com](https://getcarina.com)
 * download and unzip the access file
 * `source docker.env` from the unzipped access file
 * `docker run --net=host -ti --rm -p 8000 betatim/carina-jupyterhub:24112015 bash`
 * find the clusters public IP: `ifconfig eth0`
 * modify `jupyterhub_config.py`, replacing `public_ips()[0]` with the public IP
   of your cluster:
   ```
c.JupyterHub.ip = '172.99.78.68'#public_ips()[0]
c.JupyterHub.hub_ip = '172.99.78.68'#public_ips()[0]
c.JupyterHub.hub_api_ip = '172.99.78.68'#public_ips()[0]
   ```
 * start jupyterhub: `jupyterhub`
 * open `http://IP:8000` in a browser
 * create a second carina cluster, download the access file
 * enter a short username, and upload the zipfile for your second
   cluster as the *auth file*


# Security

While not an immediate threat to your health, please think carefully
about the security implications of running untrusted code, giving
away credentials to computing resources, etc before doing any of the
above.
