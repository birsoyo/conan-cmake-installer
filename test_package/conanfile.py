import io
import conans


class ConanFileInst(conans.ConanFile):

    def build(self):
        pass

    def test(self):
        output = io.StringIO()
        self.run("cmake --version", output=output)
        self.output.info("Installed: %s" % str(output.getvalue()))
        if self.requires["cmake_installer"].conan_reference.version != "1.0":
            ver = str(self.requires["cmake_installer"].conan_reference.version)
        else:
            ver = str(self.options["cmake_installer"].version)

        assert(ver in str(output.getvalue()))
