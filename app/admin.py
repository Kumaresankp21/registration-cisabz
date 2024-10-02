from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ExportMixin
from import_export.widgets import ManyToManyWidget
from .models import Registration, Event, TeamMember

# Resource class for exporting TeamMember data
class TeamMemberResource(resources.ModelResource):
    technical_events = fields.Field(
        column_name='Technical Events',
        attribute='technical_events',
        widget=ManyToManyWidget(Event, 'name')
    )
    non_technical_events = fields.Field(
        column_name='Non-Technical Events',
        attribute='non_technical_events',
        widget=ManyToManyWidget(Event, 'name')
    )

    class Meta:
        model = TeamMember
        fields = (
            'id', 
            'name', 
            'email', 
            'phone', 
            'registration__paper_id', 
            'registration__college', 
            'registration__department', 
            'technical_events', 
            'non_technical_events'
        )
        export_order = (
            'registration__paper_id', 
            'name', 
            'email', 
            'phone', 
            'registration__college', 
            'registration__department', 
            'technical_events', 
            'non_technical_events'
        )

# Admin class for TeamMember
class TeamMemberAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = TeamMemberResource  # Specify the resource class
    list_display = (
        'get_paper_id', 
        'name', 
        'get_paper_title', 
        'get_technical_events', 
        'get_non_technical_events'
    )
    search_fields = (
        'name', 
        'registration__college', 
        'registration__paper_id', 
        'registration__department', 
        'registration__email'
    )
    list_filter = (
        'registration__college',
        'technical_events', 
        'non_technical_events', 
    )

    def get_paper_id(self, obj):
        return obj.registration.paper_id
    get_paper_id.short_description = 'Paper ID'

    def get_paper_title(self, obj):
        return obj.registration.paper_title or "No Paper Title"
    get_paper_title.short_description = 'Paper Title'

    def get_technical_events(self, obj):
        return ", ".join([event.name for event in obj.technical_events.all()]) or "No Technical Events"
    
    def get_non_technical_events(self, obj):
        return ", ".join([event.name for event in obj.non_technical_events.all()]) or "No Non-Technical Events"

    get_technical_events.short_description = 'Technical Events'
    get_non_technical_events.short_description = 'Non-Technical Events'

# Register the models and the admin classes
admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(TeamMember, TeamMemberAdmin)
