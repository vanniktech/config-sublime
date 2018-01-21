import sublime
import sublime_plugin

class MarkdownPreviewGithubCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.run_all_views()

  def run_all_views(self):
    for view in sublime.active_window().views():
      self.process(view)

  def process(self, view):
    if view.file_name().endswith('.md'):
      view.run_command("markdown_preview", { "target": "browser", "parser": "github" })