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
            "disableArguments": False,

            "formatting": SettingsProxy({

                "paths": SettingsProxy({
                    "startWithNewline": True,
                    "indentLevel": 2,
                    "useSingleQuote": True,
                    "newlineAfterEach": True,
                    "newlineAfterLast": True,
                    "indentLevelAfterLastNewline": 1
                    }),

                "arguments": SettingsProxy({
                    "startWithNewline": True,
                    "indentLevel": 2,
                    "newlineAfterEach": True,
                    "newlineAfterLast": True,
                    "indentLevelAfterLastNewline": 1
                    })
                })
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
        argFormatting = self.defaultSettings.get('formatting').get('arguments')
        pathFormatting = self.defaultSettings.get('formatting').get('paths')
        argFormatting.set('indentLevel', 1)
        pathFormatting.set('indentLevel', 1)
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('settings-1indentlevel')
        self.assertEquals(result, expectedResult)

    def test_settings_2indentlevelafterlastnewline(self):
        initial = self.getInitialTestString('3modules-singlequotes')
        argFormatting = self.defaultSettings.get('formatting').get('arguments')
        pathFormatting = self.defaultSettings.get('formatting').get('paths')
        argFormatting.set('indentLevelAfterLastNewline', 2)
        pathFormatting.set('indentLevelAfterLastNewline', 2)
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('settings-2indentlevelafterlastnewline')
        self.assertEquals(result, expectedResult)

    def test_settings_doublequote(self):
        initial = self.getInitialTestString('3modules-singlequotes')
        pathFormatting = self.defaultSettings.get('formatting').get('paths')
        pathFormatting.set('useSingleQuote', False)
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('settings-doublequote')
        self.assertEquals(result, expectedResult)

    def test_settings_nonewlineaftereach(self):
        initial = self.getInitialTestString('3modules-singlequotes')
        argFormatting = self.defaultSettings.get('formatting').get('arguments')
        pathFormatting = self.defaultSettings.get('formatting').get('paths')
        argFormatting.set('newlineAfterEach', False)
        pathFormatting.set('newlineAfterEach', False)
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('settings-nonewlineaftereach')
        self.assertEquals(result, expectedResult)

    def test_settings_nonewlineafterlast(self):
        initial = self.getInitialTestString('3modules-singlequotes')
        argFormatting = self.defaultSettings.get('formatting').get('arguments')
        pathFormatting = self.defaultSettings.get('formatting').get('paths')
        argFormatting.set('newlineAfterLast', False)
        pathFormatting.set('newlineAfterLast', False)
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('settings-nonewlineafterlast')
        self.assertEquals(result, expectedResult)

    def test_settings_nonewlineatstart(self):
        initial = self.getInitialTestString('3modules-singlequotes')
        argFormatting = self.defaultSettings.get('formatting').get('arguments')
        pathFormatting = self.defaultSettings.get('formatting').get('paths')
        argFormatting.set('startWithNewline', False)
        pathFormatting.set('startWithNewline', False)
        modList = AMDModuleList(initial, self.defaultSettings, self.defaultTabCharacter)
        result = str(modList)
        expectedResult = self.getExpectedResultString('settings-nonewlineatstart')
        self.assertEquals(result, expectedResult)

if __name__ == '__main__':
    unittest.main()
