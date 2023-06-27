from src.controllers.suffix import SuffixResource

suffix = SuffixResource()

def routes(app):
    app.add_route('/all', suffix, suffix='all')
    app.add_route('/list', suffix, suffix='list')