## Nord color palette
theme = dict(
    # Polar Night
    nord0='#2e3440',
    nord1='#3b4252',
    nord2='#434c5e',
    nord3='#4c566a',
    # Snow Storm
    nord4='#d8dee9',
    nord5='#e5e9f0',
    nord6='#eceff4',
    # Frost
    nord7='#8fbcbb',
    nord8='#88c0d0',
    nord9='#81a1c1',
    nord10='#5e81ac',
    # Aurora
    nord11='#bf616a',
    nord12='#d08770',
    nord13='#ebcb8b',
    nord14='#a3be8c',
    nord15='#b48ead',
)

## Background color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.bg = theme['nord0']

## Bottom border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.bottom = theme['nord0']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.top = theme['nord0']

## Foreground color of completion widget category headers.
## Type: QtColor
c.colors.completion.category.fg = theme['nord5']

## Background color of the completion widget for even rows.
## Type: QssColor
c.colors.completion.even.bg = theme['nord1']

## Background color of the completion widget for odd rows.
## Type: QssColor
c.colors.completion.odd.bg = theme['nord1']

## Text color of the completion widget.
## Type: QtColor
c.colors.completion.fg = theme['nord4']

## Background color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.bg = theme['nord3']

## Bottom border color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.border.bottom = theme['nord3']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.item.selected.border.top = theme['nord3']

## Foreground color of the selected completion item.
## Type: QtColor
c.colors.completion.item.selected.fg = theme['nord6']

## Foreground color of the matched text in the completion.
## Type: QssColor
c.colors.completion.match.fg = theme['nord13']

## Color of the scrollbar in completion view
## Type: QssColor
c.colors.completion.scrollbar.bg = theme['nord1']

## Color of the scrollbar handle in completion view.
## Type: QssColor
c.colors.completion.scrollbar.fg = theme['nord5']

## Background color for the download bar.
## Type: QssColor
c.colors.downloads.bar.bg = theme['nord0']

## Background color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.bg = theme['nord11']

## Foreground color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.fg = theme['nord5']

## Color gradient stop for download backgrounds.
## Type: QtColor
c.colors.downloads.stop.bg = theme['nord15']

## Color gradient interpolation system for download backgrounds.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'none'

## Background color for hints. Note that you can use a `rgba(...)` value
## for transparency.
## Type: QssColor
c.colors.hints.bg = theme['nord13']

## Font color for hints.
## Type: QssColor
c.colors.hints.fg = theme['nord0']

## Font color for the matched part of hints.
## Type: QssColor
c.colors.hints.match.fg = theme['nord10']

## Background color of the keyhint widget.
## Type: QssColor
c.colors.keyhint.bg = theme['nord1']

## Text color for the keyhint widget.
## Type: QssColor
c.colors.keyhint.fg = theme['nord5']

## Highlight color for keys to complete the current keychain.
## Type: QssColor
c.colors.keyhint.suffix.fg = theme['nord13']

## Background color of an error message.
## Type: QssColor
c.colors.messages.error.bg = theme['nord11']

## Border color of an error message.
## Type: QssColor
c.colors.messages.error.border = theme['nord11']

## Foreground color of an error message.
## Type: QssColor
c.colors.messages.error.fg = theme['nord5']

## Background color of an info message.
## Type: QssColor
c.colors.messages.info.bg = theme['nord8']

## Border color of an info message.
## Type: QssColor
c.colors.messages.info.border = theme['nord8']

## Foreground color an info message.
## Type: QssColor
c.colors.messages.info.fg = theme['nord5']

## Background color of a warning message.
## Type: QssColor
c.colors.messages.warning.bg = theme['nord12']

## Border color of a warning message.
## Type: QssColor
c.colors.messages.warning.border = theme['nord12']

## Foreground color a warning message.
## Type: QssColor
c.colors.messages.warning.fg = theme['nord5']

## Background color for prompts.
## Type: QssColor
c.colors.prompts.bg = theme['nord2']

# ## Border used around UI elements in prompts.
# ## Type: String
c.colors.prompts.border = '1px solid ' + theme['nord0']

## Foreground color for prompts.
## Type: QssColor
c.colors.prompts.fg = theme['nord5']

## Background color for the selected item in filename prompts.
## Type: QssColor
c.colors.prompts.selected.bg = theme['nord3']

## Background color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.bg = theme['nord15']

## Foreground color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.fg = theme['nord5']

## Background color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.bg = theme['nord15']

## Foreground color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.fg = theme['nord5']

## Background color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.bg = theme['nord2']

## Foreground color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.fg = theme['nord5']

## Background color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.bg = theme['nord2']

## Foreground color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.fg = theme['nord5']

## Background color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.bg = theme['nord14']

## Foreground color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.fg = theme['nord1']

## Background color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.bg = theme['nord0']

## Foreground color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.fg = theme['nord5']

## Background color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.bg = theme['nord10']

## Foreground color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.fg = theme['nord5']

## Background color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.bg = theme['nord3']

## Foreground color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.fg = theme['nord5']

## Background color of the progress bar.
## Type: QssColor
c.colors.statusbar.progress.bg = theme['nord5']

## Foreground color of the URL in the statusbar on error.
## Type: QssColor
c.colors.statusbar.url.error.fg = theme['nord11']

## Default foreground color of the URL in the statusbar.
## Type: QssColor
c.colors.statusbar.url.fg = theme['nord5']

## Foreground color of the URL in the statusbar for hovered links.
## Type: QssColor
c.colors.statusbar.url.hover.fg = theme['nord8']

## Foreground color of the URL in the statusbar on successful load
## (http).
## Type: QssColor
c.colors.statusbar.url.success.http.fg = theme['nord5']

## Foreground color of the URL in the statusbar on successful load
## (https).
## Type: QssColor
c.colors.statusbar.url.success.https.fg = theme['nord14']

## Foreground color of the URL in the statusbar when there's a warning.
## Type: QssColor
c.colors.statusbar.url.warn.fg = theme['nord12']

## Background color of the tab bar.
## Type: QtColor
c.colors.tabs.bar.bg = theme['nord3']

## Background color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.bg = theme['nord3']

## Foreground color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.fg = theme['nord5']

## Color for the tab indicator on errors.
## Type: QtColor
c.colors.tabs.indicator.error = theme['nord11']

## Color gradient start for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.start = theme['violet']

## Color gradient end for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.stop = theme['orange']

## Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'

## Background color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.bg = theme['nord3']

## Foreground color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.fg = theme['nord5']

# ## Background color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.bg = theme['nord0']

# ## Foreground color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.fg = theme['nord5']

# ## Background color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.bg = theme['nord0']

# ## Foreground color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.fg = theme['nord5']

## Background color for webpages if unset (or empty to use the theme's
## color)
## Type: QtColor
# c.colors.webpage.bg = 'white'
