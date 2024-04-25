import medicos
import cadastro_plano_saude

usuario = str(input('Digite seu número de usuário'))
if usuario in cadastro_plano_saude.usuarios.keys():
    if usuario =='001':
        usuario = 'Fernando'
        print('Bem-vindo Fernando!!!')
        #return usuario
    if usuario =='002':
        usuario = 'Ana Clara'
        print('Bem-vinda Ana Clara')
        #return usuario
else:
    print('Usuario desconhecido ou não cadastrado')

menu = str(input("Deseja agendar uma consulta? (S ou N)")).upper()

if menu == "S":
    paciente = input("Por favor, digite seu nome completo:")
    print(f"{paciente}, escolha com qual médico deseja consultar:")
    print("1 - Grazielle Veiga")
    print("2 - Matheus Correa")

    medico = int(input("Com qual médico deseja agendar consulta?"))

    if medico == 1:
        print(f"Sua consulta com a Dra {medicos.medicos[0]} será agendada")
    elif medico == 2:  # Changed to elif to ensure only one message is printed
        print(f"Sua consulta com o Dr. {medicos.medicos[1]} está agendada")
    else:
        print("Opção inválida!")
else:
    print("Usuário não cadastrado.")    
    
    
                
