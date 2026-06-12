from search_service import (
    get_search_intelligence
)

results = get_search_intelligence(
    "protein snacks"
)

print(results[:3])