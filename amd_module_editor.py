import sublime
import sublime_plugin
import copy
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import amd_module_list
import copy


def formatModuleList(modList, missingArgument, missingPath):
    args = copy.copy(modList.args)
    paths = copy.copy(modList.paths)
    while len(paths) > len(args):
        args.append(missingArgument)
    while len(args) > len(paths):
        paths.append(missingPath)

    def combinePathsAndArgs(t):
        if t[1] == missingArgument:
            return t[0]
        else:
            return t[0] + " - " + t[1]
    return list(map(combinePathsAndArgs, list(zip(paths, args))))


class EditAmdModulesCommand(sublime_plugin.TextCommand):
    MISSING_ARGUMENT = "[Missing Argument]"
    MISSING_PATH = "[Missing Path]"
    NEW_MODULE = "[Add New Module]"
    DELETE_MODULE = "[Delete A Module]"

    def saveModList(self):
        argsRange = self.modList.originalArgsRange
        argsRegion = sublime.Region(argsRange[0], argsRange[1])
        pathsRange = self.modList.originalPathsRange
        pathsRegion = sublime.Region(pathsRange[0], pathsRange[1])
        mainEdit = self.view.begin_edit('edit_modules')
        self.view.replace(mainEdit, argsRegion, self.modList.generateArgs())
        self.view.replace(mainEdit, pathsRegion, self.modList.generatePaths())
        self.view.end_edit(mainEdit)

    @property
    def tabCharacter(self):
        settings = sublime.active_window().active_view().settings()
        if settings.get('translate_tabs_to_spaces'):
            numSpaces = settings.get('tab_size')
            retval = ""
            for x in range(0, numSpaces):
                retval += " "
            return retval
        else:
            return '\t'

    def run(self, edit, action="edit"):
        print(action)
        self.settings = sublime.load_settings('AMD Module Editor.sublime-settings')
        self.entireFileRegion = self.view.find(r'(.*\n*)*', 0)
        if self.entireFileRegion == None:
            sublime.error_message("No require statement found.")
        else:
            entireFileString = self.view.substr(self.entireFileRegion)
            self.modList = amd_module_list.AMDModuleList(entireFileString,
                                                         self.settings,
                                                         self.tabCharacter)
            if self.modList.args == None or self.modList.paths == None:
                sublime.error_message("No require statement found.")
                return

            if action == "edit":
                self.editAction()
            elif action == "delete":
                self.deleteAction()

    def editAction(self):
        quickPanelOptions = formatModuleList(self.modList,
                                             self.MISSING_ARGUMENT,
                                             self.MISSING_PATH)
        quickPanelOptions.insert(0, self.NEW_MODULE)

        indexChosen = -1

        def handleUserSelection(choice):
            def handleArgChosen(newArg):
                if newArg != "":
                    newArg = newArg.strip(' \t')
                    if indexChosen < len(self.modList.args):
                        self.modList.args[indexChosen] = newArg
                    elif indexChosen == len(self.modList.args):
                        self.modList.args.append(newArg)
                self.saveModList()

            def handlePathChosen(newPath):
                newPath = newPath.strip(' \t"\'')
                if newPath == "":
                    sublime.error_message("Path cannot be blank")
                    return
                if indexChosen < len(self.modList.paths):
                    self.modList.paths[indexChosen] = newPath
                elif indexChosen == len(self.modList.paths):
                    self.modList.paths.append(newPath)
                if indexChosen < len(self.modList.args):
                    initialText = self.modList.args[indexChosen]
                else:
                    initialText = ""
                if (not self.settings.get('disableArguments')
                    and indexChosen <= len(self.modList.args)):
                    sublime.active_window().show_input_panel("Argument",
                                                             initialText,
                                                             handleArgChosen,
                                                             None, None)
                else:
                    self.saveModList()

            if choice == 0:
                # The user chose to add a new module, so add it to the
                # end.
                indexChosen = len(self.modList.paths)
            else:
                indexChosen = choice - 1
            if choice != -1:
                if (choice != 0):
                    initialText = self.modList.paths[indexChosen]
                else:
                    initialText = ""
                sublime.active_window().show_input_panel("Path",
                                                         initialText,
                                                         handlePathChosen,
                                                         None, None)

        sublime.active_window().show_quick_panel(quickPanelOptions, handleUserSelection)

    def deleteAction(self):
        quickPanelOptions = formatModuleList(self.modList,
                                             self.MISSING_ARGUMENT,
                                             self.MISSING_PATH)
        quickPanelOptions.insert(0, self.DELETE_MODULE)

        def handleUserSelection(choice):
            if choice > 0:
                indexChosen = choice - 1
                self.modList.paths.pop(indexChosen)
                if indexChosen < len(self.modList.args):
                    self.modList.args.pop(indexChosen)
                self.saveModList()

        sublime.active_window().show_quick_panel(quickPanelOptions, handleUserSelection)
