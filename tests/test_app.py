from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import *

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        # Create table
        db.create_all()
        # Create test registree
        Kafka=author(first_name="Franz",last_name="Kafka",nationality="Czech Republic")
        book4=books(title="The Metamorphosis", genre="magical realism",booksbr=Kafka)
        # save users to database
        db.session.add(Kafka)
        db.session.commit()
        
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()



class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))  
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The Library Of Babel', response.data)
        self.assertIn(b'Home', response.data)
        self.assertIn(b'Update', response.data)
        self.assertIn(b'Delete', response.data)
        self.assertIn(b'View All', response.data)
        self.assertIn(b'Add Books', response.data)
        self.assertIn(b'Add Author', response.data)

    
    def test_update_get(self):
        response = self.client.get(url_for('update'))  
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The Library Of Babel', response.data)

    def test_delete_get(self):
        response = self.client.get(url_for('delete'))  
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The Library Of Babel', response.data)
    
    def test_addauthors_get(self):
        response = self.client.get(url_for('register'))  
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'submit', response.data)

    def test_registerbooks_get(self):
        response = self.client.get(url_for('registerbooks'))  
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'submit', response.data)

    #this page pulls the authors name and books onto the webpage from the databse
    def test_viewing_all_get(self):
        response = self.client.get(url_for('viewing_all'))  
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Kafka', response.data)
        self.assertIn(b"The Metamorphosis", response.data)

    def test_search_get(self):
        response = self.client.get(url_for('kaf',name='Kafka'))  
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Kafka', response.data)

        authorcheck=author.query.filter_by(id=1).first()
        assert authorcheck.last_name=='Kafka'

    def test_redirect_get(self):
        response = self.client.get(url_for('re'))  
        self.assertEqual(response.status_code, 302)
        follow_redirects=True

    def test_addauthors_post(self):        
        response = self.client.post(url_for('register',)) 
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'all fields need to be filled', response.data)

    def test_deleting_post(self):        
        response = self.client.post(url_for('delete', deletetitle="The Metamorphosissssss")) 
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Title not in database", response.data)


    
    # def test_addingbooks_post(self):
    #     response = self.client.post(url_for('registerbooks',addtitle="stoner"))  
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b'to database' , response.data)



    # def test_booksinput_post(self):
    #     response = self.client.post(url_for('update', data={
    #             'form-book_update-book': 1,
    #             'form-book_update-title': "the castle",
                 
                
    #         }))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b"book has been updated", response.data)


