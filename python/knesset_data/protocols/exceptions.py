from subprocess import CalledProcessError


class AntiwordException(CalledProcessError):

    def __str__(self):
        if not self.output:
            return "antiword processing failed, probably because antiword is not installed, try 'sudo apt-get install antiword'"
        else:
            return "antiword processing failed: {output}".format(output=self.output.split("\n")[0])
