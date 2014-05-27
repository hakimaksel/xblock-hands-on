from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

from .utils import load_resource, render_template

class HandsOnBlock(XBlock):
    """
    An XBlock providing hands on tutorials and remote access to linux shell/windows app
    """

    workpad_url = String(help="URL for the workpad server", default=None, scope=Scope.content)
    instruction_url = String(help="URL of the instructions file", default=None, scope=Scope.content)
    video_url = String(help="URL for the video instruction", default=None, scope=Scope.content)

    def student_view(self, context):
        """
        Lab view, displayed to the student
        """
        fragment = Fragment()

        context = {
            'instruction': self.instruction_url.replace(':', '%3A').replace('/', '%2F'),
            'workpad': self.workpad_url,
            'video': self.video_url,
        }

        fragment.add_content(render_template('/templates/handson.html', context))

        return fragment
