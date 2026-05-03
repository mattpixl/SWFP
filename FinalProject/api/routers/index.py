from . import (
    orders,
    order_details,
    customer,
    menu,
    promotion,
    recipes,
    resource,
    review,
    sandwiches,
)

def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customer.router)
    app.include_router(menu.router)
    app.include_router(promotion.router)
    app.include_router(recipes.router)
    app.include_router(resource.router)
    app.include_router(review.router)
    app.include_router(sandwiches.router)