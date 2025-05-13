# filters.py
class FilterHandler:
    def __init__(self):
        self.next = None

    def set_next(self, handler):
        self.next = handler
        return handler

    def handle(self, pets):
        if self.next:
            return self.next.handle(pets)
        return pets


class TypeFilter(FilterHandler):
    def handle(self, pets):
        print("Apply filter by type? y/n")
        if input().lower() == 'y':
            available_types = set([p.type.capitalize() for p in pets])
            print("Available types:", ', '.join(available_types))
            chosen = input("Choose type: ").capitalize()
            pets = [p for p in pets if p.type.capitalize() == chosen]
        return super().handle(pets)


class ColorFilter(FilterHandler):
    def handle(self, pets):
        print("Apply filter by color? y/n")
        if input().lower() == 'y':
            available_colors = set([p.color.capitalize() for p in pets])
            print("Available colors:", ', '.join(available_colors))
            chosen = input("Choose color: ").capitalize()
            pets = [p for p in pets if p.color.capitalize() == chosen]
        return super().handle(pets)


class SizeFilter(FilterHandler):
    def handle(self, pets):
        print("Apply filter by size? y/n")
        if input().lower() == 'y':
            available_sizes = set([p.size.capitalize() for p in pets])
            print("Available sizes:", ', '.join(available_sizes))
            chosen = input("Choose size: ").capitalize()
            pets = [p for p in pets if p.size.capitalize() == chosen]
        return super().handle(pets)


class GenderFilter(FilterHandler):
    def handle(self, pets):
        print("Apply filter by gender? y/n")
        if input().lower() == 'y':
            available_genders = set([p.gender.capitalize() for p in pets])
            print("Available genders:", ', '.join(available_genders))
            chosen = input("Choose gender: ").capitalize()
            pets = [p for p in pets if p.gender.capitalize() == chosen]
        return super().handle(pets)


def build_filter_chain():
    
    type_filter = TypeFilter()
    color_filter = ColorFilter()
    size_filter = SizeFilter()
    gender_filter = GenderFilter()

    type_filter.set_next(color_filter).set_next(size_filter).set_next(gender_filter)
    return type_filter
