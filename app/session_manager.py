from wtforms import SelectField, SelectMultipleField

class SessionManager():

    @staticmethod
    def exists_data_for(session,form):
        return form.__name__ in session if isinstance(form,type) else form.__class__.__name__ in session 
    
    @staticmethod
    def store_form_data(session,form,exclude=['csrf_token','submit'],new_select_choices={}):
        data = form.data
        for field in exclude:
            data.pop(field)
        session[form.__class__.__name__] = data
        for field_name, field in form._fields.items():
            if field_name not in exclude and (isinstance(field, SelectField) or isinstance(field, SelectMultipleField)):
                new_options = new_select_choices.get(field_name)
                if new_options:
                    for option in [(value,value) for value in new_options]:
                        if option not in session[form.__class__.__name__+'_choices'][field_name]:
                            session[form.__class__.__name__+'_choices'][field_name].append(option)


    @staticmethod
    def load_form_data(session,form,exclude=[]):
        for field_name, value in session[form.__class__.__name__].items():
            if hasattr(form,field_name) and  field_name not in exclude:
                getattr(form,field_name).data = value
        for field_name, choices in session[form.__class__.__name__+'_choices'].items():
            if hasattr(form, field_name) and (isinstance(form[field_name], SelectField) or isinstance(form[field_name], SelectMultipleField)):
                getattr(form, field_name).choices = choices

    @staticmethod
    def create_form_data(session,form,select_choices={}):
         session[form.__class__.__name__] = {}
         session[form.__class__.__name__+'_choices'] = {}
         for select_field, choices in select_choices.items():
             session[form.__class__.__name__+'_choices'][select_field] = choices

    @staticmethod
    def drop_form_data(session,form):
        session.pop(form.__class__.__name__)
        session.pop(form.__class__.__name__+'_choices')

    @staticmethod
    def get_form_data(session,form):
        return session[form.__name__] if isinstance(form,type) else session[form.__class__.__name__]

        

        
