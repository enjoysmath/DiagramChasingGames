from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from diagram_chasing_games.http_tools import render_error
from database.models import Diagram

@login_required
def diagram_editor(request, diagram_name:str):
    try: 
        given_theorems = Diagram.nodes
        
        context = {
            'diagram_name': diagram_name,
            'given_theorems': given_theorems,
        }
        return render(request, 'diagram_editor.html', context)
    
    except Exception as e:
        return render_error(request, excep=e)


#@login_required
#def create_new_diagram(request):
    #diagram = Diagram.our_create(name='', checked_out_by=request.user.username)
    #session = request.session
    
    #if 'diagram ids' not in session:
        #session['diagram ids'] = [diagram.uid]
    #else:
        #if diagram.uid not in session['diagram ids']:
            #session['diagram ids'].append(diagram.uid)
            #session.save()

    #diagrams = []
    
    ##for diagram_id in session['diagram ids']:
        ##diagram = get_model_by_uid(Diagram, uid=diagram_id)
        ##diagrams.append(diagram)
        
    #context={
        #'diagram_id': diagram.uid,
        #'diagrams' : diagrams,
    #} 
                
    #return render(request, 'create_diagram.html', context)