from conans import ConanFile, CMake, tools


class PyBind11Conan(ConanFile):
    name = "pybind11"
    version = "2.4.3"
    license = "BSD 3-Clause"
    homepage = "https://github.com/pybind/pybind11"
    url = "https://github.com/torshind/conan-pybind11"
    description = "Seamless operability between C++11 and Python"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"

    def source(self):
        tools.get("%s/archive/v%s.tar.gz" % (self.homepage, self.version))

    def build(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.definitions["PYBIND11_TEST"] = False
        cmake.configure(source_folder="pybind11-%s" % self.version)
        cmake.install()

    def package_info(self):
        self.info.header_only()
