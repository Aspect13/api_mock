from flask import request

from pylon.core.tools import log
from tools import api_tools, db, serialize, auth

from pydantic import ValidationError


class API(api_tools.APIBase):
    url_params = [
        '<int:project_id>',
    ]

    def post(self, project_id: int, **kwargs):
        data = dict(request.json)
        data['project_id'] = project_id
        try:
            if not data.get('user_id'):
                data['user_id'] = auth.current_user().get("id")
            from ....notifications.models.pd.notification import NotificationCreateModel, NotificationBaseModel
            try:
                parsed = NotificationCreateModel.parse_obj(data)
            except ValidationError as e:
                return e.errors(), 400

            self.module.context.event_manager.fire_event('notifications_stream', parsed.dict())

            return serialize(parsed), 201
        except Exception as e:
            return {'error': str(e), 'payload': data}, 400
