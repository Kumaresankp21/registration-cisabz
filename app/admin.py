from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Registration, Team, TeamMember

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
            'registration__team_name__name',  # Include team name for export
        )
        export_order = (
            'registration__paper_id', 
            'name', 
            'email', 
            'phone', 
            'registration__college', 
            'registration__department',
            'registration__team_name__name',  # Add team name to export order
        )

# Admin class for TeamMember
class TeamMemberAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = TeamMemberResource
    list_display = (
        'get_registration_id',  # Display paper ID
        'get_paper_title',      # Display paper title
        'get_team_name',        # Display team name
        'name', 
        'email', 
        'phone', 
        'get_department',
    )
    search_fields = (
        'registration__paper_id',         # Search by paper ID
        'registration__paper_title',      # Search by paper title
        'registration__team_name__name',  # Search by team name
        'name', 
        'email', 
        'phone',
    )
    list_per_page = 20

    @admin.display(description='Registration ID')
    def get_registration_id(self, obj):
        return obj.registration.paper_id or "No Paper ID"  # Display paper ID

    @admin.display(description='Paper Title')
    def get_paper_title(self, obj):
        return obj.registration.paper_title or "No Paper Title"  # Display paper title

    @admin.display(description='Team Name')
    def get_team_name(self, obj):
        return obj.registration.team_name.name if obj.registration.team_name else "No Team"  # Display team name

    @admin.display(description='Department')
    def get_department(self, obj):
        return obj.registration.department or "No Department"

# Register the models and the admin classes
admin.site.register(Registration)
admin.site.register(Team)
admin.site.register(TeamMember, TeamMemberAdmin)
