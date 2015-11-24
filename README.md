# carina-jupyterhub

[Jupyterhub](https://github.com/jupyter/jupyterhub) backed by [carina](https://getcarina.com)!


# Wut?

This allows you to host a jupyterhub instance where the users bring
their own computing power. You host the frontend to jupyterhub, your
users bring the computing power. Amazing!


# Wat?

Head over to [getcarina.com](https://getcarina.com), register for an
account, and fire up a cluster. Click "Get access" to download a
zipfile with the credentials of your cluster. This is your *auth file*.


# Do it yourself

To setup your own jupyterhub frontend running on carina:

 * create a new cluster on [getcarina.com](https://getcarina.com)
 * download and unzip the credentials
 * `source docker.env` from the unzipped access file
 * `docker run --net=host -ti --rm -p 8000 betatim/carina-jupyterhub:24112015 bash`
 * find the clusters public IP: `ifconfig eth0`
 * modify `jupyterhub_config.py` with ```sed -i -e "s/public_ips()\[0\]/\'`ip addr list eth0 |grep "inet "|cut -d' ' -f6|cut -d/ -f1`'/g" jupyterhub_config.py``` This replaces `public_ips()[0]` with the public IP
   of your cluster
 * start jupyterhub: `jupyterhub`
 * open `http://IP:8000` in a browser
 * create a second carina cluster, download the access file
 * on `http://IP:8000` enter a short username, and upload the credentials file of your second
   cluster as the *auth file*
 * Have fun!


# Security

While not an immediate threat to your health, please think carefully
about the security implications of running untrusted code, giving
away credentials to computing resources, etc before doing any of the
above.
