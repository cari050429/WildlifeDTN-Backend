from django.test import TestCase, Client
from django.urls import reverse
from data.models import TemperatureData, HumidityData, PictureData

class TestViews(TestCase):

    def setUp(self):
        self.client=Client()
        self.list_url=reverse('listdata')
        self.detailhumidity_url=reverse('humiditydetail', args=[1])
        self.detailpicture_url=reverse('picturedetail',args=[1])
        self.detailtemp_url=reverse('tempdetail', args=[1])
        self.detailtemp_url_post=reverse('post')
        self.testtemp=TemperatureData.objects.create(temperature='30.00', node_origination='3', date_created= '2023-07-06T00:00:00Z', file_type='jpeg', dataid=3555)
        self.testhumidity=HumidityData.objects.create(humidity='30.00', node_origination='3', date_created= '2023-07-06T00:00:00Z', file_type='jpeg', dataid=3555)

    def test_project_list_GET(self):

        response=self.client.get(self.list_url)
        self.assertEquals(response.status_code,200)

    def test_project_detail_temp_GET(self):
            response = self.client.get(self.detailtemp_url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual((response.data['temperature']), self.testtemp.temperature)
            self.assertEqual(response.data['node_origination'], self.testtemp.node_origination)
            self.assertEqual(response.data['date_created'], self.testtemp.date_created)
            self.assertEqual(response.data['file_type'], self.testtemp.file_type)
            self.assertEqual(response.data['dataid'], self.testtemp.dataid)

    def test_project_detail_humidity_GET(self):
            response = self.client.get(self.detailhumidity_url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['humidity'], self.testhumidity.humidity)
            self.assertEqual(response.data['node_origination'], self.testhumidity.node_origination)
            self.assertEqual(response.data['date_created'], self.testhumidity.date_created)
            self.assertEqual(response.data['file_type'], self.testhumidity.file_type)
            self.assertEqual(response.data['dataid'], self.testhumidity.dataid)
    
    #def test_project_detail_picture_GET(self):

     #   response=self.client.get(self.detailpicture_url)
      #  self.assertEquals(response.status_code,200)
    
    def test_temp_POST(self):
        data = [{
            'temperature':30.00,
            'node_origination': 3,
            'date_created': '2023-07-06T00:00:00Z',
            'file_type': 'jpeg',
            'dataid': 3555
        }]
        response = self.client.post(self.detailtemp_url_post, data, content_type='application/json')
        response_data = response.json()
        self.assertEqual(response.status_code, 200)

