import pytest
from redes_sociais.redes_sociais import facebook, linkedin, github, instagram
from redes_sociais.sessoes import AlbumSection, PersonalSection, PublicationSection, UploadCodeSection


class TestFacebook:
    def test_instanciar_facebook(self):
        objeto = facebook()
        assert isinstance(objeto, facebook)


class TestLinkedin:
    def test_instanciar_linkedin(self):
        objeto = linkedin()
        assert isinstance(objeto, linkedin)


class TestGithub:
    def test_instanciar_github(self):
        objeto = github()
        assert isinstance(objeto, github)


class TestInstagram:
    def test_instanciar_instagram(self):
        objeto = instagram()
        assert isinstance(objeto, instagram)


class Test_nomes:  
    def test_facebook(self):
        perfil_facebook = eval('facebook')()
        assert (type(perfil_facebook).__name__) == 'facebook'
        perfil_facebook = facebook().getSections()
        assert (str(perfil_facebook)) == '[Dados Pessoais, Sessão para fotos]'

    def test_linkedin(self):
        perfil_linkedin = eval('linkedin')()
        assert (type(perfil_linkedin).__name__) == 'linkedin'
        perfil_linkedin = linkedin().getSections()
        assert (str(perfil_linkedin)) == '[Dados Pessoais, Sessão publicações]'

    def test_github(self):
        perfil_github = eval('github')()
        assert (type(perfil_github).__name__) == 'github'
        perfil_github = github().getSections()
        assert (str(perfil_github)) == '[Dados Pessoais, Sessão Upload]'

    def test_instagram(self):
        perfil_instagram = eval('instagram')()
        assert (type(perfil_instagram).__name__) == 'instagram'
        perfil_instagram = instagram().getSections()
        assert (str(perfil_instagram)) == '[Dados Pessoais, Sessão para fotos]'
