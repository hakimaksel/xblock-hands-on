import textwrap
from lxml import etree
from xml.etree import ElementTree as ET

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

from .utils import load_resource, render_template

from StringIO import StringIO

class ImgCarouselBlock(XBlock):
    """
    An XBlock providing a responsive images carousel
    """

    display_name = String(help="This name appears in horizontal navigation at the top of the page.", 
        default="Images-carousel", 
        scope=Scope.content
    )

    data = String(help="",  
       scope=Scope.content,
       default=textwrap.dedent("""
            <images>
              <img>https://s3.amazonaws.com/xblock/slider/Slide1.JPG</img>
              <img>https://s3.amazonaws.com/xblock/slider/Slide2.JPG</img>
              <img>https://s3.amazonaws.com/xblock/slider/Slide3.JPG</img>
            </images>
          """
    ))

    def student_view(self, context):
        """
        Lab view, displayed to the student
        """

	root = ET.fromstring(self.data)
        images = []
        for child in root:
            images.append(child.text)
        fragment = Fragment()

        context = {
            'images': images,
        }

        fragment.add_content(render_template('/templates/html/img_carousel.html', context))
        fragment.add_javascript(load_resource('public/js/jquery-ui-1.10.4.custom.js'))
        fragment.add_css(load_resource('public/css/responsive-carousel.css'))
        fragment.add_css(load_resource('public/css/responsive-carousel.slide.css'))
        fragment.add_javascript(load_resource('public/js/responsive-carousel.js'))
        fragment.add_javascript('function ImgCarouselBlock(runtime, element) { console.log("ok..."); }')
        fragment.initialize_js('ImgCarouselBlock')

        return fragment

    def studio_view(self, context):
        """
        Studio edit view
        """

        fragment = Fragment()
        fragment.add_content(render_template('templates/html/img_carousel_edit.html', {'self': self, }))
        fragment.add_javascript(load_resource('public/js/jquery-ui-1.10.4.custom.js'))
        fragment.add_javascript(load_resource('public/js/img_carousel_edit.js'))
        fragment.initialize_js('ImgCarouselEditBlock')

        return fragment

    @XBlock.json_handler
    def studio_submit(self, submissions, suffix=''):
        self.display_name = submissions['display_name']
        xml_content = submissions['data']

        try:
            etree.parse(StringIO(xml_content))
            self.data = xml_content
        except etree.XMLSyntaxError as e:
            return {
                'result': 'error',
                'message': e.message
            }

        return {
            'result': 'success',
        }
