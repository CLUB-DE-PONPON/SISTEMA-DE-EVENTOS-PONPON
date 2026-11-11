from fontTools.ttLib import TTFont
from fontTools.subset import Subsetter, Options
from pathlib import Path
import io,json
fonts=[]
for filename in ['DejaVuSans.ttf','DejaVuSans-Bold.ttf']:
 f=TTFont('/usr/share/fonts/truetype/dejavu/'+filename)
 chars=[]
 for b in range(256):
  try: chars.append(ord(bytes([b]).decode('cp1252')))
  except UnicodeDecodeError: chars.append(ord('?'))
 sub=Subsetter(options=Options());sub.populate(unicodes=set(chars));sub.subset(f)
 cmap=f.getBestCmap();scale=1000/f['head'].unitsPerEm
 widths=[round(f['hmtx'].metrics[cmap.get(c,'.notdef')][0]*scale) for c in chars]
 output=io.BytesIO();f.save(output);b=output.getvalue()
 fonts.append(dict(name='DejaVuSans-Bold' if 'Bold' in filename else 'DejaVuSans',hex=b.hex(),length=len(b),widths=widths,bbox=[round(getattr(f['head'],a)*scale) for a in ['xMin','yMin','xMax','yMax']],ascent=round(f['hhea'].ascent*scale),descent=round(f['hhea'].descent*scale)))
Path('dist/pdf-fonts.js').write_text('export const pdfFonts='+json.dumps(fonts,separators=(',',':'))+';\n')
