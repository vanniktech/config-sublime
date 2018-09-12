import sublime, sublime_plugin

class German(sublime_plugin.TextCommand):
	def run(self, edit):
		self.search_replace(edit, "oe", "ö")
		self.search_replace(edit, "Oe", "Ö")
		self.search_replace(edit, "ae", "ä")
		self.search_replace(edit, "Ae", "Ä")
		self.search_replace(edit, "ue", "ü")
		self.search_replace(edit, "Ue", "Ü")

		# Correct some of the ones we didn't exclude.
		self.search_replace(edit, "Neü", "Neue")
		self.search_replace(edit, "neü", "neue")
		self.search_replace(edit, "eventüll", "eventuell")
		self.search_replace(edit, "Eventüll", "Eventuell")
		self.search_replace(edit, "söben", "soeben")
		self.search_replace(edit, "Söben", "Soeben")
		self.search_replace(edit, "aktüllen", "aktuellen")
		self.search_replace(edit, "Aktüllen", "Aktuellen")
		self.search_replace(edit, "steür", "steuer")
		self.search_replace(edit, "Steür", "Steuer")
		self.search_replace(edit, "Blütooth", "Bluetooth")
		self.search_replace(edit, "blütooth", "bluetooth")
		self.search_replace(edit, "daürt", "dauert")
		self.search_replace(edit, "Daürt", "Dauert")
		self.search_replace(edit, "baün", "bauen")
		self.search_replace(edit, "Baün", "Bauen")
		self.search_replace(edit, "schaün", "schauen")
		self.search_replace(edit, "Schaün", "Schauen")
		self.search_replace(edit, "individüll", "individuell")
		self.search_replace(edit, "Individüll", "Individuell")
		self.search_replace(edit, "vertraün", "vertrauen")
		self.search_replace(edit, "Vertraün", "Vertrauen")

		# ß cases.
		self.search_replace(edit, "weiss", "weiß")
		self.search_replace(edit, "Weiss", "Weiß")
		self.search_replace(edit, "grüsse", "grüße")
		self.search_replace(edit, "Grüsse", "Grüße")
		self.search_replace(edit, "grösse", "größe")
		self.search_replace(edit, "Grösse", "Größe")

	def search_replace(self, edit, search, replace):
		regions = self.view.find_all(search)

		for region in reversed(regions):
			self.view.replace(edit, region, replace)