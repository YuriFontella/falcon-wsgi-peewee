class SuffixResource:
    def on_get_all(self, req, resp):
        resp.text = 'all'

    def on_get_list(self, req, resp):
        resp.text = 'list'