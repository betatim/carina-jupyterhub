import re
from os.path import join as pjoin
import pdb

from tornado import gen

import docker
from docker.errors import APIError

from dockerspawner import DockerSpawner


class CarinaSpawner(DockerSpawner):
    @property
    def client(self):
        carina_dir = self.authenticator.docker_env_dir
        tls_config = docker.tls.TLSConfig(
            client_cert=(pjoin(carina_dir, 'cert.pem'),
                         pjoin(carina_dir, 'key.pem')),
            ca_cert=pjoin(carina_dir, 'ca.pem'),
            verify=pjoin(carina_dir, 'ca.pem'),
            # XXX why does True not work??
            assert_hostname=False)
        with open(pjoin(carina_dir, 'docker.env')) as f:
            env = f.read()
        docker_host = re.findall("DOCKER_HOST=tcp://(\d+\.\d+\.\d+\.\d+:\d+)", env)[0]
        docker_host = 'https://' + docker_host
        client = docker.Client(version='auto', tls=tls_config, base_url=docker_host)
        return client

    @gen.coroutine
    def get_container(self):
        if not self.container_id:
            return None

        self.log.debug("Getting container: %s", self.container_id)
        try:
            container = yield self.docker(
                'inspect_container', self.container_id
            )
            self.container_id = container['Id']
        except APIError as e:
            if e.response.status_code == 404:
                self.log.info("Container '%s' is gone", self.container_id)
                container = None
                # my container is gone, forget my id
                self.container_id = ''
            else:
                raise
        return container

    @gen.coroutine
    def start(self, image=None):
        yield super(CarinaSpawner, self).start(
            image=image,
            extra_host_config={'port_bindings': {8888: 8888}},
        )

        container = yield self.get_container()
        if container is not None:
            node_name = container['Node']['IP']
            self.user.server.ip = node_name
            self.log.info("{} was started on {} ({}:{})".format(
            self.container_name, node_name, self.user.server.ip, self.user.server.port))

        
