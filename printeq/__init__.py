import subprocess

def printeq(tex):
    try: subprocess.run(["printeq", tex], check=True, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as err:
        raise ValueError(err.stderr.decode())
