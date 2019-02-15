# Imports
import importlib
from cmd import Cmd
from termutils import clear
import os

version = "1.7"


def run_plugin(plugin_name):
    try:
        # add `plugin.` to the string to account for the plugin folder
        plugin_name = "plugins.{}".format(plugin_name)
        # Import the python script into a var
        plugin_module = importlib.import_module(plugin_name, ".")
        # Create an instance of the scripts 'Plugin' class
        plugin = plugin_module.Plugin()
        # Run the `main()` function from the `Plugin` instance
        plugin.main()
    # If can't import
    except ModuleNotFoundError:
        # Return an error message if plugin name is invalid
        print("Module '{}' doesn't exist, please verify its location and try again.".format(plugin_name))
    # If nothing was entered
    except ValueError:
        print("Please enter a plugin name")


# List all of the plugins in the "plugins" folder
def list_plugins():
    # Create an empty list
    plugins = []
    # Save the `plugins` folder to the "plugins_folder" var
    plugins_folder = os.listdir("./plugins")
    # Iterate over all files in the plugins folder
    for file in plugins_folder:
        # If the file is the __pycache__ directory
        if file == "__pycache__":
            # Ignore it
            pass
        # Otherwise
        else:
            # Add it to the list of available plugins.
            plugins.append(file)
    # Return the list of plugins
    return plugins


# Define shell class
# noinspection PyMethodMayBeStatic
class Shell(Cmd):
    # Add run command to shell
    def do_run(self, plugin):
        """
        Launch a plugin

        :param plugin: The name of the plugin to use
        :type plugin: str
        """
        run_plugin(plugin)

    def do_clear(self, arg):
        """
        Clears the console screen
        """
        clear()

    def do_list(self, args):
        """
        Prints a list of all the available plugins.
        """
        plugins = list_plugins()
        print("Available plugins:")
        for plugin in plugins:
            print(plugin.replace(".py", ""))

    # Add exit command to shell
    def do_exit(self, arg):
        """
        Exit the program
        """
        exit(1)


# Execute if code is not imported
if __name__ == '__main__':
    # Clear screen (from termutils)
    clear()
    print("Welcome to the probability simulator!")
    print("Version", version)
    # Initiate shell instance
    shell = Shell()
    shell.prompt = ">> "
    # Run shell
    shell.cmdloop()
