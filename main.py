# Main script

### IMPORTS ###
import importlib


version = "0.0"


print("Welcome to the probability simulator!")
print("Version", version)

plugin_name = input(str("Please enter a plugin name: "))

try:
    # Import the python script into a var
    plugin_module = importlib.import_module(plugin_name, ".")
    # Create an instance of the scripts 'Plugin' class
    plugin = plugin_module.Plugin()
    # Run the `main()` function from the `Plugin` instance
    plugin.main()
# If can't import
except ModuleNotFoundError:
    # Return an error message
    print("Module '{}' doesn't exist, please verify its location and "
          "try again.".format(plugin_name))
# If nothing was entered
except ValueError:
    print("Please enter a plugin name")


class Shell:
    def mainloop(self):
        """
        Begins the main loop for the shell.

        :return nothing
        """
        pass