from src.apis import app
from src.apis.v1_0.web.check_service import checking_service_mod
from src.apis.v1_0.web.task import task_service_mod
from src.apis.v1_0.web.staff import staff_service_mod

v1_0_url_prefix = '/api/v1.0'

app.register_blueprint(checking_service_mod, url_prefix=v1_0_url_prefix)
app.register_blueprint(task_service_mod, url_prefix=v1_0_url_prefix)
app.register_blueprint(staff_service_mod, url_prefix=v1_0_url_prefix)

