from django.contrib import admin


from .models import PageResult
from .models import PageRuleCategoryResult
from .models import PageGuidelineResult
from .models import PageRuleScopeResult
from .models import PageRuleResult

class PageResultAdmin(admin.ModelAdmin):
    list_display  = ('url', 'page_number', 'rules_violation', 'rules_warning', 'rules_manual_check', 'rules_passed', 'implementation_pass_fail_score', 'implementation_score', 'implementation_status')
    list_filter   = ('ws_report',)    

admin.site.register(PageResult, PageResultAdmin)


class PageRuleCategoryResultAdmin(admin.ModelAdmin):
    list_display = ('page_result', 'rule_category', 'rules_violation', 'rules_warning', 'rules_manual_check', 'rules_passed', 'implementation_pass_fail_score', 'implementation_score', 'implementation_status')
    list_filter  = ('page_result', 'rule_category')    

admin.site.register(PageRuleCategoryResult, PageRuleCategoryResultAdmin)

class PageGuidelineResultAdmin(admin.ModelAdmin):
    list_display = ('page_result', 'guideline', 'rules_violation', 'rules_warning', 'rules_manual_check', 'rules_passed', 'implementation_pass_fail_score', 'implementation_score', 'implementation_status')
    list_filter  = ('page_result', 'guideline')

admin.site.register(PageGuidelineResult, PageGuidelineResultAdmin)

class PageRuleScopeResultAdmin(admin.ModelAdmin):
    list_display = ('page_result', 'rule_scope', 'rules_violation', 'rules_warning', 'rules_manual_check', 'rules_passed', 'implementation_pass_fail_score', 'implementation_score', 'implementation_status')
    list_filter  = ('page_result', 'rule_scope')    

admin.site.register(PageRuleScopeResult, PageRuleScopeResultAdmin)

class PageRuleResultAdmin(admin.ModelAdmin):
    list_display = ('page_result', 'rule', 'result_value', 'elements_violation', 'elements_warning', 'elements_mc_identified', 'elements_mc_failed', 'elements_mc_passed', 'elements_mc_na', 'elements_passed', 'implementation_pass_fail_score', 'implementation_score', 'implementation_status')
    list_filter  = ('page_result', 'rule')

admin.site.register(PageRuleResult, PageRuleResultAdmin)
# Register your models here.

