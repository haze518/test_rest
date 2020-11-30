from aiohttp import web

from app.handlers import limits_list, limits_client, create_limit


def setup_routes(app: web.Application):
    app.router.add_post("/limits", create_limit)
    app.router.add_get("/limits", limits_list)
    app.router.add_get("/limits/client/{client_id:\d+}", limits_client)