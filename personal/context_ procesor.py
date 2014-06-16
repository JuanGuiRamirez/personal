

def crearMenu( request ):
    
    menus = { 'menu' : [
                { 'name' : 'Inicio', 'url' : '#' },
                { 'name' : 'Experiencia', 'url' : '#' },
                { 'name' : 'Estudios', 'url' : '#' },
                { 'name' : 'Proyectos', 'url' : '#' },
                { 'name' : 'Empresa', 'url' : '#' },
                { 'name' : 'Contacto', 'url' : '#' },               
              
              ]}
    
    for item in menus['menu']:
        if request.path == item['url']:
            item['active'] = True        
    return menus   

   