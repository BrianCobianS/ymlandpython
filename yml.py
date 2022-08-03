def controller(host,user,password):
    contenido = open("ola.txt").read().splitlines()
    contenido.insert(6,"            "+host)
    contenido.remove("            host")
    contenido.insert(9,"        ansible_user: "+user)
    contenido.remove("        ansible_user: master")
    contenido.insert(10,"        ansible_ssh_pass: "+password)
    contenido.remove("        ansible_ssh_pass: m1")
    f = open('fileDirectory.yml', "w")
    f.writelines("\n".join(contenido))

controller("olaaaaaaa","user","pasword")

