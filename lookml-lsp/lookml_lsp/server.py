from pygls.capabilities import COMPLETION
from pygls.server import LanguageServer
from pygls.lsp import CompletionItem, CompletionList, CompletionOptions, CompletionParams

class LookMLLanguageServer(LanguageServer):
    def __init__(self):
        super().__init__()


lookml_server = LookMLLanguageServer()


@lookml_server.feature(COMPLETION, CompletionOptions(trigger_characters=[',']))
def completions(params: CompletionParams):
    """Returns completion items."""
    return CompletionList(
        is_incomplete=False,
        items=[
            CompletionItem(label='"'),
            CompletionItem(label='['),
            CompletionItem(label=']'),
            CompletionItem(label='{'),
            CompletionItem(label='}'),
        ]
    )