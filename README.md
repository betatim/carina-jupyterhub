# carina-jupyterhub

[Jupyterhub](https://github.com/jupyter/jupyterhub) backed by [carina](https://getcarina.com)!


# Wat?

`carina-jupyterhub` allows you to host a jupyterhub instance where the users bring
their own computing power. You host the jupyterhub frontend, and your
users bring the computing power. Amazing!


# Impress your friends

To setup your own jupyterhub frontend hosted on carina:

 1. Create a new cluster on [getcarina.com](https://getcarina.com)
 1. Install and configure the [Carina CLI](https://github.com/getcarina/carina) with your Carina username and API key.
 1. Run `eval $(carina env name-of-your-cluster)` to set up your environment.
 1. `docker run --net=host -ti --rm -p 8000 betatim/carina-jupyterhub:25112015 bash`
 1. In the container modify `jupyterhub_config.py` with ```sed -i -e "s/public_ips()\[0\]/\'`ip addr list eth0 |grep "inet "|cut -d' ' -f6|cut -d/ -f1`'/g" jupyterhub_config.py```
    This replaces `public_ips()[0]` with the public IP of your cluster in `jupyterhub_config.py`
 1. start jupyterhub: `jupyterhub`. This will eventually print
    `JupyterHub is now running at http://SomeIPAddress:8000/`. Congratulations, you now running
    `jupyterhub` on a carina cluster!
 
To use the service you just built:

 1. Create a second carina cluster, and download the access credentials using the "Get Access" button in the web UI.
 1. Visit `http://SomeIPAddress:8000` enter a short username, and upload the credentials file of your second
    cluster as the *Credentials file*
 1. Share `http://SomeIPAddress:8000` with your friends (they have to repeat these last three steps)!


# Be safe out there! 

While not an immediate threat to your health, please think carefully
about the security implications of running untrusted code, giving
away credentials to computing resources, etc before doing any of the
above.
