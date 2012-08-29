import re
from cStringIO import StringIO


class AMDModuleList:
    PATHS_GROUP = 2
    ARGS_GROUP = 3
    NUM_GROUPS = 3
    newline = '\n'

    def __init__(self, jsFileString, settings, tabCharacter):
        self.jsFileString = jsFileString
        self.settings = settings
        self.tabCharacter = tabCharacter
        pattern = r'(define|require)\s*\(\s*\[(.*?)\]\s*?,\s*?function\s*?\((.*?)\)'
        self.requireMatch = re.search(pattern, jsFileString,
                                 flags=re.MULTILINE | re.DOTALL)
        if (self.requireMatch != None
            and len(self.requireMatch.groups()) == self.NUM_GROUPS
            ):

            def removeQuotes(s):
                return s.replace('"', '').replace("'", "")
            pathsGroupString = str(self.requireMatch.group(self.PATHS_GROUP))
            pathsGroupString = pathsGroupString.strip(' \t\n')
            splitPaths = re.split('[\s\n]*,[\s\n]*', pathsGroupString)
            self.paths = map(removeQuotes, splitPaths)

            self.args = re.split('[\s\n]*,[\s\n]*',
                                 str(self.requireMatch.group(self.ARGS_GROUP)).strip(' \t\n'))

            if len(self.paths) > 0 and len(self.paths[0]) == 0:
                self.paths = []
            if len(self.args) > 0 and len(self.args[0]) == 0:
                self.args = []
        else:
            self.path = None
            self.args = None

    def indentString(self, level):
        tabCharacter = self.tabCharacter
        retval = ""
        for x in range(0, level):
            retval += tabCharacter
        return retval

    def generateArgs(self):
        return self.generateListString(
            self.args,
            self.settings.get('arguments_indent_level'),
            self.settings.get('arguments_start_with_newline'),
            self.settings.get('arguments_newline_after_each'),
            self.settings.get('arguments_newline_after_last'),
            self.settings.get('arguments_indent_level_after_last_newline'))

    def generatePaths(self):
        if self.settings.get('paths_use_single_quote'):
            quoteStr = "'"
        else:
            quoteStr = '"'
        paths = map(lambda p: quoteStr + str(p) + quoteStr, self.paths)
        return self.generateListString(
            paths,
            self.settings.get('paths_indent_level'),
            self.settings.get('paths_start_with_newline'),
            self.settings.get('paths_newline_after_each'),
            self.settings.get('paths_newline_after_last'),
            self.settings.get('paths_indent_level_after_last_newline'))

    def generateListString(self, values, indentLevel, startWithNewline,
                           newlineAfterEach, newlineAfterLast,
                           indentLevelAfterLastNewline):
        buffer = StringIO()
        if len(values) > 0:
            indentString = self.indentString(indentLevel)
            for idx, arg in enumerate(values):
                if idx == 0 and startWithNewline:
                    buffer.write(self.newline)
                    buffer.write(indentString)
                buffer.write(arg)
                if idx != len(values) - 1:
                    buffer.write(',')
                    if newlineAfterEach:
                        buffer.write(self.newline)
                        buffer.write(indentString)
                    else:
                        buffer.write(' ')
                else:
                    if newlineAfterLast:
                        buffer.write(self.newline)
                        buffer.write(self.indentString(indentLevelAfterLastNewline))
        return buffer.getvalue()

    @property
    def originalArgsRange(self):
        return (self.requireMatch.start(self.ARGS_GROUP),
                self.requireMatch.end(self.ARGS_GROUP))

    @property
    def originalPathsRange(self):
        return (self.requireMatch.start(self.PATHS_GROUP),
                self.requireMatch.end(self.PATHS_GROUP))

    def __str__(self):
        generatedArgs = self.generateArgs()
        generatedPaths = self.generatePaths()

        argsStart = self.requireMatch.start(self.ARGS_GROUP)
        argsEnd = self.requireMatch.end(self.ARGS_GROUP)
        pathStart = self.requireMatch.start(self.PATHS_GROUP)
        pathEnd = self.requireMatch.end(self.PATHS_GROUP)

        replacement = self.jsFileString[0:pathStart]
        replacement += generatedPaths
        replacement += self.jsFileString[pathEnd:argsStart]
        replacement += generatedArgs
        replacement += self.jsFileString[argsEnd:]

        return replacement
