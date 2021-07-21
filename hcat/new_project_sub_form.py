from django import forms
from .models import Project, Tag, Organ, OrganPart, Disease, Publication, Contributor, Url, Lab, CdnaLibraryPrep


class NewProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'short_name', 'description', 'status',
                  'tags', 'project_source', 'privacy', 'comments',
                  'geo_series', 'dbGap_accession', 'array_express_accession', 'ena_accession', 'sra_accession',
                  'ncbi_bioproject_accession', 'cirm_accession', 'ega_study_accesion',
                  'primary_wrangler', 'secondary_wrangler', 'wrangling_status',
                  'organ', 'organ_part', 'disease', 'sample_type', 'source_url', 'cells_expected',
                  'species', 'publications', 'urls', 'labs', 'contributors', 'cdna_library_prep']
        widgets = {'title': forms.TextInput(attrs={'size': 40}), 'short_name': forms.TextInput(attrs={'size': 40}),
                   'description': forms.Textarea(attrs={'rows': 7, 'cols': 125}),
                   'comments': forms.Textarea(attrs={'rows': 5, 'cols': 50})}


class AddTag(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag', 'description']


class AddOrgan(forms.ModelForm):
    class Meta:
        model = Organ
        fields = ['short_name', 'ontology_id', 'ontology_label', 'description', 'comments']


class AddOrganPart(forms.ModelForm):
    class Meta:
        model = OrganPart
        fields = ['short_name', 'ontology_id', 'ontology_label', 'description', 'comments']


class AddDisease(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['short_name', 'description']


class AddLibPrep(forms.ModelForm):
    class Meta:
        model = CdnaLibraryPrep
        fields = ['short_name', 'description', 'comments']


class AddLab(forms.ModelForm):
    class Meta:
        model = Lab
        fields = ['short_name', 'institution', 'pi', 'comments']


class AddPub(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['short_name', 'title', 'pmid', 'comments', 'doi']


class AddContributors(forms.ModelForm):
    class Meta:
        model = Contributor
        fields = ['name', 'email', 'phone', 'address', 'institute', 'city', 'country', 'zip_postal_code']


class AddUrl(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['short_name', 'path', 'description']
