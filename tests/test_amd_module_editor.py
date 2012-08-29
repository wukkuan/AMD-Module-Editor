import unittest
from amd_module_list import AMDModuleList


class SettingsProxy:
    def __init__(self, settings):
        self.settings = settings

    def get(self, name, default=None):
        if name not in self.settings:
            return default
        else:
            return self.settings[name]

    def set(self, name, val):
        self.settings[name] = val


class TestAMDModuleList(unittest.TestCase):

    def setUp(self):
        self.defaultSettings = SettingsProxy({
            "disable_arguments": False,

            "paths_start_with_newline": True,
            "paths_indent_level": 2,
            "paths_use_single_quote": True,
            "paths_newline_after_each": True,
            "paths_newline_after_last": True,
            "paths_indent_level_after_last_newline": 1,

            "arguments_start_with_newline": True,
            "arguments_indent_level": 2,
            "arguments_newline_after_each": True,
            "arguments_newline_after_last": True,
            "arguments_indent_level_after_last_newline": 1
            })

        self.defaultTabCharacter = "  "
        return

    def tearDown(self):
        return

    def getInitialTestString(self, name):
        return open('tests/test-files/' + name + '.js').read()

    def getExpectedResultString(self, name):
        return open('tests/test-files/' + name + '-result.js').read()

    def test_3modules_singlequotes_missingarg(self):
        initial = self.getInitialTestString('3modules-singlequotes-missingarg')
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('3modules-singlequotes-missingarg')
        self.assertEquals(result, expectedResult)

    def test_3modules_singlequotes_noargs(self):
        initial = self.getInitialTestString('3modules-singlequotes-noargs')
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('3modules-singlequotes-noargs')
        self.assertEquals(result, expectedResult)

    def test_3modules_singlequotes(self):
        initial = self.getInitialTestString('3modules-singlequotes')
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('3modules-singlequotes')
        self.assertEquals(result, expectedResult)

    def test_1module(self):
        initial = self.getInitialTestString('1module')
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('1module')
        self.assertEquals(result, expectedResult)

    def test_0modules(self):
        initial = self.getInitialTestString('0modules')
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('0modules')
        self.assertEquals(result, expectedResult)

    def test_settings_1indentlevel(self):
        initial = self.getInitialTestString('3modules-singlequotes')
        self.defaultSettings.set('arguments_indent_level', 1)
        self.defaultSettings.set('paths_indent_level', 1)
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('settings-1indentlevel')
        self.assertEquals(result, expectedResult)

    def test_settings_2indentlevelafterlastnewline(self):
        initial = self.getInitialTestString('3modules-singlequotes')
        self.defaultSettings.set('arguments_indent_level_after_last_newline', 2)
        self.defaultSettings.set('paths_indent_level_after_last_newline', 2)
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('settings-2indentlevelafterlastnewline')
        self.assertEquals(result, expectedResult)

    def test_settings_doublequote(self):
        initial = self.getInitialTestString('3modules-singlequotes')
        self.defaultSettings.set('paths_use_single_quote', False)
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('settings-doublequote')
        self.assertEquals(result, expectedResult)

    def test_settings_nonewlineaftereach(self):
        initial = self.getInitialTestString('3modules-singlequotes')
        self.defaultSettings.set('arguments_newline_after_each', False)
        self.defaultSettings.set('paths_newline_after_each', False)
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('settings-nonewlineaftereach')
        self.assertEquals(result, expectedResult)

    def test_settings_nonewlineafterlast(self):
        initial = self.getInitialTestString('3modules-singlequotes')
        self.defaultSettings.set('arguments_newline_after_last', False)
        self.defaultSettings.set('paths_newline_after_last', False)
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('settings-nonewlineafterlast')
        self.assertEquals(result, expectedResult)

    def test_settings_nonewlineatstart(self):
        initial = self.getInitialTestString('3modules-singlequotes')
        self.defaultSettings.set('arguments_start_with_newline', False)
        self.defaultSettings.set('paths_start_with_newline', False)
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('settings-nonewlineatstart')
        self.assertEquals(result, expectedResult)

if __name__ == '__main__':
    unittest.main()
