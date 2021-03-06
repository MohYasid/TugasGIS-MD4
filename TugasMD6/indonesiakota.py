import mapnik
m = mapnik.Map(600,300)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'), 1)
line_symbolizer.stroke_width = 10.0



r.symbols.append(line_symbolizer)

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[NAME]'), 'DejaVu Sans Bold',2,mapnik.Color('black'))
basinsLabels.halo_fill = mapnik.Color('yellow')
basinsLabels.halo_radius = 2
r.symbols.append(basinsLabels)


point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
r.symbols.append(point_sym)

s.rules.append(r)

highlight = mapnik.PolygonSymbolizer()
highlight.fill = mapnik.Color('red')
netherlands = mapnik.Rule()
netherlands.filter = mapnik.Expression("[NAME] = 'Netherlands'")
netherlands.symbols.append(highlight)
s.rules.append(netherlands)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="Natural_Earth/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds 
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()

s = mapnik.Style()
r = mapnik.Rule()

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
r.symbols.append(point_sym)

m.append_style('My Style2',s)
ds = mapnik.Shapefile(file="shp/indonesiakota/indonesiakota.shp")
layer = mapnik.Layer('indonesiakota')
layer.datasource = ds 
layer.styles.append('My Style2')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

mapnik.render_to_file(m,'indonesiakota.pdf', 'pdf')
print "rendered image to 'indonesiakota.pdf'"
