c = get_config()

c.JupyterHub.authenticator_class = 'carinahub.CarinaAuth'

c.JupyterHub.spawner_class = 'carinahub.CarinaSpawner'
c.Spawner.use_docker_client_env = True
c.Spawner.container_ip = '192.168.99.100'
c.Spawner.remove_containers = True

from IPython.utils.localinterfaces import public_ips
c.JupyterHub.ip = public_ips()[0]
c.JupyterHub.hub_ip = public_ips()[0] 
c.JupyterHub.hub_api_ip = public_ips()[0]
