from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from data.views import ListData,  DeleteData, LoginView, post_view, LogoutView, CheckAuthenticationView, PictureDetailData, HumidityDetailData, TemperatureDetailData
from data.models import TemperatureData

class TestUrls(TestCase):

  def test_temperature_detail_url_resolved(self):
    url = reverse('tempdetail', args=[1])
    self.assertEquals(resolve(url).func.view_class, TemperatureDetailData)
  
  def test_humidity_detail_url_resolved(self):
    url = reverse('humiditydetail', args=[1])
    self.assertEquals(resolve(url).func.view_class, HumidityDetailData)
  
  def test_picture_detail_url_resolved(self):
    url = reverse('picturedetail', args=[1])
    self.assertEquals(resolve(url).func.view_class, PictureDetailData)
  
  def test_list_url_resolved(self):
    url = reverse('listdata')
    self.assertEquals(resolve(url).func.view_class, ListData)

  def test_delete_detail_url_resolved(self):
   url = reverse('deletedetail', args=[1])
   self.assertEquals(resolve(url).func.view_class, DeleteData)
  
  def test_post_url_resolved(self):
    url = reverse('post')
    self.assertEquals(resolve(url).func, post_view)
  
  def test_login_url_resolved(self):
    url = reverse('login')
    self.assertEquals(resolve(url).func.view_class, LoginView)
  

  

