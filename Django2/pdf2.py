#coding=utf-8
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
pdfmetrics.registerFont(TTFont('song', 'SURSONG.TTF'))
pdfmetrics.registerFont(TTFont('hei', 'SIMHEI.TTF'))

from reportlab.lib import fonts
fonts.addMapping('song', 0, 0, 'song')
fonts.addMapping('song', 0, 1, 'song')
fonts.addMapping('song', 1, 0, 'hei')
fonts.addMapping('song', 1, 1, 'hei')

import copy

from reportlab.platypus import Paragraph, SimpleDocTemplate, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
stylesheet=getSampleStyleSheet()
normalStyle = copy.deepcopy(stylesheet['Normal'])
normalStyle.fontName ='song'
normalStyle.fontSize = 20
story = []
story.append(Paragraph('<b>你好</b>,中文', normalStyle))
doc = SimpleDocTemplate('hello.pdf')
doc.build(story)