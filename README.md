# carina-jupyterhub

[Jupyterhub](https://github.com/jupyter/jupyterhub) backed by [carina](https://getcarina.com)!


# Wut?

This allows you to host a jupyterhub instance where the users bring
their own computing power. You host the frontend to jupyterhub, your
users bring the computing power.


# How

Head over to [getcarina.com](https://getcarina.com), register for an
account, and fire up a cluster. Click "Get access" to download a
zipfile containing all the information on how to connect to your
cluster. This is your *auth file*.

Configure your jupyterhub instance with `CarinaAuth` and
`CarinaSpawner`. Now it will ask you for a name and a auth file.
Use what ever name you like, and upload the *auth file* you
previously downloaded.


# Security

While not an immediate threat to your health, please think carefully
about the security implications of running untrusted code, giving
away credentials to computing resources, etc before doing any of the
above.
