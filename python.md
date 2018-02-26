# python

- abstractmethods in ABC are not checked to be callable. [link](https://stackoverflow.com/questions/25183424/can-a-python-abstract-base-class-enforce-function-signatures) -- wonder why one would use this anyway then..
- All about decorators https://github.com/hchasestevens/hchasestevens.github.io/blob/master/notebooks/the-decorators-they-wont-tell-you-about.ipynb
- [List all available fonts in matplotlib nicely](http://jonathansoma.com/lede/data-studio/matplotlib/list-all-fonts-available-in-matplotlib-plus-samples/)
```python
import matplotlib.font_manager
from IPython.core.display import HTML

def make_html(fontname):
    return "<p>{font}: <span style='font-family:{font}; font-size: 24px;'>{font}</p>".format(font=fontname)

code = "\n".join([make_html(font) for font in sorted(set([f.name for f in matplotlib.font_manager.fontManager.ttflist]))])

HTML("<div style='column-count: 2;'>{}</div>".format(code))
```
