try:
    import cx_Freeze
except:
    pip install cx_Freeze

executables = [cx_Freeze.Executable("Sprinting Shark Three.py")]

cx_Freeze.setup(
    name="Sprinting Shark - Remastered",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["crate.png"]}},

    executables = executables


    )
