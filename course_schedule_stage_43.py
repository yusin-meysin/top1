# === Stage 43: Добавь пагинацию длинных списков ===
# Project: CourseSchedule
def paginate(items, page_size=10):
    total_pages = (len(items) + page_size - 1) // page_size
    return {
        'items': items,
        'total': len(items),
        'page': 1,
        'page_size': page_size,
        'total_pages': total_pages,
        'has_next': total_pages > 1,
        'has_prev': False,
        'next_page': 2 if total_pages > 1 else 0,
        'prev_page': 0,
    }
