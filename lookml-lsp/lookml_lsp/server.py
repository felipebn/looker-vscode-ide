from pygls.features import COMPLETION
from pygls.server import LanguageServer
from pygls.types import CompletionItem, CompletionList, CompletionOptions, CompletionParams

server = LanguageServer()

@server.feature(COMPLETION, CompletionOptions(trigger_characters=[',']))
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

