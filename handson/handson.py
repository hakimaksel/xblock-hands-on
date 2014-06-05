from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

from .utils import load_resource, render_template

class HandsOnBlock(XBlock):
    """
    An XBlock providing hands on tutorials and remote access to linux shell/windows app
    """

    workpad_url = String(help="URL for the workpad server", default=None, scope=Scope.content)
    video_url = String(help="URL for the video instruction", default=None, scope=Scope.content)

    def student_view(self, context):
        """
        Lab view, displayed to the student
        """
        fragment = Fragment()

        context = {
            'workpad': self.workpad_url,
            'video': self.video_url,
        }

        fragment.add_content(render_template('/templates/handson.html', context))

        return fragment

    def studio_view(self, context):
        """
        Studio edit view
        """

        fragment = Fragment()
        fragment.add_content(render_template('templates/handson_edit.html', {'self': self, }))
        fragment.add_javascript(load_resource('public/js/jquery-ui-1.10.4.custom.js'))
        fragment.add_javascript(load_resource('public/js/handson_edit.js'))
        fragment.initialize_js('HandsOnEditBlock')

        return fragment

    @XBlock.json_handler
    def studio_submit(self, submissions, suffix=''):
        self.workpad_url = submissions['workpad']
        self.video_url = submissions['video']
        return {'result': 'success',}

    @staticmethod
    def workbench_scenarios():
        return [('handson', '<handson video_url="http://www.youtube.com/watch?v=Z1xHvWjJtOo" workpad_url="https://met-vs105.bu.edu:8443/met-excel71.html" />')]
