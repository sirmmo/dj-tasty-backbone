from crm.models import *
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class CompanyWebsiteInline(admin.TabularInline):
        model = CompanyWebsite
        
class CompanyAddressInline(admin.TabularInline):
        model = CompanyAddress
        
class CompanySocialInline(admin.TabularInline):
        model = CompanySocial

class CompanyAreaInline(admin.TabularInline):
        model = CompanyArea
    
class CompanyAddressAdmin(admin.ModelAdmin):
        list_display=['address', 'place', ]
        
class CompanyWebsiteAdmin(admin.ModelAdmin):
        list_display=['address','post_code', 'place']
        
class CompanySocialAdmin():
        list_display=["medium", "account"]

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['abbreviation', 'name']
        list_display_links = ['abbreviation']
	list_select_related = True
        inlines = [ 
            CompanyAddressInline,
	     CompanyAreaInline,
            CompanyWebsiteInline,
            CompanySocialInline
        ]

class ContactEmailInline(admin.TabularInline):
        model = ContactEmail

class ContactPhoneInline(admin.TabularInline):
        model = ContactPhone

class ContactSocialInline(admin.TabularInline):
        model = ContactSocial

class ContactFRelationshipInline(admin.TabularInline):
		model = ContactRelationship
		fk_name = 'contact_from'

class ContactTRelationshipInline(admin.TabularInline):
		model = ContactRelationship
		fk_name = 'contact_to'

class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'surname','company','active']
	list_select_related = True
        inlines = [ 
            ContactEmailInline,
            ContactPhoneInline,
            ContactSocialInline,
			ContactFRelationshipInline,
			ContactTRelationshipInline
        ]

    
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyArea)
admin.site.register(Social)

admin.site.register(CompanyAddress, CompanyAddressAdmin)
admin.site.register(CompanyWebsite)
admin.site.register(CompanySocial)

admin.site.register(CompanyRole)

admin.site.register(UserProfile)
admin.site.register(Place)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactEmail)
admin.site.register(ContactPhoneType)
admin.site.register(ContactPhone)

admin.site.register(ContactSocial)
admin.site.register(ContactRelationship)
admin.site.register(Relationship)

