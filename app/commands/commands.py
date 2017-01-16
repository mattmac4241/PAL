from weather import Weather


class CommandManager(object):

    def __init__(self, zip_code):
        super(CommandManager, self).__init__()
        self.weather = Weather(zip_code)

    def get_commands(self):
        commands = self.weather.get_commands()
        return commands

    def proccess_command(self, command):
        command = command.lower()
        commands = self.get_commands()
        if command in commands:
            function = commands[command]
            return function()
        else:
            return "command not found"
