from flask import request

from pylon.core.tools import log
from tools import api_tools, auth, config as c
import random


def enrich_user(user: dict, roles: list) -> None:
    user['roles'] = roles
    if user['last_login']:
        user['last_login'] = user['last_login'].isoformat(timespec='seconds')
    user['avatar'] = None
    user['level'] = random.randint(1, 100)
    user['exp_current'] = random.randint(1, 200)
    user['exp_next'] = 300
    user['rewards'] = random.randint(0, 10)
    user['likes'] = random.randint(0, 100000)
    user['prompts'] = random.randint(0, 100)
    user['contributions'] = random.randint(0, 100)


class API(api_tools.APIBase):
    url_params = [
        '<int:project_id>',
        '<int:project_id>/<int:user_id>',
    ]

    def get(self, project_id: int, user_id: int = None, **kwargs):
        if user_id:
            user = auth.list_users(user_ids={user_id})[0]
            roles = self.module.context.rpc_manager.call.admin_get_user_roles(project_id, user_id)
            roles = [r['name'] for r in roles]
            enrich_user(user, roles)
            result = user
        else:
            project_users = self.module.context.rpc_manager.call.admin_get_users_roles_in_project(
                project_id,
                filter_system_user=True
            )
            all_users = auth.list_users(user_ids=set(project_users.keys()))

            for user in all_users:
                roles = project_users.pop(user['id'], [])
                enrich_user(user, roles)
            result = all_users

        return result, 200
