from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Registration, TeamMember

# Resource class for exporting TeamMember data
class TeamMemberResource(resources.ModelResource):
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
        )
        export_order = (
            'registration__paper_id', 
            'name', 
            'email', 
            'phone', 
            'registration__college', 
            'registration__department',
        )

# Admin class for TeamMember
class TeamMemberAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = TeamMemberResource  # Specify the resource class
    list_display = (
        'get_paper_id', 
        'name', 
        'get_paper_title', 
        'get_college',
    )
    search_fields = (
        'name', 
        'registration__college', 
        'registration__paper_id', 
        'registration__department', 
        'registration__email'
    )

    def get_paper_id(self, obj):
        return obj.registration.paper_id
    get_paper_id.short_description = 'Paper ID'

    def get_paper_title(self, obj):
        return obj.registration.paper_title or "No Paper Title"
    get_paper_title.short_description = 'Paper Title'

    def get_college(self, obj):
        return obj.registration.college or "No College"
    get_college.short_description = 'College'

# Register the models and the admin classes
admin.site.register(Registration)
admin.site.register(TeamMember, TeamMemberAdmin)
