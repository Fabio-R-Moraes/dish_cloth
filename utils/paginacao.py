import math
from django.core.paginator import Paginator

def make_pagination(request, cloth_query, quantity_page):
    try:
        actual_page = int(request.GET.get('page', 1))
    except ValueError:
        actual_page = 1

    paginador = Paginator(cloth_query, quantity_page)
    pagina_objeto = paginador.get_page(actual_page)
    page_range = make_pagination_range(
        paginador.page_range,
        4,
        actual_page,
    )

    return pagina_objeto, page_range

def make_pagination_range(
        page_range,
        quantity,
        actual_page,
):
    middle_range = math.ceil(quantity / 2)
    initial_range = actual_page - middle_range
    final_range = actual_page + middle_range
    page_total = len(page_range)

    initial_range_offset = abs(initial_range) if initial_range < 0 else 0

    if initial_range < 0:
        initial_range = 0
        final_range += initial_range_offset

    if final_range >= page_total:
        initial_range = initial_range - abs(page_total - final_range)

    pagination = page_range[initial_range:final_range]

    return {
        'pagination': pagination,
        'page_range': page_range,
        'quantity': quantity,
        'actual_page': actual_page,
        'page_total': page_total,
        'initial_range': initial_range,
        'final_range': final_range,
        'first_page_out_of_range': actual_page > middle_range,
        'last_page_out_of_range': final_range < page_total,
    }
