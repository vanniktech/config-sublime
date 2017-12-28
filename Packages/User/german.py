import sublime, sublime_plugin

class German(sublime_plugin.TextCommand):
	def run(self, edit):
		self.search_replace(edit, "oe", "ö")
		self.search_replace(edit, "Oe", "Ö")
		self.search_replace(edit, "ae", "ä")
		self.search_replace(edit, "Ae", "Ä")
		self.search_replace(edit, "ue", "ü")
		self.search_replace(edit, "Ue", "Ü")

	def search_replace(self, edit, search, replace):
		regions = self.view.find_all(search)

		for region in reversed(regions):
			self.view.replace(edit, region, replace)