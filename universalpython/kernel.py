from ipykernel.kernelbase import Kernel

from ipykernel.ipkernel import IPythonKernel

from urdupython import run_module, SCRIPTDIR

from io import StringIO
import sys

import os

LANG_DICTIONARIES = {
    "ur": os.path.join(SCRIPTDIR, 'languages/ur/ur_native.lang.yaml'),
    "hi": os.path.join(SCRIPTDIR, 'languages/hi/hi_native.lang.yaml'),
    # Add more languages here as needed
}

def get_language_and_code(code):
    lines = code.splitlines()
    lang = "ur"  # default
    if lines and lines[0].strip().startswith("# language:"):
        lang_flag = lines[0].strip().split(":", 1)[-1].strip()
        if lang_flag in LANG_DICTIONARIES:
            lang = lang_flag
        code = "\n".join(lines[1:])  # Remove the flag line
    return lang, code

class UniversalPythonKernel(IPythonKernel):
    implementation = 'UniversalPython'
    implementation_version = '1.1'
    # language_version = '0.1'
    language_info = {
        'name': 'python',
        'version': sys.version.split()[0],
        'mimetype': 'text/x-python',
        'file_extension': '.py',
    }
    banner = "UniversalPython kernel"

    
    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        error_thrown = False

        lang, code = get_language_and_code(code)
        dictionary_path = LANG_DICTIONARIES.get(lang, LANG_DICTIONARIES["ur"])

        try:
            compiled_code = run_module("lex", code, args = {
                            'translate': True,
                            'dictionary': dictionary_path,
                            'reverse': False,
                            'keep': False,         
                            'keep_only': False,
                            'return': True,
                        })
        except Exception as e:
            error_thrown = True
            error_message = "Error: " + str(e)
            print (error_message)

        return super(UniversalPythonKernel, self).do_execute(compiled_code, silent, store_history, user_expressions,
                   allow_stdin)


    def do_complete(self, code, cursor_pos):
        error_thrown = False

        lang, code = get_language_and_code(code)
        dictionary_path = LANG_DICTIONARIES.get(lang, LANG_DICTIONARIES["ur"])

        compiled_code = run_module("lex", code, args = {
            'translate': True,
            'dictionary': dictionary_path,
            'reverse': False,
            'keep': False,         
            'keep_only': False,
            'return': True,
        })

        return super(UniversalPythonKernel, self).do_complete(compiled_code, cursor_pos)