df = None

# a. bar plots
def horizontal_count_plot(title, var, hue=None, ddata=df, order=None, dodge=False):
    order = order if order is not None else ddata[var].value_counts().index 
    sns.countplot(y=var, hue=hue, data=ddata, dodge=dodge, order=order ).set_title( title)
    
# b. helper @ facet grid bar plots 
def cplot(x, **kwargs):
    sns.countplot(y=x,  **kwargs, palette= sns.husl_palette(9, s=0.7 ))#.set_title( title )
    
# c. facetgrid
def facet_grid(title, var, col, ptype=cplot, ddata=df, order=None, **kwargs):
    order = order if order is not None else ddata[var].value_counts().index 
    g = sns.FacetGrid(col=col, col_wrap=3, size=4, aspect=1.25, data=ddata)
    fg = g.map( ptype, var, order=order)

# d.
def swarm_grouped(title, var_x, var_y, ls_grpby, ddata=df):
    dtmp = ddata.groupby( ls_grpby).size().reset_index()
    sns.swarmplot(x=var_x, y=var_y, data=ddata).set_title( title ) 
    
# e. show in grid
def show_in_grid(ncolz, sharex=True):
    fig, ax = plt.subplots( ncols=ncolz, figsize=(20.0, 9.0), sharex=sharex)
    
    fig.tight_layout()
    
