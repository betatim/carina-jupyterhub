from os.path import join as pjoin
from os.path import split as psplit
from io import BytesIO
import zipfile
from tempfile import mkdtemp

from tornado import gen, web

from jupyterhub.auth import Authenticator


class CarinaAuth(Authenticator):
    custom_html = """
    <form enctype="multipart/form-data" action="login" method="post">
    <label for="username_input">Username:</label>
    <input
      id="username_input"
      type="username"
      autocapitalize="off"
      autocorrect="off"
      class="form-control"
      name="username"
      tabindex="1"
      autofocus="autofocus"
    />
    <label for="zipfile_input">Auth file:</label>
    <input
      id="zipfile_input"
      type="file"
      class="form-control"
      name="zipfile"
      tabindex="2"
    />
    <input
      type="submit"
      id="login_submit"
      class='btn btn-jupyter'
      value='Sign In'
      tabindex="3"
    />
    </form>
    """

    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        if not handler.find_user(username):
            zf = zipfile.ZipFile(BytesIO(handler.request.files['zipfile'][0]['body']))

            cluster_name = psplit(zf.namelist()[0])[0]
            self.docker_env_dir = mkdtemp(suffix='-carinaauth')

            for name in ('docker.env', 'cert.pem', 'ca.pem', 'ca-key.pem', 'key.pem'):
                zf.extract(pjoin(cluster_name, name), path=self.docker_env_dir)

            self.docker_env_dir = pjoin(self.docker_env_dir, cluster_name)

            print(self.docker_env_dir)
            return username

        
