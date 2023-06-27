from src.controllers.suffix import SuffixResource

def routes(app):
    app.add_route('/all', SuffixResource(), suffix='all')
    app.add_route('/list', SuffixResource(), suffix='list')